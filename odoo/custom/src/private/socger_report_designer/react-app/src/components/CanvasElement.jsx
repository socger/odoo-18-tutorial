import React, {useRef} from "react";
import {useDrag, useDrop} from "react-dnd";

/**
 * A single element on the canvas. Supports click-to-select,
 * drag-to-reorder, and inline editing.
 */
export default function CanvasElement({
    element,
    index,
    isSelected,
    onSelect,
    onUpdate,
    onRemove,
    onMove,
    fields,
}) {
    const ref = useRef(null);

    const [{isDragging}, drag] = useDrag({
        type: "CANVAS_ELEMENT",
        item: () => ({id: element.id, index}),
        collect: (monitor) => ({
            isDragging: monitor.isDragging(),
        }),
    });

    const [, drop] = useDrop({
        accept: "CANVAS_ELEMENT",
        hover(item, monitor) {
            if (!ref.current) return;
            const dragIndex = item.index;
            const hoverIndex = index;
            if (dragIndex === hoverIndex) return;
            onMove(dragIndex, hoverIndex);
            item.index = hoverIndex;
        },
    });

    drag(drop(ref));

    const style = buildStyle(element.style || {});
    const fieldLabel = getFieldLabel(element.fieldPath, fields);

    function renderContent() {
        switch (element.type) {
            case "text":
                if (element.fieldPath) {
                    return (
                        <span className="o_canvas_element_field">
                            <i className="fa fa-database text-muted me-1" />
                            {fieldLabel || element.fieldPath}
                        </span>
                    );
                }
                return <span>{element.content || "Text"}</span>;

            case "heading":
                return (
                    <span className="o_canvas_element_heading">
                        {element.content || "Heading"}
                    </span>
                );

            case "line":
                return <hr className="my-1" />;

            case "image":
                if (element.fieldPath) {
                    return (
                        <span className="o_canvas_element_field">
                            <i className="fa fa-image me-1" />
                            Image: {fieldLabel || element.fieldPath}
                        </span>
                    );
                }
                return <span className="text-muted">Image placeholder</span>;

            case "table":
                return (
                    <span className="o_canvas_element_table">
                        <i className="fa fa-table me-1" />
                        Table ({element.dataSource || "unknown"})
                    </span>
                );

            case "spacer":
                return (
                    <span className="text-muted small">
                        <i className="fa fa-arrows-v me-1" />
                        Spacer ({element.style?.height || "20px"})
                    </span>
                );

            case "pagebreak":
                return (
                    <span className="text-muted small">
                        <i className="fa fa-file-o me-1" />
                        Page Break
                    </span>
                );

            case "container":
                return (
                    <span className="o_canvas_element_container">
                        <i className="fa fa-columns me-1" />
                        Container
                        {element.columns ? ` (${element.columns.length} cols)` : ""}
                    </span>
                );

            case "html":
                if (element.fieldPath) {
                    return (
                        <span className="o_canvas_element_field">
                            <i className="fa fa-code text-muted me-1" />
                            HTML: {fieldLabel || element.fieldPath}
                        </span>
                    );
                }
                return <span className="text-muted">HTML block</span>;

            default:
                return <span>{element.type}</span>;
        }
    }

    return (
        <div
            ref={ref}
            className={`o_canvas_element ${
                isSelected ? "o_canvas_element_selected" : ""
            } ${isDragging ? "o_canvas_element_dragging" : ""}`}
            style={style}
            onClick={(e) => {
                e.stopPropagation();
                onSelect();
            }}
        >
            <div className="o_canvas_element_content">{renderContent()}</div>
            {isSelected && (
                <button
                    className="o_canvas_element_remove btn btn-sm btn-danger"
                    onClick={(e) => {
                        e.stopPropagation();
                        onRemove();
                    }}
                    title="Remove element"
                >
                    <i className="fa fa-times" />
                </button>
            )}
        </div>
    );
}

function buildStyle(s) {
    const style = {};
    if (s.fontSize) style.fontSize = `${s.fontSize}pt`;
    if (s.fontWeight) style.fontWeight = s.fontWeight;
    if (s.color) style.color = s.color;
    if (s.textAlign) style.textAlign = s.textAlign;
    if (s.backgroundColor) style.backgroundColor = s.backgroundColor;
    if (s.padding) style.padding = `${s.padding}px`;
    if (s.margin) style.margin = `${s.margin}px`;
    return style;
}

function getFieldLabel(fieldPath, fields) {
    const field = fields.find((f) => f.name === fieldPath);
    return field ? field.string : null;
}
