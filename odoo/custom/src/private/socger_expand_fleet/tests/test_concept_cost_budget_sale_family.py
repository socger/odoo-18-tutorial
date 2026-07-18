import psycopg2

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


class TestConceptCostBudgetSaleFamily(TransactionCase):
    def test_create_family(self):
        family = self.env["concept.cost.budget.sale.family"].create(
            {"name": "Fuel", "description": "Fuel costs"}
        )
        self.assertEqual(family.name, "Fuel")
        self.assertEqual(family.description, "Fuel costs")

    def test_name_unique_constraint(self):
        self.env["concept.cost.budget.sale.family"].create({"name": "Fuel"})
        with mute_logger("odoo.sql_db"), self.assertRaises(psycopg2.IntegrityError):
            self.env["concept.cost.budget.sale.family"].create({"name": "Fuel"})
