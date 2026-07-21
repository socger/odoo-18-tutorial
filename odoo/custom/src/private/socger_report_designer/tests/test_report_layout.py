import json

from odoo.exceptions import UserError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestReportLayout(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.company = cls.env.company

        # Create a test layout
        cls.layout = cls.env["report.designer.layout"].create(
            {
                "name": "Test Layout",
                "target_model": "res.partner",
                "layout_json": json.dumps(
                    {
                        "elements": [
                            {
                                "id": "el_001",
                                "type": "text",
                                "content": "Test Report",
                                "style": {"fontSize": 24, "fontWeight": "bold"},
                            }
                        ]
                    }
                ),
                "company_id": cls.company.id,
            }
        )

    def test_create_layout(self):
        """Test basic layout creation."""
        self.assertTrue(self.layout.id)
        self.assertEqual(self.layout.state, "draft")
        self.assertEqual(self.layout.version, 1)

    def test_element_count(self):
        """Test element count computation."""
        self.assertEqual(self.layout.element_count, 1)

    def test_invalid_model_constraint(self):
        """Test that invalid model raises error."""
        with self.assertRaises(UserError):
            self.env["report.designer.layout"].create(
                {
                    "name": "Invalid Layout",
                    "target_model": "non.existent.model",
                }
            )

    def test_invalid_json_constraint(self):
        """Test that invalid JSON raises error."""
        with self.assertRaises(UserError):
            self.env["report.designer.layout"].create(
                {
                    "name": "Invalid JSON Layout",
                    "target_model": "res.partner",
                    "layout_json": "not valid json {{{",
                }
            )

    def test_publish_requires_data(self):
        """Test that publishing requires layout data."""
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Empty Layout",
                "target_model": "res.partner",
                "layout_json": "{}",
            }
        )
        # Should raise error for empty layout
        with self.assertRaises(UserError):
            layout.action_publish()

    def test_copy_layout(self):
        """Test layout copy."""
        copied = self.layout.copy()
        self.assertNotEqual(copied.id, self.layout.id)
        self.assertEqual(copied.state, "draft")
        self.assertEqual(copied.version, 1)


