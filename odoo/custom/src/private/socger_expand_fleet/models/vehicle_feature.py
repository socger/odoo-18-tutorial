from odoo import fields, models


class VehicleFeature(models.Model):
    _name = "vehicle.feature"
    _description = "Vehicle Feature"

    vehicle_feature_category_id: int = fields.Many2one(
        comodel_name="vehicle.feature.category",
        required=True,
        ondelete="restrict",
        index="btree",
    )
    name: str = fields.Char(required=True, index="btree")

    _sql_constraints = [
        (
            "category_name_unique",
            "UNIQUE(vehicle_feature_category_id, name)",
            "The feature name must be unique per category.",
        ),
    ]
