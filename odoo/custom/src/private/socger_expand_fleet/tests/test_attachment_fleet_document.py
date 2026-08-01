import base64

from odoo.exceptions import UserError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestAttachmentFleetDocument(TransactionCase):
    def setUp(self):
        super().setUp()
        self.category = self.env["fleet.vehicle.document.category"].create(
            {"name": "ITV"}
        )
        brand = self.env["fleet.vehicle.model.brand"].create({"name": "TestBrand"})
        model = self.env["fleet.vehicle.model"].create(
            {"brand_id": brand.id, "name": "TestModel"}
        )
        self.vehicle = self.env["fleet.vehicle"].create(
            {"model_id": model.id, "plan_to_change_car": False}
        )

    def _create_attachment(self, name, **overrides):
        values = {
            "name": name,
            "type": "binary",
            "datas": base64.b64encode(b"test"),
            "res_model": "fleet.vehicle",
            "res_id": self.vehicle.id,
            "fleet_vehicle_document_category_id": self.category.id,
        }
        values.update(overrides)
        return self.env["ir.attachment"].create(values)

    def _create_other_vehicle(self):
        brand = self.env["fleet.vehicle.model.brand"].create({"name": "TestBrand2"})
        model = self.env["fleet.vehicle.model"].create(
            {"brand_id": brand.id, "name": "TestModel2"}
        )
        return self.env["fleet.vehicle"].create(
            {"model_id": model.id, "plan_to_change_car": False}
        )

    def test_create_attachment_with_category(self):
        attachment = self._create_attachment("ITV.pdf")
        self.assertEqual(attachment.fleet_vehicle_document_category_id, self.category)
        self.assertEqual(attachment.fleet_vehicle_id, self.vehicle)

    def test_duplicate_attachment_raises_user_error(self):
        self._create_attachment("ITV.pdf")
        with self.assertRaises(UserError):
            self._create_attachment("ITV.pdf")

    def test_same_name_different_vehicle_allowed(self):
        other_vehicle = self._create_other_vehicle()
        self._create_attachment("ITV.pdf")
        attachment = self._create_attachment("ITV.pdf", res_id=other_vehicle.id)
        self.assertEqual(attachment.fleet_vehicle_id, other_vehicle)

    def test_duplicate_name_on_write_raises_user_error(self):
        self._create_attachment("ITV.pdf")
        other = self._create_attachment("Seguro.pdf")
        with self.assertRaises(UserError):
            other.name = "ITV.pdf"
