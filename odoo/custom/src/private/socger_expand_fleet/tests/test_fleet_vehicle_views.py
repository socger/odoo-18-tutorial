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

    def test_form_engine_and_bodywork_after_color(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        seq = self._field_sequence(root)
        self.assertLess(seq.index("color"), seq.index("engine_Chassis"))
        self.assertLess(seq.index("engine_Chassis"), seq.index("bodywork"))
        self.assertLess(seq.index("bodywork"), seq.index("build_Number"))

    def test_form_seats_replaced_by_seating_capacity(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        seq = self._field_sequence(root)
        self.assertNotIn("seats", seq)
        self.assertLess(
            seq.index("build_Number"), seq.index("seating_capacity_per_permit")
        )
        self.assertLess(
            seq.index("seating_capacity_per_permit"),
            seq.index("seating_capacity_per_technical_datasheet"),
        )
        self.assertLess(
            seq.index("seating_capacity_per_technical_datasheet"),
            seq.index("seating_capacity_bookable_seats"),
        )
        self.assertLess(
            seq.index("seating_capacity_bookable_seats"), seq.index("doors")
        )

    def test_form_model_id_before_category_id(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        seq = self._field_sequence(root)
        self.assertLess(seq.index("model_id"), seq.index("category_id"))

    def test_form_vehicle_type_and_booleans_before_order_date(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        seq = self._field_sequence(root)
        self.assertLess(seq.index("vehicle_type_id"), seq.index("order_date"))
        self.assertLess(seq.index("vehicle_type_id"), seq.index("digital_tachograph"))
        self.assertLess(
            seq.index("digital_tachograph"),
            seq.index("professional_diesel_tax_relief_beneficiary"),
        )
        self.assertLess(
            seq.index("professional_diesel_tax_relief_beneficiary"),
            seq.index("order_date"),
        )

    def test_form_mileage_and_age_positions(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        seq = self._field_sequence(root)
        self.assertLess(seq.index("vin_sn"), seq.index("mileage_at_purchase"))
        self.assertLess(seq.index("mileage_at_purchase"), seq.index("odometer"))
        self.assertLess(seq.index("write_off_date"), seq.index("vehicle_age"))

    def test_form_tag_ids_below_vehicle_code(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        seq = self._field_sequence(root)
        self.assertLess(seq.index("vehicle_code"), seq.index("tag_ids"))

    def test_form_features_page_two_groups(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        page = root.xpath("//page[@name='vehicle_features']")[0]
        inner_groups = page.xpath("./group/group")
        self.assertEqual(len(inner_groups), 2)
        self.assertTrue(
            inner_groups[0].xpath(".//field[@name='vehicle_feature_by_vehicle_ids']")
        )
        self.assertTrue(
            inner_groups[1].xpath(".//field[@name='special_configurations']")
        )

    def test_form_accounting_page_between_concepts_and_note(self):
        root = self._combined_arch(
            "socger_expand_fleet.view_fleet_vehicle_form_inherit"
        )
        page_names = [page.get("name") for page in root.xpath("//page")]
        self.assertLess(page_names.index("concepts"), page_names.index("accounting"))
        self.assertLess(page_names.index("accounting"), page_names.index("note"))
        accounting = root.xpath("//page[@name='accounting']")[0]
        accounting_fields = [
            field.get("name") for field in accounting.xpath(".//field")
        ]
        self.assertIn("accounting_national_mileage", accounting_fields)
        self.assertIn("accounting_international_mileage", accounting_fields)
        self.assertIn("accounting_accounting_project", accounting_fields)
