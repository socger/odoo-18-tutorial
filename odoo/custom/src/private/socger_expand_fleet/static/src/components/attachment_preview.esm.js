/** @odoo-module **/

import {Component} from "@odoo/owl";
import {FileModel} from "@web/core/file_viewer/file_model";
import {useFileViewer} from "@web/core/file_viewer/file_viewer_hook";

/**
 * Reusable component that renders a thumbnail for an ir.attachment record and
 * opens the native Odoo `fileViewer` (the same used by the chatter) on click.
 *
 * The component builds a `FileModel` instance from the attachment fields
 * (id, name, mimetype, access_token, checksum, type, url) so it benefits from
 * all the getters the fileViewer relies on: `isImage`, `isPdf`, `isViewable`,
 * `defaultSource`, `downloadUrl`, ...
 *
 * Props:
 *  - attachment: object with at least { id, name, mimetype, access_token,
 *    checksum, type, url } (falsy values are allowed to render a placeholder).
 */
export class AttachmentPreview extends Component {
    static template = "socger_expand_fleet.AttachmentPreview";
    static props = {
        attachment: {type: Object, optional: true},
    };

    setup() {
        super.setup(...arguments);
        this.fileViewer = useFileViewer();
    }

    /**
     * Build a FileModel-like object the fileViewer can consume. We use the
     * native `FileModel` class from web so all the getters (isImage, isPdf,
     * defaultSource, downloadUrl, ...) are inherited for free.
     * @returns {FileModel|undefined}
     */
    get file() {
        const att = this.props.attachment;
        if (!att || !att.id) {
            return undefined;
        }
        const file = new FileModel();
        file.id = att.id;
        file.name = att.name || "";
        file.filename = att.name || "";
        file.mimetype = att.mimetype || "";
        file.access_token = att.access_token || false;
        file.checksum = att.checksum || false;
        file.type = att.type || "binary";
        file.url = att.url || "";
        file.uploading = false;
        return file;
    }

    /**
     * Opens the native Odoo file viewer (full screen with zoom, rotate,
     * navigate, download) — the very same one used by the chatter when you
     * click an attachment thumbnail.
     */
    onClickPreview() {
        const file = this.file;
        if (file && file.isViewable) {
            this.fileViewer.open(file, [file]);
        }
    }

    /**
     * Returns true when the attachment can be opened in the file viewer.
     */
    get isViewable() {
        const file = this.file;
        return Boolean(file && file.isViewable);
    }

    get isImage() {
        const file = this.file;
        return Boolean(file && file.isImage);
    }

    get isPdf() {
        const file = this.file;
        return Boolean(file && file.isPdf);
    }

    /**
     * Thumbnail URL for images. Uses the canonical /web/image/<id> route so
     * no binary payload is loaded from the server (the chatter does the same).
     */
    get imageUrl() {
        const file = this.file;
        if (!file || !file.isImage) {
            return "";
        }
        return file.defaultSource;
    }

    /**
     * Download URL for non-viewable files.
     */
    get downloadUrl() {
        const file = this.file;
        if (!file) {
            return "";
        }
        return file.downloadUrl;
    }

    /**
     * File extension upper-cased (used for the generic icon badge).
     */
    get extension() {
        const file = this.file;
        if (!file || !file.name) {
            return "";
        }
        const parts = file.name.split(".");
        return parts.length > 1 ? parts.pop().toUpperCase() : "";
    }

    get displayName() {
        const file = this.file;
        return file ? file.displayName : "";
    }
}
