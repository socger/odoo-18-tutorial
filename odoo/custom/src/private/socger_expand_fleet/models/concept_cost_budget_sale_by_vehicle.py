from psycopg2 import IntegrityError

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ConceptCostBudgetSaleByVehicle(models.Model):
    _name = "concept.cost.budget.sale.by.vehicle"
    _description = "Concept Cost Budget Sale By Vehicle"

    fleet_vehicle_id = fields.Many2one(
        comodel_name="fleet.vehicle",
        string="Vehículo",
        required=True,
        ondelete="restrict",
        tracking=True,
        index="btree",
    )
    concept_cost_budget_sale_by_vehicle_type_id = fields.Many2one(
        comodel_name="concept.cost.budget.sale.by.vehicle.type",
        string="Concepto por tipo de vehículo",
        required=True,
        ondelete="restrict",
        tracking=True,
        index="btree",
    )

    _sql_constraints = [
        (
            "vehicle_concept_unique",
            "UNIQUE(fleet_vehicle_id, concept_cost_budget_sale_by_vehicle_type_id)",
            "The concept must be unique per vehicle.",
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        try:
            return super().create(vals_list)
        except IntegrityError as e:
            if "vehicle_concept_unique" in str(e):
                raise UserError(
                    _("This concept is already assigned to the selected vehicle.")
                ) from e
            raise

    def write(self, vals):
        try:
            return super().write(vals)
        except IntegrityError as e:
            if "vehicle_concept_unique" in str(e):
                raise UserError(
                    _("This concept is already assigned to the selected vehicle.")
                ) from e
            raise
