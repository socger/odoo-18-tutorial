from psycopg2 import IntegrityError

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"

    vehicle_type_id = fields.Many2one(
        comodel_name="vehicle.type",
        string="Vehicle Type",
        required=True,
        tracking=True,
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
    ]

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
        except IntegrityError as e:
            if "model_license_plate_unique" in str(e):
                raise UserError(
                    _("A vehicle with this model and license plate " "already exists.")
                ) from e
            if "vehicle_type_license_plate_unique" in str(e):
                raise UserError(
                    _("A vehicle with this type and license plate " "already exists.")
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
