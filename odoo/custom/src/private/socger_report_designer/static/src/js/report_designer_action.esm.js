/** @odoo-module **/

import {Component, onMounted, onWillUnmount, useRef, useState} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {rpc} from "@web/core/network/rpc";

/**
 * OWL wrapper that loads the React Report Designer inside Odoo.
 * Registered as a client action so it can be opened from:
 *   - The "Open Designer" button on the report.designer.layout form
 *   - Menu: Reporting > Report Designer
 *
 * The React app is built separately (npm run build inside react-app/)
 * and loaded as an external script. The OWL component mounts the React app
 * into a container div and bridges Odoo RPC calls to the React API client.
 */
export class ReportDesignerAction extends Component {
    static template = "socger_report_designer.ReportDesignerAction";
    static props = {
        action: {type: Object, optional: true},
        actionId: {type: Number, optional: true},
        context: {type: Object, optional: true},
    };

    setup() {
        this.containerRef = useRef("react-container");
        this.notification = useService("notification");
        this.state = useState({
            loaded: false,
            error: null,
        });
        this.reactApp = null;

        onMounted(() => {
            this.loadReactApp();
        });

        onWillUnmount(() => {
            this.unmountReactApp();
        });
    }

    /**
     * Load the React bundle script and mount the app.
     */
    async loadReactApp() {
        try {
            // Check if React app is already loaded
            if (window.ReportDesigner) {
                this.mountReactApp();
                return;
            }

            // Load the React bundle dynamically
            await this.loadScript(
                "/socger_report_designer/static/dist/report_designer.js"
            );

            // Wait a tick for script execution
            await new Promise((resolve) => setTimeout(resolve, 50));

            if (!window.ReportDesigner) {
                throw new Error("ReportDesigner global not found after loading script");
            }

            this.mountReactApp();
        } catch (err) {
            console.error("Failed to load Report Designer:", err);
            this.state.error = err.message || "Failed to load Report Designer";
        }
    }

    /**
     * Mount the React app into the container div.
     */
    mountReactApp() {
        const container = this.containerRef.el;
        if (!container) return;

        const layoutId =
            this.props.context?.active_id ||
            this.props.action?.context?.active_id ||
            null;

        // Create an RPC bridge function for the React app
        const rpcBridge = async (url, params = {}) => {
            try {
                return await rpc(url, params);
            } catch (err) {
                console.error("RPC error:", url, err);
                throw err;
            }
        };

        this.reactApp = window.ReportDesigner.mount(container, {
            layoutId,
            backendRpc: rpcBridge,
        });

        this.state.loaded = true;
    }

    /**
     * Unmount the React app.
     */
    unmountReactApp() {
        if (this.reactApp) {
            try {
                this.reactApp.unmount();
            } catch {
                // Ignore
            }
            this.reactApp = null;
        }
    }

    /**
     * Dynamically load a JavaScript file.
     */
    loadScript(src) {
        return new Promise((resolve, reject) => {
            // Check if already loaded
            const existing = document.querySelector(`script[src="${src}"]`);
            if (existing) {
                resolve();
                return;
            }
            const script = document.createElement("script");
            script.src = src;
            script.onload = resolve;
            script.onerror = () => reject(new Error(`Failed to load script: ${src}`));
            document.head.appendChild(script);
        });
    }
}

// Register as a client action
registry
    .category("actions")
    .add("socger_report_designer.ReportDesignerAction", ReportDesignerAction);
