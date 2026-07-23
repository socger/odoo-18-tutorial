import React, {useState, useCallback, useRef, useEffect, useMemo} from "react";
import {previewLayoutHtml, fetchRecords} from "../api.jsx";
import usePreviewCache from "../hooks/usePreviewCache.js";

/**
 * Preview panel — renders a live HTML preview of the current layout.
 *
 * Shows the report as it would appear when printed, inside a sandboxed
 * iframe.  The preview is re-rendered on demand or via a record selector,
 * passing the current elements JSON to the backend which generates QWeb
 * on-the-fly and returns rendered HTML.
 *
 * Uses a client-side cache (in-memory + sessionStorage) so revisiting
 * the same layout+record combo is instant.
 *
 * Props:
 *   elements    – current canvas elements array
 *   targetModel – selected Odoo model name
 *   rpc         – backend RPC function
 */
export default function Preview({
    elements,
    targetModel,
    rpc,
    paperFormat,
    paperOrientation,
}) {
    const [html, setHtml] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [lastRendered, setLastRendered] = useState(null);
    const [records, setRecords] = useState([]);
    const [selectedRecordId, setSelectedRecordId] = useState(null);
    const [loadingRecords, setLoadingRecords] = useState(false);
    const iframeRef = useRef(null);
    const seqRef = useRef(0);
    const cache = usePreviewCache();

    // Stable stringification of elements for cache key
    const layoutJson = useMemo(() => JSON.stringify({elements}), [elements]);

    // Fetch records when target model changes
    useEffect(() => {
        if (!targetModel) {
            setRecords([]);
            setSelectedRecordId(null);
            return;
        }
        let cancelled = false;
        async function loadRecords() {
            setLoadingRecords(true);
            try {
                const recs = await fetchRecords(targetModel, rpc, 50);
                if (!cancelled) {
                    setRecords(recs);
                    setSelectedRecordId(null);
                }
            } catch {
                if (!cancelled) setRecords([]);
            } finally {
                if (!cancelled) setLoadingRecords(false);
            }
        }
        loadRecords();
        return () => {
            cancelled = true;
        };
    }, [targetModel, rpc]);

    const handleRefresh = useCallback(async () => {
        if (!targetModel || !elements || elements.length === 0) {
            setHtml("");
            setError(null);
            setLoading(false);
            return;
        }

        const mySeq = ++seqRef.current;

        // Check cache first (includes paper format/orientation in key)
        const cached = cache.get(
            layoutJson,
            targetModel,
            selectedRecordId,
            paperFormat,
            paperOrientation
        );
        if (cached) {
            setHtml(cached);
            setLastRendered(new Date());
            setLoading(false);
            return;
        }

        setLoading(true);
        setError(null);
        try {
            const result = await previewLayoutHtml(
                layoutJson,
                targetModel,
                rpc,
                selectedRecordId,
                paperFormat,
                paperOrientation
            );
            if (mySeq !== seqRef.current) return;
            if (result.error) {
                setError(result.error);
                setHtml("");
            } else {
                const content = result.html || "";
                setHtml(content);
                setLastRendered(new Date());
                cache.set(
                    layoutJson,
                    targetModel,
                    selectedRecordId,
                    content,
                    paperFormat,
                    paperOrientation
                );
            }
        } catch (err) {
            if (mySeq !== seqRef.current) return;
            setError(err.message || "Preview failed");
            setHtml("");
        } finally {
            if (mySeq === seqRef.current) setLoading(false);
        }
    }, [
        elements,
        targetModel,
        rpc,
        selectedRecordId,
        layoutJson,
        cache,
        paperFormat,
        paperOrientation,
    ]);

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
                    {/* Record selector */}
                    {targetModel && (
                        <select
                            className="form-select form-select-sm me-2"
                            style={{width: "auto", maxWidth: "180px"}}
                            value={selectedRecordId || ""}
                            onChange={(e) => {
                                setSelectedRecordId(
                                    e.target.value ? parseInt(e.target.value, 10) : null
                                );
                                // Invalidate cache when switching records
                                cache.invalidateAll();
                            }}
                        >
                            <option value="">(first record)</option>
                            {loadingRecords ? (
                                <option disabled>Loading...</option>
                            ) : (
                                records.map((rec) => (
                                    <option key={rec.id} value={rec.id}>
                                        {rec.display_name}
                                    </option>
                                ))
                            )}
                        </select>
                    )}
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
