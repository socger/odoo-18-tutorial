# Skill: Odoo Crons Resilientes

Guía completa para diseñar y implementar crons resilientes en Odoo, basada en la
documentación de Álvaro Alvariño (@alvarino).

> **Objetivo:** Construir crons que sean **resilientes** → idempotentes, incrementales,
> robustos, completos, verbosos y no obstinados.

## Cuándo usar este skill

- Al **crear** un nuevo cron/job programado en Odoo
- Al **modificar** un cron existente
- Al **revisar** código de crons (code review)
- Al encontrar problemas de timeout, duplicación o pérdida de datos en crons

## Contenido

1. [Definiciones clave](#definiciones-clave)
2. [Características esenciales](#características-esenciales)
3. [Caso de uso 1: Facturación recurrente](#caso-de-uso-1-facturación-recurrente)
4. [Caso de uso 2: Sincronización externa](#caso-de-uso-2-sincronización-externa)
5. [Checklist de verificación](#checklist-de-verificación)
6. [Plantillas de código](#plantillas-de-código)
7. [Errores comunes](#errores-comunes)

---

## Definiciones clave

| Término                  | Definición                                                                        |
| ------------------------ | --------------------------------------------------------------------------------- |
| **Resiliente**           | Capaz de volver rápidamente a una buena condición previa tras detectar problemas  |
| **Idempotente** (must)   | Operación que se puede aplicar múltiples veces sin modificar el resultado inicial |
| **Incremental** (must)   | Divide en pequeños bloques y guarda al finalizar cada bloque                      |
| **Robusto** (must)       | Previene que un error puntual en un registro genere un fallo general              |
| **Completo** (must)      | No debe quedar ningún registro sin procesar                                       |
| **Verboso** (should)     | Log de lo que ocurre durante la ejecución                                         |
| **No obstinado** (could) | No reintentar registros malos eternamente                                         |

### Prioridad de implementación

- **must**: Obligatorio para un cron resiliente
- **should**: Muy recomendado, pero no bloqueante
- **could**: Deseable, implementar cuando sea posible

---

## Características esenciales

### 1. Idempotente (must)

**Problema:** Si un cron se ejecuta 2 veces, produce 2 resultados (duplicados).

**Solución:** Usar campos de control para evitar procesamiento duplicado.

```python
# MAL - No idempotente
def _run_process(self):
    records = self.search([('state', '=', 'pending')])
    for record in records:
        record.process()

# BIEN - Idempotente
def _run_process(self):
    records = self.search([
        ('state', '=', 'pending'),
        ('next_execute_date', '<=', fields.Date.today()),  # ← Control temporal
    ])
    for record in records:
        record.process()
        record.next_execute_date += relativedelta(month=1)  # ← Avanza el puntero
```

**Patrones de idempotencia:**

| Patrón                         | Cuándo usarlo                                  |
| ------------------------------ | ---------------------------------------------- |
| Campo `next_execute_date`      | Tareas periódicas (facturación, recordatorios) |
| Campo `dirty` / `needs_sync`   | Sincronizaciones externas                      |
| Campo `state` con transiciones | Flujos con estados claros                      |
| UUID de ejecución              | Para evitar procesamiento concurrente          |

### 2. Incremental (must)

**Problema:** Timeout por procesar demasiados registros de golpe.

**Solución:** Procesar en lotes pequeños y hacer commit después de cada lote.

```python
# MAL - Monolítico (timeout si hay muchos registros)
def _run_process(self):
    records = self.search([('state', '=', 'pending')])
    for record in records:
        record.process()
    self.env.cr.commit()  # ← Un solo commit al final

# BIEN - Incremental
def _run_process(self):
    records = self.search([('state', '=', 'pending')], limit=100)  # ← Lote pequeño
    for record in records:
        record.process()
        self.env.cr.commit()  # ← Commit por registro (o por lote)
```

**Configuración del límite:**

```python
# En el modelo del cron
_execute = fields.Integer(string="Block size", default=100)

def _run_process(self):
    records = self.search([...], limit=self._execute)
    for record in records:
        # ...
        self.env.cr.commit()
```

### 3. Robusto (must)

**Problema:** Un error en un registro detiene todo el procesamiento.

**Solución:** Try/except por registro con rollback individual.

```python
# MAL - Frágil
def _run_process(self):
    records = self.search([...])
    for record in records:
        record.process()  # ← Si falla uno, fallan todos

# BIEN - Robusto
def _run_process(self):
    records = self.search([...], limit=100)
    for record in records:
        try:
            record.process()
            self.env.cr.commit()
        except Exception:
            self.env.cr.rollback()
            _logger.exception(
                "Failed to process record %s", record.id
            )
```

**Nota:** El rollback es necesario para limpiar el estado de la transacción y permitir
que el siguiente registro se procese correctamente.

### 4. Completo (must)

**Problema:** Si el cron falla a mitad de ejecución, algunos registros quedan sin
procesar indefinidamente.

**Solución:** Usar `<=` en lugar de `=` para capturar registros pendientes de
ejecuciones anteriores.

```python
# MAL - Incompleto
def _run_process(self):
    records = self.search([
        ('next_execute_date', '=', fields.Date.today()),  # ← Solo los de hoy
    ])

# BIEN - Completo
def _run_process(self):
    records = self.search([
        ('next_execute_date', '<=', fields.Date.today()),  # ← Hoy o anteriores
    ])
```

### 5. Verboso (should)

**Problema:** Difícil diagnosticar problemas sin logs.

**Solución:** Log de éxito y error con contexto suficiente.

```python
def _run_process(self):
    records = self.search([...], limit=100)
    for record in records:
        try:
            record.process()
            self.env.cr.commit()
            _logger.debug(
                "Processed record %s successfully", record.id
            )
        except Exception:
            self.env.cr.rollback()
            _logger.exception(
                "Failed to process record %s", record.id
            )
```

**Niveles de log recomendados:**

| Nivel                 | Cuándo usarlo                               |
| --------------------- | ------------------------------------------- |
| `_logger.debug()`     | Éxito normal (solo visible con debug mode)  |
| `_logger.info()`      | Eventos importantes (inicio/fin de lote)    |
| `_logger.warning()`   | Problemas recuperables (retry, skip)        |
| `_logger.exception()` | Errores (automáticamente incluye traceback) |

### 6. No obstinado (could)

**Problema:** Un registro con error se reintenta eternamente, bloqueando el
procesamiento de otros registros.

**Solución:** Contador de reintentos con límite máximo.

```python
# En el modelo
retry_count = fields.Integer(string="Retry count", default=0)
max_retries = fields.Integer(string="Max retries", default=3)

def _run_process(self):
    records = self.search([
        ('next_execute_date', '<=', fields.Date.today()),
        ('retry_count', '<', self.max_retries),  # ← Limitar reintentos
    ], limit=100)
    for record in records:
        try:
            record.process()
            record.retry_count = 0  # ← Resetear contador en éxito
            self.env.cr.commit()
        except Exception:
            self.env.cr.rollback()
            record.retry_count += 1
            record.next_execute_date = fields.Date.today()  # ← Reintentar mañana
            self.env.cr.commit()
            _logger.warning(
                "Record %s failed (attempt %d/%d)",
                record.id,
                record.retry_count,
                record.max_retries,
            )
```

---

## Caso de uso 1: Facturación recurrente

Crear una factura desde una suscripción cada mes.

### Punto de partida (código frágil)

```python
def _run_subscription_invoice(self):
    subscriptions_to_invoice = self.search([
        ('stage_id.category', '=', 'progress'),
    ])
    for subscription in subscriptions_to_invoice:
        subscription.create_invoice()
```

**Problemas:**

- Poco robusto: falla uno, fallan todos
- Monolítico: en caso de timeout, rollback de todo
- Rollback inconsistente: algunos emails enviados
- Si se salta un factura un mes, se pierde
- Alto riesgo de de actualización concurrente (mucho tiempo)
- Si se ejecuta 2 veces, 2 facturas

### Evolución del código

```python
# 1. Idempotente
def _run_subscription_invoice(self):
    subscriptions_to_invoice = self.search([
        ('stage_id.category', '=', 'progress'),
        ('next_invoice_date', '=', fields.Date.today()),  # ← Solo las de hoy
    ])
    for subscription in subscriptions_to_invoice:
        subscription.create_invoice()
        subscription.next_invoice_date += relativedelta(month=1)  # ← Avanzar fecha

# 2. Incremental
def _run_subscription_invoice(self):
    subscriptions_to_invoice = self.search([
        ('stage_id.category', '=', 'progress'),
        ('next_invoice_date', '=', fields.Date.today()),
    ])
    for subscription in subscriptions_to_invoice:
        subscription.create_invoice()
        subscription.next_invoice_date += relativedelta(month=1)
        self.env.cr.commit()  # ← Commit por registro

# 3. Robusto
def _run_subscription_invoice(self):
    subscriptions_to_invoice = self.search([
        ('stage_id.category', '=', 'progress'),
        ('next_invoice_date', '=', fields.Date.today()),
    ])
    for subscription in subscriptions_to_invoice:
        try:
            subscription.create_invoice()
            subscription.next_invoice_date += relativedelta(month=1)
            self.env.cr.commit()
        except Exception:
            self.env.cr.rollback()

# 4. Completo
def _run_subscription_invoice(self):
    subscriptions_to_invoice = self.search([
        ('stage_id.category', '=', 'progress'),
        ('next_invoice_date', '<=', fields.Date.today()),  # ← <= en vez de =
    ])
    for subscription in subscriptions_to_invoice:
        try:
            subscription.create_invoice()
            subscription.next_invoice_date += relativedelta(month=1)
            self.env.cr.commit()
        except Exception:
            self.env.cr.rollback()

# 5. No obstinado
def _run_subscription_invoice(self):
    subscriptions_to_invoice = self.search([
        ('stage_id.category', '=', 'progress'),
        ('next_invoice_date', '<=', fields.Date.today()),
        ('next_invoice_date', '>', fields.Date.today() - timedelta(days=10)),  # ← Límite
    ])
    for subscription in subscriptions_to_invoice:
        try:
            subscription.create_invoice()
            subscription.next_invoice_date += relativedelta(month=1)
            self.env.cr.commit()
        except Exception:
            self.env.cr.rollback()
```

---

## Caso de uso 2: Sincronización externa

Sincronizar contactos con una herramienta externa todos los días.

### Punto de partida (código frágil)

```python
def _sync_partner(self):
    partners = self.search([])
    data = partners._prepare_data()
    self._send_data(data)
```

**Problemas:**

- Siempre procesa todos los datos: crece, timeout
- Monolítico: en caso de timeout, seguirá haciendo retry para siempre
- Si se ejecuta dos veces en el mismo día, se sincronizará todo dos veces
- Lo intenta sólo una vez al día. Si el servicio externo no está disponible, no hay
  reintento.

### Evolución del código

```python
# 1. Idempotente
def _sync_partner(self):
    partners = self.search([('dirty', '=', True)])  # ← Solo los modificados
    data = partners._prepare_data()
    self._send_data(data)
    partners.write({'dirty': False})  # ← Marcar como sincronizados

# 2. Incremental
def _sync_partner(self):
    partners = self.search([('dirty', '=', True)], limit=100)  # ← Lote pequeño
    if not partners:
        return  # ← No hay nada que sincronizar
    data = partners._prepare_data()
    self._send_data(data)
    partners.write({'dirty': False})
    self.env.cr.commit()

# 3. Robusto
def _sync_partner(self):
    partners = self.search([('dirty', '=', True)], limit=100)
    if not partners:
        return
    try:
        data = partners._prepare_data()
        self._send_data(data)
        partners.write({'dirty': False})
        self.env.cr.commit()
    except Exception:
        self.env.cr.rollback()

# 4. Verboso
def _sync_partner(self):
    partners = self.search([('dirty', '=', True)], limit=100)
    if not partners:
        return
    try:
        data = partners._prepare_data()
        self._send_data(data)
        partners.write({'dirty': False})
        self.env.cr.commit()
        _logger.debug("Batch of %d partners synced", len(partners))
    except Exception:
        self.env.cr.rollback()
        _logger.exception("Batch sync failed for %d partners", len(partners))

# 5. No obstinado
def _sync_partner(self):
    # dirty es un entero: 5 = nuevo, decrementa con cada error, 0 = ok
    partners = self.search([('dirty', '>', 1)], limit=100)  # ← Filtrar por reintentos
    if not partners:
        return
    for partner in partners:
        try:
            data = partner._prepare_data()
            self._send_data(data)
            partner.write({'dirty': 0})  # ← Marcar como sincronizado
            self.env.cr.commit()
            _logger.debug("Partner %s synced", partner.id)
        except Exception:
            self.env.cr.rollback()
            partner.dirty -= 1  # ← Decrementar contador
            self.env.cr.commit()
            _logger.exception("Partner %s sync failed", partner.id)
```

---

## Checklist de verificación

Al crear o modificar un cron, verificar:

- [ ] **Idempotente**: ¿Puede ejecutarse 2 veces sin duplicar resultados?
- [ ] **Incremental**: ¿Procesa en lotes pequeños con commit intermedio?
- [ ] **Robusto**: ¿Un error en un registro no detiene el resto?
- [ ] **Completo**: ¿Usa `<=` para capturar registros pendientes?
- [ ] **Verboso**: ¿Tiene logs de éxito y error?
- [ ] **No obstinado**: ¿Limita reintentos de registros problemáticos?

---

## Plantillas de código

### Plantilla base para cron resiliente

```python
import logging
from datetime import timedelta

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MyModel(models.Model):
    _name = "my.model"
    _description = "My Model"

    state = fields.Selection(
        selection=[
            ("pending", "Pending"),
            ("done", "Done"),
            ("error", "Error"),
        ],
        default="pending",
    )
    next_execute_date = fields.Date(string="Next Execute Date")
    retry_count = fields.Integer(string="Retry Count", default=0)
    max_retries = fields.Integer(string="Max Retries", default=3)

    def _run_cron_process(self):
        """Main cron method - resilient implementation."""
        records = self.search([
            ("state", "=", "pending"),
            ("next_execute_date", "<=", fields.Date.today()),
            ("retry_count", "<", self.max_retries),
        ], limit=100)

        if not records:
            return

        for record in records:
            try:
                self._process_record(record)
                record.state = "done"
                record.retry_count = 0
                self.env.cr.commit()
                _logger.debug("Record %s processed successfully", record.id)
            except Exception:
                self.env.cr.rollback()
                record.retry_count += 1
                record.next_execute_date = fields.Date.today() + timedelta(days=1)
                self.env.cr.commit()
                _logger.exception(
                    "Failed to process record %s (attempt %d/%d)",
                    record.id,
                    record.retry_count,
                    record.max_retries,
                )

    def _process_record(self, record):
        """Process a single record. Override in specific models."""
        raise NotImplementedError("Subclasses must implement _process_record")
```

### Plantilla para sincronización externa

```python
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MySyncModel(models.Model):
    _name = "my.sync.model"
    _description = "My Sync Model"

    dirty = fields.Integer(
        string="Dirty Flag",
        default=0,
        help="0: synced, >0: needs sync (decrements on retry)",
    )
    max_retries = fields.Integer(string="Max Retries", default=3)

    def _run_sync_cron(self):
        """Sync cron with external service."""
        records = self.search([
            ("dirty", ">", 1),
        ], limit=100)

        if not records:
            return

        for record in records:
            try:
                data = record._prepare_sync_data()
                self._send_to_external(data)
                record.write({"dirty": 0})
                self.env.cr.commit()
                _logger.debug("Record %s synced", record.id)
            except Exception:
                self.env.cr.rollback()
                record.dirty -= 1
                self.env.cr.commit()
                _logger.exception("Failed to sync record %s", record.id)

    def _prepare_sync_data(self):
        """Prepare data for external sync. Override in specific models."""
        raise NotImplementedError("Subclasses must implement _prepare_sync_data")

    def _send_to_external(self, data):
        """Send data to external service. Override in specific models."""
        raise NotImplementedError("Subclasses must implement _send_to_external")
```

### Plantilla XML para cron

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <data noupdate="1">
        <record id="cron_my_process" model="ir.cron">
            <field name="name">My Model: Process Records</field>
            <field name="model_id" ref="model_my_model" />
            <field name="state">code</field>
            <field name="code">model._run_cron_process()</field>
            <field name="interval_number">1</field>
            <field name="interval_type">days</field>
            <field name="numbercall">-1</field>
            <field name="active">True</field>
        </record>
    </data>
</odoo>
```

---

## Errores comunes

### 1. Timeout por procesar demasiados registros

```python
# MAL
def _run_cron(self):
    records = self.search([])  # ← Todos los registros
    for record in records:
        record.process()

# BIEN
def _run_cron(self):
    records = self.search([], limit=100)  # ← Lote pequeño
    for record in records:
        record.process()
        self.env.cr.commit()
```

### 2. Duplicación por falta de idempotencia

```python
# MAL
def _run_cron(self):
    records = self.search([('state', '=', 'pending')])
    for record in records:
        record.create_invoice()  # ← Se duplica si se ejecuta 2 veces

# BIEN
def _run_cron(self):
    records = self.search([
        ('state', '=', 'pending'),
        ('next_execute_date', '<=', fields.Date.today()),
    ])
    for record in records:
        record.create_invoice()
        record.next_execute_date += relativedelta(month=1)  # ← Avanzar fecha
        self.env.cr.commit()
```

### 3. Pérdida de registros por `=` en vez de `<=`

```python
# MAL - Pierde registros si el cron falla
def _run_cron(self):
    records = self.search([
        ('next_execute_date', '=', fields.Date.today()),
    ])

# BIEN - Captura registros pendientes
def _run_cron(self):
    records = self.search([
        ('next_execute_date', '<=', fields.Date.today()),
    ])
```

### 4. Falta de rollback en except

```python
# MAL - La transacción queda en estado inconsistente
def _run_cron(self):
    for record in records:
        try:
            record.process()
            self.env.cr.commit()
        except Exception:
            pass  # ← No hace rollback

# BIEN - Limpia la transacción
def _run_cron(self):
    for record in records:
        try:
            record.process()
            self.env.cr.commit()
        except Exception:
            self.env.cr.rollback()
```

### 5. Intentar infinitamente registros problemáticos

```python
# MAL - Bucle infinito con registros problemáticos
def _run_cron(self):
    records = self.search([('state', '=', 'pending')])
    for record in records:
        try:
            record.process()
            self.env.cr.commit()
        except Exception:
            self.env.cr.rollback()
            # ← El registro sigue pendiente, se reintenta eternamente

# BIEN - Limitar reintentos
def _run_cron(self):
    records = self.search([
        ('state', '=', 'pending'),
        ('retry_count', '<', 3),  # ← Máximo 3 reintentos
    ])
    for record in records:
        try:
            record.process()
            record.retry_count = 0
            self.env.cr.commit()
        except Exception:
            self.env.cr.rollback()
            record.retry_count += 1
            self.env.cr.commit()
```

---

## Referencias

- [Fuente original: Cómo diseñar crons resilientes](https://docs.alvarino.cloud/s/crons-resilientes)
- [YouTube: How to Design Resilient Odoo Crons](https://www.youtube.com/watch?v=CLdeQLxwJPU)
