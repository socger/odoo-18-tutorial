-- Seed data for vehicle.feature (model in socger_expand_fleet).
-- Table name in Postgres: vehicle_feature
-- (Odoo maps "vehicle.feature" -> "vehicle_feature").
--
-- Idempotent upsert on the natural key (vehicle_feature_category_id, name),
-- which has a UNIQUE constraint. Ids are assigned by the sequence; re-running
-- the seed updates existing rows in place and does not duplicate.
--
-- Note: the model has NO description field (only name + category). Some
-- feature names repeat across categories (e.g. "Climatizador independiente"
-- in cat 1 and cat 8); the UNIQUE constraint is on the (category, name) pair
-- so there is no conflict.
--
-- Depends on: vehicle_feature_category seed (ids 1-9) already loaded.
--
-- Run manually from repo root:
--   docker compose exec -T db psql -U odoo -d devel \
--     < resources/scripts/seeds/vehicle_feature/seed_vehicle_feature.sql
-- or via the wrapper:
--   ./resources/scripts/seeds/vehicle_feature/run.sh

SET client_encoding TO 'UTF8';

INSERT INTO vehicle_feature
    (vehicle_feature_category_id, name, create_uid, write_uid, create_date, write_date)
VALUES
    -- Category 1: Confort (12)
    (1, 'Aire acondicionado',                        1, 1, now(), now()),
    (1, 'Calefacción',                               1, 1, now(), now()),
    (1, 'Asientos reclinables',                      1, 1, now(), now()),
    (1, 'Asientos de cuero',                         1, 1, now(), now()),
    (1, 'Reposapiés',                                1, 1, now(), now()),
    (1, 'Reposabrazos',                              1, 1, now(), now()),
    (1, 'Mesitas plegables',                         1, 1, now(), now()),
    (1, 'Cortinas',                                  1, 1, now(), now()),
    (1, 'Cristales tintados',                        1, 1, now(), now()),
    (1, 'Iluminación LED individual',                1, 1, now(), now()),
    (1, 'Luz de lectura',                            1, 1, now(), now()),
    (1, 'Climatización independiente por pasajero',  1, 1, now(), now()),
    -- Category 2: Tecnología (12)
    (2, 'Wi-Fi',                                     1, 1, now(), now()),
    (2, 'Tomas USB',                                 1, 1, now(), now()),
    (2, 'Enchufes 230 V',                            1, 1, now(), now()),
    (2, 'Cargadores USB-C',                          1, 1, now(), now()),
    (2, 'Pantallas LCD',                             1, 1, now(), now()),
    (2, 'Pantallas individuales',                    1, 1, now(), now()),
    (2, 'Sistema multimedia',                        1, 1, now(), now()),
    (2, 'DVD / Blu-ray',                             1, 1, now(), now()),
    (2, 'Equipo de sonido',                          1, 1, now(), now()),
    (2, 'Micrófono para guía',                       1, 1, now(), now()),
    (2, 'GPS',                                       1, 1, now(), now()),
    (2, 'Seguimiento GPS en tiempo real',            1, 1, now(), now()),
    -- Category 3: Accesibilidad (6)
    (3, 'Plataforma elevadora PMR',                  1, 1, now(), now()),
    (3, 'Rampa de acceso',                           1, 1, now(), now()),
    (3, 'Espacio para silla de ruedas',              1, 1, now(), now()),
    (3, 'Anclajes para silla de ruedas',             1, 1, now(), now()),
    (3, 'Asientos reservados',                       1, 1, now(), now()),
    (3, 'Pasillo ancho',                             1, 1, now(), now()),
    -- Category 4: Seguridad (13)
    (4, 'Cinturones de seguridad',                   1, 1, now(), now()),
    (4, 'ABS',                                       1, 1, now(), now()),
    (4, 'ESP (control de estabilidad)',              1, 1, now(), now()),
    (4, 'Frenado de emergencia',                     1, 1, now(), now()),
    (4, 'Aviso de cambio involuntario de carril',    1, 1, now(), now()),
    (4, 'Control de crucero adaptativo',             1, 1, now(), now()),
    (4, 'Detector de fatiga',                        1, 1, now(), now()),
    (4, 'Cámara de marcha atrás',                    1, 1, now(), now()),
    (4, 'Cámaras 360°',                              1, 1, now(), now()),
    (4, 'Extintores',                                1, 1, now(), now()),
    (4, 'Martillos rompecristales',                  1, 1, now(), now()),
    (4, 'Botiquín',                                  1, 1, now(), now()),
    (4, 'Tacógrafo digital',                         1, 1, now(), now()),
    -- Category 5: Equipaje (5)
    (5, 'Gran maletero',                             1, 1, now(), now()),
    (5, 'Portaequipajes superior',                   1, 1, now(), now()),
    (5, 'Compartimento para esquís',                 1, 1, now(), now()),
    (5, 'Remolque para equipaje',                    1, 1, now(), now()),
    (5, 'Porta bicicletas',                          1, 1, now(), now()),
    -- Category 6: Servicios premium (11)
    (6, 'Nevera',                                    1, 1, now(), now()),
    (6, 'Cafetera',                                  1, 1, now(), now()),
    (6, 'Máquina de café',                           1, 1, now(), now()),
    (6, 'Dispensador de agua',                       1, 1, now(), now()),
    (6, 'WC',                                        1, 1, now(), now()),
    (6, 'Cocina básica',                             1, 1, now(), now()),
    (6, 'Zona VIP',                                  1, 1, now(), now()),
    (6, 'Mesas de reuniones',                        1, 1, now(), now()),
    (6, 'Asientos enfrentados',                      1, 1, now(), now()),
    (6, 'Tapicería premium',                         1, 1, now(), now()),
    (6, 'Iluminación ambiental',                     1, 1, now(), now()),
    -- Category 7: Turismo (5)
    (7, 'Techo panorámico',                          1, 1, now(), now()),
    (7, 'Ventanas panorámicas',                      1, 1, now(), now()),
    (7, 'Techo de cristal',                          1, 1, now(), now()),
    (7, 'Sistema de audio para guía',                1, 1, now(), now()),
    (7, 'Megafonía',                                 1, 1, now(), now()),
    -- Category 8: Conductor (6)
    (8, 'Asiento neumático',                         1, 1, now(), now()),
    (8, 'Climatizador independiente',                1, 1, now(), now()),
    (8, 'Cámara de vigilancia interior',             1, 1, now(), now()),
    (8, 'Sistema de gestión de flotas',              1, 1, now(), now()),
    (8, 'Limitador de velocidad',                    1, 1, now(), now()),
    (8, 'Ayuda al aparcamiento',                     1, 1, now(), now()),
    -- Category 9: Medio ambiente (7)
    (9, 'Motor Euro VI',                             1, 1, now(), now()),
    (9, 'Híbrido',                                   1, 1, now(), now()),
    (9, 'Eléctrico',                                 1, 1, now(), now()),
    (9, 'GNC',                                       1, 1, now(), now()),
    (9, 'Bajo consumo',                              1, 1, now(), now()),
    (9, 'Etiqueta ECO',                              1, 1, now(), now()),
    (9, 'Etiqueta CERO',                             1, 1, now(), now())
ON CONFLICT (vehicle_feature_category_id, name) DO UPDATE SET
    name       = EXCLUDED.name,
    write_uid  = EXCLUDED.write_uid,
    write_date = now();

-- Keep the sequence in sync so the next ORM-created record does not
-- collide with the ids assigned by this bulk insert.
SELECT setval(
    'vehicle_feature_id_seq',
    GREATEST((SELECT MAX(id) FROM vehicle_feature), 1),
    true
);
