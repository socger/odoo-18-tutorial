from odoo import fields, models


class VehicleFeatureCategory(models.Model):
    _name = "vehicle.feature.category"
    _description = "Vehicle Feature Category"

    name: str = fields.Char(required=True, index="btree")
    description: str = fields.Char()

    _sql_constraints = [
        (
            "name_unique",
            "UNIQUE(name)",
            "The category name must be unique.",
        ),
    ]
