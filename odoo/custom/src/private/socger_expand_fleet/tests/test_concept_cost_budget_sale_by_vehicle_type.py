import psycopg2

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


class TestConceptCostBudgetSaleByVehicleType(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.family = cls.env["concept.cost.budget.sale.family"].create({"name": "Fuel"})
        cls.concept = cls.env["concept.cost.budget.sale"].create(
            {
                "concept_cost_budget_sale_family_id": cls.family.id,
                "name": "Gasoline",
                "to_cost": True,
            }
        )
        cls.vehicle_type = cls.env["vehicle.type"].create(
            {"name": "Sedan", "seats": "5"}
        )

    def test_create_by_vehicle_type(self):
        record = self.env["concept.cost.budget.sale.by.vehicle.type"].create(
            {
                "vehicle_type_id": self.vehicle_type.id,
                "concept_cost_budget_sale_id": self.concept.id,
                "value": 1.5,
                "price_guide": "Premium",
                "description": "Premium gasoline",
            }
        )
        self.assertEqual(record.value, 1.5)
        self.assertEqual(record.price_guide, "Premium")

    def test_vehicle_type_concept_unique_constraint(self):
        self.env["concept.cost.budget.sale.by.vehicle.type"].create(
            {
                "vehicle_type_id": self.vehicle_type.id,
                "concept_cost_budget_sale_id": self.concept.id,
                "value": 1.5,
            }
        )
        with mute_logger("odoo.sql_db"), self.assertRaises(psycopg2.IntegrityError):
            self.env["concept.cost.budget.sale.by.vehicle.type"].create(
                {
                    "vehicle_type_id": self.vehicle_type.id,
                    "concept_cost_budget_sale_id": self.concept.id,
                    "value": 2.0,
                }
            )
