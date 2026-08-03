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

En la ficha del vehículo, ver porqué no funciona bien lo siguiente:

- En la pestaña "Características/equipamiento de vehículos", está el field
  "vehicle_feature_id". Queremos que la pestaña mencionada se divida en dos apartados.
  Uno para el field mencionado y otro (a su derecha) para el field
  "special_configurations". NO SE PUEDE EDITAR

- Después del field "write_off_date" poner el field vehicle_age. NO LO CALCULA BIEN