@tagged("post_install", "-at_install")
class TestQWebGeneration(TransactionCase):
    """Tests for the QWeb XML generation from layout JSON."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.layout_model = cls.env["report.designer.layout"]

    def _render(self, elements):
        """Helper: render a list of elements to QWeb body XML."""
        layout_json = json.dumps({"elements": elements})
        return self.layout_model.generate_preview_qweb(layout_json)

    def test_text_element_field_binding(self):
        """Text element bound to a field produces t-field span."""
        xml = self._render([{"type": "text", "fieldPath": "partner_id", "content": ""}])
        self.assertIn('t-field="o.partner_id"', xml)

    def test_text_element_static_content(self):
        """Text element with static content produces escaped text."""
        xml = self._render([{"type": "text", "content": "Hello & World"}])
        self.assertIn("Hello &amp; World", xml)

    def test_heading_element(self):
        """Heading element produces the correct h-tag level."""
        xml = self._render(
            [{"type": "heading", "content": "Title", "style": {"level": 1}}]
        )
        self.assertIn("<h1", xml)
        self.assertIn("Title", xml)

    def test_line_element(self):
        """Line element produces an <hr/> tag."""
        xml = self._render([{"type": "line"}])
        self.assertIn("<hr/>", xml)

    def test_pagebreak_element(self):
        """Page break element produces a div with page-break-after CSS."""
        xml = self._render([{"type": "pagebreak"}])
        self.assertIn("page-break-after: always", xml)

    def test_spacer_element(self):
        """Spacer element produces a div with the given height."""
        xml = self._render([{"type": "spacer", "style": {"height": "40px"}}])
        self.assertIn("height: 40px", xml)

    def test_table_element_basic(self):
        """Table element produces a <table> with t-foreach over the O2M field."""
        xml = self._render(
            [
                {
                    "type": "table",
                    "dataSource": "order_line",
                    "columns": [
                        {"header": "Product", "fieldPath": "product_id"},
                        {"header": "Qty", "fieldPath": "product_uom_qty"},
                    ],
                }
            ]
        )
        self.assertIn("<table", xml)
        self.assertIn('t-foreach="o.order_line"', xml)
        self.assertIn("Product", xml)
        self.assertIn("Qty", xml)
        self.assertIn("line.product_id", xml)

    def test_table_element_empty_returns_empty(self):
        """Table without data source or columns renders nothing."""
        xml = self._render([{"type": "table", "dataSource": "", "columns": []}])
        # The body should fall back to the "No content" placeholder
        self.assertIn("No content", xml)

    def test_condition_wraps_element(self):
        """When a condition is set, the element is wrapped in a t-if."""
        xml = self._render(
            [
                {
                    "type": "text",
                    "content": "Conditional",
                    "condition": "o.state == 'done'",
                }
            ]
        )
        self.assertIn("t-if=\"o.state == 'done'\"", xml)

    def test_style_string_builder(self):
        """_build_style_string converts a style dict to CSS correctly."""
        css = self.layout_model._build_style_string(
            {"fontSize": 12, "color": "#ff0000", "fontWeight": "bold"}
        )
        self.assertIn("font-size: 12pt", css)
        self.assertIn("color: #ff0000", css)
        self.assertIn("font-weight: bold", css)

    def test_template_wraps_with_external_layout(self):
        """Generated QWeb wraps body in web.external_layout."""
        xml = self._render([{"type": "text", "content": "Body"}])
        self.assertIn('t-call="web.html_container"', xml)
        self.assertIn('t-call="web.external_layout"', xml)
        self.assertIn('t-foreach="docs"', xml)


@tagged("post_install", "-at_install")
class TestPublishUnpublish(TransactionCase):
    """Tests for the publish / unpublish lifecycle."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))

    def test_publish_creates_view_and_action(self):
        """Publishing creates an ir.ui.view and an ir.actions.report."""
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Pub Test",
                "target_model": "res.partner",
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "Hello"}]}
                ),
            }
        )
        layout.action_publish()
        self.assertEqual(layout.state, "published")
        self.assertTrue(layout.qweb_template_id)
        self.assertTrue(layout.report_action_id)
        self.assertTrue(layout.last_publish_date)
        # The report action should be bound to res.partner
        self.assertEqual(layout.report_action_id.model, "res.partner")

    def test_unpublish_removes_view_and_action(self):
        """Unpublishing deletes the ir.ui.view and ir.actions.report."""
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Unpub Test",
                "target_model": "res.partner",
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "Hello"}]}
                ),
            }
        )
        layout.action_publish()
        view_id = layout.qweb_template_id.id
        action_id = layout.report_action_id.id

        layout.action_unpublish()
        self.assertEqual(layout.state, "draft")
        self.assertFalse(layout.qweb_template_id)
        self.assertFalse(layout.report_action_id)
        # Records should be gone
        self.assertFalse(self.env["ir.ui.view"].browse(view_id).exists())
        self.assertFalse(self.env["ir.actions.report"].browse(action_id).exists())

    def test_publish_updates_existing_view(self):
        """Re-publishing updates the existing view rather than creating a new one."""
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Repub Test",
                "target_model": "res.partner",
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "V1"}]}
                ),
            }
        )
        layout.action_publish()
        view_id = layout.qweb_template_id.id
        action_id = layout.report_action_id.id

        # Change layout and re-publish
        layout.write(
            {
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "V2"}]}
                )
            }
        )
        layout.action_publish()
        # Same view and action records should be reused
        self.assertEqual(layout.qweb_template_id.id, view_id)
        self.assertEqual(layout.report_action_id.id, action_id)
        self.assertIn("V2", layout.qweb_template_id.arch)

    def test_write_after_publish_reverts_to_draft(self):
        """Editing layout_json after publishing reverts state to draft."""
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Edit After Pub",
                "target_model": "res.partner",
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "Original"}]}
                ),
            }
        )
        layout.action_publish()
        self.assertEqual(layout.state, "published")

        layout.write(
            {
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "New"}]}
                )
            }
        )
        self.assertEqual(layout.state, "draft")
        self.assertEqual(layout.version, 2)
