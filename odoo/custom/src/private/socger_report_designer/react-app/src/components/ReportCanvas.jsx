import React, {useEffect, useRef, useCallback, useState} from "react";
import * as fabric from "fabric";
import {createFabricObject} from "./fabricObjects.js";

/**
 * A4 paper dimensions in pixels at 96 DPI.
 * Actual A4 = 210mm × 297mm ≈ 794px × 1123px.
 */
const A4_WIDTH = 794;
const A4_HEIGHT = 1123;
const GRID_SIZE = 10;
const MIN_ZOOM = 0.25;
const MAX_ZOOM = 3;
const ZOOM_STEP = 0.1;

/**
 * Snap a numeric value to the nearest grid line.
 */
function snapToGrid(value) {
    return Math.round(value / GRID_SIZE) * GRID_SIZE;
}

/**
 * ReportCanvas — the main visual editor powered by Fabric.js.
 *
 * Props:
 *   elements         – array of layout elements (source of truth in React)
 *   onElementsChange – called when elements change (receives new array)
 *   onSelectElement  – called when user clicks an element (passes element id)
 *   selectedId       – id of currently selected element (for highlight)
 *   fields           – available model fields (for drop mapping)
 *   onAddElement     – called when a field is dropped onto the canvas
 *   onUndo           – undo callback (Ctrl+Z)
 *   onRedo           – redo callback (Ctrl+Y)
 */
