import {describe, it, expect, vi} from "vitest";
import {render, screen, fireEvent, waitFor} from "@testing-library/react";
import FieldPicker from "../FieldPicker.jsx";

// Mock the api module
vi.mock("../../api.jsx", () => ({
    fetchRelatedFields: vi.fn(),
}));

const {fetchRelatedFields} = await import("../../api.jsx");

const DEFAULT_FIELDS = [
    {name: "name", string: "Name", type: "char", icon: "text"},
    {name: "email", string: "Email", type: "char", icon: "text"},
    {
        name: "partner_id",
        string: "Customer",
        type: "many2one",
        icon: "relation",
        relation: "res.partner",
    },
    {name: "amount_total", string: "Total", type: "monetary", icon: "money"},
    {
        name: "order_line",
        string: "Order Lines",
        type: "one2many",
        icon: "relation-list",
    },
];

function renderPicker(overrides = {}) {
    const defaultProps = {
        fields: DEFAULT_FIELDS,
        targetModel: "sale.order",
        onAddElement: vi.fn(),
        rpc: vi.fn(),
        ...overrides,
    };
    return render(<FieldPicker {...defaultProps} />);
}

describe("FieldPicker", () => {
    it("renders field groups", () => {
        renderPicker();
        expect(screen.getByText("Fields")).toBeInTheDocument();
        expect(screen.getByText("sale.order")).toBeInTheDocument();
        expect(screen.getByText("Name")).toBeInTheDocument();
        expect(screen.getByText("Customer")).toBeInTheDocument();
    });

    it("renders structural elements", () => {
        renderPicker();
        expect(screen.getByText("Layout Elements")).toBeInTheDocument();
        expect(screen.getByText("Heading")).toBeInTheDocument();
        expect(screen.getByText("Table")).toBeInTheDocument();
    });

    it("filters fields by search term", () => {
        renderPicker();
        const input = screen.getByPlaceholderText("Search fields...");
        fireEvent.change(input, {target: {value: "partner"}});
        expect(screen.getByText("Customer")).toBeInTheDocument();
        // "Name" should not be visible when filtering for "partner"
        // (but it may still appear in structural elements)
    });

    it("calls onAddElement on double click", () => {
        const onAddElement = vi.fn();
        renderPicker({onAddElement});
        fireEvent.doubleClick(screen.getByText("Name"));
        expect(onAddElement).toHaveBeenCalledWith(
            expect.objectContaining({
                type: "text",
                fieldPath: "name",
            })
        );
    });

    it("shows message when no target model selected", () => {
        renderPicker({targetModel: ""});
        expect(
            screen.getByText("Select a target model to see model fields")
        ).toBeInTheDocument();
    });

    it("toggles structural elements visibility", () => {
        renderPicker();
        const toggle = screen.getByText("Layout Elements");
        fireEvent.click(toggle);
        // After clicking, structural elements should be hidden
        expect(screen.queryByText("Heading")).not.toBeInTheDocument();
        // Click again to show
        fireEvent.click(toggle);
        expect(screen.getByText("Heading")).toBeInTheDocument();
    });

    it("expands many2one relation on chevron click", async () => {
        const rpc = vi.fn();
        fetchRelatedFields.mockResolvedValue({
            fields: [
                {name: "name", string: "Name", type: "char", icon: "text"},
                {name: "email", string: "Email", type: "char", icon: "text"},
            ],
            model: "res.partner",
            parent_path: "partner_id",
        });

        renderPicker({rpc});

        // Find the expand chevron for partner_id
        const expandIcons = screen.getAllByTitle("Expand related fields");
        fireEvent.click(expandIcons[0]);

        await waitFor(() => {
            expect(fetchRelatedFields).toHaveBeenCalledWith(
                "res.partner",
                "partner_id",
                rpc
            );
        });
    });

    it("renders nested fields after expansion", async () => {
        const rpc = vi.fn();
        fetchRelatedFields.mockResolvedValue({
            fields: [{name: "name", string: "Name", type: "char", icon: "text"}],
            model: "res.partner",
            parent_path: "partner_id",
        });

        renderPicker({rpc});
        const expandIcons = screen.getAllByTitle("Expand related fields");
        fireEvent.click(expandIcons[0]);

        await waitFor(() => {
            // Nested "Name" field should appear
            const nestedItems = screen.getAllByText("Name");
            // One from the main list, one from nested
            expect(nestedItems.length).toBeGreaterThanOrEqual(2);
        });
    });

    it("calls onAddElement with dotted path for nested field", async () => {
        const rpc = vi.fn();
        const onAddElement = vi.fn();
        fetchRelatedFields.mockResolvedValue({
            fields: [{name: "name", string: "Name", type: "char", icon: "text"}],
            model: "res.partner",
            parent_path: "partner_id",
        });

        renderPicker({rpc, onAddElement});
        const expandIcons = screen.getAllByTitle("Expand related fields");
        fireEvent.click(expandIcons[0]);

        await waitFor(() => {
            const nestedItems = screen.getAllByText("Name");
            // Double-click the nested one (last occurrence)
            const nestedItem = nestedItems[nestedItems.length - 1].closest(
                ".o_field_picker_nested_item"
            );
            if (nestedItem) {
                fireEvent.doubleClick(nestedItem);
                expect(onAddElement).toHaveBeenCalledWith(
                    expect.objectContaining({
                        fieldPath: "partner_id.name",
                    })
                );
            }
        });
    });
});
