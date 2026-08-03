Añadir a flota-Documentación el campo id del modelo Documentación/categorías Modificar
vista list y form para que aparezca este campo many2one

La vista form y list que he creado para los documentos de vehículos ver si filtran por
vehículo y si agrupan también.

Crear un modelo para categorías de documentación. Una categoría puede ser hija de otra
categoría (así crearíamos subcarpetas)

El modelo que presenta documentaciones por vehículo añadirle la categoría de
documentación y su vista list poder filtrar/agrupar por esta categoría.

Crear un modelo para actualizar los km.actuales de un vehículo. Sus campos serán:

- Fecha de actualizacion
- Km. actuales En la ficha del vehículo, buscar un sitio para que la vista form ponga
  los km.más actuales del vehículo.

En la ficha del vehículo, ver si existen estos conceptos que detallo (si no existen
crearlos):

- Matrícula ... YA EXISTIA EN MODULO
- Nº.bastidor ... YA EXISTIA EN MODULO
- Precio de compra
  - Precio ... YA EXISTIA EN MODULO
- Equipamiento ... YA SE EXTENDIÓ EL MÓDULO CON UN MODELO PARA ESTE TEMA
- Tipo de vehículo ... YA SE EXTENDIÓ EL MÓDULO CON UN MODELO PARA ESTE TEMA ... Pestaña
  Modelo de la vista form
- Matriculación
  - 1ª matriculación (fecha) ... YA EXISTIA EN MODULO
- Conductor habitual ... YA EXISTIA EN MODULO
- Cochera ... EXISTE ya un campo llamado Ubicación (field location) ... pero no es una
  tabla ... al final creé una tabla (fleet_garage)

=================================================

- Motor/chasis ... YA EN PROMPT
- Carrocería ... YA EN PROMPT
- Nº.de obra ... YA EN PROMPT
- Precio de compra

  - Km cuando se compró ... YA EN PROMPT

- Plazas

  - Según permiso ... YA EN PROMPT
  - Según ficha técnica ... YA EN PROMPT
  - Ofertables ... YA EN PROMPT

- Configuraciones especiales ... YA EN PROMPT

- Tacógrafo digital ... YA EN PROMPT

- Matriculación

  - Posterior (fecha) ... NO SE VA A CREAR
  - Edad actual = Fecha actual - 1ª matriculación ... YA EN PROMPT

- Beneficiario gasoleo profesional ... Professional diesel tax relief beneficiary ... YA
  EN PROMPT

- Ctas y proyecto contable

  - Ventas km.nacional ... YA EN PROMPT
  - Ventas km. internacional ... YA EN PROMPT
  - Proyecto contable ... YA EN PROMPT

- Km. actuales
  - Km. ... YA EN PROMPT
  - Actualizados el ... YA EN PROMPT

=======================================================

Se necesitan modelos nuevos para controlar lo de abajo

=======================================================

- Empresa
  - Empresa a la que pertenece
  - Empresa colaboradora / agregada
