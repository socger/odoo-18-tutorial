import React, {useRef, useCallback} from "react";
import {useDrop} from "react-dnd";
import CanvasElement from "./CanvasElement.jsx";

/**
 * Canvas component - the main drop zone where report elements are arranged.
 * Supports drag-and-drop from FieldPicker and reordering of elements.
 */
export default function Canvas({
    elements,
    selectedElement,
    onSelectElement,
    onUpdateElement,
    onRemoveElement,
    onMoveElement,
    onAddElement,
    fields,
}) {
    const canvasRef = useRef(null);

    const [{isOver}, drop] = useDrop({
        accept: "FIELD",
        drop: (item, monitor) => {
            const delta = monitor.getClientOffset();
            if (item.field) {
                onAddElement({
                    type: "text",
                    fieldPath: item.field.name,
                    content: item.field.string || item.field.name,
                    style: {},
                    position: {x: delta?.x || 0, y: delta?.y || 0},
                });
            }
        },
        collect: (monitor) => ({
            isOver: monitor.isOver(),
        }),
    });

    // Handle native HTML5 drop for FieldPicker transfers
    const handleNativeDrop = useCallback(
        (e) => {
            e.preventDefault();
            const data = e.dataTransfer.getData("application/json");
            if (data) {
                try {
                    const element = JSON.parse(data);
                    onAddElement(element);
                } catch {
                    // ignore invalid JSON
                }
            }
        },
        [onAddElement]
    );

    const handleNativeDragOver = useCallback((e) => {
        e.preventDefault();
        e.dataTransfer.dropEffect = "copy";
    }, []);

    const setDropRef = useCallback(
        (node) => {
            canvasRef.current = node;
            drop(node);
        },
        [drop]
    );

    return (
        <div
            ref={setDropRef}
            className={`o_report_canvas ${isOver ? "o_report_canvas_hover" : ""}`}
            onDrop={handleNativeDrop}
            onDragOver={handleNativeDragOver}
        >
            <div className="o_report_canvas_header">
                <span className="o_report_canvas_title">Report Canvas</span>
                <span className="o_report_canvas_info text-muted">
                    {elements.length} element{elements.length !== 1 ? "s" : ""}
                </span>
            </div>
            <div className="o_report_canvas_content">
                {elements.length === 0 ? (
                    <div className="o_report_canvas_empty">
                        <i className="fa fa-arrows-alt fa-3x text-muted" />
                        <p>Drag fields from the sidebar to build your report</p>
                    </div>
                ) : (
                    <div className="o_report_canvas_elements">
                        {elements.map((element, index) => (
                            <CanvasElement
                                key={element.id}
                                element={element}
                                index={index}
                                isSelected={selectedElement?.id === element.id}
                                onSelect={() => onSelectElement(element)}
                                onUpdate={(updates) =>
                                    onUpdateElement(element.id, updates)
                                }
                                onRemove={() => onRemoveElement(element.id)}
                                onMove={onMoveElement}
                                fields={fields}
                            />
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}
