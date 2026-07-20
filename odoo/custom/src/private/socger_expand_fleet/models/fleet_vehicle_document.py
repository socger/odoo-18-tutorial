from odoo import api, fields, models


class IrAttachment(models.Model):
    """Extend ir.attachment to expose a real Many2one to fleet.vehicle.

    Documents attached to fleet vehicles are stored in ``ir.attachment`` and
    linked to the vehicle through the polymorphic pair ``res_model`` /
    ``res_id``. Exposing a dedicated, stored and indexed ``fleet_vehicle_id``
    field makes it possible to filter, group by and order by vehicle directly
    from the views, while keeping the canonical storage untouched.

    Future extensions (document type, expiry date, etc.) can be added on this
    inherited model without modifying the base one.
    """

    _inherit = "ir.attachment"

    fleet_vehicle_id: int = fields.Many2one(
        comodel_name="fleet.vehicle",
        string="Vehículo",
        compute="_compute_fleet_vehicle_id",
        inverse="_inverse_fleet_vehicle_id",
        store=True,
        index="btree",
        readonly=False,
        ondelete="restrict",
    )

    @api.depends("res_model", "res_id")
    def _compute_fleet_vehicle_id(self):
        for attachment in self:
            if attachment.res_model == "fleet.vehicle" and attachment.res_id:
                attachment.fleet_vehicle_id = attachment.res_id
            else:
                attachment.fleet_vehicle_id = False

    def _inverse_fleet_vehicle_id(self):
        for attachment in self:
            if attachment.fleet_vehicle_id:
                attachment.res_model = "fleet.vehicle"
                attachment.res_id = attachment.fleet_vehicle_id.id
