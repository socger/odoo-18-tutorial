{
    "name": "Visual Report Designer",
    "summary": "Drag & drop visual report builder for Odoo with React frontend",
    "version": "18.0.1.2.0",
    "category": "Technical",
    "website": "https://cuidamet.duckdns.org/",
    "author": "Galvintec, SocGer",
    "license": "LGPL-3",
    "depends": ["base", "mail", "web"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/paper_formats.xml",
        "views/report_layout_views.xml",
        "views/report_designer_action_views.xml",
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "socger_report_designer/static/src/js/report_designer_action.esm.js",
            "socger_report_designer/static/src/xml/report_designer_action.xml",
            "socger_report_designer/static/src/scss/report_designer.scss",
            "socger_report_designer/static/dist/assets/style.css",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}
