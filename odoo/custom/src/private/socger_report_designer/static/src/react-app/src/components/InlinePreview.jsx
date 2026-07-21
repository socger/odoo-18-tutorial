import React, {useState, useCallback, useRef, useEffect} from "react";
import {previewLayoutHtml} from "../api.jsx";

/**
 * InlinePreview - compact live preview panel for split-view within design mode.
 *
 * Unlike the full-screen Preview.jsx, this component is narrower and has
 * a debounce so it auto-refreshes as the user edits (without spamming the
 * backend on every keystroke).
 *
 * Props:
 *   elements    – current canvas elements array
 *   targetModel – selected Odoo model name
 *   rpc         – backend RPC function
 */
export default function InlinePreview({elements, targetModel, rpc}) {
    const [html, setHtml] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [autoRefresh, setAutoRefresh] = useState(true);
    const iframeRef = useRef(null);
    const debounceRef = useRef(null);
    const seqRef = useRef(0);

    const handleRefresh = useCallback(async () => {
        if (!targetModel || !elements || elements.length === 0) {
            setHtml("");
            setError(null);
            setLoading(false);
            return;
        }

        const mySeq = ++seqRef.current;
        setLoading(true);
        setError(null);
        try {
            const layoutJson = JSON.stringify({elements});
            const result = await previewLayoutHtml(layoutJson, targetModel, rpc);
            // Ignore stale responses
            if (mySeq !== seqRef.current) return;
            if (result.error) {
                setError(result.error);
                setHtml("");
            } else {
                setHtml(result.html || "");
            }
        } catch (err) {
            if (mySeq !== seqRef.current) return;
            setError(err.message || "Preview failed");
            setHtml("");
        } finally {
            if (mySeq === seqRef.current) setLoading(false);
        }
    }, [elements, targetModel, rpc]);

    // Debounced auto-refresh when elements change
    useEffect(() => {
        if (!autoRefresh) return;
        if (debounceRef.current) clearTimeout(debounceRef.current);
        debounceRef.current = setTimeout(() => {
            handleRefresh();
        }, 600);
        return () => {
            if (debounceRef.current) clearTimeout(debounceRef.current);
        };
    }, [elements, autoRefresh, handleRefresh]);

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
                    'color:#999;font-family:sans-serif;font-size:12px;">' +
                    "<p>Add elements to see preview</p>" +
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
        <div className="o_inline_preview">
            <div className="o_inline_preview_header">
                <span className="o_inline_preview_title">
                    <i className="fa fa-eye me-1" />
                    Live Preview
                </span>
                <div className="o_inline_preview_actions">
                    <label
                        className="o_inline_preview_autorefresh"
                        title="Auto refresh on changes"
                    >
                        <input
                            type="checkbox"
                            checked={autoRefresh}
                            onChange={(e) => setAutoRefresh(e.target.checked)}
                        />
                        <span className="small ms-1">Auto</span>
                    </label>
                    <button
                        className="btn btn-sm btn-outline-secondary"
                        onClick={handleRefresh}
                        disabled={loading}
                        title="Refresh now"
                    >
                        <i
                            className={`fa ${
                                loading ? "fa-spinner fa-spin" : "fa-sync"
                            }`}
                        />
                    </button>
                </div>
            </div>
            {error && (
                <div className="o_inline_preview_error small">
                    <i className="fa fa-exclamation-triangle me-1" />
                    {error}
                </div>
            )}
            <iframe
                ref={iframeRef}
                className="o_inline_preview_iframe"
                title="Inline Report Preview"
                sandbox="allow-same-origin"
            />
        </div>
    );
}