export default function ReportCanvas({
    elements,
    onElementsChange,
    onSelectElement,
    selectedId,
    fields,
    onAddElement,
    onUndo,
    onRedo,
}) {
    const canvasRef = useRef(null);
    const fabricRef = useRef(null);
    const containerRef = useRef(null);
    const [zoom, setZoom] = useState(1);
    const [gridVisible, setGridVisible] = useState(true);
    const [snapEnabled, setSnapEnabled] = useState(true);
    const elementsMapRef = useRef(new Map());
    const clipboardRef = useRef(null);
    // Always-current reference to avoid stale closures in event handlers
    const elementsRef = useRef(elements);
    elementsRef.current = elements;

    // === INIT FABRIC CANVAS === //
    useEffect(() => {
        if (!canvasRef.current || fabricRef.current) return;

        const fc = new fabric.Canvas(canvasRef.current, {
            width: A4_WIDTH,
            height: A4_HEIGHT,
            backgroundColor: "#ffffff",
            selection: true,
            preserveObjectStacking: true,
        });

        fabricRef.current = fc;

        // Click on empty canvas = deselect
        fc.on("selection:created", (e) => {
            const obj = e.selected?.[0];
            if (obj && obj._elementId) {
                onSelectElement(obj._elementId);
            }
        });

        fc.on("selection:updated", (e) => {
            const obj = e.selected?.[0];
            if (obj && obj._elementId) {
                onSelectElement(obj._elementId);
            }
        });

        fc.on("selection:cleared", () => {
            onSelectElement(null);
        });

        // Snap to grid during drag
        fc.on("object:moving", (e) => {
            if (!snapEnabled) return;
            const obj = e.target;
            if (!obj || obj.data === "grid") return;
            obj.set({
                left: snapToGrid(obj.left),
                top: snapToGrid(obj.top),
            });
        });

        // Sync object moves/resizes back to React
        fc.on("object:modified", (e) => {
            const obj = e.target;
            if (!obj || !obj._elementId) return;
            // Final snap on modification
            if (snapEnabled) {
                obj.set({
                    left: snapToGrid(obj.left),
                    top: snapToGrid(obj.top),
                });
                obj.setCoords();
            }
            syncObjectToElement(obj, elementsRef, onElementsChange);
        });

        // Draw initial grid
        drawGrid(fc);

        return () => {
            fc.dispose();
            fabricRef.current = null;
        };
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    // === SYNC ELEMENTS → FABRIC OBJECTS === //
    useEffect(() => {
        const fc = fabricRef.current;
        if (!fc) return;

        const currentIds = new Set(elements.map((el) => el.id));
        const existingIds = new Set(elementsMapRef.current.keys());

        // Remove objects that no longer exist
        for (const id of existingIds) {
            if (!currentIds.has(id)) {
                const obj = elementsMapRef.current.get(id);
                if (obj) {
                    fc.remove(obj);
                    elementsMapRef.current.delete(id);
                }
            }
        }

        // Complex types that must be recreated because they are Groups
        // whose children can't be updated individually
        const complexTypes = new Set(["image", "pagebreak", "table", "container"]);

        // Add or update objects
        for (const element of elements) {
            const existing = elementsMapRef.current.get(element.id);
            if (existing) {
                // If type changed or it's a complex type, recreate from scratch
                if (
                    element.type !== existing._elementType ||
                    complexTypes.has(element.type)
                ) {
                    fc.remove(existing);
                    elementsMapRef.current.delete(element.id);
                    const obj = createFabricObject(element);
                    if (obj) {
                        obj._elementId = element.id;
                        obj._elementType = element.type;
                        fc.add(obj);
                        elementsMapRef.current.set(element.id, obj);
                    }
                } else {
                    // Update simple objects in-place
                    updateFabricObject(existing, element);
                }
            } else {
                const obj = createFabricObject(element);
                if (obj) {
                    obj._elementId = element.id;
                    obj._elementType = element.type;
                    fc.add(obj);
                    elementsMapRef.current.set(element.id, obj);
                }
            }
        }

        fc.renderAll();
    }, [elements]);

    // === HIGHLIGHT SELECTED ELEMENT === //
    useEffect(() => {
        const fc = fabricRef.current;
        if (!fc) return;

        if (selectedId) {
            const obj = elementsMapRef.current.get(selectedId);
            if (obj) {
                fc.setActiveObject(obj);
                fc.renderAll();
            }
        } else {
            fc.discardActiveObject();
            fc.renderAll();
        }
    }, [selectedId]);

    // === DRAG & DROP FROM FIELD PICKER === //
    const handleDrop = useCallback(
        (e) => {
            e.preventDefault();
            const data = e.dataTransfer.getData("application/json");
            if (!data) return;

            try {
                const payload = JSON.parse(data);
                // Calculate drop position relative to the canvas
                const fc = fabricRef.current;
                const rect = canvasRef.current.getBoundingClientRect();
                const zoomVal = fc.getZoom();
                const rawX = (e.clientX - rect.left) / zoomVal;
                const rawY = (e.clientY - rect.top) / zoomVal;

                onAddElement({
                    ...payload,
                    position: {
                        x: snapEnabled ? snapToGrid(rawX) : Math.round(rawX),
                        y: snapEnabled ? snapToGrid(rawY) : Math.round(rawY),
                    },
                });
            } catch {
                // ignore invalid JSON
            }
        },
        [onAddElement, snapEnabled]
    );

    const handleDragOver = useCallback((e) => {
        e.preventDefault();
        e.dataTransfer.dropEffect = "copy";
    }, []);

    // === ZOOM CONTROLS === //
    const handleZoom = useCallback((direction) => {
        const fc = fabricRef.current;
        if (!fc) return;

        const current = fc.getZoom();
        const newZoom =
            direction === "in"
                ? Math.min(current + ZOOM_STEP, MAX_ZOOM)
                : Math.max(current - ZOOM_STEP, MIN_ZOOM);

        fc.zoomToPoint(new fabric.Point(A4_WIDTH / 2, A4_HEIGHT / 2), newZoom);
        fc.renderAll();
        setZoom(newZoom);
    }, []);

    const handleZoomReset = useCallback(() => {
        const fc = fabricRef.current;
        if (!fc) return;
        fc.setViewportTransform([1, 0, 0, 1, 0, 0]);
        fc.renderAll();
        setZoom(1);
    }, []);

    // === TOGGLE GRID === //
    const toggleGrid = useCallback(() => {
        setGridVisible((prev) => {
            const next = !prev;
            const fc = fabricRef.current;
            if (fc) {
                if (next) drawGrid(fc);
                else clearGrid(fc);
                fc.renderAll();
            }
            return next;
        });
    }, []);

    // === TOGGLE SNAP === //
    const toggleSnap = useCallback(() => {
        setSnapEnabled((prev) => !prev);
    }, []);

    // === CLIPBOARD OPERATIONS === //
    const copySelected = useCallback(() => {
        const fc = fabricRef.current;
        if (!fc) return;
        const active = fc.getActiveObject();
        if (!active || !active._elementId) return;
        const elData = elementsRef.current.find((el) => el.id === active._elementId);
        if (elData) {
            clipboardRef.current = JSON.parse(JSON.stringify(elData));
        }
    }, []);

    const pasteClipboard = useCallback(() => {
        if (!clipboardRef.current) return;
        const elData = JSON.parse(JSON.stringify(clipboardRef.current));
        // Generate new ID and offset position
        elData.id = `el_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
        if (elData.position) {
            elData.position = {
                x: elData.position.x + 20,
                y: elData.position.y + 20,
            };
        }
        onAddElement(elData);
    }, [onAddElement]);

    const duplicateSelected = useCallback(() => {
        const fc = fabricRef.current;
        if (!fc) return;
        const active = fc.getActiveObject();
        if (!active || !active._elementId) return;
        const elData = elementsRef.current.find((el) => el.id === active._elementId);
        if (elData) {
            const clone = JSON.parse(JSON.stringify(elData));
            clone.id = `el_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
            if (clone.position) {
                clone.position = {x: clone.position.x + 20, y: clone.position.y + 20};
            }
            onAddElement(clone);
        }
    }, [onAddElement]);

    const selectAll = useCallback(() => {
        const fc = fabricRef.current;
        if (!fc) return;
        const objs = fc.getObjects().filter((o) => o._elementId && o.selectable);
        if (objs.length === 0) return;
        const sel = new fabric.ActiveSelection(objs, {canvas: fc});
        fc.setActiveObject(sel);
        fc.renderAll();
    }, []);

    // === KEYBOARD SHORTCUTS === //
    useEffect(() => {
        const handleKey = (e) => {
            const fc = fabricRef.current;
            if (!fc) return;

            // Skip shortcuts when focus is inside an input/textarea/select
            const tag = e.target.tagName.toLowerCase();
            if (tag === "input" || tag === "textarea" || tag === "select") return;

            const ctrl = e.ctrlKey || e.metaKey;

            // Ctrl+Z — Undo
            if (ctrl && e.key === "z" && !e.shiftKey) {
                e.preventDefault();
                onUndo?.();
                return;
            }

            // Ctrl+Y or Ctrl+Shift+Z — Redo
            if ((ctrl && e.key === "y") || (ctrl && e.key === "z" && e.shiftKey)) {
                e.preventDefault();
                onRedo?.();
                return;
            }

            // Ctrl+C — Copy
            if (ctrl && e.key === "c") {
                e.preventDefault();
                copySelected();
                return;
            }

            // Ctrl+V — Paste
            if (ctrl && e.key === "v") {
                e.preventDefault();
                pasteClipboard();
                return;
            }

            // Ctrl+D — Duplicate
            if (ctrl && e.key === "d") {
                e.preventDefault();
                duplicateSelected();
                return;
            }

            // Ctrl+A — Select all
            if (ctrl && e.key === "a") {
                e.preventDefault();
                selectAll();
                return;
            }

            // Escape — Deselect
            if (e.key === "Escape") {
                fc.discardActiveObject();
                fc.renderAll();
                onSelectElement(null);
                return;
            }

            // Delete / Backspace — Remove selected
            if (e.key === "Delete" || e.key === "Backspace") {
                const active = fc.getActiveObject();
                if (active && active._elementId) {
                    const id = active._elementId;
                    fc.remove(active);
                    elementsMapRef.current.delete(id);
                    fc.renderAll();
                    const newElements = elementsRef.current.filter(
                        (el) => el.id !== id
                    );
                    onElementsChange(newElements);
                    onSelectElement(null);
                }
            }
        };
        window.addEventListener("keydown", handleKey);
        return () => window.removeEventListener("keydown", handleKey);
    }, [
        onElementsChange,
        onSelectElement,
        onUndo,
        onRedo,
        copySelected,
        pasteClipboard,
        duplicateSelected,
        selectAll,
    ]);

    return (
        <div className="o_report_canvas_wrapper">
            {/* Canvas toolbar */}
            <div className="o_canvas_toolbar">
                <span className="o_canvas_toolbar_label">Canvas</span>
                <div className="o_canvas_toolbar_actions">
                    <button
                        className="btn btn-sm btn-outline-secondary"
                        onClick={() => handleZoom("out")}
                        title="Zoom out"
                    >
                        <i className="fa fa-search-minus" />
                    </button>
                    <span className="o_canvas_zoom_label">
                        {Math.round(zoom * 100)}%
                    </span>
                    <button
                        className="btn btn-sm btn-outline-secondary"
                        onClick={() => handleZoom("in")}
                        title="Zoom in"
                    >
                        <i className="fa fa-search-plus" />
                    </button>
                    <button
                        className="btn btn-sm btn-outline-secondary"
                        onClick={handleZoomReset}
                        title="Reset zoom"
                    >
                        <i className="fa fa-crosshairs" />
                    </button>
                    <div className="vr mx-1" />
                    <button
                        className={`btn btn-sm ${
                            gridVisible
                                ? "btn-outline-primary"
                                : "btn-outline-secondary"
                        }`}
                        onClick={toggleGrid}
                        title="Toggle grid"
                    >
                        <i className="fa fa-th" />
                    </button>
                    <button
                        className={`btn btn-sm ${
                            snapEnabled
                                ? "btn-outline-success"
                                : "btn-outline-secondary"
                        }`}
                        onClick={toggleSnap}
                        title="Toggle snap to grid"
                    >
                        <i className="fa fa-magnet" />
                    </button>
                </div>
            </div>

            {/* Canvas viewport — scrollable + zoomable */}
            <div
                ref={containerRef}
                className="o_canvas_viewport"
                onDrop={handleDrop}
                onDragOver={handleDragOver}
            >
                <div
                    className="o_canvas_paper"
                    style={{
                        transform: `scale(${zoom})`,
                        transformOrigin: "top center",
                    }}
                >
                    {/* A4 paper shadow + border */}
                    <div className="o_canvas_paper_frame">
                        <canvas ref={canvasRef} />
                    </div>
                    {/* Empty state overlay — shown when canvas has no elements */}
                    {elements.length === 0 && (
                        <div className="o_canvas_empty_overlay">
                            <div className="o_canvas_empty_content">
                                <i className="fa fa-paint-brush fa-2x mb-3 text-muted" />
                                <h5>Start designing your report</h5>
                                <p>
                                    <strong>Drag fields</strong> from the left panel
                                    onto this canvas, or <strong>double-click</strong> a
                                    field to add it here.
                                </p>
                                <p className="text-muted small mb-0">
                                    Use the Properties panel on the right to customize
                                    each element. Click <strong>Preview</strong> to see
                                    the live result.
                                </p>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

// === HELPERS === //

function updateFabricObject(fabObj, element) {
    const pos = element.position;
    const style = element.style || {};

    // Always update position
    if (pos) {
        fabObj.set({left: pos.x, top: pos.y});
    }

    // Update based on element type
    if (element.type === "text" || element.type === "heading") {
        // Text content
        const text = element.fieldPath
            ? `[${element.fieldPath}]`
            : element.content || (element.type === "text" ? "Text" : "Heading");

        // Font size depends on heading level
        const headingSizes = {1: 24, 2: 20, 3: 16, 4: 14, 5: 12, 6: 11};
        let fontSize = parseInt(style.fontSize, 10) || 12;
        let fontWeight = style.fontWeight || "normal";
        if (element.type === "heading") {
            const level = parseInt(style.level, 10) || 2;
            fontSize = headingSizes[level] || 20;
            fontWeight = style.fontWeight || "bold";
        }

        fabObj.set({
            text: text,
            fontSize: fontSize,
            fontWeight: fontWeight,
            fill: style.color || "#000000",
            textAlign: style.textAlign || "left",
            fontFamily: style.fontFamily || "sans-serif",
            width: style.width || fabObj.width,
            padding: style.padding !== undefined ? parseInt(style.padding, 10) : 4,
            backgroundColor: style.backgroundColor || "transparent",
            opacity: style.opacity !== undefined ? parseFloat(style.opacity) : 1,
            lineHeight:
                style.lineHeight !== undefined
                    ? parseFloat(style.lineHeight)
                    : undefined,
            underline: style.textDecoration === "underline",
            linethrough: style.textDecoration === "line-through",
            overline: style.textDecoration === "overline",
        });

        // Handle border via stroke
        if (style.borderBottom && typeof style.borderBottom === "string") {
            const match = style.borderBottom.match(
                /([\d.]+)px\s+solid\s+(#[0-9a-fA-F]+)/
            );
            if (match) {
                fabObj.set({
                    stroke: match[2],
                    strokeWidth: parseInt(match[1], 10),
                });
            }
        }
    } else if (element.type === "line") {
        const lineWidth = style.width || 700;
        fabObj.set({
            x1: 0,
            y1: 0,
            x2: lineWidth,
            y2: 0,
            stroke: style.color || "#cccccc",
            strokeWidth: parseInt(style.strokeWidth, 10) || 1,
            opacity: style.opacity !== undefined ? parseFloat(style.opacity) : 1,
        });
    } else if (element.type === "spacer") {
        const height = parseInt(style.height, 10) || 20;
        fabObj.set({
            height: height,
            fill: style.backgroundColor || "transparent",
            opacity: style.opacity !== undefined ? parseFloat(style.opacity) : 1,
        });
    }

    // Common for all non-group objects
    if (fabObj.type !== "group") {
        fabObj.set({
            opacity: style.opacity !== undefined ? parseFloat(style.opacity) : 1,
        });
    }

    fabObj.setCoords();
}

function syncObjectToElement(fabObj, elementsRef, onElementsChange) {
    // Sync position and size from fabric object back to React state
    if (!fabObj._elementId) return;
    const id = fabObj._elementId;
    const updated = elementsRef.current.map((el) => {
        if (el.id !== id) return el;
        return {
            ...el,
            position: {
                x: Math.round(fabObj.left),
                y: Math.round(fabObj.top),
            },
            size: {
                width: Math.round(fabObj.width * fabObj.scaleX),
                height: Math.round(fabObj.height * fabObj.scaleY),
            },
        };
    });
    onElementsChange(updated);
}

function drawGrid(fc) {
    // Remove existing grid lines
    clearGrid(fc);

    const lines = [];
    for (let i = GRID_SIZE; i < A4_WIDTH; i += GRID_SIZE) {
        lines.push(
            new fabric.Line([i, 0, i, A4_HEIGHT], {
                stroke: "#e9ecef",
                strokeWidth: 0.5,
                selectable: false,
                evented: false,
                excludeFromExport: true,
            })
        );
    }
    for (let j = GRID_SIZE; j < A4_HEIGHT; j += GRID_SIZE) {
        lines.push(
            new fabric.Line([0, j, A4_WIDTH, j], {
                stroke: "#e9ecef",
                strokeWidth: 0.5,
                selectable: false,
                evented: false,
                excludeFromExport: true,
            })
        );
    }

    const gridGroup = new fabric.Group(lines, {
        selectable: false,
        evented: false,
        excludeFromExport: true,
        data: "grid",
    });
    fc.add(gridGroup);
    fc.sendObjectToBack(gridGroup);
}

function clearGrid(fc) {
    const objs = fc.getObjects().filter((o) => o.data === "grid");
    objs.forEach((o) => fc.remove(o));
}
