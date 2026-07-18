-- Seed data for concept.cost.budget.sale (model in socger_expand_fleet).
-- Table name in Postgres: concept_cost_budget_sale
-- (Odoo maps "concept.cost.budget.sale" -> "concept_cost_budget_sale").
--
-- Idempotent upsert: re-run safely. On conflict by id, it updates
-- family/name/description/flags/write metadata and preserves create_* fields.
-- description is set to NULL explicitly (not empty string).
--
-- Depends on: concept_cost_budget_sale_family seed (ids 1-4) already loaded.
--
-- Run manually from repo root:
--   docker compose exec -T db psql -U odoo -d devel \
--     < resources/scripts/seeds/concept_cost_budget_sale/seed_concept_cost_budget_sale.sql
-- or via the wrapper:
--   ./resources/scripts/seeds/concept_cost_budget_sale/run.sh

SET client_encoding TO 'UTF8';

INSERT INTO concept_cost_budget_sale
    (id, concept_cost_budget_sale_family_id, name, description,
     to_cost, to_budget, to_sale,
     create_uid, write_uid, create_date, write_date)
VALUES
    (1,  1, 'Km. nacionales - Con carga / llenos',       NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (2,  1, 'Km. nacionales - Sin carga / vacíos',       NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (3,  1, 'Km. internacionales - Con carga / llenos',  NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (4,  1, 'Km. internacionales - Sin carga / vacíos',  NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (5,  2, 'Territorio nacional',                        NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (6,  2, 'Territorio internacional',                   NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (7,  3, 'Km. nacionales - Con carga / llenos',        NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (8,  3, 'Km. nacionales - Sin carga / vacíos',        NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (9,  3, 'Km. internacionales - Con carga / llenos',  NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (10, 3, 'Km. internacionales - Sin carga / vacíos',  NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (11, 4, 'Km. nacionales - Con carga / llenos',        NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (12, 4, 'Km. nacionales - Sin carga / vacíos',        NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (13, 4, 'Km. internacionales - Con carga / llenos',  NULL, TRUE, TRUE, TRUE, 1, 1, now(), now()),
    (14, 4, 'Km. internacionales - Sin carga / vacíos',  NULL, TRUE, TRUE, TRUE, 1, 1, now(), now())
ON CONFLICT (id) DO UPDATE SET
    concept_cost_budget_sale_family_id = EXCLUDED.concept_cost_budget_sale_family_id,
    name        = EXCLUDED.name,
    description = EXCLUDED.description,
    to_cost     = EXCLUDED.to_cost,
    to_budget   = EXCLUDED.to_budget,
    to_sale     = EXCLUDED.to_sale,
    write_uid   = EXCLUDED.write_uid,
    write_date  = now();

-- Keep the sequence in sync so the next ORM-created record gets id = 15
-- instead of colliding with these manually-assigned ids.
SELECT setval(
    'concept_cost_budget_sale_id_seq',
    GREATEST((SELECT MAX(id) FROM concept_cost_budget_sale), 1),
    true
);
