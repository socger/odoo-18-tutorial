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
