Extensiones de la flota de vehículos. Añade los siguientes modelos relacionados con la
gestión de flota:

- `vehicle.type`: clasificación de vehículos por tipo (nombre, plazas y descripción).
- `concept.cost.budget.sale.family`: familias de conceptos para el control de costes,
  presupuestos y ventas.
- `concept.cost.budget.sale`: conceptos vinculados a una familia, con indicadores
  `to_cost`, `to_budget` y `to_sale` (al menos uno debe estar activo).
- `concept.cost.budget.sale.by.vehicle.type`: valor de un concepto por tipo de vehículo.

Los modelos incluyen índices únicos para evitar duplicados y validaciones de negocio
para garantizar la integridad de los datos.
