-- Seed data for concept.cost.budget.sale.by.vehicle.type (model in socger_expand_fleet).
-- Table name in Postgres: concept_cost_budget_sale_by_vehicle_type
-- (Odoo maps "concept.cost.budget.sale.by.vehicle.type" ->
--  "concept_cost_budget_sale_by_vehicle_type").
--
-- Generates one row per (vehicle_type, concept) by CROSS JOIN-ing the
-- current contents of vehicle_type with a fixed set of 14 concepts.
-- With 18 vehicle_types, this produces 18 * 14 = 252 rows.
--
-- Auto-extensible: if a new vehicle_type is added later and this seed is
-- re-run, its 14 rows are created automatically (CROSS JOIN iterates over
-- the current state of vehicle_type).
--
-- Idempotent: the (vehicle_type_id, concept_cost_budget_sale_id) pair has
-- a UNIQUE constraint, so ON CONFLICT does an update on re-run.
--
-- Depends on: vehicle_type seed (ids 1-18) AND concept_cost_budget_sale
-- seed (ids 1-14) already loaded.
--
-- Run manually from repo root:
--   docker compose exec -T db psql -U odoo -d devel \
--     < resources/scripts/seeds/concept_cost_budget_sale_by_vehicle_type/seed_concept_cost_budget_sale_by_vehicle_type.sql
-- or via the wrapper:
--   ./resources/scripts/seeds/concept_cost_budget_sale_by_vehicle_type/run.sh

SET client_encoding TO 'UTF8';

INSERT INTO concept_cost_budget_sale_by_vehicle_type
    (vehicle_type_id, concept_cost_budget_sale_id, description, value,
     price_guide, create_uid, write_uid, create_date, write_date)
SELECT
    vt.id,
    c.concept_cost_budget_sale_id,
    c.description,
    c.value,
    c.price_guide,
    1, 1, now(), now()
FROM vehicle_type vt
CROSS JOIN (VALUES
    (1,  'Precio venta/km nacional (lleno)',                                 2.20, '2,20–3,20 €/km'),
    (2,  'Precio venta/km nacional (vacío)',                                 1.30, '1,30–2,20 €/km'),
    (3,  'Precio venta/km internacional (lleno)',                            2.80, '2,80–4,20 €/km'),
    (4,  'Precio venta/km internacional (vacío)',                            1.80, '1,80–3,00 €/km'),
    (5,  'Pago al conductor por día / Territorio nacional',                140.00, '140–180 €/día'),
    (6,  'Pago al conductor por día / Territorio internacional',           180.00, '180–250 €/día'),
    (7,  'Pago al conductor por kilómetro nacional lleno (servicio fijo)',   0.10, '0,10–0,16 €/km'),
    (8,  'Pago al conductor por kilómetro nacional vacío (servicio fijo)',   0.06, '0,06–0,10 €/km'),
    (9,  'Pago al conductor por kilómetro internacional lleno (servicio fijo)', 0.14, '0,14–0,20 €/km'),
    (10, 'Pago al conductor por kilómetro internacional vacío (servicio fijo)', 0.08, '0,08–0,14 €/km'),
    (11, 'Pago al conductor por kilómetro nacional lleno (servicio discrecional)',   0.12, '0,12–0,18 €/km'),
    (12, 'Pago al conductor por kilómetro nacional vacío (servicio discrecional)',   0.08, '0,08–0,12 €/km'),
    (13, 'Pago al conductor por kilómetro internacional lleno (servicio discrecional)', 0.16, '0,16–0,22 €/km'),
    (14, 'Pago al conductor por kilómetro internacional vacío (servicio discrecional)', 0.10, '0,10–0,16 €/km')
) AS c(concept_cost_budget_sale_id, description, value, price_guide)
ON CONFLICT (vehicle_type_id, concept_cost_budget_sale_id) DO UPDATE SET
    description = EXCLUDED.description,
    value       = EXCLUDED.value,
    price_guide = EXCLUDED.price_guide,
    write_uid   = EXCLUDED.write_uid,
    write_date  = now();

-- Keep the sequence in sync so the next ORM-created record does not
-- collide with the ids assigned by this bulk insert.
SELECT setval(
    'concept_cost_budget_sale_by_vehicle_type_id_seq',
    GREATEST((SELECT MAX(id) FROM concept_cost_budget_sale_by_vehicle_type), 1),
    true
);
