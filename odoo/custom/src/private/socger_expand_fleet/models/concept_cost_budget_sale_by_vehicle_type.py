from odoo import fields, models


class ConceptCostBudgetSaleByVehicleType(models.Model):
    _name = "concept.cost.budget.sale.by.vehicle.type"
    _description = "Concept Cost Budget Sale By Vehicle Type"

    vehicle_type_id = fields.Many2one(
        string="Tipo de vehículo",
        comodel_name="vehicle.type",
        required=True,
        ondelete="restrict",
        index=True,
    )
    concept_cost_budget_sale_id = fields.Many2one(
        string="Concepto",
        comodel_name="concept.cost.budget.sale",
        required=True,
        ondelete="restrict",
        index=True,
    )
    value = fields.Float(string="Valor", required=True)
    price_guide = fields.Char(string="Guía de precios")
    description = fields.Char(string="Descripción")

    _sql_constraints = [
        (
            "vehicle_type_concept_unique",
            "UNIQUE(vehicle_type_id, concept_cost_budget_sale_id)",
            "The concept must be unique per vehicle type.",
        ),
    ]
