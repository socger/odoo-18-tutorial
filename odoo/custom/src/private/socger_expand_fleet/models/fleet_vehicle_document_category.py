from psycopg2 import IntegrityError

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class FleetVehicleDocumentCategory(models.Model):
    """Document categories for the fleet vehicles.

    Categories are hierarchical: a category may have a parent category, which
    lets the module group documents (ITV, insurance, driving licence, ...) and
    evolve later (e.g. linking categories to ``fleet.vehicle.document``) without
    changing the base structure.
    """

    _name = "fleet.vehicle.document.category"
    _description = "Fleet Vehicle Document Category"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name: str = fields.Char(
        string="Nombre",
        required=True,
        tracking=True,
    )

    fleet_vehicle_document_category_id: int = fields.Many2one(
        comodel_name="fleet.vehicle.document.category",
        string="Categoría padre",
        required=False,
        tracking=True,
    )

    _sql_constraints = [
        (
            "name_unique",
            "UNIQUE(name)",
            "The document category name must be unique.",
        ),
    ]

    @api.constrains("fleet_vehicle_document_category_id")
    def _check_category_recursion(self):
        if self._has_cycle("fleet_vehicle_document_category_id"):
            raise ValidationError(
                _(
                    "You cannot create recursive document categories: a "
                    "category cannot be its own parent nor the parent of one "
                    "of its ancestors."
                )
            )

    @api.model_create_multi
    def create(self, vals_list):
        try:
            return super().create(vals_list)
        except IntegrityError as e:
            if "name_unique" in str(e):
                raise UserError(
                    _(
                        "A document category with this name already exists. "
                        "Please use a different name."
                    )
                ) from e
            raise

    def write(self, vals):
        try:
            result = super().write(vals)
            # Write is lazy since Odoo 16: the SQL UPDATE only happens at the
            # next flush. Force it here so a unique-constraint violation is
            # caught and reported as a friendly UserError instead of a raw DB
            # error surfacing later in the transaction.
            self.flush_model()
            return result
        except IntegrityError as e:
            if "name_unique" in str(e):
                raise UserError(
                    _(
                        "A document category with this name already exists. "
                        "Please use a different name."
                    )
                ) from e
            raise
