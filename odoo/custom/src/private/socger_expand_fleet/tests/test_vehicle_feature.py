import psycopg2

from odoo.tests import TransactionCase, tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestVehicleFeature(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = cls.env["vehicle.feature.category"].create({"name": "Comfort"})

    def test_create_feature(self):
        feature = self.env["vehicle.feature"].create(
            {
                "vehicle_feature_category_id": self.category.id,
                "name": "Air conditioning",
            }
        )
        self.assertEqual(feature.name, "Air conditioning")
        self.assertEqual(feature.vehicle_feature_category_id, self.category)

    def test_category_name_unique_constraint(self):
        self.env["vehicle.feature"].create(
            {
                "vehicle_feature_category_id": self.category.id,
                "name": "Air conditioning",
            }
        )
        with mute_logger("odoo.sql_db"), self.assertRaises(psycopg2.IntegrityError):
            self.env["vehicle.feature"].create(
                {
                    "vehicle_feature_category_id": self.category.id,
                    "name": "Air conditioning",
                }
            )

    def test_same_name_different_category(self):
        """Same feature name is allowed under different categories."""
        other_category = self.env["vehicle.feature.category"].create({"name": "Safety"})
        self.env["vehicle.feature"].create(
            {
                "vehicle_feature_category_id": self.category.id,
                "name": "Shared name",
            }
        )
        feature = self.env["vehicle.feature"].create(
            {
                "vehicle_feature_category_id": other_category.id,
                "name": "Shared name",
            }
        )
        self.assertTrue(feature.id)
