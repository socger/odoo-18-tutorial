import psycopg2

from odoo.tests import TransactionCase, tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestVehicleFeatureByVehicle(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = cls.env["vehicle.feature.category"].create({"name": "Comfort"})
        cls.feature = cls.env["vehicle.feature"].create(
            {
                "vehicle_feature_category_id": cls.category.id,
                "name": "Air conditioning",
            }
        )
        brand = cls.env["fleet.vehicle.model.brand"].create({"name": "TestBrand"})
        model = cls.env["fleet.vehicle.model"].create(
            {"name": "TestModel", "brand_id": brand.id}
        )
        cls.vehicle = cls.env["fleet.vehicle"].create({"model_id": model.id})

    def test_create_feature_by_vehicle(self):
        record = self.env["vehicle.feature.by.vehicle"].create(
            {
                "fleet_vehicle_id": self.vehicle.id,
                "vehicle_feature_id": self.feature.id,
            }
        )
        self.assertEqual(record.fleet_vehicle_id, self.vehicle)
        self.assertEqual(record.vehicle_feature_id, self.feature)

    def test_vehicle_feature_unique_constraint(self):
        self.env["vehicle.feature.by.vehicle"].create(
            {
                "fleet_vehicle_id": self.vehicle.id,
                "vehicle_feature_id": self.feature.id,
            }
        )
        with mute_logger("odoo.sql_db"), self.assertRaises(psycopg2.IntegrityError):
            self.env["vehicle.feature.by.vehicle"].create(
                {
                    "fleet_vehicle_id": self.vehicle.id,
                    "vehicle_feature_id": self.feature.id,
                }
            )
