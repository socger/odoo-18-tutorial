import json
import logging

from odoo import _, api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class ReportDesignerLayout(models.Model):
    _name = "report.designer.layout"
    _description = "Report Designer Layout"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, name"
    _check_company_auto = True

    # === BASIC FIELDS === #
    name: str = fields.Char(
        string="Name",
        required=True,
        tracking=True,
        index="btree",
    )
    active: bool = fields.Boolean(default=True)
    sequence: int = fields.Integer(default=10)
    description: str = fields.Text(string="Description")

    # === TARGET MODEL === #
    target_model: str = fields.Char(
        string="Target Model",
        required=True,
        tracking=True,
        help="Odoo model to generate report for (e.g., sale.order)",
    )

    # === LAYOUT DATA (JSON) === #
    layout_json: str = fields.Text(
        string="Layout JSON",
        help="Visual layout definition in JSON format",
        tracking=True,
    )

    # === PUBLISHED REPORT === #
    state: str = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("published", "Published"),
        ],
        string="Status",
        default="draft",
        required=True,
        tracking=True,
        copy=False,
    )
    qweb_template_id: int = fields.Many2one(
        comodel_name="ir.ui.view",
        string="QWeb Template",
        readonly=True,
        copy=False,
        help="Published QWeb template",
    )
    report_action_id: int = fields.Many2one(
        comodel_name="ir.actions.report",
        string="Report Action",
        readonly=True,
        copy=False,
        help="Published report action (appears in Print menu)",
    )
    paper_format_id: int = fields.Many2one(
        comodel_name="report.paperformat",
        string="Paper Format",
        default=lambda self: self.env.ref(
            "base.paperformat_euro", raise_if_not_found=False
        ),
    )
    paper_format: str = fields.Selection(
        selection=[
            ("a4", "A4"),
            ("letter", "Letter"),
            ("legal", "Legal"),
            ("a3", "A3"),
        ],
        string="Paper Size",
        default="a4",
        required=True,
    )
    paper_orientation: str = fields.Selection(
        selection=[
            ("portrait", "Portrait"),
            ("landscape", "Landscape"),
        ],
        string="Orientation",
        default="portrait",
        required=True,
    )

    # === VERSION CONTROL === #
    version: int = fields.Integer(
        string="Version",
        default=1,
        readonly=True,
        copy=False,
    )
    last_publish_date: str = fields.Datetime(
        string="Last Published",
        readonly=True,
        copy=False,
    )

    # === COMPANY === #
    company_id: int = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )

    # === COMPUTED FIELDS === #
    element_count: int = fields.Integer(
        string="Elements",
        compute="_compute_element_count",
    )
    has_template: bool = fields.Boolean(
        string="Has Published Template",
        compute="_compute_has_template",
    )

    @api.depends("layout_json")
    def _compute_element_count(self):
        for record in self:
            if record.layout_json:
                try:
                    layout = json.loads(record.layout_json)
                    record.element_count = len(layout.get("elements", []))
                except (json.JSONDecodeError, TypeError):
                    record.element_count = 0
            else:
                record.element_count = 0

    @api.depends("qweb_template_id")
    def _compute_has_template(self):
        for record in self:
            record.has_template = bool(record.qweb_template_id)

    # === CONSTRAINTS === #
    @api.constrains("target_model")
    def _check_target_model(self):
        for record in self:
            if record.target_model:
                try:
                    self.env[record.target_model]
                except KeyError:
                    raise UserError(
                        _(
                            "Model '%s' does not exist in Odoo.",
                            record.target_model,
                        )
                    ) from None

    @api.constrains("layout_json")
    def _check_layout_json(self):
        for record in self:
            if record.layout_json:
                try:
                    json.loads(record.layout_json)
                except json.JSONDecodeError as e:
                    raise UserError(_("Invalid JSON in layout: %s", str(e))) from e

    # === CRUD METHODS === #
    @api.model_create_multi
    def create(self, vals_list: list[dict]) -> "ReportDesignerLayout":
        for vals in vals_list:
            if not vals.get("name"):
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "report.designer.layout"
                ) or _("New Report Layout")
        return super().create(vals_list)

    def write(self, vals: dict) -> bool:
        if "layout_json" in vals and self.state == "published":
            # Increment version when layout changes after publishing
            vals["version"] = self.version + 1
            vals["state"] = "draft"
        return super().write(vals)

    def copy(self, default=None):
        default = dict(default or {})
        default.update(
            {
                "name": _("%s (Copy)", self.name),
                "state": "draft",
                "version": 1,
                "qweb_template_id": False,
                "report_action_id": False,
                "last_publish_date": False,
            }
        )
        return super().copy(default)

    # === ACTION METHODS === #
    def action_publish(self):
        """Publish the report layout to Odoo."""
        for record in self:
            if not record.layout_json:
                raise UserError(_("Cannot publish a layout without design data."))
            # Verify the layout actually has elements
            try:
                layout = json.loads(record.layout_json)
            except (json.JSONDecodeError, TypeError):
                raise UserError(
                    _("Layout JSON is invalid. Fix it before publishing.")
                ) from None
            if not layout.get("elements"):
                raise UserError(
                    _("Cannot publish a layout without elements. Add some first.")
                )

            # Generate QWeb XML from JSON
            qweb_xml = self._generate_qweb_xml(record)

            # Create or update QWeb template
            if record.qweb_template_id:
                record.qweb_template_id.write({"arch": qweb_xml})
            else:
                template = self.env["ir.ui.view"].create(
                    {
                        "name": f"Report: {record.name}",
                        "type": "qweb",
                        "arch": qweb_xml,
                    }
                )
                record.qweb_template_id = template

            # Create or update report action
            report_name = f"socger_report_designer.report_designer_layout_{record.id}"
            if record.report_action_id:
                record.report_action_id.write(
                    {
                        "name": record.name,
                        "report_name": report_name,
                        "report_file": report_name,
                        "paperformat_id": record.paper_format_id.id
                        if record.paper_format_id
                        else False,
                    }
                )
            else:
                model_id = self.env["ir.model"]._get(record.target_model).id
                action = self.env["ir.actions.report"].create(
                    {
                        "name": record.name,
                        "model": record.target_model,
                        "report_type": "qweb-pdf",
                        "report_name": report_name,
                        "report_file": report_name,
                        "binding_model_id": model_id,
                        "binding_type": "report",
                        "paperformat_id": record.paper_format_id.id
                        if record.paper_format_id
                        else False,
                    }
                )
                record.report_action_id = action

            record.write(
                {
                    "state": "published",
                    "last_publish_date": fields.Datetime.now(),
                }
            )

        return True

    def action_unpublish(self):
        """Unpublish the report layout."""
        for record in self:
            if record.report_action_id:
                record.report_action_id.unlink()
            if record.qweb_template_id:
                record.qweb_template_id.unlink()
            record.write(
                {
                    "state": "draft",
                    "qweb_template_id": False,
                    "report_action_id": False,
                }
            )

    def action_preview(self):
        """Open preview of the report."""
        self.ensure_one()
        if not self.report_action_id:
            raise UserError(_("Please publish the report first."))
        return self.report_action_id.report_action(self.report_action_id.id)

    def action_open_designer(self):
        """Open the visual report designer (React client action)."""
        self.ensure_one()
        return {
            "type": "ir.actions.client",
            "tag": "socger_report_designer.ReportDesignerAction",
            "name": _("Report Designer"),
            "context": {"active_id": self.id},
        }

    # === PRIVATE METHODS === #
    def _generate_qweb_xml(self, record):
        """Generate QWeb XML template from layout JSON."""
        body_content = self._build_body_content(record)

        # Build complete QWeb template
        template_xml_id = (
            f"socger_report_designer.template_report_designer_layout_{record.id}"
        )
        template_xml = f"""<template id="{template_xml_id}">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    {body_content}
                </div>
            </t>
        </t>
    </t>
</template>"""

        return template_xml

    def generate_preview_qweb(self, layout_json):
        """Generate QWeb XML from layout JSON without persisting to ir.ui.view.

        Used by the live-preview endpoint so the user can preview without
        publishing first.
        """
        try:
            layout = (
                json.loads(layout_json) if isinstance(layout_json, str) else layout_json
            )
        except (json.JSONDecodeError, TypeError):
            layout = {}

        elements = layout.get("elements", [])
        xml_elements = []
        for element in elements:
            xml_elem = self._render_element_to_xml(element)
            if xml_elem:
                xml_elements.append(xml_elem)

        body_content = "\n".join(xml_elements) if xml_elements else "<p>No content</p>"

        return f"""<template>
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    {body_content}
                </div>
            </t>
        </t>
    </t>
</template>"""

    def _build_body_content(self, record):
        """Parse layout JSON and render all elements to QWeb XML body."""
        try:
            layout = json.loads(record.layout_json)
        except (json.JSONDecodeError, TypeError):
            layout = {}

        elements = layout.get("elements", [])
        xml_elements = []
        for element in elements:
            xml_elem = self._render_element_to_xml(element)
            if xml_elem:
                xml_elements.append(xml_elem)

        return "\n".join(xml_elements) if xml_elements else "<p>No content</p>"

    # === STYLE HELPERS === #

    def _build_style_string(self, style):
        """Convert a style dict to an inline CSS string.

        Supported keys: fontSize, fontWeight, color, textAlign, backgroundColor,
        padding, margin, marginTop, marginBottom, marginLeft, marginRight,
        borderBottom, borderTop, lineHeight, textDecoration, width, maxWidth,
        minWidth, height, opacity, display.
        """
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
        }

        parts = []
        for key, formatter in mapping.items():
            val = style.get(key)
            if val is not None and val != "":
                parts.append(formatter(val))
        return "; ".join(parts)

    def _style_attr(self, style):
        """Return `` style="..." `` attribute string (with leading space) or empty."""
        css = self._build_style_string(style)
        return f' style="{css}"' if css else ""

    # === ELEMENT RENDERING === #

    def _render_element_to_xml(self, element):
        """Render a single element to QWeb XML."""
        elem_type = element.get("type", "text")
        condition = element.get("condition", "")

        renderers = {
            "text": lambda: self._render_text_element(element),
            "heading": lambda: self._render_heading_element(element),
            "line": lambda: self._render_line_element(element),
            "image": lambda: self._render_image_element(element),
            "table": lambda: self._render_table_element(element),
            "spacer": lambda: self._render_spacer_element(element),
            "pagebreak": lambda: self._render_pagebreak_element(element),
            "container": lambda: self._render_container_element(element),
            "html": lambda: self._render_html_element(element),
        }

        renderer = renderers.get(elem_type)
        if not renderer:
            _logger.warning("Unknown element type: %s", elem_type)
            return ""

        inner_xml = renderer()
        if not inner_xml:
            return ""

        # Wrap in t-if when a condition is set
        if condition:
            return f'<t t-if="{condition}">\n{inner_xml}\n</t>'

        return inner_xml

    def _render_text_element(self, element):
        """Render a text element — can bind to a field or show static content."""
        field_path = element.get("fieldPath", "")
        content = element.get("content", "")
        style = element.get("style", {})
        attr = self._style_attr(style)

        if field_path:
            # Use t-field for automatic formatting (dates, monetary, etc.)
            return f'<p{attr}><span t-field="o.{field_path}"/></p>'
        if content:
            # Static text — escape XML entities
            safe = (
                content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            )
            return f"<p{attr}>{safe}</p>"
        return ""

    def _render_heading_element(self, element):
        """Render a heading element (h1–h6)."""
        content = element.get("content", "Heading")
        style = element.get("style", {})
        level = style.get("level", 2)
        attr = self._style_attr(style)
        safe = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f"<h{level}{attr}>{safe}</h{level}>"

    def _render_line_element(self, _element):
        """Render a horizontal rule."""
        return "<hr/>"

    def _render_image_element(self, element):
        """Render an image — binds to a binary/image field."""
        field_path = element.get("fieldPath", "")
        style = element.get("style", {})
        max_width = style.get("maxWidth", "200px")

        if not field_path:
            return '<p class="text-muted">[Image — no field bound]</p>'

        return (
            f'<img t-att-src="image_data_uri(o.{field_path})"'
            f' style="max-width: {max_width};"/>'
        )

    def _render_spacer_element(self, element):
        """Render an empty spacer div with configurable height."""
        style = element.get("style", {})
        height = style.get("height", "20px")
        attr = self._style_attr({"height": height})
        return f"<div{attr}/>\n"

    def _render_pagebreak_element(self, _element):
        """Render a page break (CSS ``page-break-after: always``)."""
        return '<div style="page-break-after: always;"/>'

    def _render_container_element(self, element):
        """Render a container (div) that groups child elements.

        The element may carry a ``columns`` list in the JSON, each column
        being a sub-list of elements.  When columns are present the output
        uses Bootstrap row/col grid; otherwise it renders as a plain div.
        """
        children = element.get("children", [])
        columns = element.get("columns", [])
        style = element.get("style", {})
        attr = self._style_attr(style)

        if columns:
            # Bootstrap multi-column grid
            col_parts = []
            total_cols = columns.__len__() or 1
            col_size = 12 // total_cols
            for col_elements in columns:
                inner = []
                for child in col_elements:
                    xml = self._render_element_to_xml(child)
                    if xml:
                        inner.append(xml)
                inner_xml = "\n".join(inner) if inner else ""
                col_parts.append(f'<div class="col-{col_size}">\n{inner_xml}\n</div>')
            cols_xml = "\n".join(col_parts)
            return f'<div class="row"{attr}>\n{cols_xml}\n</div>'

        if children:
            inner = []
            for child in children:
                xml = self._render_element_to_xml(child)
                if xml:
                    inner.append(xml)
            inner_xml = "\n".join(inner) if inner else ""
            return f"<div{attr}>\n{inner_xml}\n</div>"

        return f"<div{attr}/>"

    def _render_html_element(self, element):
        """Render an HTML field (raw content from Odoo, e.g. ``t-field`` for html)."""
        field_path = element.get("fieldPath", "")
        style = element.get("style", {})
        attr = self._style_attr(style)

        if field_path:
            return f'<div{attr}><t t-field="o.{field_path}"/></div>'
        content = element.get("content", "")
        return f"<div{attr}>{content}</div>"

    # === TABLE RENDERING === #

    def _render_table_element(self, element):
        """Render a table element to QWeb XML.

        The element JSON may contain:
            - dataSource: O2M field name to iterate over
            - columns: list of {header, fieldPath, fieldType, align, width}
            - style: optional table-level styling
        """
        data_source = element.get("dataSource", "")
        columns = element.get("columns", [])
        table_style = element.get("style", {})

        if not data_source or not columns:
            return ""

        table_attr = self._style_attr(table_style)

        # Build header cells
        header_cells = []
        for col in columns:
            header_text = col.get("header", "")
            safe = (
                header_text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            header_cells.append(f"<th>{safe}</th>")
        header_row = "<tr>\n" + "\n".join(header_cells) + "\n</tr>"

        # Build body rows
        body_cells = []
        for col in columns:
            field_path = col.get("fieldPath", "")
            align = col.get("align", "")
            width = col.get("width", "")
            td_style_parts = []
            if align:
                td_style_parts.append(f"text-align: {align}")
            if width:
                td_style_parts.append(f"width: {width}")
            td_attr = f' style="{"; ".join(td_style_parts)}"' if td_style_parts else ""
            if field_path:
                body_cells.append(
                    f"<td{td_attr}><span t-field='line.{field_path}'/></td>"
                )
            else:
                body_cells.append(f"<td{td_attr}/>")

        body_row = "<tr>\n" + "\n".join(body_cells) + "\n</tr>"

        return f"""<table class="table table-sm"{table_attr}>
    <thead>
        {header_row}
    </thead>
    <tbody>
        <t t-foreach="o.{data_source}" t-as="line">
            {body_row}
        </t>
    </tbody>
</table>"""
