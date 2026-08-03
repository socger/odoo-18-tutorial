from dateutil.relativedelta import relativedelta

from odoo import fields
from odoo.exceptions import UserError, ValidationError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestFleetVehicle(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env["res.company"].create({"name": "Empresa de Prueba"})
        cls.partner = cls.env["res.partner"].create({"name": "Colaborador de Prueba"})
        cls.garage = cls.env["fleet.garage"].create(
            {"name": "Cochera de Prueba", "res_company_id": cls.company.id}
        )
        brand = cls.env["fleet.vehicle.model.brand"].create({"name": "Marca de Prueba"})
        cls.model = cls.env["fleet.vehicle.model"].create(
            {"name": "Modelo de Prueba", "brand_id": brand.id}
        )

    def _create_vehicle(self, **kwargs):
        vals = {
            "model_id": self.model.id,
            "fleet_garage_id": self.garage.id,
            "vehicle_code": kwargs.pop("vehicle_code", "VHC-0001"),
            "license_plate": kwargs.pop("license_plate", "0001 ABC"),
            "seating_capacity_per_permit": kwargs.pop("seating_capacity_per_permit", 4),
            "seating_capacity_per_technical_datasheet": kwargs.pop(
                "seating_capacity_per_technical_datasheet", "4"
            ),
            "seating_capacity_bookable_seats": kwargs.pop(
                "seating_capacity_bookable_seats", 4
            ),
        }
        vals.update(kwargs)
        return self.env["fleet.vehicle"].create(vals)

    def test_vehicle_code_field_attributes(self):
        field = self.env["fleet.vehicle"]._fields["vehicle_code"]
        self.assertEqual(field.type, "char")
        self.assertTrue(field.required)
        self.assertTrue(field.tracking)
        self.assertEqual(field.string, "Código de vehículo")

    def test_res_company_id_field_attributes(self):
        field = self.env["fleet.vehicle"]._fields["res_company_id"]
        self.assertEqual(field.comodel_name, "res.company")
        self.assertFalse(field.required)
        self.assertTrue(field.tracking)
        self.assertEqual(field.string, "Empresa")

    def test_res_partner_id_field_attributes(self):
        field = self.env["fleet.vehicle"]._fields["res_partner_id"]
        self.assertEqual(field.comodel_name, "res.partner")
        self.assertFalse(field.required)
        self.assertTrue(field.tracking)
        self.assertEqual(field.string, "Empresa colaboradora")

    def test_vehicle_code_unique_on_create(self):
        self._create_vehicle(vehicle_code="VHC-UNICO", license_plate="0001 ABC")
        with self.assertRaises(UserError):
            self._create_vehicle(vehicle_code="VHC-UNICO", license_plate="0002 ABC")

    def test_vehicle_code_unique_allows_different_code(self):
        first = self._create_vehicle(vehicle_code="VHC-A", license_plate="0001 ABC")
        second = self._create_vehicle(vehicle_code="VHC-B", license_plate="0002 ABC")
        self.assertEqual(len(first | second), 2)

    def test_vehicle_code_unique_on_write(self):
        self._create_vehicle(vehicle_code="VHC-WRITE-A", license_plate="0001 ABC")
        other = self._create_vehicle(
            vehicle_code="VHC-WRITE-B", license_plate="0002 ABC"
        )
        with self.assertRaises(UserError):
            other.vehicle_code = "VHC-WRITE-A"

    def test_company_partner_mutual_exclusion_on_create(self):
        with self.assertRaises(ValidationError):
            self._create_vehicle(
                res_company_id=self.company.id,
                res_partner_id=self.partner.id,
            )

    def test_company_partner_mutual_exclusion_on_write(self):
        vehicle = self._create_vehicle(res_company_id=self.company.id)
        with self.assertRaises(ValidationError):
            vehicle.res_partner_id = self.partner.id

    def test_license_plate_with_code(self):
        vehicle = self._create_vehicle(
            license_plate="0001 ABC",
            vehicle_code="VHC-COD",
        )
        self.assertEqual(vehicle.license_plate_with_code, "0001 ABC / VHC-COD")

    def test_vehicle_identification_fields(self):
        fields_dict = self.env["fleet.vehicle"]._fields
        expected = [
            ("engine_Chassis", "char", "Motor/chasis"),
            ("bodywork", "char", "Carrocería"),
            ("build_Number", "char", "Nº. de obra"),
            ("mileage_at_purchase", "float", "Km cuando se compró"),
            ("seating_capacity_per_permit", "integer", "Plazas - según permiso"),
            (
                "seating_capacity_per_technical_datasheet",
                "char",
                "Plazas - según ficha técnica",
            ),
            ("seating_capacity_bookable_seats", "integer", "Plazas - Ofertables"),
            ("special_configurations", "html", "Configuraciones especiales"),
            ("vehicle_age", "integer", "Edad del vehículo"),
            ("digital_tachograph", "boolean", "Tacógrafo digital"),
            (
                "professional_diesel_tax_relief_beneficiary",
                "boolean",
                "Beneficiario gasoleo profesional",
            ),
            ("accounting_national_mileage", "char", "Contabilidad - km nacional"),
            (
                "accounting_international_mileage",
                "char",
                "Contabilidad - km internacional",
            ),
            (
                "accounting_accounting_project",
                "char",
                "Contabilidad - proyecto contable",
            ),
        ]
        for field_name, field_type, field_string in expected:
            field = fields_dict[field_name]
            self.assertEqual(field.type, field_type, field_name)
            self.assertEqual(field.string, field_string, field_name)
        # All new fields are tracked in the chatter, except ``vehicle_age``:
        # being a non-stored computed field it has no tracking by design.
        for field_name, _, _ in expected:
            if field_name != "vehicle_age":
                field = fields_dict[field_name]
                self.assertTrue(getattr(field, "tracking", False), field_name)

    def test_seating_fields_required(self):
        fields_dict = self.env["fleet.vehicle"]._fields
        for field_name in (
            "seating_capacity_per_permit",
            "seating_capacity_per_technical_datasheet",
            "seating_capacity_bookable_seats",
        ):
            self.assertTrue(fields_dict[field_name].required, field_name)

    def test_boolean_fields_defaults(self):
        vehicle = self._create_vehicle()
        self.assertTrue(vehicle.digital_tachograph)
        self.assertTrue(vehicle.professional_diesel_tax_relief_beneficiary)

    def test_driver_id_relabeled(self):
        field = self.env["fleet.vehicle"]._fields["driver_id"]
        self.assertEqual(field.type, "many2one")
        self.assertEqual(field.comodel_name, "res.partner")
        self.assertEqual(field.string, "Conductor habitual")

    def test_vehicle_age_with_write_off_date(self):
        vehicle = self._create_vehicle(
            acquisition_date="2020-01-01",
            write_off_date="2022-06-15",
        )
        self.assertEqual(vehicle.vehicle_age, 2)

    def test_vehicle_age_without_write_off_date(self):
        today = fields.Date.context_today(self.env["fleet.vehicle"])
        vehicle = self._create_vehicle(
            acquisition_date=today - relativedelta(years=5),
        )
        self.assertEqual(vehicle.vehicle_age, 5)

    def test_vehicle_age_without_acquisition_date(self):
        vehicle = self._create_vehicle(acquisition_date=False)
        self.assertEqual(vehicle.vehicle_age, 0)

    def test_vehicle_age_write_off_before_acquisition(self):
        vehicle = self._create_vehicle(
            acquisition_date="2022-01-01",
            write_off_date="2020-01-01",
        )
        self.assertEqual(vehicle.vehicle_age, 0)
