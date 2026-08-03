Extensiones de la flota de vehículos. Añade los siguientes modelos relacionados con la
gestión de flota:

- `vehicle.type`: clasificación de vehículos por tipo (nombre, plazas y descripción).
- `concept.cost.budget.sale.family`: familias de conceptos para el control de costes,
  presupuestos y ventas.
- `concept.cost.budget.sale`: conceptos vinculados a una familia, con indicadores
  `to_cost`, `to_budget` y `to_sale` (al menos uno debe estar activo).
- `concept.cost.budget.sale.by.vehicle.type`: valor de un concepto por tipo de vehículo.
- `vehicle.feature.category`: familias de características/equipamiento de vehículos
  (nombre único).
- `vehicle.feature`: características vinculadas a una categoría (nombre único por
  categoría).
- `vehicle.feature.by.vehicle`: asignación de características a vehículos de la flota
  (una misma característica no se puede asignar dos veces al mismo vehículo).

Además, el modelo `fleet.vehicle` se amplía con:

- `vehicle_code`: código único de vehículo (obligatorio).
- `res_company_id` / `res_partner_id`: empresa o empresa colaboradora asociada al
  vehículo (solo una de las dos puede tener valor).
- `license_plate_with_code`: matrícula y código combinados para vistas analíticas.
- `engine_Chassis`, `bodywork` y `build_Number`: identificación del motor/chasis y de la
  carrocería/obra.
- `mileage_at_purchase`: kilómetros en el momento de la compra.
- `seating_capacity_per_permit`, `seating_capacity_per_technical_datasheet` y
  `seating_capacity_bookable_seats`: plazas según permiso, según ficha técnica y
  ofertables (las tres obligatorias).
- `special_configurations`: configuraciones especiales del vehículo (HTML).
- `vehicle_age`: edad del vehículo en años, calculada desde `acquisition_date` hasta la
  fecha actual o hasta `write_off_date` si el vehículo fue dado de baja.
- `driver_id`: relabel del conductor como "Conductor habitual".
- `digital_tachograph` y `professional_diesel_tax_relief_beneficiary`: indicadores
  booleanos (por defecto activados).
- `accounting_national_mileage`, `accounting_international_mileage` y
  `accounting_accounting_project`: datos de contabilidad por kilómetro y proyecto.

Los modelos incluyen índices únicos para evitar duplicados y validaciones de negocio
para garantizar la integridad de los datos.

En las vistas de `fleet.vehicle`:

- Form: `vehicle_code` entre `license_plate` y `tag_ids`.
- Form (pestaña "Modelo"): `engine_Chassis`, `bodywork` y `build_Number` tras `color`;
  el campo `seats` se sustituye por los tres campos de plazas.
- Form (pestaña "Características/equipamiento de vehículos"): dividida en dos apartados,
  el listado de características y las `special_configurations`.
- Form (pestaña "Contabilidad"): km nacional, km internacional y proyecto contable.
- Kanban: empresa/empresa colaboradora bajo la matrícula y `vehicle_code` entre
  `tag_ids` y `driver_id`.
- Pivot y actividad: `license_plate_with_code` (matrícula + " / " + código) en lugar de
  `license_plate`.
