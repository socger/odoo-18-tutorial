import React, {useState, useEffect, useCallback} from "react";

/**
 * TableEditorPanel - visual editor for configuring table columns.
 *
 * Props:
 *   element      - the table element being edited
 *   fields       - parent model fields (to find the O2M relation model)
 *   rpc          - RPC function to fetch related model fields
 *   onUpdate     - callback(elementId, updates) to update the element
 */
export default function TableEditorPanel({element, fields, rpc, onUpdate}) {
    const [relatedFields, setRelatedFields] = useState([]);
    const [loadingFields, setLoadingFields] = useState(false);

    const columns = element.columns || [];
    const dataSource = element.dataSource || "";

    // Find the related model name from the O2M field definition
    const o2mField = fields.find((f) => f.name === dataSource);
    const relationModel = o2mField?.relation || "";

    // Fetch related model fields when dataSource changes
    const fetchRelatedFields = useCallback(async () => {
        if (!relationModel || !rpc) {
            setRelatedFields([]);
            return;
        }
        setLoadingFields(true);
        try {
            const result = await rpc(
                `/api/report-designer/fields/${relationModel}`,
                {}
            );
            setRelatedFields(result.fields || []);
        } catch {
            setRelatedFields([]);
        } finally {
            setLoadingFields(false);
        }
    }, [relationModel, rpc]);

    useEffect(() => {
        fetchRelatedFields();
    }, [fetchRelatedFields]);

    function addColumn() {
        const newColumns = [
            ...columns,
            {
                header: `Column ${columns.length + 1}`,
                fieldPath: "",
                align: "left",
                width: "",
            },
        ];
        onUpdate(element.id, {columns: newColumns});
    }

    function removeColumn(index) {
        const newColumns = columns.filter((_, i) => i !== index);
        onUpdate(element.id, {columns: newColumns});
    }

    function updateColumn(index, key, value) {
        const newColumns = columns.map((col, i) =>
            i === index ? {...col, [key]: value} : col
        );
        onUpdate(element.id, {columns: newColumns});
    }

    function moveColumn(fromIndex, direction) {
        const toIndex = fromIndex + direction;
        if (toIndex < 0 || toIndex >= columns.length) return;
        const newColumns = [...columns];
        const [moved] = newColumns.splice(fromIndex, 1);
        newColumns.splice(toIndex, 0, moved);
        onUpdate(element.id, {columns: newColumns});
    }

    if (!dataSource) {
        return (
            <div className="o_table_editor o_table_editor_empty">
                <div className="o_table_editor_header">
                    <h5>
                        <i className="fa fa-table me-1" />
                        Table Columns
                    </h5>
                </div>
                <p className="text-muted small p-2 text-center">
                    Select a data source (O2M field) first to configure columns.
                </p>
            </div>
        );
    }

    return (
        <div className="o_table_editor">
            <div className="o_table_editor_header">
                <h5>
                    <i className="fa fa-table me-1" />
                    Table Columns
                </h5>
                <span className="badge bg-info">{relationModel}</span>
            </div>

            {loadingFields ? (
                <p className="text-muted small p-2 text-center">
                    <i className="fa fa-spinner fa-spin me-1" />
                    Loading fields...
                </p>
            ) : (
                <>
                    {/* Column list */}
                    <div className="o_table_editor_columns">
                        {columns.length === 0 ? (
                            <p className="text-muted small p-2 text-center">
                                No columns yet. Add one to start.
                            </p>
                        ) : (
                            columns.map((col, index) => (
                                <div
                                    key={`col_${index}`}
                                    className="o_table_column_card"
                                >
                                    <div className="o_table_column_header">
                                        <span className="o_table_column_index">
                                            {index + 1}
                                        </span>
                                        <div className="o_table_column_moves">
                                            <button
                                                className="btn btn-link btn-sm p-0"
                                                onClick={() => moveColumn(index, -1)}
                                                disabled={index === 0}
                                                title="Move up"
                                            >
                                                <i className="fa fa-chevron-up" />
                                            </button>
                                            <button
                                                className="btn btn-link btn-sm p-0"
                                                onClick={() => moveColumn(index, 1)}
                                                disabled={index === columns.length - 1}
                                                title="Move down"
                                            >
                                                <i className="fa fa-chevron-down" />
                                            </button>
                                        </div>
                                        <button
                                            className="btn btn-link btn-sm text-danger p-0 ms-auto"
                                            onClick={() => removeColumn(index)}
                                            title="Remove column"
                                        >
                                            <i className="fa fa-times" />
                                        </button>
                                    </div>

                                    {/* Header label */}
                                    <div className="o_table_column_field">
                                        <label>Header</label>
                                        <input
                                            type="text"
                                            className="form-control form-control-sm"
                                            value={col.header || ""}
                                            onChange={(e) =>
                                                updateColumn(
                                                    index,
                                                    "header",
                                                    e.target.value
                                                )
                                            }
                                            placeholder="Column title"
                                        />
                                    </div>

                                    {/* Field binding */}
                                    <div className="o_table_column_field">
                                        <label>Field</label>
                                        <select
                                            className="form-select form-select-sm"
                                            value={col.fieldPath || ""}
                                            onChange={(e) =>
                                                updateColumn(
                                                    index,
                                                    "fieldPath",
                                                    e.target.value
                                                )
                                            }
                                        >
                                            <option value="">None (empty)</option>
                                            {relatedFields.map((f) => (
                                                <option key={f.name} value={f.name}>
                                                    {f.string} ({f.type})
                                                </option>
                                            ))}
                                        </select>
                                    </div>

                                    {/* Alignment */}
                                    <div className="o_table_column_row">
                                        <div className="o_table_column_field o_table_column_half">
                                            <label>Align</label>
                                            <select
                                                className="form-select form-select-sm"
                                                value={col.align || "left"}
                                                onChange={(e) =>
                                                    updateColumn(
                                                        index,
                                                        "align",
                                                        e.target.value
                                                    )
                                                }
                                            >
                                                <option value="left">Left</option>
                                                <option value="center">Center</option>
                                                <option value="right">Right</option>
                                            </select>
                                        </div>
                                        <div className="o_table_column_field o_table_column_half">
                                            <label>Width</label>
                                            <input
                                                type="text"
                                                className="form-control form-control-sm"
                                                value={col.width || ""}
                                                onChange={(e) =>
                                                    updateColumn(
                                                        index,
                                                        "width",
                                                        e.target.value
                                                    )
                                                }
                                                placeholder="auto"
                                            />
                                        </div>
                                    </div>
                                </div>
                            ))
                        )}
                    </div>

                    {/* Add column button */}
                    <button
                        className="btn btn-sm btn-outline-primary w-100 mt-2"
                        onClick={addColumn}
                    >
                        <i className="fa fa-plus me-1" />
                        Add Column
                    </button>
                </>
            )}
        </div>
    );
}
