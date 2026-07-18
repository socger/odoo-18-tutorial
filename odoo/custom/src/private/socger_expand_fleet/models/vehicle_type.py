from odoo import fields, models


class VehicleType(models.Model):
    _name = "vehicle.type"
    _description = "Vehicle Type"
    _order = "description asc"

    name = fields.Char(required=True)
    seats = fields.Char(required=True)
    description = fields.Char()
