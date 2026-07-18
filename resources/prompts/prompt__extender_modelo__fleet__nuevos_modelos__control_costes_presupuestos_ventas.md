Actúa como un desarrollador senior de Odoo (versiones 18) trabajando como un agente
autónomo.

# 🎯 Objetivo

Al módulo que creaste, socger_expand_fleet, vas añadirle varios modelos más. No te
detengas en el análisis: implementa el resultado final (añadir los modelos, vistas,
lógica y seguridad que te pediremos).

Debes de añadir los siguientes modelos:

- concept_cost_budget_sale_family

  - Fields:
    - field: name type: Char required: Si
    - field: description type: Char required: No
  - Crear índice:
    - Por field "name" Indice único: Si
  - Crear la siguiente lógica:
    - Si este modelo tiene algún índice único, y la Base de Datos devuelve un error (por
      este concepto), devolver una excepción explicando lo que ocurre.

- concept_cost_budget_sale

  - Fields:
    - field: concept_cost_budget_sale_family_id type: Many2one con tabla
      concept_cost_budget_sale_family required: Si
    - field: connamecept_cost_budget_sale_family_id type: Char required: Si
    - field: description type: Char required: No
    - field: to_cost type: Boolean, por defecto = false required: No
    - field: to_budget type: Boolean, por defecto = false required: No
    - field: to_sale type: Boolean, por defecto = false required: No
  - Crear los siguientes índices:
    - Por field "name" Indice único: No
    - Por los fields "concept_cost_budget_sale_family_id" + "name" Indice único: Si
  - Crear la siguiente lógica:
    - Como mínimo uno de los tres campos boolean (to_cost, to_budget ó to_sale) debe de
      ser elegido. Los tres no pueden estar con valor false. Pero se pueden elegir uno,
      dos o tres de los boolean. Esto se debe de controlar tanto en la creación, como en
      la modificación, de cualquier registro.
    - Si este modelo tiene algún índice único, y la Base de Datos devuelve un error (por
      este concepto), devolver una excepción explicando lo que ocurre.

- concept_cost_budget_sale_by_vehicle_type
  - Fields:
    - field: vehicle_type_id type: Many2one con tabla vehicle_type required: Si
    - field: concept_cost_budget_sale_id type: Many2one con tabla
      concept_cost_budget_sale required: Si
    - field: value type: Float required: Si
    - field: price_guide type: Char required: No
    - field: description type: Char required: No
  - Crear índice:
    - Por los fields "vehicle_type_id" + "concept_cost_budget_sale_id" Indice único: Si
  - Crear la siguiente lógica:
    - Si este modelo tiene algún índice único, y la Base de Datos devuelve un error (por
      este concepto), devolver una excepción explicando lo que ocurre.

# ⚙️ Reglas de versión Odoo

- Usar Odoo 18
- Las vistas tipo lista deben usar <list> (no <tree>)
- No usar attrs en XML
- Seguir buenas prácticas modernas de Odoo

# 🧠 Necesidad del negocio

Al módulo que creaste, socger_expand_fleet, añadele los modelos detallados
anteriormente. Todos estos modelos están relacionados con la flota de vehículos. Por eso
el módulo socger_expand_fleet es en realidad un módulo que extenderá el módulo fleet de
Odoo.

Este módulos nuevos tendrán las siguientes vistas:

- Módulo "concept_cost_budget_sale_family"

  - Vista List. Esta vista presentará los campos:
    - name
    - description
  - Vista Form. Esta vista presentará los campos:
    - name
    - description

- Módulo "concept_cost_budget_sale"

  - Vista List. Esta vista presentará los campos:
    - concept_cost_budget_sale_family_id
    - name
    - description
  - Vista Form. Esta vista presentará los campos:
    - concept_cost_budget_sale_family_id
    - name
    - description
    - to_cost
    - to_budget
    - to_sale

- Módulo "concept_cost_budget_sale_by_vehicle_type"
  - Vista List. Esta vista presentará los campos:
    - vehicle_type_id
    - concept_cost_budget_sale_id
    - value
  - Vista Form. Esta vista presentará los campos:
    - vehicle_type_id
    - concept_cost_budget_sale_id
    - value
    - price_guide
    - description

# ⚙️ Comportamiento esperado

Añade al menú "Configuración", del addon
"/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet" de
Odoo, un submenú con el título "Conceptos para control de costes, presupuestos ó
ventas".

Este submenú tendrá el mismo estilo que el submenú "Confituración/Modelos" y se dividirá
en los siguientes submenús con las siguientes acciones:

- Submenú "Familia de conceptos". Acción: llamará al modelo
  "concept_cost_budget_sale_family"
- Submenú "Conceptos". Acción: llamará al modelo "concept_cost_budget_sale"
- Submenú "Conceptos por tipo de vehículo". Acción: llamará al modelo
  "concept_cost_budget_sale_by_vehicle_type"

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
