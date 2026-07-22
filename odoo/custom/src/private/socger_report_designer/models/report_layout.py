import json
import logging
from xml.etree import ElementTree

from odoo import _, api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


# Paper format/orientation → report.paperformat XML-ID mapping.
# A4 Portrait uses Odoo's built-in ``base.paperformat_euro``.
_PAPER_FORMAT_MAP = {
    ("a4", "portrait"): "base.paperformat_euro",
    ("a4", "landscape"): "socger_report_designer.paperformat_a4_landscape",
    ("letter", "portrait"): "socger_report_designer.paperformat_letter_portrait",
    ("letter", "landscape"): "socger_report_designer.paperformat_letter_landscape",
    ("legal", "portrait"): "socger_report_designer.paperformat_legal_portrait",
    ("legal", "landscape"): "socger_report_designer.paperformat_legal_landscape",
    ("a3", "portrait"): "socger_report_designer.paperformat_a3_portrait",
    ("a3", "landscape"): "socger_report_designer.paperformat_a3_landscape",
}

# Dimensions in mm for @page CSS overrides (width, height).
_PAPER_SIZE_MM = {
    "a4": (210, 297),
    "letter": (216, 279),
    "legal": (216, 356),
    "a3": (297, 420),
}


def _resolve_paper_format(env, paper_format, paper_orientation):
    """Resolve paper_format + orientation to a ``report.paperformat`` record.

    Works without needing a record on ``report.designer.layout``.
    Falls back to ``base.paperformat_euro`` when no mapping is found.
    """
    key = (paper_format, paper_orientation)
    xml_id = _PAPER_FORMAT_MAP.get(key, "base.paperformat_euro")
    return env.ref(xml_id, raise_if_not_found=False) or env.ref("base.paperformat_euro")


def _build_page_css(env, paper_format, paper_orientation, paper_format_id=None):
    """Return ``@page`` CSS string for the given paper format.

    Works at module / model level without needing a layout record.
    """
    pf = paper_format_id or _resolve_paper_format(env, paper_format, paper_orientation)
    w_mm, h_mm = _PAPER_SIZE_MM.get(paper_format, (210, 297))
    if paper_orientation == "landscape":
        w_mm, h_mm = h_mm, w_mm
    # Margins in mm from the paperformat record
    mt = pf.margin_top or 40
    mb = pf.margin_bottom or 20
    ml = pf.margin_left or 7
    mr = pf.margin_right or 7
    return (
        f"@page {{ size: {w_mm}mm {h_mm}mm; " f"margin: {mt}mm {mr}mm {mb}mm {ml}mm; }}"
    )


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

    # === PAPER FORMAT RESOLUTION === #

    def _resolve_paper_format_id(self):
        """Resolve paper_format + paper_orientation to a ``report.paperformat`` record.

        Falls back to ``base.paperformat_euro`` when no mapping is found.
        """
        self.ensure_one()
        return _resolve_paper_format(
            self.env, self.paper_format, self.paper_orientation
        )

    def _page_css(self):
        """Return ``@page`` CSS string derived from the paper format.

        This is injected into QWeb templates so wkhtmltopdf renders with the
        correct page dimensions and margins.
        """
        self.ensure_one()
        return _build_page_css(
            self.env,
            self.paper_format,
            self.paper_orientation,
            self.paper_format_id,
        )

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

    # === XML VALIDATION === #

    def _validate_xml(self, xml_string):
        """Validate that a string is well-formed XML.

        Raises UserError if parsing fails.
        """
        try:
            ElementTree.fromstring(xml_string)
        except ElementTree.ParseError as exc:
            # pylint: disable=translation-not-lazy
            raise UserError(
                _("Generated XML is not well-formed: %s") % (str(exc),)
            ) from exc

    def generate_xml_from_json(self, layout_json):
        """Public method: generate QWeb XML from layout JSON string or dict.

        Returns the validated XML string.
        """
        if isinstance(layout_json, str):
            try:
                layout = json.loads(layout_json)
            except (json.JSONDecodeError, TypeError):
                layout = {}
        else:
            layout = layout_json or {}

        elements = layout.get("elements", [])
        xml_elements = []
        for element in elements:
            xml_elem = self._render_element_to_xml(element)
            if xml_elem:
                xml_elements.append(xml_elem)

        body_content = "\n".join(xml_elements) if xml_elements else "<p>No content</p>"

        template_xml = f"""<template>
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
        self._validate_xml(template_xml)
        return template_xml

    # === PRIVATE METHODS === #
    def _generate_qweb_xml(self, record):
        """Generate QWeb XML template from layout JSON."""
        body_content = self._build_body_content(record)

        # Auto-resolve paper format if not set
        if not record.paper_format_id:
            record.paper_format_id = record._resolve_paper_format_id()

        # Build @page CSS for paper dimensions and margins
        page_css = record._page_css()

        # Build complete QWeb template
        template_xml_id = (
            f"socger_report_designer.template_report_designer_layout_{record.id}"
        )
        template_xml = f"""<template id="{template_xml_id}">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    <style>{page_css}</style>
                    {body_content}
                </div>
            </t>
        </t>
    </t>
