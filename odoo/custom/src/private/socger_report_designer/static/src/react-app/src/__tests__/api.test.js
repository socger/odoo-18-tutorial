import {describe, it, expect, vi, beforeEach} from "vitest";
import {
    fetchModels,
    fetchFields,
    fetchRelatedFields,
    fetchLayouts,
    saveLayout,
    createLayout,
    deleteLayout,
    publishLayout,
    unpublishLayout,
    generateXml,
    fetchRecords,
    previewLayoutHtml,
    previewLayoutPdf,
} from "../api.jsx";

describe("API client", () => {
    let rpc;

    beforeEach(() => {
        rpc = vi.fn();
    });

    it("fetchModels calls correct endpoint", async () => {
        rpc.mockResolvedValue({models: [{id: 1, model: "sale.order"}]});
        const result = await fetchModels(rpc);
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/models", {});
        expect(result).toEqual([{id: 1, model: "sale.order"}]);
    });

    it("fetchModels handles empty response", async () => {
        rpc.mockResolvedValue({});
        const result = await fetchModels(rpc);
        expect(result).toEqual([]);
    });

    it("fetchFields calls correct endpoint", async () => {
        rpc.mockResolvedValue({fields: [{name: "name", type: "char"}]});
        const result = await fetchFields("sale.order", rpc);
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/fields/sale.order", {});
        expect(result).toEqual([{name: "name", type: "char"}]);
    });

    it("fetchRelatedFields calls correct endpoint", async () => {
        rpc.mockResolvedValue({
            fields: [{name: "name", type: "char"}],
            model: "res.partner",
            parent_path: "partner_id",
        });
        const result = await fetchRelatedFields("res.partner", "partner_id", rpc);
        expect(rpc).toHaveBeenCalledWith(
            "/api/report-designer/fields/res.partner/related",
            {parent_path: "partner_id"}
        );
        expect(result.model).toBe("res.partner");
        expect(result.parent_path).toBe("partner_id");
    });

    it("fetchLayouts calls correct endpoint", async () => {
        rpc.mockResolvedValue({layouts: [{id: 1, name: "Test"}]});
        const result = await fetchLayouts(rpc);
        expect(result).toEqual([{id: 1, name: "Test"}]);
    });

    it("saveLayout sends layout_json and name", async () => {
        rpc.mockResolvedValue({success: true});
        const result = await saveLayout(1, '{"elements":[]}', "Test", rpc);
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/layouts/1/save", {
            layout_json: '{"elements":[]}',
            name: "Test",
        });
        expect(result).toEqual({success: true});
    });

    it("createLayout sends name and target_model", async () => {
        rpc.mockResolvedValue({id: 1, name: "New"});
        const result = await createLayout("New", "sale.order", rpc);
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/layouts/create", {
            name: "New",
            target_model: "sale.order",
        });
        expect(result.id).toBe(1);
    });

    it("deleteLayout calls correct endpoint", async () => {
        rpc.mockResolvedValue({success: true});
        await deleteLayout(1, rpc);
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/layouts/1/delete", {});
    });

    it("publishLayout calls correct endpoint", async () => {
        rpc.mockResolvedValue({success: true, state: "published"});
        const result = await publishLayout(1, rpc);
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/layouts/1/publish", {});
        expect(result.state).toBe("published");
    });

    it("unpublishLayout calls correct endpoint", async () => {
        rpc.mockResolvedValue({success: true, state: "draft"});
        const result = await unpublishLayout(1, rpc);
        expect(rpc).toHaveBeenCalledWith(
            "/api/report-designer/layouts/1/unpublish",
            {}
        );
        expect(result.state).toBe("draft");
    });

    it("generateXml sends layout_json", async () => {
        rpc.mockResolvedValue({xml: "<template/>"});
        const result = await generateXml({elements: []}, rpc);
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/generate-xml", {
            layout_json: {elements: []},
        });
        expect(result.xml).toBe("<template/>");
    });

    it("fetchRecords calls correct endpoint with limit", async () => {
        rpc.mockResolvedValue({records: [{id: 1, display_name: "Record 1"}]});
        const result = await fetchRecords("sale.order", rpc, 10);
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/records/sale.order", {
            limit: 10,
        });
        expect(result).toEqual([{id: 1, display_name: "Record 1"}]);
    });

    it("previewLayoutHtml sends correct params", async () => {
        rpc.mockResolvedValue({html: "<div>preview</div>", record_count: 1});
        const result = await previewLayoutHtml(
            '{"elements":[]}',
            "sale.order",
            rpc,
            42
        );
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/preview/html", {
            layout_json: '{"elements":[]}',
            target_model: "sale.order",
            format: "html",
            record_id: 42,
        });
        expect(result.html).toContain("preview");
    });

    it("previewLayoutPdf sends correct params", async () => {
        rpc.mockResolvedValue({pdf_base64: "abc123", record_count: 1});
        const result = await previewLayoutPdf(
            '{"elements":[]}',
            "sale.order",
            rpc,
            null
        );
        expect(rpc).toHaveBeenCalledWith("/api/report-designer/preview/live", {
            layout_json: '{"elements":[]}',
            target_model: "sale.order",
            format: "pdf",
        });
        expect(result.pdf_base64).toBe("abc123");
    });

    it("previewLayoutPdf omits record_id when null", async () => {
        rpc.mockResolvedValue({pdf_base64: "abc"});
        await previewLayoutPdf("{}", "sale.order", rpc, null);
        const params = rpc.mock.calls[0][1];
        expect(params).not.toHaveProperty("record_id");
    });
});
