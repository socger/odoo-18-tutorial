from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ConceptCostBudgetSale(models.Model):
    _name = "concept.cost.budget.sale"
    _description = "Concept Cost Budget Sale"

    concept_cost_budget_sale_family_id = fields.Many2one(
        string="Categoría",
        comodel_name="concept.cost.budget.sale.family",
        required=True,
        ondelete="restrict",
        index=True,
    )
    name = fields.Char(string="Concepto", required=True, index=True)
    description = fields.Char(string="Descripción", required=False)
    to_cost = fields.Boolean(string="Para costes", default=False)
    to_budget = fields.Boolean(string="Para presupuestos", default=False)
    to_sale = fields.Boolean(string="Para ventas", default=False)

    _sql_constraints = [
        (
            "name_family_unique",
            "UNIQUE(concept_cost_budget_sale_family_id, name)",
            "The concept name must be unique per family.",
        ),
    ]

    @api.constrains("to_cost", "to_budget", "to_sale")
    def _check_at_least_one_flag(self):
        for record in self:
            if not (record.to_cost or record.to_budget or record.to_sale):
                raise ValidationError(
                    _(
                        "At least one of the following flags must be "
                        "selected: to_cost, to_budget or to_sale."
                    )
                )
