import React, {useState} from "react";
import {createLayout, deleteLayout} from "../api.jsx";

/**
 * LayoutManager - lets the user select, create, or delete report layouts
 * and configure the target model.
 */
export default function LayoutManager({
    layouts,
    currentLayout,
    onSelectLayout,
    targetModel,
    models,
    onModelChange,
}) {
    const [newName, setNewName] = useState("");
    const [showCreate, setShowCreate] = useState(false);

    async function handleCreate() {
        if (!newName.trim() || !targetModel) return;
        try {
            const rpc = window.odoo?.services?.["core.rpc"] || defaultRpc;
            const result = await createLayout(newName.trim(), targetModel, rpc);
            setNewName("");
            setShowCreate(false);
            if (result.id) {
                onSelectLayout(result.id);
            }
        } catch (err) {
            console.error("Failed to create layout:", err);
        }
    }

    async function handleDelete(e, layoutId) {
        e.stopPropagation();
        if (!confirm("Delete this layout?")) return;
        try {
            const rpc = window.odoo?.services?.["core.rpc"] || defaultRpc;
            await deleteLayout(layoutId, rpc);
            window.location.reload();
        } catch (err) {
            console.error("Failed to delete layout:", err);
        }
    }

    return (
        <div className="o_layout_manager">
            <div className="o_layout_manager_header">
                <h4>Layouts</h4>
                <button
                    className="btn btn-sm btn-primary"
                    onClick={() => setShowCreate(!showCreate)}
                    title="New layout"
                >
                    <i className="fa fa-plus" />
                </button>
            </div>

            {/* Target model selector */}
            <div className="o_layout_manager_model">
                <label>Target Model</label>
                <select
                    className="form-select form-select-sm"
                    value={targetModel}
                    onChange={(e) => onModelChange(e.target.value)}
                >
                    <option value="">-- Select model --</option>
                    {models.map((m) => (
                        <option key={m.model} value={m.model}>
                            {m.name} ({m.model})
                        </option>
                    ))}
                </select>
            </div>

            {/* Create new layout form */}
            {showCreate && (
                <div className="o_layout_manager_create">
                    <input
                        type="text"
                        className="form-control form-control-sm"
                        placeholder="Layout name"
                        value={newName}
                        onChange={(e) => setNewName(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && handleCreate()}
                    />
                    <button
                        className="btn btn-sm btn-success mt-1"
                        onClick={handleCreate}
                        disabled={!newName.trim() || !targetModel}
                    >
                        Create
                    </button>
                </div>
            )}

            {/* Layout list */}
            <div className="o_layout_manager_list">
                {layouts.map((layout) => (
                    <div
                        key={layout.id}
                        className={`o_layout_manager_item ${
                            currentLayout?.id === layout.id
                                ? "o_layout_manager_item_active"
                                : ""
                        }`}
                        onClick={() => onSelectLayout(layout.id)}
                    >
                        <div className="o_layout_item_info">
                            <span className="o_layout_item_name">{layout.name}</span>
                            <span className="o_layout_item_meta text-muted">
                                v{layout.version} | {layout.element_count} elements
                            </span>
                        </div>
                        <button
                            className="btn btn-sm btn-link text-danger p-0"
                            onClick={(e) => handleDelete(e, layout.id)}
                            title="Delete layout"
                        >
                            <i className="fa fa-trash" />
                        </button>
                    </div>
                ))}
                {layouts.length === 0 && (
                    <p className="text-muted text-center p-2 small">No layouts yet</p>
                )}
            </div>
        </div>
    );
}

function defaultRpc(url, params = {}) {
    return fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({jsonrpc: "2.0", method: "call", params, id: Date.now()}),
    })
        .then((r) => r.json())
        .then((d) => d.result);
}
