Actúa como un desarrollador senior de Odoo (versiones 18) trabajando como un agente
autónomo.

# 🎯 Objetivo

Al módulo que creaste, socger_expand_fleet, vas añadirle varios modelos más. No te
detengas en el análisis: implementa el resultado final (añadir los modelos, vistas,
lógica y seguridad que te pediremos).

Debes de añadir los siguientes modelos:

- vehicle_feature_categorie

  - Fields:
    - field: name, type: Char required: Si
    - field: description, type: Char required: No
  - Crear índice:
    - Por field "name", índice único: Si
  - Crear la siguiente lógica:
    - Si este modelo tiene algún índice único, y la Base de Datos devuelve un error (por
      este concepto), devolver una excepción explicando lo que ocurre.

- vehicle_feature

  - Fields:
    - field: vehicle_feature_categorie_id, type: Many2one con tabla
      vehicle_feature_categorie, required: Si
    - field: name, type: Char required: Si
  - Crear los siguientes índices:
    - Por field "name", índice único: No
    - Por los fields "vehicle_feature_categorie_id" + "name", índice único: Si
  - Crear la siguiente lógica:
    - Si este modelo tiene algún índice único, y la Base de Datos devuelve un error (por
      este concepto), devolver una excepción explicando lo que ocurre.

- vehicle_feature_by_vehicle
  - Fields:
    - field: fleet_vehicle_id, type: Many2one con tabla fleet_vehicle, required: Si
    - field: vehicle_feature_id, type: Many2one con tabla vehicle_feature, required: Si
  - Crear índice:
    - Por los fields "fleet_vehicle_id" + "vehicle_feature_id", índice único: Si
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

- Módulo "vehicle_feature_categorie"

  - Vista List. Esta vista presentará los campos:
    - name
    - description
  - Vista Form. Esta vista presentará los campos:
    - name
    - description

- Módulo "vehicle_feature"

  - Vista List. Esta vista presentará los campos:
    - vehicle_feature_categorie_id
    - name
  - Vista Form. Esta vista presentará los campos:
    - vehicle_feature_categorie_id
    - name

- Módulo "vehicle_feature_by_vehicle"
  - Vista List.
    - Esta vista presentará los campos:
      - fleet_vehicle_id
      - vehicle_feature_id
    - Esta vista podrá filtrar por:
      - fleet_vehicle_id
      - vehicle_feature_id
    - Esta vista podrá agrupar por:
      - fleet_vehicle_id
      - vehicle_feature_id
  - Vista Form.
    - Esta vista presentará los campos:
      - fleet_vehicle_id
      - vehicle_feature_id

# ⚙️ Comportamiento esperado

- Añade al menú "Configuración", del addon
  "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet" de
  Odoo, un submenú con el título "Características de vehículos". Este submenú tendrá el
  mismo estilo que el submenú "Confituración/Modelos" y se dividirá en los siguientes
  submenús con las siguientes acciones:

  - Submenú "Familia de características". Acción: llamará al modelo "vehicle_feature"
  - Submenú "Características". Acción: llamará al modelo "vehicle_feature"

- Añade al menú "Flota", del addon
  "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet" de
  Odoo, un submenú con el título "Características por vehículo". Este submenú estará
  debajo del menú "Flota/Flota" y llamará al modelo "vehicle_feature_by_vehicle".

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
