import React, {useState, useCallback, useRef, useEffect} from "react";
import {previewLayoutHtml} from "../api.jsx";

/**
 * Preview panel — renders a live HTML preview of the current layout.
 *
 * Shows the report as it would appear when printed, inside a sandboxed
 * iframe.  The preview is re-rendered each time the user clicks
 * "Refresh" (or on demand), passing the current elements JSON to the
 * backend which generates QWeb on-the-fly and returns rendered HTML.
 *
 * Props:
 *   elements    – current canvas elements array
 *   targetModel – selected Odoo model name
 *   rpc         – backend RPC function
 */
export default function Preview({elements, targetModel, rpc}) {
    const [html, setHtml] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [lastRendered, setLastRendered] = useState(null);
    const iframeRef = useRef(null);

    const handleRefresh = useCallback(async () => {
        if (!targetModel || !elements || elements.length === 0) {
            setHtml("");
            setError(null);
            return;
        }

        setLoading(true);
        setError(null);
        try {
            const layoutJson = JSON.stringify({elements});
            const result = await previewLayoutHtml(layoutJson, targetModel, rpc);
            if (result.error) {
                setError(result.error);
                setHtml("");
            } else {
                setHtml(result.html || "");
                setLastRendered(new Date());
            }
        } catch (err) {
            setError(err.message || "Preview failed");
            setHtml("");
        } finally {
            setLoading(false);
        }
    }, [elements, targetModel, rpc]);

    // Auto-refresh on first render when elements exist
    useEffect(() => {
        if (elements.length > 0 && targetModel && !lastRendered) {
            handleRefresh();
        }
    }, [elements.length, targetModel, handleRefresh, lastRendered]);

    // Write HTML into the iframe
    useEffect(() => {
        const iframe = iframeRef.current;
        if (!iframe) return;

        const doc = iframe.contentDocument || iframe.contentWindow?.document;
        if (!doc) return;

        if (!html) {
            doc.open();
            doc.write(
                '<!DOCTYPE html><html><body style="display:flex;align-items:center;' +
                    "justify-content:center;height:100vh;background:#f5f5f5;" +
                    'color:#999;font-family:sans-serif;">' +
                    "<p>Click Refresh to generate a preview</p>" +
                    "</body></html>"
            );
            doc.close();
            return;
        }

        doc.open();
        doc.write(html);
        doc.close();
    }, [html]);

    return (
        <div className="o_preview_panel">
            <div className="o_preview_header">
                <span className="o_preview_title">Preview</span>
                <div className="o_preview_actions">
                    <button
                        className="btn btn-sm btn-secondary"
                        onClick={handleRefresh}
                        disabled={loading}
                        title="Refresh preview"
                    >
                        <i
                            className={`fa ${
                                loading ? "fa-spinner fa-spin" : "fa-sync"
                            } me-1`}
                        />
                        Refresh
                    </button>
                    {lastRendered && (
                        <span className="text-muted small ms-2">
                            {lastRendered.toLocaleTimeString()}
                        </span>
                    )}
                </div>
            </div>
            <div className="o_preview_body">
                {error && (
                    <div className="o_preview_error alert alert-warning m-2 py-1 px-2 small">
                        <i className="fa fa-exclamation-triangle me-1" />
                        {error}
                    </div>
                )}
                <iframe
                    ref={iframeRef}
                    className="o_preview_iframe"
                    title="Report Preview"
                    sandbox="allow-same-origin"
                />
            </div>
        </div>
    );
}
