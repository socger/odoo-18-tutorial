Actúa como un desarrollador senior de Odoo (versiones 18) trabajando como un agente
autónomo.

# 🧠 Estudio realizado

En una consulta anterior hiciste el siguiente estudio sobre como se guardan en Odoo
(v.18) los documentos asociados a modelos existentes como vehículos, presupuestos,
pedidos, etc.

Este fué el estudio que realizaste ...
"/home/socger/trabajo/galvintec/odoo/tutorial/resources/prompts/004 -
prompt**extender_modelo**fleet\_\_documentos_by_vehicle/session.md". Debes de leerlo y
si entiendes este estudio que hiciste continuarías con el objetivo que más abajo te
detallo. Si no lo entiendes, me lo dirás y no continuarías con los procesos pendientes
de realizar.

# 🎯 Objetivo

Vas a crear las vistas necesarias para poder ver los documentos asociados a vehículos y
poder filtrar entre esos documentos.

# ⚙️ Reglas de versión Odoo

- Usar Odoo 18.
- Las vistas tipo lista deben usar <list> (no <tree>).
- No usar attrs en XML.
- Seguir buenas prácticas modernas de Odoo.

# 🧠 Necesidad del negocio

Teniendo en cuenta todo lo que has estudiado sobre como están guardándose los documentos
asociados a un modelo (tabla: ir_attachment), crea en el módulo socger_expand_fleet una
nueva vista, de tipo LIST, para poder presentar todos los documentos asociados a
vehículos.

En esta vista habrá un search para poder filtrar por vehículo y también le crearás un
group by vehículo. Los datos los presentarás ordenados por vehículo + nombre de la
imagen asociada a ese vehículo.

También crearás una vista de tipo form para poder añadir desde ella nuevos documentos y
asociarlos a vehículos. Por lo que tendrás que ver que campos pedirás como mínimo en
este form nuevo a crear.

Decide tú si tienes que crear un nuevo modelo que herede del modelo donde se creó la
tabla donde se guardan los documentos. De hecho decide tú todo lo que tengas que
crear/modificar para crear las dos vistas que te he comentado.

Luego hazme un resumen de todos lo que hayas creado ó modificado para que tenga
constancia de ello.

# ⚙️ Comportamiento esperado

- Añade al menú "Flota", del addon
  "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet" de
  Odoo, un submenú con el título "Flota - Documentación". Este submenú estará debajo del
  menú "Flota/Flota - Características por vehículo" y llamará al modelo/vista LIST que
  crearás para poder ver las documentaciones de los vehículos y donde
  filtraremos/agruparemos, entre varias cosas, por vehículo.

# ⚠️ Consideración importante

- En esta primera versión, el sistema puede ser sencillo.
- Pero debe estar preparado para evolucionar en el futuro (por ejemplo: nuevos campos a
  añadir).

No sobrecomplicar la solución, pero tampoco limitar su crecimiento futuro.

# 🔐 Accesos

- Los permisos de usuarios tienen que ser los mismos que tuviera el addon "fleet" de
  Odoo.

# 🧾 Calidad del código

- Código limpio y organizado.
- Archivos correctamente estructurados.
- Vistas bien definidas y coherentes.
- El módulo/modelo/vistas que crees, debe poder instalarse sin errores.
- Debes de usar los skill que tienes instalados para programar para Odoo.

# ⚡ Forma de trabajar

- Actúa de forma autónoma
- No pidas confirmaciones innecesarias
- Toma decisiones razonables si algo no está completamente definido
- Entrega una solución completa, no parcial

# ✅ Resultado esperado

- Generar el módulo/modelo/vistas que se te pide, completo con todos sus archivos
- Código listo para instalar en Odoo
- No dejar tareas pendientes

Al finalizar, hazme un resumen de todo lo que has hecho, incluyéndome (con máximo
detalle) que nombre de fichero has modificado y porqué lo has hecho.

Después imprime: Tarea terminada.
