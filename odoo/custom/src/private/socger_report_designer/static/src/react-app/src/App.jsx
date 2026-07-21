import React, {useState, useCallback, useEffect} from "react";
import {DndProvider} from "react-dnd";
import {HTML5Backend} from "react-dnd-html5-backend";
import FieldPicker from "./components/FieldPicker.jsx";
import ReportCanvas from "./components/ReportCanvas.jsx";
import PropertiesPanel from "./components/PropertiesPanel.jsx";
import Toolbar from "./components/Toolbar.jsx";
import LayoutManager from "./components/LayoutManager.jsx";
import Preview from "./components/Preview.jsx";
import InlinePreview from "./components/InlinePreview.jsx";
import useCanvasHistory from "./hooks/useCanvasHistory.js";
import {
    fetchModels,
    fetchFields,
    fetchLayouts,
    saveLayout,
    publishLayout,
    unpublishLayout,
} from "./api.jsx";

/**
 * Main Report Designer application.
 *
 * Props:
 *   layoutId   - pre-selected layout ID (from Odoo form)
 *   backendRpc - Odoo RPC function (from OWL wrapper)
 */
export default function App({layoutId, backendRpc}) {
    // === STATE === //
    const [models, setModels] = useState([]);
    const [fields, setFields] = useState([]);
    const [layouts, setLayouts] = useState([]);
    const [currentLayout, setCurrentLayout] = useState(null);
    const [selectedId, setSelectedId] = useState(null);
    const [targetModel, setTargetModel] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    // View mode: "design" (canvas) or "preview" (live preview)
    const [viewMode, setViewMode] = useState("design");
    // Preview refresh counter — bump to force Preview re-render
    const [previewKey, setPreviewKey] = useState(0);
    // Inline preview toggle within design mode (split-view)
    const [showInlinePreview, setShowInlinePreview] = useState(false);

    // Elements managed via undo/redo history hook
    const {elements, push, undo, redo, canUndo, canRedo} = useCanvasHistory([]);

    // === INITIALIZATION === //
    useEffect(() => {
        loadInitialData();
    }, []);

    useEffect(() => {
        if (layoutId && backendRpc) {
            loadLayout(layoutId);
        }
    }, [layoutId, backendRpc]);

    async function loadInitialData() {
        setLoading(true);
        try {
            const rpc = backendRpc || defaultRpc;
            const [modelsData, layoutsData] = await Promise.all([
                fetchModels(rpc),
                fetchLayouts(rpc),
            ]);
            setModels(modelsData);
            setLayouts(layoutsData);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    async function loadLayout(id) {
        setLoading(true);
        try {
            const rpc = backendRpc || defaultRpc;
            const layout = await fetchLayout(id, rpc);
            setCurrentLayout(layout);
            setTargetModel(layout.target_model);
            const parsed = JSON.parse(layout.layout_json || '{"elements":[]}');
            push(parsed.elements || []);
            // Load fields for the target model
            const fieldsData = await fetchFields(layout.target_model, rpc);
            setFields(fieldsData);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    async function handleModelChange(modelName) {
        setTargetModel(modelName);
        setSelectedId(null);
        push([]);
        setLoading(true);
        try {
            const rpc = backendRpc || defaultRpc;
            const fieldsData = await fetchFields(modelName, rpc);
            setFields(fieldsData);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    // === ELEMENT OPERATIONS (all go through undo/redo history) === //
    const addElement = useCallback(
        (element) => {
            push([
                ...elements,
                {
                    ...element,
                    id: `el_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`,
                },
            ]);
        },
        [elements, push]
    );

    const updateElement = useCallback(
        (id, updates) => {
            push(elements.map((el) => (el.id === id ? {...el, ...updates} : el)));
        },
        [elements, push]
    );

    const removeElement = useCallback(
        (id) => {
            push(elements.filter((el) => el.id !== id));
            setSelectedId((prev) => (prev === id ? null : prev));
        },
        [elements, push]
    );

    const moveElement = useCallback(
        (dragIndex, hoverIndex) => {
            const updated = [...elements];
            const [removed] = updated.splice(dragIndex, 1);
            updated.splice(hoverIndex, 0, removed);
            push(updated);
        },
        [elements, push]
    );

    // === SAVE === //
    async function handleSave() {
        if (!currentLayout) return;
        setLoading(true);
        try {
            const rpc = backendRpc || defaultRpc;
            const layoutJson = JSON.stringify({elements});
            await saveLayout(currentLayout.id, layoutJson, currentLayout.name, rpc);
            setError(null);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    // === PUBLISH / UNPUBLISH === //
    async function handlePublish() {
        if (!currentLayout) return;
        setLoading(true);
        try {
            const rpc = backendRpc || defaultRpc;
            // Auto-save before publishing
            const layoutJson = JSON.stringify({elements});
            await saveLayout(currentLayout.id, layoutJson, currentLayout.name, rpc);
            const result = await publishLayout(currentLayout.id, rpc);
            if (result.error) {
                setError(result.error);
                return;
            }
            setCurrentLayout((prev) => ({...prev, state: result.state}));
            setError(null);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    async function handleUnpublish() {
        if (!currentLayout) return;
        setLoading(true);
        try {
            const rpc = backendRpc || defaultRpc;
            const result = await unpublishLayout(currentLayout.id, rpc);
            if (result.error) {
                setError(result.error);
                return;
            }
            setCurrentLayout((prev) => ({...prev, state: result.state}));
            setError(null);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    // === VIEW MODE TOGGLE === //
    function handlePreview() {
        setViewMode("preview");
        setPreviewKey((k) => k + 1);
    }

    function handleDesign() {
        setViewMode("design");
    }

    // === RENDER === //
    return (
        <DndProvider backend={HTML5Backend}>
            <div className="o_report_designer">
                <Toolbar
                    layoutName={currentLayout?.name || "New Report"}
                    targetModel={targetModel}
                    loading={loading}
                    state={currentLayout?.state}
                    onSave={handleSave}
                    onPublish={handlePublish}
                    onUnpublish={handleUnpublish}
                    onPreview={handlePreview}
                    viewMode={viewMode}
                    onDesign={handleDesign}
                    onUndo={undo}
                    onRedo={redo}
                    canUndo={canUndo}
                    canRedo={canRedo}
                    showInlinePreview={showInlinePreview}
                    onToggleInlinePreview={() => setShowInlinePreview((v) => !v)}
                />
                <div className="o_report_designer_body">
                    {viewMode === "design" ? (
                        <>
                            <div className="o_report_designer_sidebar">
                                <LayoutManager
                                    layouts={layouts}
                                    currentLayout={currentLayout}
                                    onSelectLayout={loadLayout}
                                    targetModel={targetModel}
                                    models={models}
                                    onModelChange={handleModelChange}
                                />
                                <FieldPicker
                                    fields={fields}
                                    targetModel={targetModel}
                                    onAddElement={addElement}
                                />
                            </div>
                            <div className="o_report_designer_canvas">
                                <ReportCanvas
                                    elements={elements}
                                    onElementsChange={push}
                                    selectedId={selectedId}
                                    onSelectElement={setSelectedId}
                                    onAddElement={addElement}
                                    fields={fields}
                                />
                            </div>
                            <div className="o_report_designer_properties">
                                <PropertiesPanel
                                    element={
                                        elements.find((el) => el.id === selectedId) ||
                                        null
                                    }
                                    fields={fields}
                                    rpc={backendRpc || defaultRpc}
                                    onUpdateElement={updateElement}
                                    onRemoveElement={removeElement}
                                />
                            </div>
                            {showInlinePreview && (
                                <InlinePreview
                                    elements={elements}
                                    targetModel={targetModel}
                                    rpc={backendRpc || defaultRpc}
                                />
                            )}
                        </>
                    ) : (
                        <div className="o_report_designer_preview_full">
                            <Preview
                                key={previewKey}
                                elements={elements}
                                targetModel={targetModel}
                                rpc={backendRpc || defaultRpc}
                            />
                        </div>
                    )}
                </div>
                {error && (
                    <div className="o_report_designer_error">
                        <span>{error}</span>
                        <button onClick={() => setError(null)}>Dismiss</button>
                    </div>
                )}
            </div>
        </DndProvider>
    );
}

// Fallback RPC for standalone mode (used during development)
async function defaultRpc(url, params = {}) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            jsonrpc: "2.0",
            method: "call",
            params,
            id: Date.now(),
        }),
    });
    const data = await response.json();
    return data.result;
}

async function fetchLayout(id, rpc) {
    const result = await rpc("/api/report-designer/layouts/" + id);
    return result;
}
