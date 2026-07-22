import {defineConfig} from "vite";
import react from "@vitejs/plugin-react";
import path from "path";
import fs from "fs";

/**
 * Plugin that writes a `version.json` file with the hashed entry filename
 * so the Odoo OWL wrapper can load the latest bundle (cache-busting).
 */
function writeVersionManifest() {
    return {
        name: "write-version-manifest",
        writeBundle(options, bundle) {
            // Find the entry chunk (report_designer.js or hashed variant)
            const entryFile = Object.keys(bundle).find(
                (f) => bundle[f].isEntry && f.endsWith(".js")
            );
            if (entryFile) {
                const manifest = {
                    version: Date.now().toString(),
                    entry: entryFile,
                };
                fs.writeFileSync(
                    path.join(options.dir, "version.json"),
                    JSON.stringify(manifest, null, 2)
                );
            }
        },
    };
}

export default defineConfig(({mode}) => ({
    plugins: [react(), writeVersionManifest()],
    root: ".",
    build: {
        outDir: "../static/dist",
        emptyOutDir: true,
        rollupOptions: {
            input: path.resolve(__dirname, "index.html"),
            output: {
                entryFileNames: "report_designer.[hash].js",
                chunkFileNames: "chunks/[name].js",
                assetFileNames: "assets/[name].[ext]",
                format: "iife",
                name: "ReportDesigner",
                globals: {},
            },
        },
        cssCodeSplit: false,
        sourcemap: false,
    },
    define:
        mode === "test"
            ? {"process.env.NODE_ENV": JSON.stringify("test")}
            : {"process.env.NODE_ENV": JSON.stringify("production")},
    test: {
        environment: "jsdom",
        globals: true,
        setupFiles: ["./test/setup.js"],
        include: ["src/**/*.test.{js,jsx}"],
    },
}));
