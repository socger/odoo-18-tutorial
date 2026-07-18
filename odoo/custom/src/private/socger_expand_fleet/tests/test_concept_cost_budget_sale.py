import psycopg2

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


class TestConceptCostBudgetSale(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.family = cls.env["concept.cost.budget.sale.family"].create({"name": "Fuel"})

    def test_create_concept_with_one_flag(self):
        concept = self.env["concept.cost.budget.sale"].create(
            {
                "concept_cost_budget_sale_family_id": self.family.id,
                "name": "Gasoline",
                "to_cost": True,
            }
        )
        self.assertEqual(concept.name, "Gasoline")
        self.assertTrue(concept.to_cost)

    def test_create_concept_without_flags_raises(self):
        with self.assertRaises(ValidationError):
            self.env["concept.cost.budget.sale"].create(
                {
                    "concept_cost_budget_sale_family_id": self.family.id,
                    "name": "Gasoline",
                }
            )

    def test_write_concept_without_flags_raises(self):
        concept = self.env["concept.cost.budget.sale"].create(
            {
                "concept_cost_budget_sale_family_id": self.family.id,
                "name": "Gasoline",
                "to_cost": True,
            }
        )
        with self.assertRaises(ValidationError):
            concept.write({"to_cost": False})

    def test_family_name_unique_constraint(self):
        self.env["concept.cost.budget.sale"].create(
            {
                "concept_cost_budget_sale_family_id": self.family.id,
                "name": "Gasoline",
                "to_cost": True,
            }
        )
        with mute_logger("odoo.sql_db"), self.assertRaises(psycopg2.IntegrityError):
            self.env["concept.cost.budget.sale"].create(
                {
                    "concept_cost_budget_sale_family_id": self.family.id,
                    "name": "Gasoline",
                    "to_budget": True,
                }
            )
