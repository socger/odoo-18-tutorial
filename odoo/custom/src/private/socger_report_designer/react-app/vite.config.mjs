import {defineConfig} from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig(({mode}) => ({
    plugins: [react()],
    root: ".",
    build: {
        outDir: "../static/dist",
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
