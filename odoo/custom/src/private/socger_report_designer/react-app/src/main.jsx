import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./styles/app.css";

/**
 * Bootstrap the React Report Designer.
 * When built as IIFE, this attaches `ReportDesigner.mount(el, props)`
 * to the global scope so the OWL wrapper can instantiate it.
 */
function mount(container, props = {}) {
    const root = ReactDOM.createRoot(container);
    root.render(
        <React.StrictMode>
            <App {...props} />
        </React.StrictMode>
    );
    return {
        unmount() {
            root.unmount();
        },
    };
}

function unmount(container) {
    const root = container?._reactRoot;
    if (root) {
        root.unmount();
    }
}

// Auto-mount in standalone dev mode (Vite dev server).
// The index.html has a #report-designer-root div; when running outside
// the OWL wrapper (standalone Vite), we mount automatically.
const autoEl =
    typeof document !== "undefined" && document.getElementById("report-designer-root");
if (autoEl && autoEl.childNodes.length === 0) {
    mount(autoEl);
}

// Expose to global scope for OWL wrapper to call
if (typeof window !== "undefined") {
    window.ReportDesigner = {mount, unmount};
}

export {mount, unmount};
