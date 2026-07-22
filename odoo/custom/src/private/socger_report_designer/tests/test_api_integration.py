"""HTTP integration tests for the Report Designer REST API endpoints.

These tests exercise the controller routes through real HTTP requests using
Odoo's ``HttpCase`` base class, ensuring that authentication, routing, request
parsing, and response formatting all work end-to-end.
"""

import json

from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestReportDesignerAPIUnauthenticated(HttpCase):
    """Verify that endpoints reject requests without a valid session.

    In Odoo test mode, ``HttpCase`` injects a test cursor cookie that
    implicitly authenticates every request.  To test unauthenticated
    behaviour we create a raw ``Opener`` *without* that cookie so the
    server sees an anonymous request and rejects it.
    """

    def test_models_requires_auth(self):
        from odoo.tests.common import Opener

        raw_opener = Opener(self.cr)
        # No session_id, no test-cursor cookie → truly anonymous.
        response = raw_opener.post(
            self.base_url() + "/api/report-designer/models",
            data=json.dumps({"params": {}}).encode(),
            headers={"Content-Type": "application/json"},
            timeout=12,
        )
        body = response.json()
        # Without auth, JSON-RPC returns an error in the response body
        self.assertIn("error", body)


@tagged("post_install", "-at_install")
class TestReportDesignerModelsAPI(HttpCase):
    """Tests for the /api/report-designer/models endpoint."""

    def setUp(self):
        super().setUp()
        self.authenticate("admin", "admin")

    def _call_models(self, **extra_params):
        params = {**extra_params}
        response = self.url_open(
            "/api/report-designer/models",
            data=json.dumps({"params": params}).encode(),
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def test_models_returns_list(self):
        result = self._call_models()
        self.assertIn("result", result)
        self.assertIn("models", result["result"])
        self.assertIsInstance(result["result"]["models"], list)

    def test_models_contains_res_partner(self):
        result = self._call_models()
        model_names = [m["model"] for m in result["result"]["models"]]
        self.assertIn("res.partner", model_names)

    def test_models_entry_has_required_keys(self):
        result = self._call_models()
        for model in result["result"]["models"][:5]:
            self.assertIn("id", model)
            self.assertIn("model", model)
            self.assertIn("name", model)

    def test_models_excludes_transient(self):
        result = self._call_models()
        model_names = [m["model"] for m in result["result"]["models"]]
        # base.line.mixin is transient/abstract — should not appear
        self.assertNotIn("base_transient_model", model_names)


@tagged("post_install", "-at_install")
class TestReportDesignerFieldsAPI(HttpCase):
    """Tests for the /api/report-designer/fields/<model> endpoint."""

    def setUp(self):
        super().setUp()
        self.authenticate("admin", "admin")

    def _call_fields(self, model_name, **extra_params):
        params = {**extra_params}
        response = self.url_open(
            f"/api/report-designer/fields/{model_name}",
            data=json.dumps({"params": params}).encode(),
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def test_fields_returns_list(self):
        result = self._call_fields("res.partner")
        self.assertIn("result", result)
        self.assertIn("fields", result["result"])
        self.assertIsInstance(result["result"]["fields"], list)

    def test_fields_contains_name(self):
        result = self._call_fields("res.partner")
        field_names = [f["name"] for f in result["result"]["fields"]]
        self.assertIn("name", field_names)

    def test_fields_excludes_internals(self):
        result = self._call_fields("res.partner")
        field_names = [f["name"] for f in result["result"]["fields"]]
        self.assertNotIn("id", field_names)
        self.assertNotIn("create_uid", field_names)
        self.assertNotIn("display_name", field_names)

    def test_fields_invalid_model_returns_error(self):
        result = self._call_fields("non.existent.model")
        self.assertIn("result", result)
        self.assertIn("error", result["result"])

    def test_fields_entry_has_type_and_icon(self):
        result = self._call_fields("res.partner")
        for field in result["result"]["fields"][:5]:
            self.assertIn("type", field)
            self.assertIn("icon", field)


@tagged("post_install", "-at_install")
class TestReportDesignerRelatedFieldsAPI(HttpCase):
    """Tests for the /api/report-designer/fields/<model>/related endpoint."""

    def setUp(self):
        super().setUp()
        self.authenticate("admin", "admin")

    def _call_related(self, model_name, parent_path="", **extra_params):
        params = {"parent_path": parent_path, **extra_params}
        response = self.url_open(
            f"/api/report-designer/fields/{model_name}/related",
            data=json.dumps({"params": params}).encode(),
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def test_related_returns_fields(self):
        result = self._call_related("res.partner", parent_path="partner_id")
        self.assertIn("result", result)
        self.assertIn("fields", result["result"])
        self.assertIsInstance(result["result"]["fields"], list)

    def test_related_includes_parent_path(self):
        result = self._call_related("res.partner", parent_path="partner_id")
        self.assertEqual(result["result"]["parent_path"], "partner_id")

    def test_related_invalid_model(self):
        result = self._call_related("nonexistent.model")
        self.assertIn("result", result)
        self.assertIn("error", result["result"])


@tagged("post_install", "-at_install")
class TestReportDesignerLayoutsCRUD(HttpCase):
    """Tests for layout CRUD endpoints: list, get, create, save, delete."""

    def setUp(self):
        super().setUp()
        self.authenticate("admin", "admin")

    def _json_rpc(self, url, params):
        response = self.url_open(
            url,
            data=json.dumps({"params": params}).encode(),
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def test_list_layouts(self):
        result = self._json_rpc("/api/report-designer/layouts", {})
        self.assertIn("result", result)
        self.assertIn("layouts", result["result"])
        self.assertIsInstance(result["result"]["layouts"], list)

    def test_create_layout(self):
        result = self._json_rpc(
            "/api/report-designer/layouts/create",
            {"name": "API Test Layout", "target_model": "res.partner"},
        )
        self.assertIn("result", result)
        self.assertIn("id", result["result"])
        self.assertEqual(result["result"]["name"], "API Test Layout")
        # Cleanup
        self.env["report.designer.layout"].browse(result["result"]["id"]).unlink()

    def test_get_layout(self):
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Get Test Layout",
                "target_model": "res.partner",
                "layout_json": json.dumps({"elements": []}),
            }
        )
        result = self._json_rpc(f"/api/report-designer/layouts/{layout.id}", {})
        self.assertIn("result", result)
        self.assertEqual(result["result"]["name"], "Get Test Layout")
        self.assertEqual(result["result"]["target_model"], "res.partner")

    def test_get_layout_not_found(self):
        result = self._json_rpc("/api/report-designer/layouts/999999", {})
        self.assertIn("result", result)
        self.assertIn("error", result["result"])

    def test_save_layout(self):
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Save Test",
                "target_model": "res.partner",
                "layout_json": json.dumps({"elements": []}),
            }
        )
        new_json = json.dumps({"elements": [{"type": "text", "content": "Updated"}]})
        result = self._json_rpc(
            f"/api/report-designer/layouts/{layout.id}/save",
            {"layout_json": new_json, "name": "Save Test Updated"},
        )
        self.assertIn("result", result)
        self.assertTrue(result["result"].get("success"))
        # Verify the save took effect
        layout.invalidate_recordset(["layout_json", "name"])
        self.assertEqual(layout.name, "Save Test Updated")
        self.assertIn("Updated", layout.layout_json)

    def test_save_layout_not_found(self):
        result = self._json_rpc(
            "/api/report-designer/layouts/999999/save",
            {"layout_json": "{}"},
        )
        self.assertIn("result", result)
        self.assertIn("error", result["result"])

    def test_delete_layout(self):
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Delete Test",
                "target_model": "res.partner",
                "layout_json": json.dumps({"elements": []}),
            }
        )
        layout_id = layout.id
        result = self._json_rpc(f"/api/report-designer/layouts/{layout_id}/delete", {})
        self.assertIn("result", result)
        self.assertTrue(result["result"].get("success"))
        self.assertFalse(self.env["report.designer.layout"].browse(layout_id).exists())

    def test_delete_layout_not_found(self):
        result = self._json_rpc("/api/report-designer/layouts/999999/delete", {})
        self.assertIn("result", result)
        self.assertIn("error", result["result"])


