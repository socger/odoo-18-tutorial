#!/usr/bin/env bash
# Seed vehicle.feature records into the Odoo `devel` database
# running in the `db` container of the Doodba docker-compose stack.
#
# Loads 77 features grouped by the 9 vehicle_feature_category rows
# (Confort, Tecnologia, Accesibilidad, Seguridad, Equipaje,
#  Servicios premium, Turismo, Conductor, Medio ambiente).
#
# Usage (from anywhere):
#   ./resources/scripts/seeds/vehicle_feature/run.sh
#
# Requires: `invoke start` already run (db container up), the
# `socger_expand_fleet` module installed (table vehicle_feature exists),
# and the vehicle_feature_category seed (ids 1-9) already loaded
# (this seed references those categories via FK).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEED_FILE="$SCRIPT_DIR/seed_vehicle_feature.sql"

if [[ ! -f "$SEED_FILE" ]]; then
    echo "ERROR: seed file not found: $SEED_FILE" >&2
    exit 1
fi

# Resolve the docker-compose project root (four levels up from
# resources/scripts/seeds/vehicle_feature/).
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
COMPOSE_FILE="$PROJECT_ROOT/devel.yaml"

if [[ ! -f "$COMPOSE_FILE" ]]; then
    echo "ERROR: devel.yaml not found at $COMPOSE_FILE" >&2
    exit 1
fi

echo "Loading vehicle_feature seed data into 'devel' (container db)..."
docker compose -f "$COMPOSE_FILE" --project-directory "$PROJECT_ROOT" \
    exec -T db psql -U odoo -d devel < "$SEED_FILE"

echo "Done. Verify with:"
echo "  docker compose -f \"$COMPOSE_FILE\" exec -T db psql -U odoo -d devel \\"
echo "    -c 'SELECT count(*) FROM vehicle_feature;'"
echo "  docker compose -f \"$COMPOSE_FILE\" exec -T db psql -U odoo -d devel \\"
echo "    -c 'SELECT vfc.name AS category, vf.name AS feature FROM vehicle_feature vf JOIN vehicle_feature_category vfc ON vfc.id = vf.vehicle_feature_category_id ORDER BY vfc.id, vf.id;'"
