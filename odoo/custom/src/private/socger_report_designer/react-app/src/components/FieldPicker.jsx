import React, {useState, useMemo, useCallback, memo} from "react";
import {fetchRelatedFields} from "../api.jsx";

/**
 * Structural elements that can be added without a field binding.
 */
const STRUCTURAL_ELEMENTS = [
    {
        type: "heading",
        label: "Heading",
        icon: "header",
    },
    {
        type: "line",
        label: "Horizontal Line",
        icon: "minus",
    },
    {
        type: "spacer",
        label: "Spacer",
        icon: "arrows-v",
    },
    {
        type: "pagebreak",
        label: "Page Break",
        icon: "file-o",
    },
    {
        type: "table",
        label: "Table",
        icon: "table",
    },
    {
        type: "container",
        label: "Container",
        icon: "columns",
    },
];

/**
 * FieldPicker component - sidebar panel that shows available Odoo model fields
 * and allows dragging them onto the canvas.  Also provides structural elements.
 *
 * Supports expanding many2one fields into nested dotted paths (e.g.
 * ``partner_id.name``) via an inline sub-list that loads related model
 * fields on demand.
 */
export default memo(function FieldPicker({fields, targetModel, onAddElement, rpc}) {
    const [searchTerm, setSearchTerm] = useState("");
    const [filterType, setFilterType] = useState("all");
    const [showStructural, setShowStructural] = useState(true);
    // Map of parentFieldName → {loading, fields, error, parentPath}
    const [expandedRelations, setExpandedRelations] = useState({});

    const typeGroups = useMemo(() => {
        const groups = {};
        const filtered = fields.filter((f) => {
            const matchesSearch =
                !searchTerm ||
                f.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                (f.string || "").toLowerCase().includes(searchTerm.toLowerCase());
            const matchesType = filterType === "all" || f.type === filterType;
            return matchesSearch && matchesType;
        });
        for (const field of filtered) {
            const group = getGroupLabel(field.type);
            if (!groups[group]) groups[group] = [];
            groups[group].push(field);
        }
        return groups;
    }, [fields, searchTerm, filterType]);

    const fieldTypes = useMemo(() => {
        const types = new Set(fields.map((f) => f.type));
        return ["all", ...Array.from(types).sort()];
    }, [fields]);

    function handleDragStart(e, field) {
        e.dataTransfer.setData(
            "application/json",
            JSON.stringify({
                type: "text",
                fieldPath: field.name,
                content: field.string || field.name,
                style: {},
            })
        );
        e.dataTransfer.effectAllowed = "copy";
    }

    function handleDoubleClick(field) {
        onAddElement({
            type: "text",
            fieldPath: field.name,
            content: field.string || field.name,
            style: {},
        });
    }

    function handleStructuralDragStart(e, elem) {
        const payload = {type: elem.type, content: elem.label, style: {}};
        if (elem.type === "spacer") {
            payload.style = {height: "20px"};
        }
        e.dataTransfer.setData("application/json", JSON.stringify(payload));
        e.dataTransfer.effectAllowed = "copy";
    }

    function handleStructuralDoubleClick(elem) {
        const payload = {type: elem.type, content: elem.label, style: {}};
        if (elem.type === "spacer") {
            payload.style = {height: "20px"};
        }
        onAddElement(payload);
    }

    /**
     * Toggle expansion of a many2one relation field.  When first expanded
     * it fetches the related model's fields from the backend.
     */
    const toggleRelation = useCallback(
        async (field) => {
            const fname = field.name;
            const currently = expandedRelations[fname];
            if (currently && !currently.error) {
                // Collapse
                setExpandedRelations((prev) => {
                    const next = {...prev};
                    delete next[fname];
                    return next;
                });
                return;
            }
            // Start loading
            setExpandedRelations((prev) => ({
                ...prev,
                [fname]: {loading: true, fields: [], parentPath: fname},
            }));
            try {
                const relatedModel = field.relation;
                if (!relatedModel || !rpc) {
                    throw new Error("No related model or RPC not available");
                }
                const result = await fetchRelatedFields(relatedModel, fname, rpc);
                if (result.error) {
                    throw new Error(result.error);
                }
                setExpandedRelations((prev) => ({
                    ...prev,
                    [fname]: {
                        loading: false,
                        fields: result.fields || [],
                        parentPath: fname,
                        modelName: relatedModel,
                    },
                }));
            } catch (err) {
                setExpandedRelations((prev) => ({
                    ...prev,
                    [fname]: {
                        loading: false,
                        fields: [],
                        error: err.message || "Failed to load fields",
                        parentPath: fname,
                    },
                }));
            }
        },
        [expandedRelations, rpc]
    );

    /**
     * Handle drag of a nested (dotted) field path.
     */
    function handleNestedDragStart(e, parentPath, field) {
        const fullPath = `${parentPath}.${field.name}`;
        e.dataTransfer.setData(
            "application/json",
            JSON.stringify({
                type: "text",
                fieldPath: fullPath,
                content: field.string || field.name,
                style: {},
            })
        );
        e.dataTransfer.effectAllowed = "copy";
    }

    function handleNestedDoubleClick(parentPath, field) {
        const fullPath = `${parentPath}.${field.name}`;
        onAddElement({
            type: "text",
            fieldPath: fullPath,
            content: field.string || field.name,
            style: {},
        });
    }

    const isExpandable = (field) => field.type === "many2one" && field.relation;

    return (
        <div className="o_field_picker">
            <div className="o_field_picker_header">
                <h4>Fields</h4>
                {targetModel && (
                    <span className="o_field_picker_model badge bg-primary">
                        {targetModel}
                    </span>
                )}
            </div>

            {/* Structural elements */}
            <div className="o_field_picker_section">
                <div
                    className="o_field_picker_group_label o_field_picker_structural_toggle"
                    onClick={() => setShowStructural(!showStructural)}
                >
                    <i
                        className={`fa fa-chevron-${
                            showStructural ? "down" : "right"
                        } me-1`}
                    />
                    Layout Elements
                </div>
                {showStructural && (
                    <div className="o_field_picker_structural_list">
                        {STRUCTURAL_ELEMENTS.map((elem) => (
                            <div
                                key={elem.type}
                                className="o_field_picker_item"
                                draggable
                                onDragStart={(e) => handleStructuralDragStart(e, elem)}
                                onDoubleClick={() => handleStructuralDoubleClick(elem)}
                                title={elem.label}
                            >
                                <span
                                    className={`o_field_picker_icon fa fa-${elem.icon}`}
                                />
                                <span className="o_field_picker_name">
                                    {elem.label}
                                </span>
                            </div>
                        ))}
                    </div>
                )}
            </div>

            {!targetModel ? (
                <p className="text-muted text-center p-3 small">
                    Select a target model to see model fields
                </p>
            ) : (
                <>
                    <div className="o_field_picker_search">
                        <input
                            type="text"
                            className="form-control form-control-sm"
                            placeholder="Search fields..."
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                        />
                        <select
                            className="form-select form-select-sm mt-1"
                            value={filterType}
                            onChange={(e) => setFilterType(e.target.value)}
                        >
                            {fieldTypes.map((t) => (
                                <option key={t} value={t}>
                                    {t === "all" ? "All types" : t}
                                </option>
                            ))}
                        </select>
                    </div>
                    <div className="o_field_picker_list">
                        {Object.entries(typeGroups).map(([group, groupFields]) => (
                            <div key={group} className="o_field_picker_group">
                                <div className="o_field_picker_group_label">
                                    {group}
                                </div>
                                {groupFields.map((field) => {
                                    const expanded = expandedRelations[field.name];
                                    return (
                                        <React.Fragment key={field.name}>
                                            <div
                                                className="o_field_picker_item"
                                                draggable
                                                onDragStart={(e) =>
                                                    handleDragStart(e, field)
                                                }
                                                onDoubleClick={() =>
                                                    handleDoubleClick(field)
                                                }
                                                title={`${field.name} (${field.type})`}
                                            >
                                                <span
                                                    className={`o_field_picker_icon fa fa-${field.icon}`}
                                                />
                                                <span className="o_field_picker_name">
                                                    {field.string}
                                                </span>
                                                <span className="o_field_picker_type text-muted">
                                                    {field.type}
                                                </span>
                                                {isExpandable(field) && (
                                                    <span
                                                        className="o_field_picker_expand fa fa-chevron-right"
                                                        onClick={(e) => {
                                                            e.stopPropagation();
                                                            toggleRelation(field);
                                                        }}
                                                        title="Expand related fields"
                                                    />
                                                )}
                                            </div>
                                            {/* Nested fields for expanded many2one */}
                                            {expanded && (
                                                <div className="o_field_picker_nested">
                                                    {expanded.loading && (
                                                        <div className="o_field_picker_nested_loading">
                                                            <i className="fa fa-spinner fa-spin me-1" />
                                                            Loading...
                                                        </div>
                                                    )}
                                                    {expanded.error && (
                                                        <div className="o_field_picker_nested_error text-danger small px-3">
                                                            {expanded.error}
                                                        </div>
                                                    )}
                                                    {expanded.fields &&
                                                        expanded.fields.map((nf) => (
                                                            <div
                                                                key={nf.name}
                                                                className="o_field_picker_item o_field_picker_nested_item"
                                                                draggable
                                                                onDragStart={(e) =>
                                                                    handleNestedDragStart(
                                                                        e,
                                                                        expanded.parentPath,
                                                                        nf
                                                                    )
                                                                }
                                                                onDoubleClick={() =>
                                                                    handleNestedDoubleClick(
                                                                        expanded.parentPath,
                                                                        nf
                                                                    )
                                                                }
                                                                title={`${expanded.parentPath}.${nf.name} (${nf.type})`}
                                                            >
                                                                <span
                                                                    className={`o_field_picker_icon fa fa-${nf.icon}`}
                                                                />
                                                                <span className="o_field_picker_name">
                                                                    {nf.string}
                                                                </span>
                                                                <span className="o_field_picker_type text-muted">
                                                                    {nf.type}
                                                                </span>
                                                            </div>
                                                        ))}
                                                </div>
                                            )}
                                        </React.Fragment>
                                    );
                                })}
                            </div>
                        ))}
                        {Object.keys(typeGroups).length === 0 && (
                            <p className="text-muted text-center p-3 small">
                                No fields found
                            </p>
                        )}
                    </div>
                </>
            )}
        </div>
    );
});

function getGroupLabel(type) {
    const groups = {
        basic: ["char", "text", "html"],
        numeric: ["integer", "float", "monetary"],
        date: ["date", "datetime"],
        boolean: ["boolean"],
        selection: ["selection"],
        relation: ["many2one", "one2many", "many2many"],
        binary: ["binary", "image"],
    };
    for (const [label, types] of Object.entries(groups)) {
        if (types.includes(type)) return label;
    }
    return "other";
}
