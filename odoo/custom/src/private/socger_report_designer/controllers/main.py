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
        """Save layout JSON data and editable fields."""
        layout = request.env["report.designer.layout"].browse(layout_id)
        if not layout.exists():
            return {"error": "Layout not found"}

        layout_json = kwargs.get("layout_json")
        name = kwargs.get("name")
        target_model = kwargs.get("target_model")
        description = kwargs.get("description")
        paper_format = kwargs.get("paper_format")
        paper_orientation = kwargs.get("paper_orientation")

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
        if target_model:
            vals["target_model"] = target_model
        if description is not None:
            vals["description"] = description
        if paper_format:
            vals["paper_format"] = paper_format
        if paper_orientation:
            vals["paper_orientation"] = paper_orientation

        layout.write(vals)
        # Invalidate preview cache so subsequent previews use fresh data
        _PREVIEW_CACHE.clear()
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
            _logger.warning(
                "Records endpoint access denied for model %s: %s", model_name, exc
            )
            return {"error": str(exc)}

        limit = kwargs.get("limit", 50)
        records = model.search([], limit=limit)
        _logger.info(
            "Records endpoint: model=%s, limit=%s, found=%s records",
            model_name,
            limit,
            len(records),
        )
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

        _logger.info(
            "live_preview raw kwargs: target_model=%s, format=%s, paper=%s, orient=%s, "
            "has_record_id=%s, layout_json_len=%s",
            target_model,
            output_format,
            paper_format,
            paper_orientation,
            "yes" if record_id else "no",
            len(str(layout_json)),
        )

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
    def _preview_cache_key(
        layout_json,
        target_model,
        record_id=None,
        paper_format=None,
        paper_orientation=None,
    ):
        """Generate a cache key for the preview result."""
        raw = json.dumps(
            {
                "json": layout_json,
                "model": target_model,
                "record": record_id,
                "format": paper_format,
                "orientation": paper_orientation,
            },
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
        If QWeb rendering fails or returns empty content, falls back to a
        direct HTML generation path that resolves field values without QWeb.
        PDF format creates a temporary ir.actions.report + ir.ui.view pair so
        that _render_qweb_pdf can resolve the template.
        """
        _logger.info(
            "_live_preview called: model=%s, format=%s, paper=%s, orient=%s, "
            "record_id=%s, json_len=%s",
            target_model,
            output_format,
            paper_format,
            paper_orientation,
            record_id,
            len(str(layout_json)),
        )
        try:
            records = self._get_preview_records(target_model, record_id)
            if isinstance(records, dict):
                return records  # error dict

            _logger.info(
                "_live_preview records OK: model=%s, record_ids=%s, count=%s",
                target_model,
                records.ids,
                len(records),
            )

            # Check preview cache (HTML only)
            if output_format == "html":
                cache_key = self._preview_cache_key(
                    layout_json,
                    target_model,
                    record_id,
                    paper_format,
                    paper_orientation,
                )
                cached = self._preview_cache_get(cache_key)
                if cached is not None:
                    _logger.info("_live_preview: cache HIT for key=%s", cache_key[:12])
                    return {"html": cached, "record_count": len(records)}

            # Generate QWeb XML on-the-fly
            layout_model = request.env["report.designer.layout"]
            qweb_xml = layout_model.generate_preview_qweb(
                layout_json,
                paper_format=paper_format,
                paper_orientation=paper_orientation,
            )
            _logger.info(
                "_live_preview QWeb XML generated: len=%d, first_300=%s",
                len(qweb_xml),
                qweb_xml[:300],
            )

            if output_format == "html":
                # --- QWeb rendering path ---
                html_content = None
                qweb_error = None
                tmp_view = None
                try:
                    tmp_view = request.env["ir.ui.view"].create(
                        {
                            "name": "socger_report_designer.preview_temp",
                            "type": "qweb",
                            "arch": qweb_xml,
                        }
                    )
                    _logger.info(
                        "_live_preview temporary view created: id=%s, key=%s",
                        tmp_view.id,
                        tmp_view.key,
                    )

                    html_content = request.env["ir.qweb"]._render(
                        tmp_view.id,
                        {
                            "docs": records,
                            "doc_ids": records.ids,
                            "doc_model": target_model,
                        },
                    )
                    _logger.info(
                        "_live_preview QWeb _render returned: type=%s, len=%s",
                        type(html_content).__name__,
                        len(html_content) if html_content else 0,
                    )
                    if html_content:
                        _logger.info(
                            "_live_preview HTML first_500=%s",
                            html_content[:500],
                        )
                    else:
                        _logger.warning(
                            "_live_preview QWeb _render returned empty/None!"
                        )

                    # Strip <template> wrapper if present — in HTML5 the
                    # <template> element is INERT (not rendered visually),
                    # so the iframe would show a blank page.
                    if html_content and isinstance(html_content, str):
                        html_content = self._strip_template_wrapper(html_content)
                except Exception as exc:
                    qweb_error = exc
                    _logger.exception("_live_preview QWeb _render FAILED: %s", exc)
                finally:
                    if tmp_view:
                        try:
                            tmp_view.unlink()
                        except Exception:
                            _logger.debug(
                                "Failed to unlink temp view %s",
                                tmp_view.id,
                                exc_info=True,
                            )

                # If QWeb produced valid HTML, use it
                if html_content and len(html_content) > 100:
                    self._preview_cache_set(cache_key, html_content)
                    return {"html": html_content, "record_count": len(records)}

                # --- Fallback: direct HTML generation (bypass QWeb) ---
                _logger.warning(
                    "_live_preview QWeb path produced empty/short content "
                    "(len=%s, error=%s). Falling back to direct HTML.",
                    len(html_content) if html_content else 0,
                    qweb_error,
                )
                html_content = self._generate_preview_html_direct(
                    layout_json,
                    records,
                    paper_format,
                    paper_orientation,
                )
                _logger.info(
                    "_live_preview direct HTML fallback: len=%d, first_500=%s",
                    len(html_content),
                    html_content[:500],
                )
                self._preview_cache_set(cache_key, html_content)
                return {"html": html_content, "record_count": len(records)}

            # --- PDF rendering path ---
            tmp_view = request.env["ir.ui.view"].create(
                {
                    "name": "socger_report_designer.preview_temp",
                    "type": "qweb",
                    "arch": qweb_xml,
                }
            )
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
            _logger.warning(
                "Preview records access denied for model %s: %s", target_model, exc
            )
            return {"error": str(exc)}

        if record_id:
            records = model.browse(record_id)
            if not records.exists():
                return {"error": f"Record {record_id} not found"}
            _logger.info(
                "Preview using record %s for model %s", record_id, target_model
            )
            return records

        records = model.search([], limit=1)
        if not records:
            _logger.warning("No records found for model %s in preview", target_model)
            return {"error": f"No records found for model {target_model}"}
        _logger.info(
            "Preview using first record ID=%s for model %s",
            records[0].id,
            target_model,
        )
        return records

    # === DIRECT HTML FALLBACK (bypass QWeb) === #

    @staticmethod
    def _strip_template_wrapper(html):
        """Remove <template>...</template> wrapper from QWeb-rendered HTML.

        Odoo's ``web.html_preview_container`` wraps the output in a
        ``<template>`` element.  In HTML5 this element is *inert* — its
        content is stored in a DocumentFragment and is **not rendered**
        visually.  Since we inject this HTML into an iframe via
        ``document.write()``, the wrapper must be stripped.
        """
        if not html:
            return html
        html = str(html)
        # Quick check — avoid regex overhead for the common case
        if not html.lstrip().startswith("<template"):
            return html

        # Strip opening <template...> tag
        import re

        html = re.sub(r"<template[^>]*>\s*", "", html, count=1, flags=re.IGNORECASE)
        # Strip closing </template> tag
        html = re.sub(r"\s*</template>\s*$", "", html, flags=re.IGNORECASE)
        return html

    @staticmethod
    def _resolve_field_value(record, field_path):
        """Resolve a dotted field path to its value on a record.

        Traverses relational fields (e.g. ``partner_id.name``).
        Returns empty string on any resolution failure.
        """
        if not field_path:
            return ""
        parts = field_path.split(".")
        value = record
        for part in parts:
            if not part:
                continue
            try:
                value = getattr(value, part)
                # If we hit a recordset, browse into it for the next part
                if hasattr(value, "ids") and len(value) == 1:
                    pass  # single-record recordset, continue traversal
                elif hasattr(value, "ids") and len(value) == 0:
                    return ""
            except Exception:
                return ""
        # Format the final value
        if hasattr(value, "ids"):
            # It's a recordset — return display_name
            return value.display_name if value else ""
        if value is False or value is None:
            return ""
        return str(value)

    def _build_style_attr(self, style):
        """Convert a style dict to an inline CSS ``style="..."`` attribute."""
        if not style:
            return ""
        mapping = {
            "fontSize": lambda v: f"font-size: {v}pt",
            "fontWeight": lambda v: f"font-weight: {v}",
            "fontStyle": lambda v: f"font-style: {v}",
            "color": lambda v: f"color: {v}",
            "backgroundColor": lambda v: f"background-color: {v}",
            "textAlign": lambda v: f"text-align: {v}",
            "textDecoration": lambda v: f"text-decoration: {v}",
            "lineHeight": lambda v: f"line-height: {v}",
            "padding": lambda v: f"padding: {v}px",
            "paddingTop": lambda v: f"padding-top: {v}px",
            "paddingBottom": lambda v: f"padding-bottom: {v}px",
            "paddingLeft": lambda v: f"padding-left: {v}px",
            "paddingRight": lambda v: f"padding-right: {v}px",
            "margin": lambda v: f"margin: {v}px",
            "marginTop": lambda v: f"margin-top: {v}px",
            "marginBottom": lambda v: f"margin-bottom: {v}px",
            "marginLeft": lambda v: f"margin-left: {v}px",
            "marginRight": lambda v: f"margin-right: {v}px",
            "borderBottom": lambda v: f"border-bottom: {v}",
            "borderTop": lambda v: f"border-top: {v}",
            "width": lambda v: f"width: {v}" if isinstance(v, str) else f"width: {v}px",
            "maxWidth": lambda v: f"max-width: {v}"
            if isinstance(v, str)
            else f"max-width: {v}px",
            "minWidth": lambda v: f"min-width: {v}"
            if isinstance(v, str)
            else f"min-width: {v}px",
            "height": lambda v: f"height: {v}"
            if isinstance(v, str)
            else f"height: {v}px",
            "opacity": lambda v: f"opacity: {v}",
            "display": lambda v: f"display: {v}",
            "level": lambda v: "",
        }
        parts = []
        for key, formatter in mapping.items():
            val = style.get(key)
            if val is not None and val != "":
                parts.append(formatter(val))
        css = "; ".join(parts)
        return f' style="{css}"' if css else ""

    @staticmethod
    def _safe_xml(text):
        """Escape XML/HTML entities in text."""
        if not text:
            return ""
        return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def _render_element_to_html_direct(self, record, element):
        """Render a single element to HTML, resolving field values directly.

        This bypasses QWeb entirely — used as a fallback when QWeb rendering
        fails or returns empty content.
        """
        elem_type = element.get("type", "text")
        style = element.get("style", {})
        attr = self._build_style_attr(style)

        if elem_type == "text":
            field_path = element.get("fieldPath", "")
            content = element.get("content", "")
            if field_path:
                clean = field_path.lstrip(".")
                value = self._resolve_field_value(record, clean)
                return f"<p{attr}>{self._safe_xml(value)}</p>"
            if content:
                return f"<p{attr}>{self._safe_xml(content)}</p>"
            return ""

        if elem_type == "heading":
            content = element.get("content", "Heading")
            level = style.get("level", 2)
            return f"<h{level}{attr}>{self._safe_xml(content)}</h{level}>"

        if elem_type == "line":
            return "<hr/>"

        if elem_type == "spacer":
            height = style.get("height", "20px")
            spacer_attr = self._build_style_attr({"height": height})
            return f"<div{spacer_attr}></div>"

        if elem_type == "pagebreak":
            return '<div style="page-break-after: always;"></div>'

        if elem_type == "html":
            field_path = element.get("fieldPath", "")
            content = element.get("content", "")
            if field_path:
                clean = field_path.lstrip(".")
                value = self._resolve_field_value(record, clean)
                return f"<div{attr}>{value}</div>"
            return f"<div{attr}>{content}</div>"

        if elem_type == "image":
            field_path = element.get("fieldPath", "")
            if not field_path:
                return '<p class="text-muted">[Image — no field bound]</p>'
            max_width = style.get("maxWidth", "200px")
            return (
                f'<img src="" alt="{self._safe_xml(field_path)}"'
                f' style="max-width: {max_width};"/>'
            )

        if elem_type == "table":
            return self._render_table_to_html_direct(record, element)

        if elem_type == "container":
            return self._render_container_to_html_direct(record, element)

        return ""

    def _render_table_to_html_direct(self, record, element):
        """Render a table element to HTML with direct field resolution."""
        data_source = element.get("dataSource", "")
        columns = element.get("columns", [])
        t_style = element.get("tableStyle", {})

        if not data_source or not columns:
            return ""

        # Resolve the O2M/M2M field
        clean_ds = data_source.lstrip(".")
        lines = self._resolve_field_value(record, clean_ds)
        # If it's a recordset, iterate; otherwise treat as list
        if hasattr(lines, "__iter__") and not isinstance(lines, str):
            line_records = list(lines)
        else:
            return ""

        # Table classes
        table_classes = "table table-bordered table-sm"
        border_color = t_style.get("borderColor", "")
        border_attr = f' style="border-color: {border_color};"' if border_color else ""

        # Header
        header_bg = t_style.get("headerBgColor", "#e9ecef")
        header_fs = t_style.get("headerFontSize", 10)
        header_color = t_style.get("headerColor", "#495057")
        header_fw = t_style.get("headerFontWeight", "bold")
        h_style = (
            f"background-color: {header_bg}; font-size: {header_fs}px;"
            f" color: {header_color}; font-weight: {header_fw};"
        )
        ths = []
        for col in columns:
            ht = self._safe_xml(col.get("header", ""))
            ths.append(f'<th style="{h_style}">{ht}</th>')

        # Body rows
        rows = []
        for line in line_records:
            tds = []
            for col in columns:
                fp = col.get("fieldPath", "")
                align = col.get("align", "")
                td_style_parts = []
                if align:
                    td_style_parts.append(f"text-align: {align}")
                if border_color:
                    td_style_parts.append(f"border-color: {border_color}")
                td_attr = (
                    f' style="{"; ".join(td_style_parts)}"' if td_style_parts else ""
                )
                if fp:
                    val = self._resolve_field_value(line, fp)
                    tds.append(f"<td{td_attr}>{self._safe_xml(val)}</td>")
                else:
                    tds.append(f"<td{td_attr}></td>")
            rows.append("<tr>\n" + "\n".join(tds) + "\n</tr>")

        thead = "<tr>\n" + "\n".join(ths) + "\n</tr>"
        tbody = "\n".join(rows)

        return (
            f'<table class="{table_classes}"{border_attr}>\n'
            f"  <thead>{thead}</thead>\n"
            f"  <tbody>{tbody}</tbody>\n"
            f"</table>"
        )

    def _render_container_to_html_direct(self, record, element):
        """Render a container element to HTML with direct field resolution."""
        columns = element.get("columns", [])
        children = element.get("children", [])
        style = element.get("style", {})
        attr = self._build_style_attr(style)

        if columns:
            total_cols = len(columns) or 1
            col_size = 12 // total_cols
            col_parts = []
            for col_elements in columns:
                inner = []
                for child in col_elements:
                    html = self._render_element_to_html_direct(record, child)
                    if html:
                        inner.append(html)
                inner_html = "\n".join(inner) if inner else ""
                col_parts.append(f'<div class="col-{col_size}">\n{inner_html}\n</div>')
            return f'<div class="row"{attr}>\n' + "\n".join(col_parts) + "\n</div>"

        if children:
            inner = []
            for child in children:
                html = self._render_element_to_html_direct(record, child)
                if html:
                    inner.append(html)
            inner_html = "\n".join(inner) if inner else ""
            return f"<div{attr}>\n{inner_html}\n</div>"

        return f"<div{attr}></div>"

    def _generate_preview_html_direct(
        self,
        layout_json,
        records,
        paper_format="a4",
        paper_orientation="portrait",
    ):
        """Generate a full HTML preview page, resolving fields directly.

        Bypasses QWeb entirely — used as fallback when QWeb rendering fails.
        Produces a standalone HTML page with inline CSS for page dimensions.
        """
        try:
            layout = (
                json.loads(layout_json)
                if isinstance(layout_json, str)
                else (layout_json or {})
            )
        except (json.JSONDecodeError, TypeError):
            layout = {}

        elements = layout.get("elements", [])

        # Page dimensions in mm
        paper_sizes = {
            "a4": (210, 297),
            "letter": (216, 279),
            "legal": (216, 356),
            "a3": (297, 420),
        }
        w_mm, h_mm = paper_sizes.get(paper_format, (210, 297))
        if paper_orientation == "landscape":
            w_mm, h_mm = h_mm, w_mm
        w_px = int(w_mm * 3.78)
        h_px = int(h_mm * 3.78)

        # Build pages — one per record
        pages = []
        for record in records:
            body_parts = []
            for element in elements:
                html = self._render_element_to_html_direct(record, element)
                if html:
                    body_parts.append(html)
            body_html = "\n".join(body_parts) if body_parts else "<p>No content</p>"
            pages.append(f'<div class="page">\n{body_html}\n</div>')

        pages_html = "\n".join(pages)

        return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  @page {{ size: {w_mm}mm {h_mm}mm; margin: 20mm 15mm 20mm 15mm; }}
  @media screen {{
    html, body {{
      background: #e0e0e0;
      margin: 0; padding: 10px 0;
      max-width: none; width: auto;
      overflow-x: auto; overflow-y: auto;
    }}
    .page {{
      display: block;
      width: {w_px}px;
      min-height: {h_px}px;
      margin: 10px auto;
      padding: 20mm 15mm 20mm 15mm;
      background: #fff;
      box-shadow: 0 2px 12px rgba(0,0,0,0.15);
      overflow: hidden;
      box-sizing: border-box;
      float: none;
      max-width: none;
      page-break-after: always;
    }}
  }}
  @media print {{
    .page {{ page-break-after: always; }}
  }}
  body {{ font-family: arial, sans-serif; font-size: 12pt; }}
  table {{ border-collapse: collapse; width: 100%; }}
  table th, table td {{ border: 1px solid #ddd; padding: 6px 8px; }}
  table th {{ background-color: #e9ecef; font-weight: bold; }}
</style>
</head>
<body>
{pages_html}
</body>
</html>"""
