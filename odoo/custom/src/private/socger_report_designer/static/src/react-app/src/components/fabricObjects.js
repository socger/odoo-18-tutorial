/**
 * Fabric.js object factory functions.
 *
 * Each function creates a Fabric.js object for a given report element type.
 * Extracted from ReportCanvas.jsx for modularity.
 */
import * as fabric from "fabric";

// === COMMON SELECTION STYLE === //

const SELECTION_STYLE = {
    borderColor: "#0d6efd",
    cornerColor: "#0d6efd",
    cornerSize: 8,
    transparentCorners: false,
};

// === FACTORY FUNCTIONS === //

/**
 * Create the appropriate Fabric.js object for an element definition.
 */
export function createFabricObject(element) {
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

/**
 * Create a text/field-bound textbox.
 */
export function createTextObject(element, pos, style) {
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
        width: style.width || 300,
        padding: 4,
        editable: false,
        hasControls: true,
        ...SELECTION_STYLE,
    });
}

/**
 * Create a heading textbox.
 */
export function createHeadingObject(element, pos, style) {
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
        width: style.width || 500,
        padding: 4,
        editable: false,
        ...SELECTION_STYLE,
    });
}

/**
 * Create a horizontal line.
 */
export function createLineObject(element, pos, style) {
    const lineWidth = style.width || 700;
    return new fabric.Line([pos.x, pos.y, pos.x + lineWidth, pos.y], {
        stroke: style.color || "#cccccc",
        strokeWidth: style.strokeWidth || 1,
        selectable: true,
        ...SELECTION_STYLE,
    });
}

/**
 * Create an image placeholder (dashed rect + label).
 */
export function createImagePlaceholder(element, pos, style) {
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
    return new fabric.Group([rect, text], {
        left: pos.x,
        top: pos.y,
        selectable: true,
        ...SELECTION_STYLE,
    });
}

/**
 * Create a spacer (transparent rect with dashed border).
 */
export function createSpacerObject(element, pos, style) {
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
        ...SELECTION_STYLE,
    });
}

/**
 * Create a page break indicator.
 */
export function createPageBreakObject(element, pos) {
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
        ...SELECTION_STYLE,
    });
}

/**
 * Create a table placeholder with header, body row, and optional footer.
 */
export function createTablePlaceholder(element, pos, style) {
    const ds = element.dataSource || "(no data source)";
    const columns = element.columns || [];
    const tableStyle = element.tableStyle || {};

    // Geometry
    const tableWidth = style.width || 700;
    const rowHeight = 22;
    const headerHeight = 26;
    const colCount = Math.max(columns.length, 1);
    const colWidth = tableWidth / colCount;

    const objects = [];

    // Header background
    const headerBg = tableStyle.headerBgColor || "#e9ecef";
    objects.push(
        new fabric.Rect({
            width: tableWidth,
            height: headerHeight,
            fill: headerBg,
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
                    fontSize: parseInt(tableStyle.headerFontSize, 10) || 10,
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

    // Empty body row (sample) with optional zebra
    const bodyHeight = rowHeight;
    const zebraFill = tableStyle.zebraStriping === false ? "transparent" : "#f8f9fa";
    objects.push(
        new fabric.Rect({
            width: tableWidth,
            height: bodyHeight,
            fill: zebraFill,
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

    // Footer row indicator
    if (tableStyle.showFooter) {
        const footerY = headerHeight + bodyHeight;
        objects.push(
            new fabric.Rect({
                width: tableWidth,
                height: 20,
                fill: "#e9ecef",
                stroke: "#6f42c1",
                strokeWidth: 1,
                originX: "left",
                originY: "top",
                left: 0,
                top: footerY,
            })
        );
        objects.push(
            new fabric.Text("Totals", {
                fontSize: 9,
                fontWeight: "bold",
                fill: "#495057",
                left: 6,
                top: footerY + 5,
                fontFamily: "sans-serif",
            })
        );
    }

    // Data source label
    const footerOffset = tableStyle.showFooter ? 20 : 0;
    objects.push(
        new fabric.Text(`O2M/M2M: ${ds}`, {
            fontSize: 9,
            fill: "#6f42c1",
            left: 0,
            top: headerHeight + bodyHeight + footerOffset + 4,
            fontFamily: "sans-serif",
        })
    );

    const totalHeight = headerHeight + bodyHeight + 18 + footerOffset;

    return new fabric.Group(objects, {
        left: pos.x,
        top: pos.y,
        selectable: true,
        ...SELECTION_STYLE,
        // Internal metadata for sizing
        _tableWidth: tableWidth,
        _tableHeight: totalHeight,
    });
}