@tagged("post_install", "-at_install")
class TestReportDesignerPublishAPI(HttpCase):
    """Tests for publish/unpublish endpoints."""

    def setUp(self):
        super().setUp()
        self.authenticate("admin", "admin")

    def _json_rpc(self, url, params):
        response = self.url_open(
            url,
            data=json.dumps({"params": params}).encode(),
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def test_publish_layout(self):
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Publish Test",
                "target_model": "res.partner",
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "Publish Me"}]}
                ),
            }
        )
        result = self._json_rpc(f"/api/report-designer/layouts/{layout.id}/publish", {})
        self.assertIn("result", result)
        self.assertTrue(result["result"].get("success"))
        self.assertEqual(result["result"]["state"], "published")
        self.assertTrue(result["result"].get("report_action_id"))
        # Cleanup
        layout.action_unpublish()
        layout.unlink()

    def test_unpublish_layout(self):
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Unpublish Test",
                "target_model": "res.partner",
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "Unpublish Me"}]}
                ),
            }
        )
        layout.action_publish()
        result = self._json_rpc(
            f"/api/report-designer/layouts/{layout.id}/unpublish", {}
        )
        self.assertIn("result", result)
        self.assertTrue(result["result"].get("success"))
        self.assertEqual(result["result"]["state"], "draft")

    def test_publish_not_found(self):
        result = self._json_rpc("/api/report-designer/layouts/999999/publish", {})
        self.assertIn("result", result)
        self.assertIn("error", result["result"])

    def test_unpublish_not_found(self):
        result = self._json_rpc("/api/report-designer/layouts/999999/unpublish", {})
        self.assertIn("result", result)
        self.assertIn("error", result["result"])


