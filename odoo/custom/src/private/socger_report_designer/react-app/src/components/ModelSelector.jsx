import React from "react";

/**
 * ModelSelector - dropdown for selecting the target Odoo model.
 *
 * Props:
 *   models       - Array of {model, name} objects
 *   targetModel  - Currently selected model name (string)
 *   onModelChange - Callback when model selection changes
 */
export default function ModelSelector({models, targetModel, onModelChange}) {
    return (
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
    );
}
