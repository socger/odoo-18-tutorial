import {test, expect} from "@playwright/test";

/**
 * E2E tests for the Visual Report Designer.
 *
 * All Odoo backend API calls are intercepted and mocked so the tests
 * run without a live Odoo instance.  The Vite dev server is started
 * automatically by the Playwright webServer config.
 */

// ── Mock data ──────────────────────────────────────────────────────────────
const MOCK_MODELS = [
    {model: "res.partner", name: "Contact"},
    {model: "sale.order", name: "Sales Order"},
];

const MOCK_FIELDS_PARTNER = [
    {name: "id", type: "integer", string: "ID", icon: "fa-hashtag"},
    {name: "name", type: "char", string: "Name", icon: "fa-font"},
    {name: "email", type: "char", string: "Email", icon: "fa-envelope"},
    {name: "phone", type: "char", string: "Phone", icon: "fa-phone"},
    {
        name: "country_id",
        type: "many2one",
        string: "Country",
        icon: "fa-globe",
        relation: "res.country",
    },
];

const MOCK_LAYOUTS = [
    {
        id: 1,
        name: "Partner Report",
        target_model: "res.partner",
        state: "draft",
        version: 1,
        element_count: 3,
    },
];

// ── Helpers ────────────────────────────────────────────────────────────────

/**
 * Intercept and mock all /api/report-designer/* calls.
 *
 * The frontend defaultRpc returns data.result, and each api.jsx function
 * destructures a specific key from that result object (e.g. result.models).
 * So the mock must return {jsonrpc, id, result: {models: [...]}} etc.
 */
async function mockApi(page) {
    await page.route("**/api/report-designer/**", async (route) => {
        const url = route.request().url();
        const method = route.request().method();

        // Models list → api.jsx expects result.models
        if (url.endsWith("/models")) {
            await route.fulfill({
                json: {
                    jsonrpc: "2.0",
                    id: 1,
                    result: {models: MOCK_MODELS},
                },
            });
            return;
        }

        // Fields for a specific model → api.jsx expects result.fields
        if (url.includes("/fields/") && !url.includes("/related")) {
            await route.fulfill({
                json: {
                    jsonrpc: "2.0",
                    id: 1,
                    result: {fields: MOCK_FIELDS_PARTNER},
                },
            });
            return;
        }

        // Layouts list → api.jsx expects result.layouts
        if (url.endsWith("/layouts") && method === "POST") {
            await route.fulfill({
                json: {
                    jsonrpc: "2.0",
                    id: 1,
                    result: {layouts: MOCK_LAYOUTS},
                },
            });
            return;
        }

        // Default: empty success for everything else
        await route.fulfill({
            json: {jsonrpc: "2.0", id: 1, result: {}},
        });
    });
}

// ── Tests ──────────────────────────────────────────────────────────────────

test.describe("Report Designer — App Loading", () => {
    test("loads the app and shows the toolbar", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        // The toolbar should render
        const toolbar = page.locator(".o_report_designer_toolbar");
        await expect(toolbar).toBeVisible({timeout: 10_000});
    });

    test("shows the model selector dropdown", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        // The model selector is inside .o_layout_manager_model
        const select = page.locator(".o_layout_manager_model select");
        await expect(select).toBeVisible({timeout: 10_000});

        // Wait for models to load (placeholder + 2 models)
        await expect(select.locator("option")).toHaveCount(MOCK_MODELS.length + 1, {
            timeout: 10_000,
        });
    });

    test("shows the field picker sidebar", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        const sidebar = page.locator(".o_field_picker");
        await expect(sidebar).toBeVisible({timeout: 10_000});
    });

    test("shows the canvas area", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        const canvas = page.locator(".o_report_canvas_wrapper");
        await expect(canvas).toBeVisible({timeout: 10_000});
    });

    test("shows the properties panel", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        const panel = page.locator(".o_properties_panel");
        await expect(panel).toBeVisible({timeout: 10_000});
    });
});

test.describe("Report Designer — Model Selection", () => {
    test("selecting a model loads its fields in the picker", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        // Select res.partner model
        const select = page.locator(".o_layout_manager_model select");
        await expect(select).toBeVisible({timeout: 10_000});
        await select.selectOption("res.partner");

        // Wait for fields to appear in the field picker
        await expect(page.locator(".o_field_picker").getByText("Name")).toBeVisible({
            timeout: 10_000,
        });
    });
});

test.describe("Report Designer — Undo/Redo Buttons", () => {
    test("undo and redo buttons are visible in toolbar", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        const toolbar = page.locator(".o_report_designer_toolbar");
        await expect(toolbar).toBeVisible({timeout: 10_000});

        // Undo button
        await expect(toolbar.locator('[title*="Undo"]')).toBeVisible();
        // Redo button
        await expect(toolbar.locator('[title*="Redo"]')).toBeVisible();
    });
});

test.describe("Report Designer — Save Button", () => {
    test("save button exists in toolbar", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        const toolbar = page.locator(".o_report_designer_toolbar");
        await expect(toolbar).toBeVisible({timeout: 10_000});

        // Save button should exist
        const saveBtn = toolbar.locator('[title="Save layout"]');
        await expect(saveBtn).toBeVisible();
    });
});

test.describe("Report Designer — Layout Manager", () => {
    test("layout list shows saved layouts", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        // LayoutManager should render
        const layoutManager = page.locator(".o_layout_manager");
        await expect(layoutManager).toBeVisible({timeout: 10_000});

        // Should show "Partner Report" from mock data
        await expect(layoutManager.getByText("Partner Report")).toBeVisible({
            timeout: 10_000,
        });
    });
});

test.describe("Report Designer — Keyboard Shortcuts", () => {
    test("Ctrl+Z does not crash the app", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        await page.waitForSelector(".o_report_canvas_wrapper", {timeout: 10_000});

        // Press Ctrl+Z — should not throw any errors
        const errors = [];
        page.on("pageerror", (err) => errors.push(err.message));
        await page.keyboard.press("Control+z");
        await page.waitForTimeout(500);

        expect(errors).toHaveLength(0);
    });

    test("Escape does not crash the app", async ({page}) => {
        await mockApi(page);
        await page.goto("/");

        await page.waitForSelector(".o_report_canvas_wrapper", {timeout: 10_000});

        const errors = [];
        page.on("pageerror", (err) => errors.push(err.message));
        await page.keyboard.press("Escape");
        await page.waitForTimeout(500);

        expect(errors).toHaveLength(0);
    });
});

test.describe("Report Designer — No Console Errors", () => {
    test("app loads without JavaScript errors", async ({page}) => {
        const errors = [];
        page.on("pageerror", (err) => errors.push(err.message));

        await mockApi(page);
        await page.goto("/");
        await page.waitForTimeout(3000);

        // Filter out expected warnings
        const critical = errors.filter(
            (e) => !e.includes("DevTools") && !e.includes("Warning:")
        );
        expect(critical).toHaveLength(0);
    });
});
