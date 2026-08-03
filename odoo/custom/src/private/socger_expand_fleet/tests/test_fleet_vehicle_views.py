from lxml import etree

from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestFleetVehicleViews(TransactionCase):
    """Check the inherited fleet.vehicle views expose the new FASE 1 fields."""

    def _combined_arch(self, xml_id):
        view = self.env.ref(xml_id)
        return etree.fromstring(view.get_combined_arch())

    def _field_sequence(self, root):
        return [field.get("name") for field in root.xpath("//field")]

    def test_form_vehicle_code_between_license_plate_and_tag_ids(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        seq = self._field_sequence(root)
        self.assertIn("vehicle_code", seq)
        self.assertLess(seq.index("license_plate"), seq.index("vehicle_code"))
        self.assertLess(seq.index("vehicle_code"), seq.index("tag_ids"))

    def test_kanban_company_partner_under_license_plate(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_kanban_inherit"
        )
        seq = self._field_sequence(root)
        self.assertIn("res_company_id", seq)
        self.assertIn("res_partner_id", seq)
        self.assertLess(seq.index("license_plate"), seq.index("res_company_id"))
        self.assertLess(seq.index("res_partner_id"), seq.index("tag_ids"))

    def test_kanban_vehicle_code_between_tags_and_driver(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_kanban_inherit"
        )
        seq = self._field_sequence(root)
        self.assertIn("vehicle_code", seq)
        self.assertLess(seq.index("tag_ids"), seq.index("vehicle_code"))
        self.assertLess(seq.index("vehicle_code"), seq.index("driver_id"))

    def test_pivot_uses_combined_plate_and_code(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_pivot_inherit"
        )
        pivot_fields = root.xpath("//pivot/field")
        names = [field.get("name") for field in pivot_fields]
        self.assertIn("license_plate_with_code", names)
        self.assertNotIn("license_plate", names)
        combined = root.xpath("//pivot/field[@name='license_plate_with_code']")[0]
        self.assertEqual(combined.get("type"), "row")

    def test_activity_uses_combined_plate_and_code(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_activity_inherit"
        )
        activity_fields = root.xpath("//activity/field/@name")
        self.assertIn("license_plate_with_code", activity_fields)
        self.assertNotIn("license_plate", activity_fields)
        template_fields = root.xpath("//div[@t-name='activity-box']//field/@name")
        self.assertIn("license_plate_with_code", template_fields)
