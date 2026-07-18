from odoo import fields, models


class ConceptCostBudgetSaleFamily(models.Model):
    _name = "concept.cost.budget.sale.family"
    _description = "Concept Cost Budget Sale Family"

    name = fields.Char(required=True)
    description = fields.Char()

    _sql_constraints = [
        (
            "name_unique",
            "UNIQUE(name)",
            "The family name must be unique.",
        ),
    ]
