Actúa como un desarrollador senior de Odoo (versiones 18) trabajando como un agente
autónomo.

# 🎯 Objetivo

Vamos a modificar el módulo socger_expand_fleet.

No te detengas en el análisis: implementa el resultado final (añadir los modelo, vistas,
lógica y seguridad que te pediremos).

Debes crear/extender/modificar modelos existentes en Odoo de la manera siguiente:

## FASE 1

- Extender modelo: fleet.vehicle.model ... modelo de Odoo que extenderemos en módulo
  socger_expand_fleet
  - Añadir fields:
    - field: vehicle_type_id, type: Many2one con tabla vehicle_type, required: True,
      tracking: True
  - Añadir índices:
    - Por los fields "vehicle_type_id" + "name", índice único: Si
  - Crear las siguientes lógicas:
    - Si este modelo tiene algún índice único, y la Base de Datos devuelve un error (por
      este concepto), devolver una excepción explicando lo que ocurre.
  - Modificar Vistas:
    - Vista form:
      - Sustituir field "vehicle_type" por "vehicle_type_id"

## FASE 2

- Modificar modelo: vehicle.type ... modelo que existe en el módulo socger_expand_fleet
  - Modificar Vistas:
    - Vista form:
      - Crear pestaña que presente los registros del modelo
        concept.cost.budget.sale.by.vehicle.type cuyo vehicle_type_id corresponda al id
        del registro del modelo vehicle.type en el que nos encontremos. El título de
        esta pestaña será "Conceptos de control de costes, presupuestos ó ventas".

## FASE 3

- Crear modelo: concept.cost.budget.sale.by.vehicle ... modelo a crear en módulo
  socger_expand_fleet
  - Añadir fields:
    - field: fleet_vehicle_id, type: Many2one con tabla fleet_vehicle, required: True,
      tracking: True
    - field: concept_cost_budget_sale_by_vehicle_type_id, type: Many2one con tabla
      concept_cost_budget_sale_by_vehicle_type, required: True, tracking: True
  - Añadir índices:
    - Por los fields "fleet_vehicle_id" + "concept_cost_budget_sale_by_vehicle_type_id",
      índice único: Si
  - Crear las siguientes lógicas:
    - Si este modelo tiene algún índice único, y la Base de Datos devuelve un error (por
      este concepto), devolver una excepción explicando lo que ocurre.
  - Crear vistas:
    - Vista list: usar todos sus fields.
    - Vista form: usar todos sus fields.
  - Crear un submenú llamado "Flota - Conceptos de control de costes, presupuestos ó
    ventas". Este submenú estará dentro del menú "Flota", después del submenú "Flota -
    Características por vehículo" y llamará a la vista de tipo list del modelo
    "concept_cost_budget_sale_by_vehicle".

## FASE 4

- Extender modelo: fleet.vehicle ... modelo de Odoo
  - Añadir fields:
    - field: vehicle_type_id, type: Many2one con tabla vehicle_type, required: True,
      tracking: True
  - Añadir índices:
    - Por los fields "model_id" + "license_plate", índice único: Si
    - Por los fields "vehicle_type_id" + "license_plate", índice único: Si
  - Crear las siguientes lógicas:
    - Si este modelo tiene algún índice único, y la Base de Datos devuelve un error (por
      este concepto), devolver una excepción explicando lo que ocurre.
    - El modelo "fleet.vehicle.model" tiene su propio field "vehicle_type_id", así que
      en el mismo momento que se rellene el field "model_id" del modelo "fleet.vehicle",
      pues que rellene "fleet_vehicle.vehicle_type_id" con el valor
      "fleet_vehicle_model.vehicle_type_id" del "fleet_vehicle.model_id" elegido.
    - En el mismo momento que se rellene el field vehicle_type_id, tienes que filtrar
      los registros de la tabla "concept_cost_budget_sale_by_vehicle_type" por
      vehicle_type_id = fleet_vehicle.vehicle_type_id. Estos registros filtrados los
      recorrerás y añadirás uno a uno al modelo "concept_cost_budget_sale_by_vehicle".
  - Modificar Vistas:
    - Vista form:
      - Antes del field "model_year", que está en la pestaña con título "Modelo" (en
        español), pintar el field "vehicle_type_id". El field "vehicle_type_id" será de
        sólo lectura (no se podrá modificar).
      - Antes de la pestaña cuyo título en español es "Nota", crear pestaña
        "Características/equipamiento de vehículos". En esta pestaña se verán los
        registros del modelo "vehicle.feature.by.vehicle" cuyo field "fleet_vehicle_id"
        coincida con el id del vehículo en el que estamos.
      - Después de la pestaña "Características/equipamiento de vehículos" y antes de la
        pestaña cuyo título en español es "Nota", crear pestaña "Conceptos de control de
        costes, presupuestos ó ventas". En esta pestaña se verán los registros del
        modelo "concept.cost.budget.sale.by.vehicle" cuyo field "fleet_vehicle_id"
        coincida con el id del vehículo en el que estamos.

# ⚙️ Reglas de versión Odoo

- Usar Odoo 18
- Las vistas tipo lista deben usar <list> (no <tree>)
- No usar attrs en XML
- Seguir buenas prácticas modernas de Odoo
- Cargar/leer/tener en cuenta, antes de realizar cambio alguno, los skills de
  Odoo/Doodba correspondientes.

# 🧠 Necesidad del negocio

Al módulo que creaste, socger_expand_fleet, añadele todas las solicitudes detalladas en
el apartado "Objetivo".

Todos estos modelos están relacionados con la flota de vehículos. Por eso el módulo
socger_expand_fleet es en realidad un módulo que extenderá el módulo fleet de Odoo.

# ⚠️ Consideración importante

- En esta primera versión, el sistema puede ser sencillo
- Pero debe estar preparado para evolucionar en el futuro (por ejemplo: nuevos campos a
  añadir)

No sobrecomplicar la solución, pero tampoco limitar su crecimiento futuro.

# 🔐 Accesos

- Los permisos de usuarios tienen que ser los mismos que tuviera el addon "fleet" de
  Odoo.

# 🧾 Calidad del código

- Código limpio y organizado
- Archivos correctamente estructurados
- Vistas bien definidas y coherentes
- El módulo debe poder instalarse sin errores

# ⚡ Forma de trabajar

- Actúa de forma autónoma
- No pidas confirmaciones innecesarias
- Toma decisiones razonables si algo no está completamente definido
- Entrega una solución completa, no parcial

# ✅ Resultado esperado

- Generar todo el módulo completo con sus archivos
- Código listo para instalar en Odoo
- No dejar tareas pendientes

Al finalizar, hazme un resumen de todo lo que has hecho, inclúyeme el nombre del addon
nuevo que has creado y imprime: Tarea terminada
