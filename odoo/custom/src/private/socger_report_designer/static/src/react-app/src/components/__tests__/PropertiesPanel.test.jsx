import {describe, it, expect, vi} from "vitest";
import {render, screen, fireEvent} from "@testing-library/react";
import PropertiesPanel from "../PropertiesPanel.jsx";

const TEXT_ELEMENT = {
    id: "el_001",
    type: "text",
    fieldPath: "name",
    content: "Hello",
    style: {fontSize: 12, color: "#000000"},
    position: {x: 10, y: 20},
};

const HEADING_ELEMENT = {
    id: "el_002",
    type: "heading",
    content: "Title",
    style: {level: 2},
};

const TABLE_ELEMENT = {
    id: "el_003",
    type: "table",
    dataSource: "order_line",
    columns: [{header: "Name", fieldPath: "name"}],
};

const DEFAULT_FIELDS = [
    {name: "name", string: "Name", type: "char", icon: "text"},
    {name: "order_line", string: "Lines", type: "one2many", icon: "relation-list"},
];

function renderPanel(overrides = {}) {
    const defaultProps = {
        element: TEXT_ELEMENT,
        fields: DEFAULT_FIELDS,
        rpc: vi.fn(),
        onUpdateElement: vi.fn(),
        onRemoveElement: vi.fn(),
        ...overrides,
    };
    return render(<PropertiesPanel {...defaultProps} />);
}

describe("PropertiesPanel", () => {
    it("shows empty state when no element selected", () => {
        renderPanel({element: null});
        expect(screen.getByText("Properties")).toBeInTheDocument();
        expect(
            screen.getByText("Select an element to edit its properties")
        ).toBeInTheDocument();
    });

    it("renders element type selector", () => {
        renderPanel();
        expect(screen.getByText("Type")).toBeInTheDocument();
        expect(screen.getByDisplayValue("Text / Field")).toBeInTheDocument();
    });

    it("shows field binding dropdown for text elements", () => {
        renderPanel();
        expect(screen.getByText("Bind to Field")).toBeInTheDocument();
    });

    it("shows field format dropdown when field is bound", () => {
        renderPanel();
        expect(screen.getByText(/Field Format/)).toBeInTheDocument();
    });

    it("calls onUpdateElement when field changes", () => {
        const onUpdateElement = vi.fn();
        renderPanel({onUpdateElement});
        // The select is after "Bind to Field" label
        const select = screen
            .getAllByRole("combobox")
            .find(
                (el) =>
                    el.querySelector('option[value=""]')?.textContent ===
                    "None (static)"
            );
        expect(select).toBeTruthy();
        fireEvent.change(select, {target: {value: "order_line"}});
        expect(onUpdateElement).toHaveBeenCalledWith(
            "el_001",
            expect.objectContaining({fieldPath: "order_line"})
        );
    });

    it("shows position fields when position exists", () => {
        renderPanel();
        expect(screen.getByText("Position")).toBeInTheDocument();
        expect(screen.getByText("X (px)")).toBeInTheDocument();
        expect(screen.getByText("Y (px)")).toBeInTheDocument();
        expect(screen.getByText("Width (px)")).toBeInTheDocument();
        expect(screen.getByText("Height (px)")).toBeInTheDocument();
    });

    it("shows typography controls", () => {
        renderPanel();
        expect(screen.getByText("Font Size (pt)")).toBeInTheDocument();
        expect(screen.getByText("Font Weight")).toBeInTheDocument();
        expect(screen.getByText("Color")).toBeInTheDocument();
    });

    it("calls onRemoveElement on delete button click", () => {
        const onRemoveElement = vi.fn();
        renderPanel({onRemoveElement});
        const deleteBtn = screen.getByText("Delete Element");
        fireEvent.click(deleteBtn);
        expect(onRemoveElement).toHaveBeenCalledWith("el_001");
    });

    it("shows table-specific controls for table elements", () => {
        renderPanel({element: TABLE_ELEMENT});
        expect(screen.getByText(/Data Source/)).toBeInTheDocument();
    });

    it("shows condition field (t-if)", () => {
        renderPanel();
        expect(screen.getByText(/Condition/)).toBeInTheDocument();
    });

    it("shows heading level control for heading elements", () => {
        renderPanel({element: HEADING_ELEMENT});
        expect(screen.getByText("Level")).toBeInTheDocument();
    });
});
