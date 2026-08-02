from psycopg2 import IntegrityError

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class FleetGarage(models.Model):
    """Garages or parking places where the fleet vehicles are stored.

    Kept as a standalone model so it can evolve later (e.g. linking
    ``fleet.vehicle`` records to a garage) without changing the base structure.
    """

    _name = "fleet.garage"
    _description = "Fleet Garage"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    res_company_id: int = fields.Many2one(
        comodel_name="res.company",
        string="Empresa",
        required=True,
        tracking=True,
        index=True,
        default=lambda self: self.env.company,
    )

    name: str = fields.Char(
        string="Cochera",
        required=True,
        tracking=True,
    )

    # Address fields mirroring res.partner/res.company.
    street: str = fields.Char(string="Dirección")
    city: str = fields.Char(string="Ciudad")
    state_id: int = fields.Many2one(
        comodel_name="res.country.state",
        string="Provincia",
        ondelete="restrict",
        domain="[('country_id', '=?', country_id)]",
    )
    zip: str = fields.Char(string="Código Postal")
    country_id: int = fields.Many2one(
        comodel_name="res.country",
        string="País",
        ondelete="restrict",
    )

    # Geolocation fields mirroring res.partner (partner_latitude/longitude).
    latitude: float = fields.Float(
        string="Latitud",
        digits=(10, 7),
        tracking=True,
    )
    longitude: float = fields.Float(
        string="Longitud",
        digits=(10, 7),
        tracking=True,
    )

    # Contact fields mirroring res.partner (phone/email).
    phone: str = fields.Char(string="Teléfono")
    email: str = fields.Char(string="eMail")

    # Contact person mirroring fleet.vehicle.driver_id.
    contact: int = fields.Many2one(
        comodel_name="res.partner",
        string="Persona de contacto",
        tracking=True,
        copy=False,
    )

    _sql_constraints = [
        (
            "company_name_uniq",
            "unique(res_company_id, name)",
            "A garage with this name already exists for this company. "
            "Please use a different name.",
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        try:
            return super().create(vals_list)
        except IntegrityError as e:
            if "company_name_uniq" in str(e):
                raise UserError(
                    _(
                        "A garage with this name already exists for this "
                        "company. Please use a different name."
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
            if "company_name_uniq" in str(e):
                raise UserError(
                    _(
                        "A garage with this name already exists for this "
                        "company. Please use a different name."
                    )
                ) from e
            raise
