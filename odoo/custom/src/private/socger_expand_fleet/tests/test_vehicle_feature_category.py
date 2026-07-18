import psycopg2

from odoo.tests import TransactionCase, tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestVehicleFeatureCategory(TransactionCase):
    def test_create_category(self):
        category = self.env["vehicle.feature.category"].create(
            {"name": "Comfort", "description": "Comfort features"}
        )
        self.assertEqual(category.name, "Comfort")
        self.assertEqual(category.description, "Comfort features")

    def test_name_unique_constraint(self):
        self.env["vehicle.feature.category"].create({"name": "Comfort"})
        with mute_logger("odoo.sql_db"), self.assertRaises(psycopg2.IntegrityError):
            self.env["vehicle.feature.category"].create({"name": "Comfort"})
