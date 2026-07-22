import {defineConfig, devices} from "@playwright/test";

/**
 * Playwright E2E test configuration for socger_report_designer.
 *
 * Tests run against the Vite dev server (started automatically by Playwright).
 * For CI/headless environments the server is launched via webServer.
 * For local dev, run `npm run dev` first and then `npx playwright test`.
 */
export default defineConfig({
    testDir: "e2e",
    fullyParallel: false,
    forbidOnly: !!process.env.CI,
    retries: process.env.CI ? 2 : 0,
    workers: 1,
    reporter: "list",
    timeout: 60_000,
    use: {
        baseURL: "http://localhost:5173",
        trace: "on-first-retry",
        screenshot: "only-on-failure",
    },
    projects: [
        {
            name: "chromium",
            use: {...devices["Desktop Chrome"]},
        },
    ],
    webServer: {
        command: "npm run dev -- --port 5173",
        port: 5173,
        reuseExistingServer: !process.env.CI,
        timeout: 30_000,
    },
});
