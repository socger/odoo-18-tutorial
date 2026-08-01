from psycopg2 import IntegrityError

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class IrAttachment(models.Model):
    """Extend ir.attachment to expose a real Many2one to fleet.vehicle.

    Documents attached to fleet vehicles are stored in ``ir.attachment`` and
    linked to the vehicle through the polymorphic pair ``res_model`` /
    ``res_id``. Exposing a dedicated, stored and indexed ``fleet_vehicle_id``
    field makes it possible to filter, group by and order by vehicle directly
    from the views, while keeping the canonical storage untouched.

    Each document can be assigned a document category. The tuple
    ``(fleet_vehicle_id, fleet_vehicle_document_category_id, name)`` is unique,
    so the same document cannot be attached twice to the same vehicle under the
    same category.

    Future extensions (expiry date, reminders, ...) can be added on this
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

    fleet_vehicle_document_category_id: int = fields.Many2one(
        comodel_name="fleet.vehicle.document.category",
        string="Categoría",
        required=False,
        tracking=True,
    )

    _sql_constraints = [
        (
            "fleet_vehicle_document_category_unique",
            "UNIQUE(fleet_vehicle_id, fleet_vehicle_document_category_id, name)",
            "A fleet vehicle document with the same category and name already "
            "exists for this vehicle.",
        ),
    ]

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

    def _handle_unique_constraint_error(self, e):
        for name, _definition, message in self._sql_constraints:
            if name in str(e):
                raise UserError(_(message)) from e
        raise

    @api.model_create_multi
    def create(self, vals_list):
        try:
            records = super().create(vals_list)
            if any(vals.get("res_model") == "fleet.vehicle" for vals in vals_list):
                # ``fleet_vehicle_id`` is a stored computed field whose SQL write
                # is deferred until the next flush. Force it here for fleet
                # documents so a unique-constraint violation is caught and
                # reported as a friendly UserError instead of a raw DB error
                # surfacing later in the transaction.
                records.flush_model()
            return records
        except IntegrityError as e:
            self._handle_unique_constraint_error(e)

    def write(self, vals):
        tracked_fields = {
            "res_model",
            "res_id",
            "fleet_vehicle_id",
            "fleet_vehicle_document_category_id",
            "name",
        }
        if not tracked_fields.intersection(vals):
            return super().write(vals)
        try:
            result = super().write(vals)
            # Write is lazy since Odoo 16: the SQL UPDATE only happens at the
            # next flush. Force it here so a unique-constraint violation is
            # caught and reported as a friendly UserError instead of a raw DB
            # error surfacing later in the transaction.
            self.flush_model()
            return result
        except IntegrityError as e:
            self._handle_unique_constraint_error(e)
