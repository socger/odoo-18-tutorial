import base64
import hashlib
import json
import logging
import time

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

# In-memory preview cache: {hash_key: (html_content, timestamp)}
_PREVIEW_CACHE = {}
_PREVIEW_CACHE_TTL = 300  # 5 minutes
_PREVIEW_CACHE_MAX = 50


class ReportDesignerController(http.Controller):
    """REST API for the Visual Report Designer React frontend."""

    # === MODEL INTROSPECTION === #

    @http.route(
        "/api/report-designer/models",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def get_models(self, **kwargs):
        """Return list of available Odoo models for report design."""
        models = request.env["ir.model"].search(
            [
                ("transient", "=", False),
                ("name", "!=", False),
            ],
            order="name",
        )

        result = []
        for model in models:
            # Check if user has read access
            try:
                request.env[model.model].check_access_rights("read")
                result.append(
                    {
                        "id": model.id,
                        "model": model.model,
                        "name": model.name,
                        "info": model.info or "",
                    }
                )
            except Exception:
                # Skip models user cannot access
                continue

        return {"models": result}

    @http.route(
        "/api/report-designer/fields/<string:model_name>",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def get_fields(self, model_name, **kwargs):
        """Return fields for a given Odoo model."""
        try:
            model = request.env[model_name]
            model.check_access_rights("read")
        except KeyError:
            return {"error": f"Model '{model_name}' not found"}
        except Exception as e:
            return {"error": str(e)}

        return {"fields": self._get_model_fields(model_name), "model": model_name}

    @http.route(
        "/api/report-designer/fields/<string:model_name>/related",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def get_related_fields(self, model_name, **kwargs):
        """Return fields for a related model (for nested many2one expansion).

        Accepts ``parent_path`` (e.g. "partner_id") so the frontend can build
        dotted paths like ``partner_id.name``.
        """
        parent_path = kwargs.get("parent_path", "")
        try:
            model = request.env[model_name]
            model.check_access_rights("read")
        except (KeyError, Exception) as exc:
            return {"error": str(exc)}

        return {
            "fields": self._get_model_fields(model_name),
            "model": model_name,
            "parent_path": parent_path,
        }

    # === FIELD INTROSPECTION HELPERS === #

    # Field type → frontend icon mapping (shared across endpoints)
    _TYPE_ICONS = {
        "char": "text",
        "text": "text",
        "html": "code",
        "integer": "number",
        "float": "number",
        "monetary": "money",
        "boolean": "check",
        "date": "calendar",
        "datetime": "clock",
        "binary": "image",
        "image": "image",
        "selection": "list",
        "many2one": "relation",
        "one2many": "relation-list",
        "many2many": "relation-many",
    }

    _INTERNAL_FIELDS = frozenset(
        {"id", "display_name", "create_uid", "create_date", "write_uid", "write_date"}
    )

    def _get_model_fields(self, model_name):
        """Return a list of field dicts for *model_name*, excluding internals."""
        fields_data = request.env[model_name].fields_get()
        result = []
        for fname, fdata in fields_data.items():
            if fname.startswith("_") or fname in self._INTERNAL_FIELDS:
                continue
            field_type = fdata.get("type", "char")
            result.append(
                {
                    "name": fname,
                    "string": fdata.get("string", fname),
                    "type": field_type,
                    "icon": self._TYPE_ICONS.get(field_type, "question"),
                    "required": fdata.get("required", False),
                    "readonly": fdata.get("readonly", False),
                    "relation": fdata.get("relation"),
                    "selection": fdata.get("selection"),
                    "help": fdata.get("help"),
                }
            )
        return result

    # === LAYOUT CRUD === #

    @http.route(
        "/api/report-designer/layouts",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def list_layouts(self, **kwargs):
        """List all report layouts."""
        layouts = request.env["report.designer.layout"].search(
            [], order="sequence, name"
        )
        result = []
        for layout in layouts:
            result.append(
                {
                    "id": layout.id,
                    "name": layout.name,
                    "target_model": layout.target_model,
                    "state": layout.state,
                    "version": layout.version,
                    "element_count": layout.element_count,
                    "create_date": (
                        layout.create_date.isoformat() if layout.create_date else False
                    ),
                    "last_publish_date": (
                        layout.last_publish_date.isoformat()
                        if layout.last_publish_date
                        else False
                    ),
                }
            )
        return {"layouts": result}

    @http.route(
        "/api/report-designer/layouts/<int:layout_id>",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def get_layout(self, layout_id, **kwargs):
        """Get a specific layout with its JSON data."""
        layout = request.env["report.designer.layout"].browse(layout_id)
        if not layout.exists():
            return {"error": "Layout not found"}

        return {
            "id": layout.id,
            "name": layout.name,
            "target_model": layout.target_model,
            "layout_json": layout.layout_json or "{}",
            "state": layout.state,
            "version": layout.version,
            "paper_format": layout.paper_format,
            "paper_orientation": layout.paper_orientation,
            "paper_format_id": (
                layout.paper_format_id.id if layout.paper_format_id else False
            ),
        }

    @http.route(
        "/api/report-designer/layouts/create",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def create_layout(self, **kwargs):
        """Create a new report layout."""
        name = kwargs.get("name", "New Report")
        target_model = kwargs.get("target_model", "sale.order")

        layout = request.env["report.designer.layout"].create(
            {
                "name": name,
                "target_model": target_model,
                "layout_json": json.dumps({"elements": []}),
            }
        )

        return {"id": layout.id, "name": layout.name}

    @http.route(
        "/api/report-designer/layouts/<int:layout_id>/save",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def save_layout(self, layout_id, **kwargs):
        """Save layout JSON data."""
        layout = request.env["report.designer.layout"].browse(layout_id)
        if not layout.exists():
            return {"error": "Layout not found"}

        layout_json = kwargs.get("layout_json")
        name = kwargs.get("name")

        vals = {}
        if layout_json is not None:
            # Validate JSON
            try:
                json.loads(layout_json) if isinstance(layout_json, str) else layout_json
            except json.JSONDecodeError as e:
                return {"error": f"Invalid JSON: {str(e)}"}
            vals["layout_json"] = (
                layout_json if isinstance(layout_json, str) else json.dumps(layout_json)
            )
        if name:
            vals["name"] = name

        layout.write(vals)
        return {"success": True, "version": layout.version}

    @http.route(
        "/api/report-designer/layouts/<int:layout_id>/delete",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def delete_layout(self, layout_id, **kwargs):
        """Delete a report layout."""
        layout = request.env["report.designer.layout"].browse(layout_id)
        if not layout.exists():
            return {"error": "Layout not found"}

        # Unpublish first if published
        if layout.state == "published":
            layout.action_unpublish()

        layout.unlink()
        return {"success": True}

    # === PUBLISH / UNPUBLISH === #

    @http.route(
        "/api/report-designer/layouts/<int:layout_id>/publish",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def publish_layout(self, layout_id, **kwargs):
        """Publish a layout to Odoo (creates QWeb template + report action)."""
        layout = request.env["report.designer.layout"].browse(layout_id)
        if not layout.exists():
            return {"error": "Layout not found"}

        try:
            layout.action_publish()
            return {
                "success": True,
                "state": "published",
                "report_action_id": (
                    layout.report_action_id.id if layout.report_action_id else False
                ),
            }
        except Exception as e:
            return {"error": str(e)}

    @http.route(
        "/api/report-designer/layouts/<int:layout_id>/unpublish",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def unpublish_layout(self, layout_id, **kwargs):
        """Unpublish a layout from Odoo."""
        layout = request.env["report.designer.layout"].browse(layout_id)
        if not layout.exists():
            return {"error": "Layout not found"}

        try:
            layout.action_unpublish()
            return {"success": True, "state": "draft"}
        except Exception as e:
            return {"error": str(e)}

    # === GENERATE XML === #

    @http.route(
        "/api/report-designer/generate-xml",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def generate_xml(self, **kwargs):
        """Generate QWeb XML from layout JSON without persisting.

        Returns {xml: str} or {error: str}.
        """
        layout_json = kwargs.get("layout_json", "{}")
        try:
            layout_model = request.env["report.designer.layout"]
            xml = layout_model.generate_xml_from_json(layout_json)
            return {"xml": xml}
        except Exception as e:
            return {"error": str(e)}

    # === RECORDS FOR PREVIEW === #

    @http.route(
        "/api/report-designer/records/<string:model_name>",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def get_records(self, model_name, **kwargs):
        """Return a list of records for the given model (for preview selector).

        Returns {records: [{id, display_name}]} or {error}.
        """
        try:
            model = request.env[model_name]
            model.check_access_rights("read")
        except (KeyError, Exception) as exc:
            return {"error": str(exc)}

        limit = kwargs.get("limit", 50)
        records = model.search([], limit=limit)
        result = []
        for rec in records:
            result.append(
                {
                    "id": rec.id,
                    "display_name": rec.display_name or str(rec.id),
                }
            )
        return {"records": result}

    # === PREVIEW === #

    @http.route(
        "/api/report-designer/layouts/<int:layout_id>/preview",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def preview_layout(self, layout_id, **kwargs):
        """Preview a published layout by rendering PDF.

        If the layout is not yet published, falls back to the live-preview
        endpoint which renders on-the-fly from the JSON.
        """
        layout = request.env["report.designer.layout"].browse(layout_id)
        if not layout.exists():
            return {"error": "Layout not found"}

        # If not published, delegate to live preview
        if not layout.report_action_id:
            return self._live_preview(
                layout.layout_json or "{}",
                layout.target_model,
                kwargs.get("record_id"),
                paper_format=layout.paper_format,
                paper_orientation=layout.paper_orientation,
            )

        record_id = kwargs.get("record_id")
        return self._render_pdf_preview(layout, record_id)

    @http.route(
        "/api/report-designer/preview/live",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def live_preview(self, **kwargs):
        """Live preview — render layout JSON to PDF or HTML without persisting.

        Accepts:
            - layout_json (str or dict): the layout definition
            - target_model (str): Odoo model name
            - record_id (int, optional): specific record to preview
            - format (str): "pdf" (default) or "html"
            - paper_format (str, optional): a4, letter, legal, a3
            - paper_orientation (str, optional): portrait, landscape

        Returns:
            - For PDF: {pdf_base64: str, record_count: int}
            - For HTML: {html: str, record_count: int}
        """
        layout_json = kwargs.get("layout_json", "{}")
        target_model = kwargs.get("target_model", "")
        record_id = kwargs.get("record_id")
        output_format = kwargs.get("format", "pdf")
        paper_format = kwargs.get("paper_format", "a4")
        paper_orientation = kwargs.get("paper_orientation", "portrait")

        if not target_model:
            return {"error": "target_model is required"}

        return self._live_preview(
            layout_json,
            target_model,
            record_id,
            output_format=output_format,
            paper_format=paper_format,
            paper_orientation=paper_orientation,
        )

    @http.route(
        "/api/report-designer/preview/html",
        type="json",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def live_preview_html(self, **kwargs):
        """Convenience endpoint that always returns HTML preview."""
        kwargs["format"] = "html"
        return self.live_preview(**kwargs)

    # === PREVIEW HELPERS (private) === #

    @staticmethod
    def _preview_cache_key(layout_json, target_model, record_id=None):
        """Generate a cache key for the preview result."""
        raw = json.dumps(
            {"json": layout_json, "model": target_model, "record": record_id},
            sort_keys=True,
            default=str,
        )
        return hashlib.sha256(raw.encode()).hexdigest()

    @staticmethod
    def _preview_cache_get(key):
        """Return cached HTML if still valid, else None."""
        entry = _PREVIEW_CACHE.get(key)
        if entry and (time.monotonic() - entry[1]) < _PREVIEW_CACHE_TTL:
            return entry[0]
        if entry:
            _PREVIEW_CACHE.pop(key, None)
        return None

    @staticmethod
    def _preview_cache_set(key, html_content):
        """Store HTML in preview cache, evicting oldest entries if needed."""
        if len(_PREVIEW_CACHE) >= _PREVIEW_CACHE_MAX:
            oldest_key = min(_PREVIEW_CACHE, key=lambda k: _PREVIEW_CACHE[k][1])
            _PREVIEW_CACHE.pop(oldest_key, None)
        _PREVIEW_CACHE[key] = (html_content, time.monotonic())

    def _live_preview(
        self,
        layout_json,
        target_model,
        record_id=None,
        output_format="pdf",
        paper_format="a4",
        paper_orientation="portrait",
    ):
        """Core live-preview: generate QWeb from JSON and render.

        HTML format creates a temporary ir.ui.view and renders via ir.qweb.
        PDF format creates a temporary ir.actions.report + ir.ui.view pair so
        that _render_qweb_pdf can resolve the template.
        """
        try:
            records = self._get_preview_records(target_model, record_id)
            if isinstance(records, dict):
                return records  # error dict

            # Check preview cache (HTML only)
            if output_format == "html":
                cache_key = self._preview_cache_key(
                    layout_json, target_model, record_id
                )
                cached = self._preview_cache_get(cache_key)
                if cached is not None:
                    return {"html": cached, "record_count": len(records)}

            # Generate QWeb XML on-the-fly
            layout_model = request.env["report.designer.layout"]
            qweb_xml = layout_model.generate_preview_qweb(
                layout_json,
                paper_format=paper_format,
                paper_orientation=paper_orientation,
            )

            # Create a temporary ir.ui.view with a stable template id
            tmp_view = request.env["ir.ui.view"].create(
                {
                    "name": "socger_report_designer.preview_temp",
                    "type": "qweb",
                    "arch": qweb_xml,
                }
            )

            try:
                if output_format == "html":
                    html_content = request.env["ir.qweb"]._render(
                        tmp_view.id, {"docs": records}
                    )
                    # Store in preview cache
                    self._preview_cache_set(cache_key, html_content)
                    return {"html": html_content, "record_count": len(records)}

                # PDF rendering — create a temporary ir.actions.report so
                # _render_qweb_pdf can resolve the template by report_name.
                report_name = f"socger_report_designer.preview_{tmp_view.id}"
                tmp_report = request.env["ir.actions.report"].create(
                    {
                        "name": "Preview",
                        "model": target_model,
                        "report_type": "qweb-pdf",
                        "report_name": report_name,
                        "report_file": report_name,
                    }
                )
                # Update the view's key so ir.qweb can find it by name
                tmp_view.write({"key": report_name})

                try:
                    pdf_content, _ = request.env["ir.actions.report"]._render_qweb_pdf(
                        report_name, records.ids
                    )
                    pdf_base64 = base64.b64encode(pdf_content).decode("utf-8")
                    return {
                        "pdf_base64": pdf_base64,
                        "record_count": len(records),
                    }
                finally:
                    tmp_report.unlink()
            finally:
                tmp_view.unlink()

        except Exception:
            _logger.exception("Error in live preview")
            return {"error": "Preview rendering failed. Check your layout elements."}

    def _render_pdf_preview(self, layout, record_id=None):
        """Render a PDF preview for a published layout."""
        try:
            records = self._get_preview_records(layout.target_model, record_id)
            if isinstance(records, dict):
                return records  # error dict

            pdf_content, _ = request.env["ir.actions.report"]._render_qweb_pdf(
                layout.report_action_id.report_name, records.ids
            )
            pdf_b64 = base64.b64encode(pdf_content).decode("utf-8")
            return {"pdf_base64": pdf_b64, "record_count": len(records)}
        except Exception:
            _logger.exception("Error rendering PDF preview")
            return {"error": "PDF rendering failed."}

    def _get_preview_records(self, target_model, record_id=None):
        """Get one or more records for preview rendering.

        Returns either an Odoo recordset or an error dict.
        """
        try:
            model = request.env[target_model]
            model.check_access_rights("read")
        except (KeyError, Exception) as exc:
            return {"error": str(exc)}

        if record_id:
            records = model.browse(record_id)
            if not records.exists():
                return {"error": f"Record {record_id} not found"}
            return records

        records = model.search([], limit=1)
        if not records:
            return {"error": f"No records found for model {target_model}"}
        return records
