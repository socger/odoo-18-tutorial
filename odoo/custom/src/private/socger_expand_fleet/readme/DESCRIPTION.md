Extensiones de la flota de vehículos. Añade los siguientes modelos relacionados con la
gestión de flota:

- `vehicle.type`: clasificación de vehículos por tipo (nombre, plazas y descripción).
- `concept.cost.budget.sale.family`: familias de conceptos para el control de costes,
  presupuestos y ventas.
- `concept.cost.budget.sale`: conceptos vinculados a una familia, con indicadores
  `to_cost`, `to_budget` y `to_sale` (al menos uno debe estar activo).
- `concept.cost.budget.sale.by.vehicle.type`: valor de un concepto por tipo de vehículo.
- `vehicle.feature.category`: familias de características de vehículos (nombre único).
- `vehicle.feature`: características vinculadas a una categoría (nombre único por
  categoría).
- `vehicle.feature.by.vehicle`: asignación de características a vehículos de la flota
  (una misma característica no se puede asignar dos veces al mismo vehículo).

Los modelos incluyen índices únicos para evitar duplicados y validaciones de negocio
para garantizar la integridad de los datos.
