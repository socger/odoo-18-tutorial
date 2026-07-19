-- Seed data for vehicle.feature.category (model in socger_expand_fleet).
-- Table name in Postgres: vehicle_feature_category
-- (Odoo maps "vehicle.feature.category" -> "vehicle_feature_category").
--
-- Idempotent upsert: re-run safely. On conflict by id, it updates
-- name/description/write metadata and preserves create_* fields.
-- description is set to NULL explicitly (not empty string).
--
-- Run manually from repo root:
--   docker compose exec -T db psql -U odoo -d devel \
--     < resources/scripts/seeds/vehicle_feature_category/seed_vehicle_feature_category.sql
-- or via the wrapper:
--   ./resources/scripts/seeds/vehicle_feature_category/run.sh

SET client_encoding TO 'UTF8';

INSERT INTO vehicle_feature_category
    (id, name, description, create_uid, write_uid, create_date, write_date)
VALUES
    (1, 'Confort',            NULL, 1, 1, now(), now()),
    (2, 'Tecnología',         NULL, 1, 1, now(), now()),
    (3, 'Accesibilidad',      NULL, 1, 1, now(), now()),
    (4, 'Seguridad',          NULL, 1, 1, now(), now()),
    (5, 'Equipaje',           NULL, 1, 1, now(), now()),
    (6, 'Servicios premium',  NULL, 1, 1, now(), now()),
    (7, 'Turismo',            NULL, 1, 1, now(), now()),
    (8, 'Conductor',          NULL, 1, 1, now(), now()),
    (9, 'Medio ambiente',     NULL, 1, 1, now(), now())
ON CONFLICT (id) DO UPDATE SET
    name        = EXCLUDED.name,
    description = EXCLUDED.description,
    write_uid   = EXCLUDED.write_uid,
    write_date  = now();

-- Keep the sequence in sync so the next ORM-created record gets id = 10
-- instead of colliding with these manually-assigned ids.
SELECT setval(
    'vehicle_feature_category_id_seq',
    GREATEST((SELECT MAX(id) FROM vehicle_feature_category), 1),
    true
);
