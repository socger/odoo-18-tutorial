#!/usr/bin/env bash
# Seed concept.cost.budget.sale.by.vehicle.type records into the Odoo `devel`
# database running in the `db` container of the Doodba docker-compose stack.
#
# Generates 18 vehicle_types x 14 concepts = 252 rows via CROSS JOIN over the
# current contents of vehicle_type. Auto-extensible: re-run after adding a new
# vehicle_type and its 14 rows are created automatically.
#
# Usage (from anywhere):
#   ./resources/scripts/seeds/concept_cost_budget_sale_by_vehicle_type/run.sh
#
# Requires: `invoke start` already run (db container up), the
# `socger_expand_fleet` module installed (table
# concept_cost_budget_sale_by_vehicle_type exists), and BOTH the vehicle_type
# seed (ids 1-18) AND the concept_cost_budget_sale seed (ids 1-14) already
# loaded (this seed references both via FKs).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEED_FILE="$SCRIPT_DIR/seed_concept_cost_budget_sale_by_vehicle_type.sql"

if [[ ! -f "$SEED_FILE" ]]; then
    echo "ERROR: seed file not found: $SEED_FILE" >&2
    exit 1
fi

# Resolve the docker-compose project root (four levels up from
# resources/scripts/seeds/concept_cost_budget_sale_by_vehicle_type/).
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
COMPOSE_FILE="$PROJECT_ROOT/devel.yaml"

if [[ ! -f "$COMPOSE_FILE" ]]; then
    echo "ERROR: devel.yaml not found at $COMPOSE_FILE" >&2
    exit 1
fi

echo "Loading concept_cost_budget_sale_by_vehicle_type seed data into 'devel' (container db)..."
docker compose -f "$COMPOSE_FILE" --project-directory "$PROJECT_ROOT" \
    exec -T db psql -U odoo -d devel < "$SEED_FILE"

echo "Done. Verify with:"
echo "  docker compose -f \"$COMPOSE_FILE\" exec -T db psql -U odoo -d devel \\"
echo "    -c 'SELECT count(*) FROM concept_cost_budget_sale_by_vehicle_type;'"
echo "  docker compose -f \"$COMPOSE_FILE\" exec -T db psql -U odoo -d devel \\"
echo "    -c 'SELECT vehicle_type_id, concept_cost_budget_sale_id, description, value, price_guide FROM concept_cost_budget_sale_by_vehicle_type ORDER BY vehicle_type_id, concept_cost_budget_sale_id LIMIT 30;'"
