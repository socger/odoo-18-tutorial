-- Seed data for concept.cost.budget.sale.family (model in socger_expand_fleet).
-- Table name in Postgres: concept_cost_budget_sale_family
-- (Odoo maps "concept.cost.budget.sale.family" -> "concept_cost_budget_sale_family").
--
-- Idempotent upsert: re-run safely. On conflict by id, it updates
-- name/description/write metadata and preserves create_* fields.
-- description is set to NULL explicitly (not empty string).
--
-- Run manually from repo root:
--   docker compose exec -T db psql -U odoo -d devel \
--     < resources/scripts/seeds/concept_cost_budget_sale_family/seed_concept_cost_budget_sale_family.sql
-- or via the wrapper:
--   ./resources/scripts/seeds/concept_cost_budget_sale_family/run.sh

SET client_encoding TO 'UTF8';

INSERT INTO concept_cost_budget_sale_family
    (id, name, description, create_uid, write_uid, create_date, write_date)
VALUES
    (1, 'Precio / km (venta)',                                                    NULL, 1, 1, now(), now()),
    (2, 'Precio / día (conductor)',                                               NULL, 1, 1, now(), now()),
    (3, 'Precio / km (conductor) - Por km. servicio fijo/regular',                NULL, 1, 1, now(), now()),
    (4, 'Precio / km (conductor) - Por km. servicio discrecional',                NULL, 1, 1, now(), now())
ON CONFLICT (id) DO UPDATE SET
    name        = EXCLUDED.name,
    description = EXCLUDED.description,
    write_uid   = EXCLUDED.write_uid,
    write_date  = now();

-- Keep the sequence in sync so the next ORM-created record gets id = 5
-- instead of colliding with these manually-assigned ids.
SELECT setval(
    'concept_cost_budget_sale_family_id_seq',
    GREATEST((SELECT MAX(id) FROM concept_cost_budget_sale_family), 1),
    true
);
