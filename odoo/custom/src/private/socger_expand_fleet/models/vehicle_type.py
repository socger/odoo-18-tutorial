from odoo import fields, models


class VehicleType(models.Model):
    _name = "vehicle.type"
    _description = "Vehicle Type"
    _order = "description asc"

    name = fields.Char(required=True)
    seats = fields.Char(required=True)
    description = fields.Char()
    concept_cost_budget_sale_by_vehicle_type_ids = fields.One2many(
        comodel_name="concept.cost.budget.sale.by.vehicle.type",
        inverse_name="vehicle_type_id",
        string="Concepts Cost Budget Sale By Vehicle Type",
    )
