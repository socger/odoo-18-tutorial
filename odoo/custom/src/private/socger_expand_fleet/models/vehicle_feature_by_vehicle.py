from odoo import fields, models


class VehicleFeatureByVehicle(models.Model):
    _name = "vehicle.feature.by.vehicle"
    _description = "Vehicle Feature By Vehicle"

    fleet_vehicle_id: int = fields.Many2one(
        comodel_name="fleet.vehicle",
        string="Vehículo",
        required=True,
        ondelete="restrict",
        index="btree",
    )
    vehicle_feature_id: int = fields.Many2one(
        comodel_name="vehicle.feature",
        string="Características",
        required=True,
        ondelete="restrict",
        index="btree",
    )

    _sql_constraints = [
        (
            "vehicle_feature_unique",
            "UNIQUE(fleet_vehicle_id, vehicle_feature_id)",
            "The feature must be unique per vehicle.",
        ),
    ]