</template>"""

        self._validate_xml(template_xml)
        return template_xml

    def generate_preview_qweb(
        self, layout_json, paper_format="a4", paper_orientation="portrait"
    ):
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

        # Resolve paper format for preview (model-level, no record needed).
        # Priority: layout JSON style > explicit params > defaults (A4 portrait).
        style = layout.get("style", {})
        pf_name = style.get("paperFormat", paper_format)
        pf_orient = style.get("paperOrientation", paper_orientation)
        page_css = _build_page_css(self.env, pf_name, pf_orient)

        return f"""<template>
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    <style>{page_css}</style>
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

    # === FIELD FORMAT → t-options WIDGET MAP === #
    _FIELD_FORMAT_OPTIONS = {
        "monetary": {"widget": "monetary"},
        "date": {"format": "dd MMMM yyyy"},
        "datetime": {"format": "dd MMMM yyyy HH:mm"},
        "float_time": {"widget": "float_time"},
        "float": {"widget": "float", "precision": 2},
        "integer": {"widget": "integer"},
        "char": {"widget": "char"},
        "html": {"widget": "html"},
        "selection": {"widget": "selection"},
        "many2one": {"widget": "many2one"},
    }

    def _render_text_element(self, element):
        """Render a text element — can bind to a field or show static content."""
        field_path = element.get("fieldPath", "")
        content = element.get("content", "")
        style = element.get("style", {})
        attr = self._style_attr(style)

        if field_path:
            # Build t-options when a custom field format is set
            field_format = (style or {}).get("fieldFormat", "")
            t_options_attr = ""
            if field_format and field_format in self._FIELD_FORMAT_OPTIONS:
                opts = self._FIELD_FORMAT_OPTIONS[field_format]
                # For monetary we need display_currency — use o.currency_id if available
                if field_format == "monetary":
                    opts = {"widget": "monetary", "display_currency": "o.currency_id"}
                opts_str = str(opts).replace("'", '"')
                t_options_attr = f" t-options='{opts_str}'"
            return f'<p{attr}><span t-field="o.{field_path}"' f"{t_options_attr}/></p>"
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
            - dataSource: O2M or M2M field name to iterate over
            - columns: list of {header, fieldPath, fieldType, align, width, aggregate}
            - style: optional table-level styling
            - tableStyle: {headerBgColor, headerFontSize, headerColor,
                          headerFontWeight, zebraStriping, evenRowBg,
                          oddRowBg, showFooter, showBorders, borderColor}
        """
        data_source = element.get("dataSource", "")
        columns = element.get("columns", [])
        table_style = element.get("style", {})
        t_style = element.get("tableStyle", {})

        if not data_source or not columns:
            return ""

        table_attr = self._style_attr(table_style)

        # Table CSS classes
        table_classes = "table"
        border_color = t_style.get("borderColor", "")
        if t_style.get("showBorders", True):
            table_classes += " table-bordered"
        else:
            table_classes += " table-borderless"
        table_classes += " table-sm"

        # Header styling
        header_bg = t_style.get("headerBgColor", "#e9ecef")
        header_font_size = t_style.get("headerFontSize", 10)
        header_color = t_style.get("headerColor", "#495057")
        header_font_weight = t_style.get("headerFontWeight", "bold")
        header_style = (
            f"background-color: {header_bg}; font-size: {header_font_size}px;"
            f" color: {header_color}; font-weight: {header_font_weight};"
        )

        # Zebra striping colours
        zebra_enabled = t_style.get("zebraStriping", True)
        even_row_bg = t_style.get("evenRowBg", "")
        odd_row_bg = t_style.get("oddRowBg", "#f8f9fa")

        # Build header cells
        header_cells = []
        for col in columns:
            header_text = col.get("header", "")
            safe = (
                header_text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            header_cells.append(f'<th style="{header_style}">{safe}</th>')
        header_row = "<tr>\n" + "\n".join(header_cells) + "\n</tr>"

        # Build body row template — uses CSS class for zebra striping
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
            if border_color:
                td_style_parts.append(f"border-color: {border_color}")
            td_attr = f' style="{"; ".join(td_style_parts)}"' if td_style_parts else ""
            if field_path:
                body_cells.append(
                    f"<td{td_attr}><span t-field='line.{field_path}'/></td>"
                )
            else:
                body_cells.append(f"<td{td_attr}/>")

        body_row = "<tr>\n" + "\n".join(body_cells) + "\n</tr>"

        # Body loop with optional zebra via CSS :nth-child
        if zebra_enabled and (even_row_bg or odd_row_bg):
            # Generate a unique CSS class for this table's zebra colours
            zebra_cls = f"zebra_{abs(hash(data_source)) % 10000:04d}"
            body_loop = (
                f'<t t-foreach="o.{data_source}" t-as="line">\n'
                f"            {body_row}\n"
                f"        </t>"
            )
            # Append a <style> block for the zebra colours
            even_bg = even_row_bg or "transparent"
            odd_bg = odd_row_bg or "transparent"
            body_loop += (
                f"\n<style>\n"
                f"  .{zebra_cls} > tbody > tr:nth-child(odd) > td "
                f"{{ background-color: {odd_bg}; }}\n"
                f"  .{zebra_cls} > tbody > tr:nth-child(even) > td "
                f"{{ background-color: {even_bg}; }}\n"
                f"</style>"
            )
        else:
            zebra_cls = ""
            body_loop = (
                f'<t t-foreach="o.{data_source}" t-as="line">\n'
                f"            {body_row}\n"
                f"        </t>"
            )

        # Build optional footer row with aggregates
        footer_row = ""
        if t_style.get("showFooter", False):
            footer_row = self._build_table_footer(columns, data_source, table_attr)

        # Table border style attribute
        table_border_attr = ""
        if border_color:
            table_border_attr = f' style="border-color: {border_color};"'

        zebra_extra = f" {zebra_cls}" if zebra_cls else ""
        return (
            f'<table class="{table_classes}{zebra_extra}"'
            f"{table_attr}{table_border_attr}>\n"
            f"    <thead>\n"
            f"        {header_row}\n"
            f"    </thead>\n"
            f"    {footer_row}\n"
            f"    <tbody>\n"
            f"        {body_loop}\n"
            f"    </tbody>\n"
            f"</table>"
        )

    def _build_table_footer(self, columns, data_source, _table_attr):
        """Build QWeb ``<tfoot>`` row for table aggregate columns."""
        footer_cells = []
        has_any_aggregate = False
        for col in columns:
            aggregate = col.get("aggregate", "none")
            field_path = col.get("fieldPath", "")
            align = col.get("align", "")
            td_style_parts = ["font-weight: bold"]
            if align:
                td_style_parts.append(f"text-align: {align}")
            td_attr = f' style="{"; ".join(td_style_parts)}"' if td_style_parts else ""
            if aggregate and aggregate != "none" and field_path:
                has_any_aggregate = True
                footer_cells.append(
                    self._agg_cell(td_attr, aggregate, data_source, field_path)
                )
            else:
                footer_cells.append(f"<td{td_attr}/>")

        if not has_any_aggregate:
            return ""
        return "<tfoot>\n<tr>\n" + "\n".join(footer_cells) + "\n</tr>\n</tfoot>"

    def _agg_cell(self, td_attr, aggregate, data_source, field_path):
        """Return a ``<td>…</td>`` string for a single aggregate cell."""
        if aggregate == "sum":
            return (
                f"<td{td_attr}>"
                f"<t t-set='__agg_sum' t-value='0'/>"
                f"<t t-foreach='o.{data_source}' t-as='__agg_line'/>"
                f"<t t-set='__agg_sum' "
                f"t-value='__agg_sum + __agg_line.{field_path}'/>"
                f"<span t-esc='__agg_sum'/>"
                f"</td>"
            )
        if aggregate == "avg":
            return (
                f"<td{td_attr}>"
                f"<t t-set='__agg_sum' t-value='0'/>"
                f"<t t-set='__agg_count' t-value='0'/>"
                f"<t t-foreach='o.{data_source}' t-as='__agg_line'/>"
                f"<t t-set='__agg_sum' "
                f"t-value='__agg_sum + __agg_line.{field_path}'/>"
                f"<t t-set='__agg_count' t-value='__agg_count + 1'/>"
                f"<t t-if='__agg_count > 0'>"
                f"<span t-esc='__agg_sum / __agg_count'/>"
                f"</t></td>"
            )
        if aggregate == "count":
            return (
                f"<td{td_attr}>"
                f"<t t-set='__agg_count' t-value='0'/>"
                f"<t t-foreach='o.{data_source}' t-as='__agg_line'/>"
                f"<t t-set='__agg_count' t-value='__agg_count + 1'/>"
                f"<span t-esc='__agg_count'/>"
                f"</td>"
            )
        if aggregate == "min":
            t_cond = f"__agg_min is None or " f"__agg_line.{field_path} < __agg_min"
            return (
                f"<td{td_attr}>"
                f"<t t-set='__agg_min' t-value='None'/>"
                f"<t t-foreach='o.{data_source}' t-as='__agg_line'/>"
                f"<t t-if='{t_cond}'>"
                f"<t t-set='__agg_min' "
                f"t-value='__agg_line.{field_path}'/>"
                f"</t></t>"
                f"<span t-esc='__agg_min'/>"
                f"</td>"
            )
        if aggregate == "max":
            t_cond = f"__agg_max is None or " f"__agg_line.{field_path} > __agg_max"
            return (
                f"<td{td_attr}>"
                f"<t t-set='__agg_max' t-value='None'/>"
                f"<t t-foreach='o.{data_source}' t-as='__agg_line'/>"
                f"<t t-if='{t_cond}'>"
                f"<t t-set='__agg_max' "
                f"t-value='__agg_line.{field_path}'/>"
                f"</t></t>"
                f"<span t-esc='__agg_max'/>"
                f"</td>"
            )
        # Fallback: show aggregate label
        return f"<td{td_attr}>{aggregate.upper()}</td>"
