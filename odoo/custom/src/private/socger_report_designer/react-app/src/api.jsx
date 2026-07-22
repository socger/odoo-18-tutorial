/**
 * API client for the Report Designer backend.
 * All endpoints use Odoo's JSON-RPC type controllers.
 */

/**
 * Fetch available Odoo models.
 * @param {Function} rpc - RPC function from OWL or standalone fetch
 * @returns {Promise<Array>} List of model objects
 */
export async function fetchModels(rpc) {
    const result = await rpc("/api/report-designer/models", {});
    return result.models || [];
}

/**
 * Fetch fields for a given Odoo model.
 * @param {string} modelName - Odoo model name (e.g. "sale.order")
 * @param {Function} rpc - RPC function
 * @returns {Promise<Array>} List of field objects
 */
export async function fetchFields(modelName, rpc) {
    const result = await rpc(`/api/report-designer/fields/${modelName}`, {});
    return result.fields || [];
}

/**
 * Fetch fields for a related model (for nested many2one expansion).
 * @param {string} modelName - Related model name (e.g. "res.partner")
 * @param {string} parentPath - Dotted path prefix (e.g. "partner_id")
 * @param {Function} rpc - RPC function
 * @returns {Promise<Object>} {fields, model, parent_path}
 */
export async function fetchRelatedFields(modelName, parentPath, rpc) {
    const result = await rpc(`/api/report-designer/fields/${modelName}/related`, {
        parent_path: parentPath,
    });
    return result;
}

/**
 * Fetch all report layouts.
 * @param {Function} rpc - RPC function
 * @returns {Promise<Array>} List of layout objects
 */
export async function fetchLayouts(rpc) {
    const result = await rpc("/api/report-designer/layouts", {});
    return result.layouts || [];
}

/**
 * Save a layout's JSON data.
 * @param {number} layoutId - Layout record ID
 * @param {string} layoutJson - Serialized JSON layout
 * @param {string} name - Layout name
 * @param {Function} rpc - RPC function
 * @returns {Promise<Object>} Save result
 */
export async function saveLayout(layoutId, layoutJson, name, rpc) {
    const result = await rpc(`/api/report-designer/layouts/${layoutId}/save`, {
        layout_json: layoutJson,
        name,
    });
    return result;
}

/**
 * Create a new layout.
 * @param {string} name - Layout name
 * @param {string} targetModel - Odoo model name
 * @param {Function} rpc - RPC function
 * @returns {Promise<Object>} Created layout {id, name}
 */
export async function createLayout(name, targetModel, rpc) {
    const result = await rpc("/api/report-designer/layouts/create", {
        name,
        target_model: targetModel,
    });
    return result;
}

/**
 * Delete a layout.
 * @param {number} layoutId - Layout record ID
 * @param {Function} rpc - RPC function
 * @returns {Promise<Object>} Delete result
 */
export async function deleteLayout(layoutId, rpc) {
    const result = await rpc(`/api/report-designer/layouts/${layoutId}/delete`, {});
    return result;
}

/**
 * Publish a layout to Odoo (creates QWeb template + report action).
 * @param {number} layoutId - Layout record ID
 * @param {Function} rpc - RPC function
 * @returns {Promise<Object>} Publish result
 */
export async function publishLayout(layoutId, rpc) {
    const result = await rpc(`/api/report-designer/layouts/${layoutId}/publish`, {});
    return result;
}

/**
 * Unpublish a layout.
 * @param {number} layoutId - Layout record ID
 * @param {Function} rpc - RPC function
 * @returns {Promise<Object>} Unpublish result
 */
export async function unpublishLayout(layoutId, rpc) {
    const result = await rpc(`/api/report-designer/layouts/${layoutId}/unpublish`, {});
    return result;
}

/**
 * Generate QWeb XML from layout JSON without persisting.
 * @param {string|Object} layoutJson - Layout JSON (string or parsed object)
 * @param {Function} rpc - RPC function
 * @returns {Promise<Object>} {xml: str} or {error}
 */
export async function generateXml(layoutJson, rpc) {
    const result = await rpc("/api/report-designer/generate-xml", {
        layout_json: layoutJson,
    });
    return result;
}

/**
 * Fetch records for a given model (for preview record selector).
 * @param {string} modelName - Odoo model name
 * @param {Function} rpc - RPC function
 * @param {number} limit - Max records to fetch (default 50)
 * @returns {Promise<Array>} List of {id, display_name}
 */
export async function fetchRecords(modelName, rpc, limit = 50) {
    const result = await rpc(`/api/report-designer/records/${modelName}`, {
        limit,
    });
    return result.records || [];
}

/**
 * Generate a live preview of the layout as HTML.
 * Does NOT require the layout to be published.
 * @param {string|Object} layoutJson - Layout JSON (string or parsed object)
 * @param {string} targetModel - Odoo model name
 * @param {Function} rpc - RPC function
 * @param {number|null} recordId - Optional specific record ID
 * @returns {Promise<Object>} {html, record_count} or {error}
 */
export async function previewLayoutHtml(layoutJson, targetModel, rpc, recordId) {
    const params = {
        layout_json: layoutJson,
        target_model: targetModel,
        format: "html",
    };
    if (recordId) params.record_id = recordId;
    const result = await rpc("/api/report-designer/preview/html", params);
    return result;
}

/**
 * Generate a live preview of the layout as PDF.
 * Does NOT require the layout to be published.
 * @param {string|Object} layoutJson - Layout JSON (string or parsed object)
 * @param {string} targetModel - Odoo model name
 * @param {Function} rpc - RPC function
 * @param {number|null} recordId - Optional specific record ID
 * @returns {Promise<Object>} {pdf_base64, record_count} or {error}
 */
export async function previewLayoutPdf(layoutJson, targetModel, rpc, recordId) {
    const params = {
        layout_json: layoutJson,
        target_model: targetModel,
        format: "pdf",
    };
    if (recordId) params.record_id = recordId;
    const result = await rpc("/api/report-designer/preview/live", params);
    return result;
}
