from psycopg2 import IntegrityError

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class FleetVehicleModel(models.Model):
    _inherit = "fleet.vehicle.model"

    vehicle_type_id = fields.Many2one(
        comodel_name="vehicle.type",
        string="Vehicle Type",
        required=True,
        tracking=True,
    )

    _sql_constraints = [
        (
            "vehicle_type_model_name_unique",
            "UNIQUE(vehicle_type_id, name)",
            "The model name must be unique per vehicle type.",
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        try:
            return super().create(vals_list)
        except IntegrityError as e:
            if "vehicle_type_model_name_unique" in str(e):
                raise UserError(
                    _(
                        "A model with this name already exists for the "
                        "selected vehicle type."
                    )
                ) from e
            raise

    def write(self, vals):
        try:
            return super().write(vals)
        except IntegrityError as e:
            if "vehicle_type_model_name_unique" in str(e):
                raise UserError(
                    _(
                        "A model with this name already exists for the "
                        "selected vehicle type."
                    )
                ) from e
            raise
