from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestFleetVehicleGarage(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.garage = cls.env["fleet.garage"].create(
            {
                "name": "Cochera Central",
                "res_company_id": cls.env.ref("base.main_company").id,
            }
        )
        brand = cls.env["fleet.vehicle.model.brand"].create({"name": "TestBrandGarage"})
        cls.model = cls.env["fleet.vehicle.model"].create(
            {"name": "TestModelGarage", "brand_id": brand.id}
        )

    def test_create_vehicle_with_garage(self):
        vehicle = self.env["fleet.vehicle"].create(
            {
                "model_id": self.model.id,
                "fleet_garage_id": self.garage.id,
                "vehicle_code": "VHC-GARAGE",
                "seating_capacity_per_permit": 4,
                "seating_capacity_per_technical_datasheet": "4",
                "seating_capacity_bookable_seats": 4,
            }
        )
        self.assertEqual(vehicle.fleet_garage_id, self.garage)

    def test_garage_display_name_is_name(self):
        vehicle = self.env["fleet.vehicle"].create(
            {
                "model_id": self.model.id,
                "fleet_garage_id": self.garage.id,
                "vehicle_code": "VHC-GARAGE-2",
                "seating_capacity_per_permit": 4,
                "seating_capacity_per_technical_datasheet": "4",
                "seating_capacity_bookable_seats": 4,
            }
        )
        self.assertEqual(vehicle.fleet_garage_id.display_name, "Cochera Central")

    def test_fleet_garage_id_field_attributes(self):
        field = self.env["fleet.vehicle"]._fields["fleet_garage_id"]
        self.assertEqual(field.comodel_name, "fleet.garage")
        self.assertEqual(field.string, "Cochera")
        self.assertTrue(field.required)
        self.assertTrue(field.tracking)
