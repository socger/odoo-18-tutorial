import {defineConfig} from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
    plugins: [react()],
    root: ".",
    build: {
        outDir: "../../dist",
        emptyOutDir: true,
        rollupOptions: {
            input: path.resolve(__dirname, "index.html"),
            output: {
                entryFileNames: "report_designer.js",
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
    define: {
        "process.env.NODE_ENV": JSON.stringify("production"),
    },
});
