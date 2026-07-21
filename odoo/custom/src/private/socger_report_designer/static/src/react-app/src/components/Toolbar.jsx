import React from "react";

/**
 * Toolbar - top bar with layout name, save, preview, and publish actions.
 * Now includes design/preview mode toggle.
 */
export default function Toolbar({
    layoutName,
    targetModel,
    loading,
    onSave,
    onPreview,
    onPublish,
    onUnpublish,
    state,
    viewMode,
    onDesign,
    onUndo,
    onRedo,
    canUndo,
    canRedo,
    showInlinePreview,
    onToggleInlinePreview,
}) {
    return (
        <div className="o_report_designer_toolbar">
            <div className="o_toolbar_left">
                <i className="fa fa-paint-brush me-2" />
                <span className="o_toolbar_title">{layoutName}</span>
                {targetModel && (
                    <span className="badge bg-secondary ms-2">{targetModel}</span>
                )}
                {state && (
                    <span
                        className={`badge ms-1 ${
                            state === "published" ? "bg-success" : "bg-warning"
                        }`}
                    >
                        {state}
                    </span>
                )}
            </div>
            <div className="o_toolbar_right">
                {/* View mode toggle */}
                <div className="btn-group me-2">
                    <button
                        className={`btn btn-sm ${
                            viewMode === "design"
                                ? "btn-primary"
                                : "btn-outline-primary"
                        }`}
                        onClick={onDesign}
                        title="Design mode"
                    >
                        <i className="fa fa-pencil me-1" />
                        Design
                    </button>
                    <button
                        className={`btn btn-sm ${
                            viewMode === "preview"
                                ? "btn-primary"
                                : "btn-outline-primary"
                        }`}
                        onClick={onPreview}
                        title="Preview mode"
                    >
                        <i className="fa fa-eye me-1" />
                        Preview
                    </button>
                </div>

                {/* Undo / Redo */}
                <div className="btn-group me-2">
                    <button
                        className="btn btn-sm btn-outline-secondary"
                        onClick={onUndo}
                        disabled={!canUndo}
                        title="Undo (Ctrl+Z)"
                    >
                        <i className="fa fa-undo" />
                    </button>
                    <button
                        className="btn btn-sm btn-outline-secondary"
                        onClick={onRedo}
                        disabled={!canRedo}
                        title="Redo (Ctrl+Y)"
                    >
                        <i className="fa fa-repeat" />
                    </button>
                </div>

                {/* Inline preview toggle (only in design mode) */}
                {viewMode === "design" && (
                    <button
                        className={`btn btn-sm me-2 ${
                            showInlinePreview ? "btn-info" : "btn-outline-info"
                        }`}
                        onClick={onToggleInlinePreview}
                        title="Toggle live preview side panel"
                    >
                        <i className="fa fa-columns me-1" />
                        Split
                    </button>
                )}

                <button
                    className="btn btn-sm btn-secondary me-1"
                    onClick={onSave}
                    disabled={loading}
                    title="Save layout"
                >
                    <i className="fa fa-save me-1" />
                    Save
                </button>
                {state === "draft" ? (
                    <button
                        className="btn btn-sm btn-primary"
                        onClick={onPublish}
                        disabled={loading}
                        title="Publish report"
                    >
                        <i className="fa fa-rocket me-1" />
                        Publish
                    </button>
                ) : (
                    <button
                        className="btn btn-sm btn-warning"
                        onClick={onUnpublish}
                        disabled={loading}
                        title="Unpublish report"
                    >
                        <i className="fa fa-stop me-1" />
                        Unpublish
                    </button>
                )}
            </div>
        </div>
    );
}
