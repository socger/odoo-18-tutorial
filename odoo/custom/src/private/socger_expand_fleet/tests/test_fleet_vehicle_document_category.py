from odoo.exceptions import UserError, ValidationError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestFleetVehicleDocumentCategory(TransactionCase):
    def test_create_category(self):
        category = self.env["fleet.vehicle.document.category"].create(
            {"name": "Mecánica"}
        )
        child = self.env["fleet.vehicle.document.category"].create(
            {
                "name": "Frenos",
                "fleet_vehicle_document_category_id": category.id,
            }
        )
        self.assertEqual(child.name, "Frenos")
        self.assertEqual(child.fleet_vehicle_document_category_id, category)

    def test_name_unique_constraint(self):
        self.env["fleet.vehicle.document.category"].create({"name": "Mecánica"})
        with self.assertRaises(UserError):
            self.env["fleet.vehicle.document.category"].create({"name": "Mecánica"})

    def test_name_unique_on_write(self):
        self.env["fleet.vehicle.document.category"].create({"name": "Mecánica"})
        other = self.env["fleet.vehicle.document.category"].create({"name": "Frenos"})
        with self.assertRaises(UserError):
            other.name = "Mecánica"

    def test_self_parent_recursion(self):
        category = self.env["fleet.vehicle.document.category"].create(
            {"name": "Mecánica"}
        )
        with self.assertRaises(ValidationError):
            category.fleet_vehicle_document_category_id = category

    def test_circular_recursion(self):
        parent = self.env["fleet.vehicle.document.category"].create(
            {"name": "Mecánica"}
        )
        child = self.env["fleet.vehicle.document.category"].create(
            {
                "name": "Frenos",
                "fleet_vehicle_document_category_id": parent.id,
            }
        )
        with self.assertRaises(ValidationError):
            parent.fleet_vehicle_document_category_id = child
