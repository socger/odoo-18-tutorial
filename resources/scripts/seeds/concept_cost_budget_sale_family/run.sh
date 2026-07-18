#!/usr/bin/env bash
# Seed concept.cost.budget.sale.family records into the Odoo `devel` database
# running in the `db` container of the Doodba docker-compose stack.
#
# Usage (from anywhere):
#   ./resources/scripts/seeds/concept_cost_budget_sale_family/run.sh
#
# Requires: `invoke start` already run (db container up) and the
# `socger_expand_fleet` module installed (table concept_cost_budget_sale_family
# exists).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEED_FILE="$SCRIPT_DIR/seed_concept_cost_budget_sale_family.sql"

if [[ ! -f "$SEED_FILE" ]]; then
    echo "ERROR: seed file not found: $SEED_FILE" >&2
    exit 1
fi

# Resolve the docker-compose project root (four levels up from
# resources/scripts/seeds/concept_cost_budget_sale_family/).
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
COMPOSE_FILE="$PROJECT_ROOT/devel.yaml"

if [[ ! -f "$COMPOSE_FILE" ]]; then
    echo "ERROR: devel.yaml not found at $COMPOSE_FILE" >&2
    exit 1
fi

echo "Loading concept_cost_budget_sale_family seed data into 'devel' (container db)..."
docker compose -f "$COMPOSE_FILE" --project-directory "$PROJECT_ROOT" \
    exec -T db psql -U odoo -d devel < "$SEED_FILE"

echo "Done. Verify with:"
echo "  docker compose -f \"$COMPOSE_FILE\" exec -T db psql -U odoo -d devel \\"
echo "    -c 'SELECT id, name, description FROM concept_cost_budget_sale_family ORDER BY id;'"