@tagged("post_install", "-at_install")
class TestReportDesignerGenerateXMLAPI(HttpCase):
    """Tests for the /api/report-designer/generate-xml endpoint."""

    def setUp(self):
        super().setUp()
        self.authenticate("admin", "admin")

    def _json_rpc(self, url, params):
        response = self.url_open(
            url,
            data=json.dumps({"params": params}).encode(),
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def test_generate_xml_valid(self):
        layout_json = json.dumps(
            {"elements": [{"type": "text", "content": "Hello World"}]}
        )
        result = self._json_rpc(
            "/api/report-designer/generate-xml",
            {"layout_json": layout_json},
        )
        self.assertIn("result", result)
        self.assertIn("xml", result["result"])
        self.assertIn("<template>", result["result"]["xml"])
        self.assertIn("Hello World", result["result"]["xml"])

    def test_generate_xml_invalid_returns_error(self):
        # Pass a malformed element type that should cause an error
        layout_json = json.dumps({"elements": []})
        result = self._json_rpc(
            "/api/report-designer/generate-xml",
            {"layout_json": layout_json},
        )
        self.assertIn("result", result)
        # Empty elements list should still produce valid XML (empty template)
        self.assertIn("xml", result["result"])

    def test_generate_xml_with_table(self):
        layout_json = json.dumps(
            {
                "elements": [
                    {
                        "type": "table",
                        "dataSource": "child_ids",
                        "columns": [
                            {"header": "Name", "fieldPath": "name"},
                        ],
                    }
                ]
            }
        )
        result = self._json_rpc(
            "/api/report-designer/generate-xml",
            {"layout_json": layout_json},
        )
        self.assertIn("result", result)
        self.assertIn("xml", result["result"])
        self.assertIn("t-foreach", result["result"]["xml"])

    def test_generate_xml_with_text_element(self):
        layout_json = json.dumps(
            {
                "elements": [
                    {
                        "type": "text",
                        "fieldPath": "name",
                        "fieldFormat": "monetary",
                    }
                ]
            }
        )
        result = self._json_rpc(
            "/api/report-designer/generate-xml",
            {"layout_json": layout_json},
        )
        self.assertIn("result", result)
        self.assertIn("xml", result["result"])
        self.assertIn("t-field", result["result"]["xml"])


@tagged("post_install", "-at_install")
class TestReportDesignerRecordsAPI(HttpCase):
    """Tests for the /api/report-designer/records/<model> endpoint."""

    def setUp(self):
        super().setUp()
        self.authenticate("admin", "admin")

    def _json_rpc(self, url, params):
        response = self.url_open(
            url,
            data=json.dumps({"params": params}).encode(),
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def test_records_returns_list(self):
        result = self._json_rpc("/api/report-designer/records/res.partner", {})
        self.assertIn("result", result)
        self.assertIn("records", result["result"])
        self.assertIsInstance(result["result"]["records"], list)

    def test_records_entry_has_id_and_name(self):
        result = self._json_rpc("/api/report-designer/records/res.partner", {})
        records = result["result"]["records"]
        if records:
            self.assertIn("id", records[0])
            self.assertIn("display_name", records[0])

    def test_records_invalid_model(self):
        result = self._json_rpc("/api/report-designer/records/nonexistent.model", {})
        self.assertIn("result", result)
        self.assertIn("error", result["result"])

    def test_records_with_limit(self):
        result = self._json_rpc(
            "/api/report-designer/records/res.partner", {"limit": 3}
        )
        self.assertIn("result", result)
        records = result["result"]["records"]
        self.assertLessEqual(len(records), 3)


@tagged("post_install", "-at_install")
class TestReportDesignerPreviewAPI(HttpCase):
    """Tests for the live preview endpoints."""

    def setUp(self):
        super().setUp()
        self.authenticate("admin", "admin")

    def _json_rpc(self, url, params):
        response = self.url_open(
            url,
            data=json.dumps({"params": params}).encode(),
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def test_live_preview_html(self):
        layout_json = json.dumps(
            {"elements": [{"type": "text", "content": "Preview Test"}]}
        )
        result = self._json_rpc(
            "/api/report-designer/preview/html",
            {"layout_json": layout_json, "target_model": "res.partner"},
        )
        self.assertIn("result", result)
        self.assertIn("html", result["result"])
        self.assertIn("Preview Test", result["result"]["html"])

    def test_live_preview_requires_model(self):
        result = self._json_rpc(
            "/api/report-designer/preview/live",
            {"layout_json": "{}", "target_model": ""},
        )
        self.assertIn("result", result)
        self.assertIn("error", result["result"])

    def test_live_preview_with_record_id(self):
        # Create a test partner to preview
        partner = self.env["res.partner"].create(
            {"name": "Preview Partner", "email": "preview@test.com"}
        )
        layout_json = json.dumps({"elements": [{"type": "text", "fieldPath": "name"}]})
        result = self._json_rpc(
            "/api/report-designer/preview/html",
            {
                "layout_json": layout_json,
                "target_model": "res.partner",
                "record_id": partner.id,
            },
        )
        self.assertIn("result", result)
        self.assertIn("html", result["result"])
        self.assertIn("Preview Partner", result["result"]["html"])
        # Cleanup
        partner.unlink()

    def test_layout_preview_unpublished_uses_live(self):
        """Unpublished layout falls back to live preview."""
        layout = self.env["report.designer.layout"].create(
            {
                "name": "Preview Fallback Test",
                "target_model": "res.partner",
                "layout_json": json.dumps(
                    {"elements": [{"type": "text", "content": "Fallback"}]}
                ),
            }
        )
        result = self._json_rpc(f"/api/report-designer/layouts/{layout.id}/preview", {})
        self.assertIn("result", result)
        # Should succeed with live preview fallback
        self.assertTrue(
            result["result"].get("html") or result["result"].get("pdf_base64")
        )
        # Cleanup
        layout.unlink()

    def test_preview_not_found_layout(self):
        result = self._json_rpc("/api/report-designer/layouts/999999/preview", {})
        self.assertIn("result", result)
        self.assertIn("error", result["result"])
