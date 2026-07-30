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
  - Modificar Vistas:
    - Vista list:
      - Sustituir field "vehicle_type" por "vehicle_type_id"

## FASE 2 ... NO SE CONSIGUIO

- Modificar modelo: vehicle.type ... modelo que existe en el módulo socger_expand_fleet
  - Modificar Vistas:
    - Vista form:
      - En la pestaña "Conceptos de control de costes, al final de presentar todos los
        registros, aparece la opción de "Añadir una línea". Esta opción debe de
        desaparecer de donde está ahora mismo y añadirla al principio de esta pestaña
        antes de presentar las columnas del modelo
        concept.cost.budget.sale.by.vehicle.type.

## FASE 3

- Modificar modelo: concept.cost.budget.sale.by.vehicle ... modelo que existe en el
  módulo socger_expand_fleet socger_expand_fleet
  - Modificar vistas:
    - Tanto en la vista form, como en la vista list, el valor que imprime para el field
      "concept_cost_budget_sale_by_vehicle_type_id" no es nada aclaratorio. Para
      aclararlo mejor, fíjate en los valores que se imprimen en el modelo
      "concept.cost.budget.sale.by.vehicle.type" para el field
      "concept_cost_budget_sale_id" (vistas list y form). Haz algo parecido, porque
      necesitamos que imprima esos mismos valores. En vez de modificarlo en las vistas,
      modificarlo en el modelo (así sólo modificaríamos en un sitio y se extendería el
      cambio a todas las vistas donde se use ese field)

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
