import React, {memo, useMemo} from "react";
import TableEditorPanel from "./TableEditorPanel.jsx";

/**
 * PropertiesPanel - right sidebar that shows and edits properties
 * of the currently selected canvas element.
 */
export default memo(function PropertiesPanel({
    element,
    fields,
    rpc,
    onUpdateElement,
    onRemoveElement,
}) {
    if (!element) {
        return (
            <div className="o_properties_panel o_properties_panel_empty">
                <div className="o_properties_panel_header">
                    <h4>Properties</h4>
                </div>
                <p className="text-muted text-center p-3">
                    Select an element to edit its properties
                </p>
            </div>
        );
    }

    function handleStyleChange(key, value) {
        onUpdateElement(element.id, {
            style: {...(element.style || {}), [key]: value},
        });
    }

    function handleFieldChange(e) {
        onUpdateElement(element.id, {fieldPath: e.target.value});
    }

    function handleContentChange(e) {
        onUpdateElement(element.id, {content: e.target.value});
    }

    function handleTypeChange(e) {
        const newType = e.target.value;
        const updates = {type: newType};
        // Reset type-specific fields when switching
        if (newType !== "text" && newType !== "image") {
            updates.fieldPath = "";
        }
        if (newType !== "text" && newType !== "heading" && newType !== "html") {
            updates.content = "";
        }
        onUpdateElement(element.id, updates);
    }

    function handleConditionChange(e) {
        onUpdateElement(element.id, {condition: e.target.value});
    }

    function handleTableStyleChange(key, value) {
        onUpdateElement(element.id, {
            tableStyle: {...(element.tableStyle || {}), [key]: value},
        });
    }

    const elementTypes = useMemo(
        () => [
            {value: "text", label: "Text / Field"},
            {value: "heading", label: "Heading"},
            {value: "html", label: "HTML Block"},
            {value: "line", label: "Horizontal Line"},
            {value: "image", label: "Image"},
            {value: "table", label: "Table"},
            {value: "spacer", label: "Spacer"},
            {value: "pagebreak", label: "Page Break"},
            {value: "container", label: "Container"},
        ],
        []
    );

    const supportsField = ["text", "image", "html"].includes(element.type);
    const supportsContent = ["text", "heading"].includes(element.type);
    const supportsLevel = element.type === "heading";

    // Find O2M and M2M fields for table data source
    const relationFields = useMemo(
        () => fields.filter((f) => f.type === "one2many" || f.type === "many2many"),
        [fields]
    );

    // Field format options for t-field rendering
    const fieldFormats = useMemo(
        () => [
            {value: "", label: "Default (auto)"},
            {value: "monetary", label: "Monetary"},
            {value: "date", label: "Date"},
            {value: "datetime", label: "Datetime"},
            {value: "float_time", label: "Float (time)"},
            {value: "float", label: "Float (decimal)"},
            {value: "integer", label: "Integer"},
            {value: "char", label: "Text"},
            {value: "html", label: "HTML"},
            {value: "selection", label: "Selection"},
            {value: "many2one", label: "Many2one (name)"},
        ],
        []
    );

    return (
        <div className="o_properties_panel">
            <div className="o_properties_panel_header">
                <h4>Properties</h4>
                <span className="badge bg-secondary">{element.type}</span>
            </div>
            <div className="o_properties_panel_body">
                {/* Position (X/Y) */}
                {element.position && (
                    <div className="o_properties_section">
                        <h5>Position</h5>
                        <div className="o_properties_field_row">
                            <div className="o_properties_field o_properties_field_half">
                                <label>X (px)</label>
                                <input
                                    type="number"
                                    className="form-control form-control-sm"
                                    value={Math.round(element.position.x) || 0}
                                    onChange={(e) =>
                                        onUpdateElement(element.id, {
                                            position: {
                                                ...element.position,
                                                x: parseInt(e.target.value, 10) || 0,
                                            },
                                        })
                                    }
                                />
                            </div>
                            <div className="o_properties_field o_properties_field_half">
                                <label>Y (px)</label>
                                <input
                                    type="number"
                                    className="form-control form-control-sm"
                                    value={Math.round(element.position.y) || 0}
                                    onChange={(e) =>
                                        onUpdateElement(element.id, {
                                            position: {
                                                ...element.position,
                                                y: parseInt(e.target.value, 10) || 0,
                                            },
                                        })
                                    }
                                />
                            </div>
                        </div>
                        {/* Width / Height */}
                        <div className="o_properties_field_row">
                            <div className="o_properties_field o_properties_field_half">
                                <label>Width (px)</label>
                                <input
                                    type="number"
                                    className="form-control form-control-sm"
                                    value={element.style?.width || ""}
                                    onChange={(e) =>
                                        handleStyleChange(
                                            "width",
                                            e.target.value
                                                ? parseInt(e.target.value, 10)
                                                : undefined
                                        )
                                    }
                                    placeholder="auto"
                                />
                            </div>
                            <div className="o_properties_field o_properties_field_half">
                                <label>Height (px)</label>
                                <input
                                    type="number"
                                    className="form-control form-control-sm"
                                    value={element.style?.height || ""}
                                    onChange={(e) =>
                                        handleStyleChange(
                                            "height",
                                            e.target.value
                                                ? parseInt(e.target.value, 10)
                                                : undefined
                                        )
                                    }
                                    placeholder="auto"
                                />
                            </div>
                        </div>
                    </div>
                )}

                {/* Type */}
                <div className="o_properties_field">
                    <label>Type</label>
                    <select
                        className="form-select form-select-sm"
                        value={element.type}
                        onChange={handleTypeChange}
                    >
                        {elementTypes.map((t) => (
                            <option key={t.value} value={t.value}>
                                {t.label}
                            </option>
                        ))}
                    </select>
                </div>

                {/* Field binding */}
                {supportsField && (
                    <div className="o_properties_field">
                        <label>Bind to Field</label>
                        <select
                            className="form-select form-select-sm"
                            value={element.fieldPath || ""}
                            onChange={handleFieldChange}
                        >
                            <option value="">None (static)</option>
                            {fields.map((f) => (
                                <option key={f.name} value={f.name}>
                                    {f.string} ({f.type})
                                </option>
                            ))}
                        </select>
                    </div>
                )}

                {/* Field format (when a field is bound) */}
                {supportsField && element.fieldPath && (
                    <div className="o_properties_field">
                        <label>
                            Field Format{" "}
                            <small className="text-muted">(t-field widget)</small>
                        </label>
                        <select
                            className="form-select form-select-sm"
                            value={element.style?.fieldFormat || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "fieldFormat",
                                    e.target.value || undefined
                                )
                            }
                        >
                            {fieldFormats.map((fmt) => (
                                <option key={fmt.value} value={fmt.value}>
                                    {fmt.label}
                                </option>
                            ))}
                        </select>
                    </div>
                )}

                {/* Content */}
                {supportsContent && !element.fieldPath && (
                    <div className="o_properties_field">
                        <label>Content</label>
                        <input
                            type="text"
                            className="form-control form-control-sm"
                            value={element.content || ""}
                            onChange={handleContentChange}
                        />
                    </div>
                )}

                {/* Heading level */}
                {supportsLevel && (
                    <div className="o_properties_field">
                        <label>Level</label>
                        <select
                            className="form-select form-select-sm"
                            value={element.style?.level || 2}
                            onChange={(e) =>
                                handleStyleChange("level", parseInt(e.target.value, 10))
                            }
                        >
                            {[1, 2, 3, 4, 5, 6].map((l) => (
                                <option key={l} value={l}>
                                    H{l}
                                </option>
                            ))}
                        </select>
                    </div>
                )}

                {/* Table configuration */}
                {element.type === "table" && (
                    <>
                        <div className="o_properties_field">
                            <label>Data Source (O2M / M2M field)</label>
                            <select
                                className="form-select form-select-sm"
                                value={element.dataSource || ""}
                                onChange={(e) =>
                                    onUpdateElement(element.id, {
                                        dataSource: e.target.value,
                                        columns: element.columns || [],
                                    })
                                }
                            >
                                <option value="">-- Select O2M / M2M field --</option>
                                {relationFields.map((f) => (
                                    <option key={f.name} value={f.name}>
                                        {f.string} ({f.name}) [{f.type}]
                                    </option>
                                ))}
                            </select>
                        </div>

                        {/* Table header styling */}
                        {element.dataSource && (
                            <div className="o_properties_section">
                                <h5>Table Style</h5>
                                <div className="o_properties_field">
                                    <label>Header Background</label>
                                    <input
                                        type="color"
                                        className="form-control form-control-sm form-control-color"
                                        value={
                                            element.tableStyle?.headerBgColor ||
                                            "#e9ecef"
                                        }
                                        onChange={(e) =>
                                            handleTableStyleChange(
                                                "headerBgColor",
                                                e.target.value
                                            )
                                        }
                                    />
                                </div>
                                <div className="o_properties_field">
                                    <label>Header Text Color</label>
                                    <input
                                        type="color"
                                        className="form-control form-control-sm form-control-color"
                                        value={
                                            element.tableStyle?.headerColor || "#495057"
                                        }
                                        onChange={(e) =>
                                            handleTableStyleChange(
                                                "headerColor",
                                                e.target.value
                                            )
                                        }
                                    />
                                </div>
                                <div className="o_properties_field">
                                    <label>Header Font Size (px)</label>
                                    <input
                                        type="number"
                                        className="form-control form-control-sm"
                                        value={element.tableStyle?.headerFontSize || 10}
                                        onChange={(e) =>
                                            handleTableStyleChange(
                                                "headerFontSize",
                                                parseInt(e.target.value, 10) || 10
                                            )
                                        }
                                    />
                                </div>
                                <div className="o_properties_field">
                                    <label>Header Font Weight</label>
                                    <select
                                        className="form-select form-select-sm"
                                        value={
                                            element.tableStyle?.headerFontWeight ||
                                            "bold"
                                        }
                                        onChange={(e) =>
                                            handleTableStyleChange(
                                                "headerFontWeight",
                                                e.target.value
                                            )
                                        }
                                    >
                                        <option value="normal">Normal</option>
                                        <option value="bold">Bold</option>
                                        <option value="lighter">Light</option>
                                    </select>
                                </div>
                                <div className="o_properties_field">
                                    <label className="o_properties_checkbox">
                                        <input
                                            type="checkbox"
                                            checked={
                                                element.tableStyle?.zebraStriping !==
                                                false
                                            }
                                            onChange={(e) =>
                                                handleTableStyleChange(
                                                    "zebraStriping",
                                                    e.target.checked
                                                )
                                            }
                                        />
                                        <span className="ms-1">Zebra striping</span>
                                    </label>
                                </div>
                                {element.tableStyle?.zebraStriping !== false && (
                                    <>
                                        <div className="o_properties_field">
                                            <label>Even Row BG</label>
                                            <input
                                                type="color"
                                                className="form-control form-control-sm form-control-color"
                                                value={
                                                    element.tableStyle?.evenRowBg ||
                                                    "#ffffff"
                                                }
                                                onChange={(e) =>
                                                    handleTableStyleChange(
                                                        "evenRowBg",
                                                        e.target.value
                                                    )
                                                }
                                            />
                                        </div>
                                        <div className="o_properties_field">
                                            <label>Odd Row BG</label>
                                            <input
                                                type="color"
                                                className="form-control form-control-sm form-control-color"
                                                value={
                                                    element.tableStyle?.oddRowBg ||
                                                    "#f8f9fa"
                                                }
                                                onChange={(e) =>
                                                    handleTableStyleChange(
                                                        "oddRowBg",
                                                        e.target.value
                                                    )
                                                }
                                            />
                                        </div>
                                    </>
                                )}
                                <div className="o_properties_field">
                                    <label className="o_properties_checkbox">
                                        <input
                                            type="checkbox"
                                            checked={
                                                element.tableStyle?.showFooter === true
                                            }
                                            onChange={(e) =>
                                                handleTableStyleChange(
                                                    "showFooter",
                                                    e.target.checked
                                                )
                                            }
                                        />
                                        <span className="ms-1">
                                            Show footer / totals
                                        </span>
                                    </label>
                                </div>
                                <div className="o_properties_field">
                                    <label className="o_properties_checkbox">
                                        <input
                                            type="checkbox"
                                            checked={
                                                element.tableStyle?.showBorders !==
                                                false
                                            }
                                            onChange={(e) =>
                                                handleTableStyleChange(
                                                    "showBorders",
                                                    e.target.checked
                                                )
                                            }
                                        />
                                        <span className="ms-1">Table borders</span>
                                    </label>
                                </div>
                                {element.tableStyle?.showBorders !== false && (
                                    <div className="o_properties_field">
                                        <label>Border Color</label>
                                        <input
                                            type="color"
                                            className="form-control form-control-sm form-control-color"
                                            value={
                                                element.tableStyle?.borderColor ||
                                                "#dee2e6"
                                            }
                                            onChange={(e) =>
                                                handleTableStyleChange(
                                                    "borderColor",
                                                    e.target.value
                                                )
                                            }
                                        />
                                    </div>
                                )}
                            </div>
                        )}

                        {element.dataSource && (
                            <div className="o_properties_section">
                                <TableEditorPanel
                                    element={element}
                                    fields={fields}
                                    rpc={rpc}
                                    onUpdate={onUpdateElement}
                                />
                            </div>
                        )}
                    </>
                )}

                {/* Spacer height */}
                {element.type === "spacer" && (
                    <div className="o_properties_field">
                        <label>Height</label>
                        <input
                            type="text"
                            className="form-control form-control-sm"
                            value={element.style?.height || "20px"}
                            onChange={(e) =>
                                handleStyleChange("height", e.target.value)
                            }
                            placeholder="e.g. 20px, 1cm"
                        />
                    </div>
                )}

                {/* Condition (t-if) */}
                <div className="o_properties_field">
                    <label>
                        Condition <small className="text-muted">(optional t-if)</small>
                    </label>
                    <input
                        type="text"
                        className="form-control form-control-sm"
                        value={element.condition || ""}
                        onChange={handleConditionChange}
                        placeholder="e.g. o.state == 'done'"
                    />
                </div>

                {/* Style properties */}
                <div className="o_properties_section">
                    <h5>Style</h5>
                    <div className="o_properties_field">
                        <label>Font Size (pt)</label>
                        <input
                            type="number"
                            className="form-control form-control-sm"
                            value={element.style?.fontSize || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "fontSize",
                                    e.target.value
                                        ? parseInt(e.target.value, 10)
                                        : undefined
                                )
                            }
                        />
                    </div>
                    <div className="o_properties_field">
                        <label>Font Weight</label>
                        <select
                            className="form-select form-select-sm"
                            value={element.style?.fontWeight || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "fontWeight",
                                    e.target.value || undefined
                                )
                            }
                        >
                            <option value="">Normal</option>
                            <option value="bold">Bold</option>
                            <option value="lighter">Light</option>
                        </select>
                    </div>
                    <div className="o_properties_field">
                        <label>Color</label>
                        <input
                            type="color"
                            className="form-control form-control-sm form-control-color"
                            value={element.style?.color || "#000000"}
                            onChange={(e) => handleStyleChange("color", e.target.value)}
                        />
                    </div>
                    <div className="o_properties_field">
                        <label>Background Color</label>
                        <input
                            type="color"
                            className="form-control form-control-sm form-control-color"
                            value={element.style?.backgroundColor || "#ffffff"}
                            onChange={(e) =>
                                handleStyleChange("backgroundColor", e.target.value)
                            }
                        />
                    </div>
                    <div className="o_properties_field">
                        <label>Text Align</label>
                        <select
                            className="form-select form-select-sm"
                            value={element.style?.textAlign || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "textAlign",
                                    e.target.value || undefined
                                )
                            }
                        >
                            <option value="">Default</option>
                            <option value="left">Left</option>
                            <option value="center">Center</option>
                            <option value="right">Right</option>
                        </select>
                    </div>
                    <div className="o_properties_field">
                        <label>Padding (px)</label>
                        <input
                            type="number"
                            className="form-control form-control-sm"
                            value={element.style?.padding || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "padding",
                                    e.target.value
                                        ? parseInt(e.target.value, 10)
                                        : undefined
                                )
                            }
                        />
                    </div>
                    <div className="o_properties_field">
                        <label>Margin (px)</label>
                        <input
                            type="number"
                            className="form-control form-control-sm"
                            value={element.style?.margin || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "margin",
                                    e.target.value
                                        ? parseInt(e.target.value, 10)
                                        : undefined
                                )
                            }
                        />
                    </div>
                    <div className="o_properties_field">
                        <label>Line Height</label>
                        <input
                            type="text"
                            className="form-control form-control-sm"
                            value={element.style?.lineHeight || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "lineHeight",
                                    e.target.value || undefined
                                )
                            }
                            placeholder="e.g. 1.5, 24px"
                        />
                    </div>
                    <div className="o_properties_field">
                        <label>Text Decoration</label>
                        <select
                            className="form-select form-select-sm"
                            value={element.style?.textDecoration || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "textDecoration",
                                    e.target.value || undefined
                                )
                            }
                        >
                            <option value="">None</option>
                            <option value="underline">Underline</option>
                            <option value="line-through">Strikethrough</option>
                            <option value="overline">Overline</option>
                        </select>
                    </div>
                    <div className="o_properties_field">
                        <label>Border (e.g. 1px solid #ccc)</label>
                        <input
                            type="text"
                            className="form-control form-control-sm"
                            value={element.style?.borderBottom || ""}
                            onChange={(e) =>
                                handleStyleChange(
                                    "borderBottom",
                                    e.target.value || undefined
                                )
                            }
                            placeholder="1px solid #dee2e6"
                        />
                    </div>
                    <div className="o_properties_field">
                        <label>Opacity</label>
                        <input
                            type="range"
                            className="form-range"
                            min="0"
                            max="1"
                            step="0.1"
                            value={element.style?.opacity ?? 1}
                            onChange={(e) =>
                                handleStyleChange("opacity", parseFloat(e.target.value))
                            }
                        />
                    </div>
                    {element.type === "image" && (
                        <div className="o_properties_field">
                            <label>Max Width</label>
                            <input
                                type="text"
                                className="form-control form-control-sm"
                                value={element.style?.maxWidth || "200px"}
                                onChange={(e) =>
                                    handleStyleChange("maxWidth", e.target.value)
                                }
                                placeholder="e.g. 200px, 50%"
                            />
                        </div>
                    )}
                </div>

                {/* Delete */}
                <div className="o_properties_actions mt-3">
                    <button
                        className="btn btn-sm btn-outline-danger w-100"
                        onClick={() => onRemoveElement(element.id)}
                    >
                        <i className="fa fa-trash me-1" />
                        Delete Element
                    </button>
                </div>
            </div>
        </div>
    );
});
