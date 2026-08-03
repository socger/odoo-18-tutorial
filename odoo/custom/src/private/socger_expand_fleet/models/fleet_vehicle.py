from dateutil.relativedelta import relativedelta
from psycopg2 import IntegrityError

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"

    vehicle_type_id = fields.Many2one(
        comodel_name="vehicle.type",
        string="Vehicle Type",
        required=True,
        tracking=True,
    )
    fleet_garage_id: int = fields.Many2one(
        comodel_name="fleet.garage",
        string="Cochera",
        required=True,
        tracking=True,
        ondelete="restrict",
    )
    vehicle_feature_by_vehicle_ids = fields.One2many(
        comodel_name="vehicle.feature.by.vehicle",
        inverse_name="fleet_vehicle_id",
        string="Vehicle Features",
    )
    concept_cost_budget_sale_by_vehicle_ids = fields.One2many(
        comodel_name="concept.cost.budget.sale.by.vehicle",
        inverse_name="fleet_vehicle_id",
        string="Concept Cost Budget Sale By Vehicle",
    )
    odometer_date = fields.Date(
        string="Km actualizados el",
        compute="_compute_odometer_date",
    )
    vehicle_code = fields.Char(
        string="Código de vehículo",
        required=True,
        tracking=True,
    )
    res_company_id = fields.Many2one(
        comodel_name="res.company",
        string="Empresa",
        required=False,
        tracking=True,
    )
    res_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Empresa colaboradora",
        required=False,
        tracking=True,
    )
    license_plate_with_code = fields.Char(
        string="Matrícula / Código",
        compute="_compute_license_plate_with_code",
        store=True,
    )
    # === Vehicle identification details === #
    engine_Chassis = fields.Char(
        string="Motor/chasis",
        tracking=True,
    )
    bodywork = fields.Char(
        string="Carrocería",
        tracking=True,
    )
    build_Number = fields.Char(
        string="Nº. de obra",
        tracking=True,
    )
    mileage_at_purchase = fields.Float(
        string="Km cuando se compró",
        tracking=True,
    )
    seating_capacity_per_permit = fields.Integer(
        string="Plazas - según permiso",
        required=True,
        tracking=True,
    )
    seating_capacity_per_technical_datasheet = fields.Char(
        string="Plazas - según ficha técnica",
        required=True,
        tracking=True,
    )
    seating_capacity_bookable_seats = fields.Integer(
        string="Plazas - Ofertables",
        required=True,
        tracking=True,
    )
    special_configurations = fields.Html(
        string="Configuraciones especiales",
        tracking=True,
    )
    vehicle_age = fields.Integer(
        string="Edad del vehículo",
        compute="_compute_vehicle_age",
    )
    driver_id = fields.Many2one(
        comodel_name="res.partner",
        string="Conductor habitual",
    )
    digital_tachograph = fields.Boolean(
        string="Tacógrafo digital",
        default=True,
        tracking=True,
    )
    professional_diesel_tax_relief_beneficiary = fields.Boolean(
        string="Beneficiario gasoleo profesional",
        default=True,
        tracking=True,
    )
    accounting_national_mileage = fields.Char(
        string="Contabilidad - km nacional",
        tracking=True,
    )
    accounting_international_mileage = fields.Char(
        string="Contabilidad - km internacional",
        tracking=True,
    )
    accounting_accounting_project = fields.Char(
        string="Contabilidad - proyecto contable",
        tracking=True,
    )

    @api.depends("license_plate", "vehicle_code")
    def _compute_license_plate_with_code(self):
        """Concatenate license plate and vehicle code for pivot/activity views."""
        for record in self:
            parts = [
                part for part in (record.license_plate, record.vehicle_code) if part
            ]
            record.license_plate_with_code = " / ".join(parts)

    @api.depends()
    def _compute_odometer_date(self):
        """Return the date of the odometer log holding the current odometer value."""
        Odometer = self.env["fleet.vehicle.odometer"]
        for record in self:
            odometer_log = Odometer.search(
                [("vehicle_id", "=", record.id)],
                limit=1,
                order="value desc",
            )
            record.odometer_date = odometer_log.date if odometer_log else False

    @api.depends("acquisition_date", "write_off_date")
    def _compute_vehicle_age(self):
        """Age of the vehicle in years, measured at the write-off date when set,
        otherwise at today's date."""
        today = fields.Date.context_today(self)
        for record in self:
            end_date = record.write_off_date or today
            if record.acquisition_date and end_date >= record.acquisition_date:
                record.vehicle_age = relativedelta(
                    end_date, record.acquisition_date
                ).years
            else:
                record.vehicle_age = 0

    _sql_constraints = [
        (
            "model_license_plate_unique",
            "UNIQUE(model_id, license_plate)",
            "A vehicle with this model and license plate already exists.",
        ),
        (
            "vehicle_type_license_plate_unique",
            "UNIQUE(vehicle_type_id, license_plate)",
            "A vehicle with this type and license plate already exists.",
        ),
        (
            "vehicle_code_unique",
            "UNIQUE(vehicle_code)",
            "A vehicle with this vehicle code already exists.",
        ),
        (
            "res_company_vehicle_code_unique",
            "UNIQUE(res_company_id, vehicle_code)",
            "A vehicle with this vehicle code already exists for this company.",
        ),
        (
            "res_partner_vehicle_code_unique",
            "UNIQUE(res_partner_id, vehicle_code)",
            "A vehicle with this vehicle code already exists for this partner.",
        ),
    ]

    @api.constrains("res_company_id", "res_partner_id")
    def _check_company_partner_exclusive(self):
        """A vehicle cannot have both a company and a partner assigned."""
        for record in self:
            if record.res_company_id and record.res_partner_id:
                raise ValidationError(
                    _(
                        "A vehicle cannot be assigned to both a company "
                        "and a partner. Please choose only one of them."
                    )
                )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("model_id") and not vals.get("vehicle_type_id"):
                model = self.env["fleet.vehicle.model"].browse(vals["model_id"])
                vals["vehicle_type_id"] = model.vehicle_type_id.id
        try:
            vehicles = super().create(vals_list)
        except IntegrityError as e:
            if "model_license_plate_unique" in str(e):
                raise UserError(
                    _("A vehicle with this model and license plate " "already exists.")
                ) from e
            if "vehicle_type_license_plate_unique" in str(e):
                raise UserError(
                    _("A vehicle with this type and license plate " "already exists.")
                ) from e
            if "vehicle_code_unique" in str(e):
                raise UserError(
                    _("A vehicle with this vehicle code already exists.")
                ) from e
            if "res_company_vehicle_code_unique" in str(e):
                raise UserError(
                    _(
                        "A vehicle with this vehicle code already exists "
                        "for this company."
                    )
                ) from e
            if "res_partner_vehicle_code_unique" in str(e):
                raise UserError(
                    _(
                        "A vehicle with this vehicle code already exists "
                        "for this partner."
                    )
                ) from e
            raise
        for vehicle in vehicles:
            vehicle._create_concept_records()
        return vehicles

    def write(self, vals):
        if vals.get("model_id") and "vehicle_type_id" not in vals:
            model = self.env["fleet.vehicle.model"].browse(vals["model_id"])
            vals["vehicle_type_id"] = model.vehicle_type_id.id
        try:
            result = super().write(vals)
            # Write is lazy since Odoo 16: the SQL UPDATE only happens at the
            # next flush. Force it here so a unique-constraint violation is
            # caught and reported as a friendly UserError instead of a raw DB
            # error surfacing later in the transaction.
            self.flush_model()
        except IntegrityError as e:
            if "model_license_plate_unique" in str(e):
                raise UserError(
                    _("A vehicle with this model and license plate " "already exists.")
                ) from e
            if "vehicle_type_license_plate_unique" in str(e):
                raise UserError(
                    _("A vehicle with this type and license plate " "already exists.")
                ) from e
            if "vehicle_code_unique" in str(e):
                raise UserError(
                    _("A vehicle with this vehicle code already exists.")
                ) from e
            if "res_company_vehicle_code_unique" in str(e):
                raise UserError(
                    _(
                        "A vehicle with this vehicle code already exists "
                        "for this company."
                    )
                ) from e
            if "res_partner_vehicle_code_unique" in str(e):
                raise UserError(
                    _(
                        "A vehicle with this vehicle code already exists "
                        "for this partner."
                    )
                ) from e
            raise
        if "vehicle_type_id" in vals:
            for vehicle in self:
                vehicle._create_concept_records()
        return result

    def _create_concept_records(self):
        """Create concept_cost_budget_sale_by_vehicle records for this vehicle
        based on the associated vehicle_type_id."""
        self.ensure_one()
        if not self.vehicle_type_id:
            return
        concepts = self.env["concept.cost.budget.sale.by.vehicle.type"].search(
            [("vehicle_type_id", "=", self.vehicle_type_id.id)]
        )
        for concept in concepts:
            existing = self.env["concept.cost.budget.sale.by.vehicle"].search_count(
                [
                    ("fleet_vehicle_id", "=", self.id),
                    (
                        "concept_cost_budget_sale_by_vehicle_type_id",
                        "=",
                        concept.id,
                    ),
                ]
            )
            if not existing:
                self.env["concept.cost.budget.sale.by.vehicle"].create(
                    {
                        "fleet_vehicle_id": self.id,
                        "concept_cost_budget_sale_by_vehicle_type_id": concept.id,
                        "value": concept.value,
                        "description": concept.description,
                    }
                )

    @api.onchange("model_id")
    def _onchange_model_id(self):
        if self.model_id and self.model_id.vehicle_type_id:
            self.vehicle_type_id = self.model_id.vehicle_type_id
