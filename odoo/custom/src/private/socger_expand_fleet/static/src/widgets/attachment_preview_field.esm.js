/** @odoo-module **/

import {AttachmentPreview} from "../components/attachment_preview.esm";
import {Component} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {standardFieldProps} from "@web/views/fields/standard_field_props";

/**
 * Field widget that renders the shared `AttachmentPreview` component inside a
 * form view. It must be declared on an ir.attachment record (typically on the
 * `id` field, but any field works since we read the whole record).
 *
 * The widget reads the attachment fields directly from the current record so
 * no extra RPC is needed. The fields it relies on must be present in the view
 * (declared as `invisible="1"` if you don't want to show them):
 *   - id, name, mimetype, access_token, checksum, type, url
 *
 * Usage in a form:
 *   <field name="id" widget="attachment_preview_field" />
 *   <field name="mimetype" invisible="1" />
 *   <field name="access_token" invisible="1" />
 *   <field name="checksum" invisible="1" />
 *   <field name="type" invisible="1" />
 *   <field name="url" invisible="1" />
 */
export class AttachmentPreviewField extends Component {
    static template = "socger_expand_fleet.AttachmentPreviewField";
    static components = {AttachmentPreview};
    static props = {
        ...standardFieldProps,
    };

    /**
     * Builds the attachment object the child component expects, from the
     * current record data.
     */
    get attachment() {
        const data = this.props.record.data;
        return {
            id: this.props.record.resId,
            name: data.name || "",
            mimetype: data.mimetype || "",
            access_token: data.access_token || false,
            checksum: data.checksum || false,
            type: data.type || "binary",
            url: data.url || "",
        };
    }
}

export const attachmentPreviewField = {
    component: AttachmentPreviewField,
    supportedTypes: ["integer", "many2one", "char"],
    relatedFields: [
        {name: "name", type: "char"},
        {name: "mimetype", type: "char"},
        {name: "access_token", type: "char"},
        {name: "checksum", type: "char"},
        {name: "type", type: "selection"},
        {name: "url", type: "char"},
    ],
    extractProps: () => ({}),
};

registry.category("fields").add("attachment_preview_field", attachmentPreviewField);
