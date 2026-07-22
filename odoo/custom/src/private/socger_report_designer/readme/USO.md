# Uso

El **Diseñador Visual de Informes** permite crear informes QWeb/PDF para cualquier
modelo de Odoo utilizando una interfaz visual de arrastrar y soltar, sin necesidad de
escribir XML a mano.

## Primeros Pasos

1. Instale el módulo `socger_report_designer` desde **Aplicaciones**.
2. Navegue a **Informes > Diseñador Visual** en el menú principal.
3. Seleccione un **modelo destino** (por ejemplo, `sale.order`, `res.partner`) del
   desplegable.
4. Diseñe su informe en el lienzo (vea los pasos a continuación).
5. **Guarde** y **Publique** cuando esté listo.

## Crear un Diseño de Informe

### Paso 1: Elegir un Modelo

Seleccione el modelo de Odoo cuyos registros desea imprimir. El panel izquierdo muestra
todos los campos disponibles en ese modelo, agrupados por tipo (básico, numérico, fecha,
relación, etc.).

### Paso 2: Arrastrar Campos al Lienzo

- **Arrastre un campo** desde el panel y suéltelo en el lienzo de papel A4.
- **Haga doble clic** en un campo para añadirlo en la posición (0, 0).
- Use la sección **Elementos de Diseño** para elementos estructurales: encabezados,
  líneas horizontales, espaciadores, saltos de página, tablas y contenedores.

### Paso 3: Posicionar y Estilizar Elementos

Haga clic en cualquier elemento del lienzo para seleccionarlo. El **panel de
Propiedades** (panel derecho) muestra:

- **Posición**: Coordenadas X/Y en píxeles. El ancho/alto se pueden definir
  numéricamente.
- **Tipo**: Cambie el tipo de elemento (texto, encabezado, imagen, tabla, etc.).
- **Vinculación de Campo**: Vincule un elemento de texto/imagen/HTML a un campo de Odoo.
  El informe renderizará el valor real del campo al imprimir.
- **Formato de Campo** (widget t-field): Elija cómo se renderiza el campo — monetario,
  fecha, fecha y hora, decimal, entero, HTML, selección, etc.
- **Contenido**: Texto estático para elementos sin vincular.
- **Estilo**: Tamaño de fuente, peso, color, fondo, alineación, relleno, margen, borde,
  opacidad y más.
- **Condición**: Expresión QWeb `t-if` opcional (por ejemplo, `o.state == 'done'`).

### Paso 4: Tablas (One2many / Many2many)

Las tablas muestran líneas de registros relacionados (por ejemplo, `order_line` en
`sale.order`):

1. Añada un elemento **Tabla** desde Elementos de Diseño.
2. Seleccione una **Fuente de Datos** — cualquier campo O2M o M2M del modelo.
3. Configure las columnas en el **Editor de Tablas**:
   - Cada columna tiene una **etiqueta de encabezado** y una **ruta de campo** del
     modelo relacionado.
   - Soporte para rutas many2one anidadas (por ejemplo, `partner_id.name`).
   - Funciones de **agregado** por columna: Suma, Promedio, Conteo, Mínimo, Máximo.
4. Opciones de estilo de tabla:
   - **Fondo del encabezado** y **Color de texto del encabezado** (selectores de color).
   - **Peso de fuente del encabezado**: Normal, Negrita o Ligera.
   - **Rayas de cebra** con colores de fondo configurables para filas pares e impares.
   - **Bordes de tabla**: Activar/desactivar, con color de borde personalizado.
   - **Fila de pie / totales**: Activar/desactivar fila de agregados al final.

### Paso 5: Vista Previa

Hay dos modos de vista previa disponibles:

- **Vista Previa Integrada**: Active la vista previa dividida dentro del modo de diseño.
  Se actualiza automáticamente al editar (con retardo de 600 ms). Un **selector de
  registros** le permite elegir qué registro previsualizar.
- **Vista Previa a Pantalla Completa**: Haga clic en el botón Vista Previa en la barra
  de herramientas para una vista completa con su propio selector de registros y
  actualización manual.

Las vistas previas se **almacenan en caché** en el lado del cliente (en memoria +
sessionStorage) durante 5 minutos, por lo que volver a visitar la misma combinación de
diseño+registro es instantáneo.

### Paso 6: Guardar y Publicar

- **Guardar**: Almacena el JSON del diseño en la base de datos. El número de versión se
  incrementa automáticamente en cada guardado después de publicar.
- **Publicar**: Crea una plantilla QWeb (`ir.ui.view`) y una `ir.actions.report` en
  Odoo. El informe aparece entonces en el menú **Imprimir** de las vistas del modelo
  destino.
- **Despublicar**: Elimina la plantilla QWeb y la acción de informe.

## Atajos de Teclado

El lienzo soporta estos atajos de teclado (cuando no hay foco en un campo de entrada):

- **Ctrl+Z**: Deshacer
- **Ctrl+Y** / **Ctrl+Shift+Z**: Rehacer
- **Ctrl+C**: Copiar elemento seleccionado
- **Ctrl+V**: Pegar (desplazado 20 px)
- **Ctrl+D**: Duplicar elemento seleccionado
- **Ctrl+A**: Seleccionar todos los elementos
- **Escape**: Deseleccionar
- **Suprimir** / **Retroceso**: Eliminar elemento seleccionado

## Funciones del Lienzo

- **Zoom**: Botones de zoom +/- en la barra de herramientas del lienzo (25 %–300 %).
- **Cuadrícula**: Mostrar/ocultar cuadrícula (líneas de 10 px).
- **Ajuste a la cuadrícula**: Activar/desactivar el ajuste para una colocación precisa
  de elementos.
- **Arrastrar y soltar**: Los elementos se ajustan a la cuadrícula de 10 px al
  arrastrar.

## Endpoints de la API REST

El módulo expone estos endpoints JSON-RPC bajo `/api/report-designer/`:

- `/models` — Listar modelos de Odoo disponibles.
- `/fields/<model>` — Listar campos de un modelo.
- `/fields/<model>/related` — Listar campos de un modelo relacionado (expansión
  anidada).
- `/layouts` — Listar todos los diseños de informe.
- `/layouts/create` — Crear un nuevo diseño.
- `/layouts/<id>/save` — Guardar el JSON del diseño.
- `/layouts/<id>/publish` — Publicar un diseño.
- `/layouts/<id>/unpublish` — Despublicar un diseño.
- `/layouts/<id>/delete` — Eliminar un diseño.
- `/layouts/<id>/preview` — Vista previa de un diseño publicado.
- `/generate-xml` — Generar XML QWeb a partir del JSON del diseño sin persistir.
- `/preview/html` — Vista previa en vivo como HTML (no requiere publicación).
- `/preview/live` — Vista previa en vivo como PDF (no requiere publicación).
- `/records/<model>` — Obtener registros para el selector de vista previa.

## Arquitectura

- **Backend** (Python): El modelo `report.designer.layout` almacena las definiciones de
  diseño como JSON. La acción de publicar genera XML QWeb y lo registra como
  `ir.actions.report`.
- **Frontend** (React): Editor de lienzo basado en Fabric.js con panel de propiedades,
  selector de campos y vista previa en vivo. Construido con Vite.
- **Comunicación**: Controladores JSON-RPC en `controllers/main.py`.
