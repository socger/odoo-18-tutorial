from odoo.tests.common import TransactionCase


class TestVehicleType(TransactionCase):
    def test_create_vehicle_type(self):
        vehicle_type = self.env["vehicle.type"].create(
            {
                "name": "Sedan",
                "seats": "5",
                "description": "Standard sedan",
            }
        )
        self.assertEqual(vehicle_type.name, "Sedan")
        self.assertEqual(vehicle_type.seats, "5")
        self.assertEqual(vehicle_type.description, "Standard sedan")
