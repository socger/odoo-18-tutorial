import React, {useState, useCallback, useRef, useEffect, useMemo} from "react";
import {previewLayoutHtml, fetchRecords} from "../api.jsx";
import usePreviewCache from "../hooks/usePreviewCache.js";

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
    const [records, setRecords] = useState([]);
    const [selectedRecordId, setSelectedRecordId] = useState(null);
    const [loadingRecords, setLoadingRecords] = useState(false);
    const iframeRef = useRef(null);
    const debounceRef = useRef(null);
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

        // Check cache first
        const cached = cache.get(layoutJson, targetModel, selectedRecordId);
        if (cached) {
            setHtml(cached);
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
                selectedRecordId
            );
            // Ignore stale responses
            if (mySeq !== seqRef.current) return;
            if (result.error) {
                setError(result.error);
                setHtml("");
            } else {
                const content = result.html || "";
                setHtml(content);
                cache.set(layoutJson, targetModel, selectedRecordId, content);
            }
        } catch (err) {
            if (mySeq !== seqRef.current) return;
            setError(err.message || "Preview failed");
            setHtml("");
        } finally {
            if (mySeq === seqRef.current) setLoading(false);
        }
    }, [elements, targetModel, rpc, selectedRecordId, layoutJson, cache]);

    // Debounced auto-refresh when elements or record change
    useEffect(() => {
        if (!autoRefresh) return;
        if (debounceRef.current) clearTimeout(debounceRef.current);
        debounceRef.current = setTimeout(() => {
            handleRefresh();
        }, 600);
        return () => {
            if (debounceRef.current) clearTimeout(debounceRef.current);
        };
    }, [elements, autoRefresh, handleRefresh, selectedRecordId]);

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

            {/* Record selector */}
            {targetModel && (
                <div className="o_inline_preview_record_selector">
                    <label className="small text-muted me-1">Record:</label>
                    <select
                        className="form-select form-select-sm"
                        value={selectedRecordId || ""}
                        onChange={(e) =>
                            setSelectedRecordId(
                                e.target.value ? parseInt(e.target.value, 10) : null
                            )
                        }
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
                </div>
            )}

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
