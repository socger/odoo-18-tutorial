import React, {useEffect, useRef, useCallback, useState} from "react";
import * as fabric from "fabric";

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
 * ReportCanvas — the main visual editor powered by Fabric.js.
 *
 * Props:
 *   elements      – array of layout elements (source of truth in React)
 *   onElementsChange – called when elements change (fabric objects moved/resized)
 *   onSelectElement  – called when user clicks an element (passes element id)
 *   selectedId       – id of currently selected element (for highlight)
 *   fields           – available model fields (for drop mapping)
 *   onAddElement     – called when a field is dropped onto the canvas
 */
export default function ReportCanvas({
    elements,
    onElementsChange,
    onSelectElement,
    selectedId,
    fields,
    onAddElement,
}) {
    const canvasRef = useRef(null);
    const fabricRef = useRef(null);
    const containerRef = useRef(null);
    const [zoom, setZoom] = useState(1);
    const [gridVisible, setGridVisible] = useState(true);
    const elementsMapRef = useRef(new Map());

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

        // Sync object moves/resizes back to React
        fc.on("object:modified", (e) => {
            const obj = e.target;
            if (!obj || !obj._elementId) return;
            syncObjectToElement(obj);
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

        // Add or update objects
        for (const element of elements) {
            const existing = elementsMapRef.current.get(element.id);
            if (existing) {
                // Update position/size if changed externally
                updateFabricObject(existing, element);
            } else {
                const obj = createFabricObject(element);
                if (obj) {
                    obj._elementId = element.id;
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
                const x = (e.clientX - rect.left) / zoomVal;
                const y = (e.clientY - rect.top) / zoomVal;

                onAddElement({
                    ...payload,
                    position: {x: Math.round(x), y: Math.round(y)},
                });
            } catch {
                // ignore invalid JSON
            }
        },
        [onAddElement]
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

    // === KEYBOARD SHORTCUTS === //
    useEffect(() => {
        const handleKey = (e) => {
            const fc = fabricRef.current;
            if (!fc) return;

            // Delete selected
            if (e.key === "Delete" || e.key === "Backspace") {
                const active = fc.getActiveObject();
                if (active && active._elementId) {
                    const id = active._elementId;
                    fc.remove(active);
                    elementsMapRef.current.delete(id);
                    fc.renderAll();
                    // Notify parent — remove element from state
                    onElementsChange((prev) => prev.filter((el) => el.id !== id));
                    onSelectElement(null);
                }
            }
        };
        window.addEventListener("keydown", handleKey);
        return () => window.removeEventListener("keydown", handleKey);
    }, [onElementsChange, onSelectElement]);

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
                </div>
            </div>
        </div>
    );
}

// === FABRIC OBJECT FACTORY === //

function createFabricObject(element) {
    const style = element.style || {};
    const pos = element.position || {x: 20, y: 20};

    switch (element.type) {
        case "text":
            return createTextObject(element, pos, style);
        case "heading":
            return createHeadingObject(element, pos, style);
        case "line":
            return createLineObject(element, pos, style);
        case "image":
            return createImagePlaceholder(element, pos, style);
        case "spacer":
            return createSpacerObject(element, pos, style);
        case "pagebreak":
            return createPageBreakObject(element, pos);
        case "table":
            return createTablePlaceholder(element, pos, style);
        default:
            return createTextObject(element, pos, style);
    }
}

function createTextObject(element, pos, style) {
    const label = element.fieldPath
        ? `[${element.fieldPath}]`
        : element.content || "Text";
    return new fabric.Textbox(label, {
        left: pos.x,
        top: pos.y,
        fontSize: style.fontSize || 12,
        fontWeight: style.fontWeight || "normal",
        fill: style.color || "#000000",
        textAlign: style.textAlign || "left",
        fontFamily: "sans-serif",
        width: 300,
        padding: 4,
        editable: false,
        hasControls: true,
        borderColor: "#0d6efd",
        cornerColor: "#0d6efd",
        cornerSize: 8,
        transparentCorners: false,
    });
}

function createHeadingObject(element, pos, style) {
    const level = style.level || 2;
    const sizes = {1: 24, 2: 20, 3: 16, 4: 14, 5: 12, 6: 11};
    const label = element.content || `Heading ${level}`;
    return new fabric.Textbox(label, {
        left: pos.x,
        top: pos.y,
        fontSize: sizes[level] || 20,
        fontWeight: "bold",
        fill: style.color || "#000000",
        textAlign: style.textAlign || "left",
        fontFamily: "sans-serif",
        width: 500,
        padding: 4,
        editable: false,
        borderColor: "#0d6efd",
        cornerColor: "#0d6efd",
        cornerSize: 8,
        transparentCorners: false,
    });
}

function createLineObject(element, pos, style) {
    return new fabric.Line([pos.x, pos.y, pos.x + 700, pos.y], {
        stroke: style.color || "#cccccc",
        strokeWidth: style.strokeWidth || 1,
        selectable: true,
        borderColor: "#0d6efd",
        cornerColor: "#0d6efd",
        cornerSize: 8,
        transparentCorners: false,
    });
}

function createImagePlaceholder(element, pos, style) {
    const maxWidth = parseInt(style.maxWidth, 10) || 200;
    const rect = new fabric.Rect({
        width: maxWidth,
        height: Math.round(maxWidth * 0.75),
        fill: "#e9ecef",
        stroke: "#adb5bd",
        strokeWidth: 1,
        strokeDashArray: [5, 5],
    });
    const text = new fabric.Text("Image", {
        fontSize: 12,
        fill: "#6c757d",
        originX: "center",
        originY: "center",
    });
    const group = new fabric.Group([rect, text], {
        left: pos.x,
        top: pos.y,
        selectable: true,
        borderColor: "#0d6efd",
        cornerColor: "#0d6efd",
        cornerSize: 8,
        transparentCorners: false,
    });
    return group;
}

function createSpacerObject(element, pos, style) {
    const height = parseInt(style.height, 10) || 20;
    return new fabric.Rect({
        left: pos.x,
        top: pos.y,
        width: 700,
        height: height,
        fill: "transparent",
        stroke: "#adb5bd",
        strokeWidth: 1,
        strokeDashArray: [3, 3],
        selectable: true,
        borderColor: "#0d6efd",
        cornerColor: "#0d6efd",
        cornerSize: 8,
        transparentCorners: false,
    });
}

function createPageBreakObject(element, pos) {
    const line = new fabric.Line([0, 0, 700, 0], {
        stroke: "#dc3545",
        strokeWidth: 1,
        strokeDashArray: [8, 4],
    });
    const label = new fabric.Text("PAGE BREAK", {
        fontSize: 9,
        fill: "#dc3545",
        fontFamily: "sans-serif",
        left: 5,
        top: -12,
    });
    return new fabric.Group([line, label], {
        left: pos.x,
        top: pos.y,
        selectable: true,
        borderColor: "#0d6efd",
        cornerColor: "#0d6efd",
        cornerSize: 8,
        transparentCorners: false,
    });
}

function createTablePlaceholder(element, pos, style) {
    const ds = element.dataSource || "(no data source)";
    const columns = element.columns || [];

    // Geometry
    const tableWidth = 700;
    const rowHeight = 22;
    const headerHeight = 26;
    const colCount = Math.max(columns.length, 1);
    const colWidth = tableWidth / colCount;

    const objects = [];

    // Header background
    objects.push(
        new fabric.Rect({
            width: tableWidth,
            height: headerHeight,
            fill: "#e9ecef",
            stroke: "#6f42c1",
            strokeWidth: 1,
            originX: "left",
            originY: "top",
            left: 0,
            top: 0,
        })
    );

    // Header cells
    if (columns.length === 0) {
        objects.push(
            new fabric.Text(`Table: ${ds} — add columns`, {
                fontSize: 11,
                fill: "#6f42c1",
                left: 8,
                top: 6,
                fontFamily: "sans-serif",
            })
        );
    } else {
        columns.forEach((col, i) => {
            const headerText = col.header || col.fieldPath || `Col ${i + 1}`;
            objects.push(
                new fabric.Text(String(headerText).slice(0, 20), {
                    fontSize: 10,
                    fontWeight: "bold",
                    fill: "#495057",
                    left: i * colWidth + 6,
                    top: 7,
                    fontFamily: "sans-serif",
                })
            );
            // Vertical separator
            if (i > 0) {
                objects.push(
                    new fabric.Line([i * colWidth, 0, i * colWidth, headerHeight], {
                        stroke: "#ced4da",
                        strokeWidth: 1,
                        originX: "left",
                        originY: "top",
                        left: i * colWidth,
                        top: 0,
                    })
                );
            }
        });
    }

    // Empty body row (sample)
    const bodyHeight = rowHeight;
    objects.push(
        new fabric.Rect({
            width: tableWidth,
            height: bodyHeight,
            fill: "transparent",
            stroke: "#6f42c1",
            strokeWidth: 1,
            originX: "left",
            originY: "top",
            left: 0,
            top: headerHeight,
        })
    );
    columns.forEach((col, i) => {
        const placeholder = col.fieldPath ? `t-field: line.${col.fieldPath}` : "...";
        objects.push(
            new fabric.Text(`[${placeholder}]`, {
                fontSize: 9,
                fill: "#adb5bd",
                fontStyle: "italic",
                left: i * colWidth + 6,
                top: headerHeight + 6,
                fontFamily: "sans-serif",
            })
        );
        if (i > 0) {
            objects.push(
                new fabric.Line(
                    [
                        i * colWidth,
                        headerHeight,
                        i * colWidth,
                        headerHeight + bodyHeight,
                    ],
                    {
                        stroke: "#e9ecef",
                        strokeWidth: 1,
                        originX: "left",
                        originY: "top",
                        left: i * colWidth,
                        top: headerHeight,
                    }
                )
            );
        }
    });

    // Data source label
    objects.push(
        new fabric.Text(`O2M: ${ds}`, {
            fontSize: 9,
            fill: "#6f42c1",
            left: 0,
            top: headerHeight + bodyHeight + 4,
            fontFamily: "sans-serif",
        })
    );

    const totalHeight = headerHeight + bodyHeight + 18 + (columns.length === 0 ? 0 : 0);

    return new fabric.Group(objects, {
        left: pos.x,
        top: pos.y,
        selectable: true,
        borderColor: "#0d6efd",
        cornerColor: "#0d6efd",
        cornerSize: 8,
        transparentCorners: false,
        // Internal metadata for sizing
        _tableWidth: tableWidth,
        _tableHeight: totalHeight,
    });
}

// === HELPERS === //

function updateFabricObject(fabObj, element) {
    const pos = element.position;
    if (pos) {
        fabObj.set({left: pos.x, top: pos.y});
    }
    fabObj.setCoords();
}

function syncObjectToElement(fabObj) {
    // This mutates the element object in-place so the parent can read it
    // The parent's onElementsChange will handle the actual state update
    if (!fabObj._elementId) return;
    // Position is synced via the object:modified event
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
