Actúa como un desarrollador senior de Odoo (versiones 18) trabajando como un agente
autónomo.

# 🎯 Objetivo

Crear un módulo completo de Odoo que resuelva la necesidad de negocio descrita a
continuación.

Debes entregar una solución funcional completa (no solo explicación), incluyendo
estructura del módulo, lógica, vistas y seguridad.

No te detengas en el análisis: implementa el resultado final.

# ⚙️ Reglas de versión Odoo

- Usar Odoo 18
- Las vistas tipo lista deben usar <list> (no <tree>)
- No usar attrs en XML
- Seguir buenas prácticas modernas de Odoo

# 🧠 Necesidad del negocio

Queremos crear un addon nuevo que extenderá funcionalidad al addon
"/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet" de
Odoo. El nombre del addon créalo tú mismo, pero en el resumen que me harás al final de
todo lo que has hecho me dirás cual es el path/nombre del addon que vas a crear.

Este addon nuevo tendrá varios nuevos modelos, pero todos ellos estarán relacionados con
la flota de vehículos.

Crea un nuevo modelo, vehicle_type. Esta será la estructura de sus campos:

- field: name type: Char required: Si

- field: seats type: Char required: Si

- field: description type: Char required: No

Este modelo vehicle_type tendrá un orden, ascendente, por el field "description"

Este módulo vehicule_type tendrá las siguientes vistas:

- Vista List Esta vista presentará los campos:

  - name
  - seats

- Vista Form Esta vista presentará los campos:
  - name
  - seats
  - description

# ⚙️ Comportamiento esperado

Añade al menú "Configuración/Modelos", del addon
"/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet" de
Odoo, un submenú con el título "Tipos de vehículo". Este submenú llamará al modelo
vehicle_type que vas a crear.

# ⚠️ Consideración importante

- En esta primera versión, el sistema puede ser sencillo
- Pero debe estar preparado para evolucionar en el futuro (por ejemplo: nuevos campos a
  añadir)

No sobrecomplicar la solución, pero tampoco limitar su crecimiento futuro.

# 🔐 Accesos

- Un vendedor debe poder ver este nuevo módulo
- Un responsable de ventas debe poder ver este nuevo módulo
- Solo usuarios con permisos adecuados pueden crear/modificar registros de este nuevo
  módulo

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
