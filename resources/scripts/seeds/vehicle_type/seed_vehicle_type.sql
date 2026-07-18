-- Seed data for vehicle.type (model in socger_expand_fleet).
-- Table name in Postgres: vehicle_type (Odoo maps "vehicle.type" -> "vehicle_type").
--
-- Idempotent upsert: re-run safely. On conflict by id, it updates
-- name/seats/description/write metadata and preserves create_* fields.
--
-- Run manually from repo root:
--   docker compose exec -T db psql -U odoo -d devel \
--     < resources/scripts/seeds/vehicle_type/seed_vehicle_type.sql
-- or via the wrapper:
--   ./resources/scripts/seeds/vehicle_type/run.sh

SET client_encoding TO 'UTF8';

INSERT INTO vehicle_type
    (id, name, seats, description, create_uid, write_uid, create_date, write_date)
VALUES
    (1,  'Microbús',                          '8–19',      'Traslados privados, eventos, hoteles, aeropuertos',                1, 1, now(), now()),
    (2,  'Minibús',                           '20–35',     'Excursiones, colegios, empresas, grupos pequeños',                1, 1, now(), now()),
    (3,  'Midibús',                           '36–45',     'Viajes de media distancia, turismo',                              1, 1, now(), now()),
    (4,  'Autocar estándar',                  '46–55',     'Excursiones, viajes nacionales, transporte de grupos',            1, 1, now(), now()),
    (5,  'Autocar de gran capacidad',         '56–70',     'Grandes grupos, eventos, congresos',                              1, 1, now(), now()),
    (6,  'Autocar de dos pisos (Double Decker)', '70–90',  'Grandes eventos y viajes turísticos',                             1, 1, now(), now()),
    (7,  'Autocar VIP / Premium',             '20–40',     'Viajes ejecutivos, equipos deportivos, clientes premium',         1, 1, now(), now()),
    (8,  'Autobús de lujo',                   '30–55',     'Largos recorridos con máximo confort',                            1, 1, now(), now()),
    (9,  'Autobús escolar',                   '30–60',     'Transporte escolar y excursiones educativas',                     1, 1, now(), now()),
    (10, 'Autobús urbano',                    '60–100',    'Eventos, transporte lanzadera (shuttle), movilidad urbana',       1, 1, now(), now()),
    (11, 'Autobús articulado',                '100–150',   'Grandes eventos y transporte masivo',                             1, 1, now(), now()),
    (12, 'Autobús lanzadera (Shuttle)',       '20–60',     'Aeropuertos, hoteles, ferias y congresos',                        1, 1, now(), now()),
    (13, 'Autobús adaptado PMR',              '20–60',     'Transporte accesible para personas con movilidad reducida',       1, 1, now(), now()),
    (14, 'Autobús para equipos deportivos',   '40–55',     'Clubes deportivos con espacio para equipaje',                     1, 1, now(), now()),
    (15, 'Autobús turístico panorámico',      '40–80',     'Rutas turísticas y visitas guiadas',                              1, 1, now(), now()),
    (16, 'Autobús para bodas y eventos',      'Variable',  'Transporte de invitados',                                         1, 1, now(), now()),
    (17, 'Autobús para incentivos y empresas','20–55',     'Eventos corporativos y convenciones',                             1, 1, now(), now()),
    (18, 'Autobús nocturno / Discobús',       '30–55',     'Fiestas, despedidas y eventos especiales',                        1, 1, now(), now())
ON CONFLICT (id) DO UPDATE SET
    name        = EXCLUDED.name,
    seats       = EXCLUDED.seats,
    description = EXCLUDED.description,
    write_uid   = EXCLUDED.write_uid,
    write_date  = now();

-- Keep the sequence in sync so the next ORM-created record gets id = 19
-- instead of colliding with these manually-assigned ids.
SELECT setval(
    'vehicle_type_id_seq',
    GREATEST((SELECT MAX(id) FROM vehicle_type), 1),
    true
);
