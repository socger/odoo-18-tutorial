# New session - 2026-07-21T16:23:12.412Z

**Session ID:** ses_07a82f4e3ffegXGEHJVUSodVSS **Created:** 7/21/2026, 6:23:12 PM
**Updated:** 7/21/2026, 7:38:08 PM

---

## User

Me han pedido que investigue como crear reports en Odoo y no se como hacerlo. Puedes
enseñarme o decirme como hacerlo. O mejor buscarme vídeos que me enseñen como hacerlo

---

## Assistant (Odoo-Dev · Nemotron 3.5 Content Safety (free) · 1.0s)

---

## User

Me han pedido que investigue como crear reports en Odoo y no se como hacerlo. Puedes
enseñarme o decirme como hacerlo. O mejor buscarme vídeos que me enseñen como hacerlo

---

## Assistant (Odoo-Dev · Big Pickle · 18.2s)

_Thinking:_

El usuario quiere aprender sobre cómo crear reports en Odoo. Esto es una tarea de
investigación/aprendizaje sobre Odoo development, por lo que debo:

1. Cargar el skill `odoo-development-skill` (regla absoluta antes de cualquier cosa
   relacionada con Odoo development)
2. Investigar patrones de reports en el skill
3. Buscar vídeos educativos en la web

Voy a empezar cargando el skill y buscando vídeos en paralelo.

Voy a cargar el skill de desarrollo Odoo para darte la información más precisa sobre
reports, y simultáneamente buscar vídeos tutoriales para ti.

**Tool: skill**

**Input:**

```json
{
  "name": "odoo-development-skill"
}
```

**Output:**

```
<skill_content name="odoo-development-skill">
# Skill: odoo-development-skill

# Odoo Development Skill (Universal)

You are a Senior Odoo Architect expert in Python and JavaScript, following strict
development standards. This skill equips you with comprehensive knowledge of Odoo
versions 14 through 19, following Odoo Community Association (OCA) conventions.

## ⚠️ CRITICAL WORKFLOW - EXECUTE IN ORDER

### 1. DETECT ODOO VERSION

**Identify target version BEFORE applying any pattern:** Read `__manifest__.py` in the
current directory and extract the version (`X.0.Y.Z`). The first number represents the
Odoo version (14, 15, 16, 17, 18, 19).

### 2. DON'T REINVENT THE WHEEL ⚡

**BEFORE developing ANY new functionality, perform an exhaustive search in this order:**

#### a) Odoo Official Source (Community)

Search locally first, then verify against the official GitHub:

- Local: `<YOUR_ODOO_SRC_PATH>/addons/`
- GitHub (by version):
  - v14: https://github.com/odoo/odoo/tree/14.0/addons
  - v15: https://github.com/odoo/odoo/tree/15.0/addons
  - v16: https://github.com/odoo/odoo/tree/16.0/addons
  - v17: https://github.com/odoo/odoo/tree/17.0/addons
  - v18: https://github.com/odoo/odoo/tree/18.0/addons
  - v19: https://github.com/odoo/odoo/tree/19.0/addons

#### b) Odoo Enterprise

- Local: `<YOUR_ENTERPRISE_SRC_PATH>/`
- GitHub: https://github.com/odoo/enterprise (requires access)

#### c) OCA (Odoo Community Association) — CRITICAL

Perform an **exhaustive search** across OCA repositories at https://github.com/OCA to
find if a module or similar functionality already exists:

- Browse the OCA organization: https://github.com/orgs/OCA/repositories
- Search by keyword: `https://github.com/OCA?q=<KEYWORD>&type=repositories`
- Key OCA repositories by domain:
  - **Accounting:** https://github.com/OCA/account-financial-reporting,
    https://github.com/OCA/account-financial-tools
  - **Stock/Warehouse:** https://github.com/OCA/stock-logistics-workflow,
    https://github.com/OCA/stock-logistics-warehouse
  - **Sale:** https://github.com/OCA/sale-workflow
  - **Purchase:** https://github.com/OCA/purchase-workflow
  - **HR:** https://github.com/OCA/hr
  - **POS:** https://github.com/OCA/pos
  - **Website:** https://github.com/OCA/website
  - **Server Tools:** https://github.com/OCA/server-tools,
    https://github.com/OCA/server-ux
  - **Reporting:** https://github.com/OCA/reporting-engine
  - **Connector:** https://github.com/OCA/connector
  - **Localizations:** https://github.com/OCA/l10n-{country_code} (e.g., `l10n-spain`,
    `l10n-brazil`)

#### d) Decision after search

- **If found in Odoo core:** Read implementation, inherit/extend.
- **If found in OCA:** Read the module, check its version compatibility, and depend on
  it or use it as a reference pattern.
- **If partially found:** Inherit and extend the closest module.
- **Only develop from scratch if** no similar functionality exists anywhere.

### 3. APPLY STRICT DEVELOPMENT STANDARDS

- **Language:** Communication with the user in **SPANISH** (or user's preferred
  language). Code, variables, and docstrings in **ENGLISH**. `README.rst` and
  `index.html` in the user's preferred language.
- **Python:** PEP8, SOLID, DRY, KISS. No `# -*- coding: utf-8 -*-`. Use `super()`.
- **JavaScript/OWL:** Modern ES6+, correct OWL version (v15: 1.x, v16-18: 2.x, v19:
  3.x).
- **XML/Views:** Version-specific visibility (`attrs` vs `invisible=...`). Always verify
  XML IDs before inheriting. Never replace.
- **Security:** Always create `ir.model.access.csv` for new models.

### 4. AVAILABLE AGENTS (WORKFLOWS)

When requested, execute the following specialized workflows:

- **Code Review:** Read `agents/odoo-code-reviewer.md` to perform comprehensive code
  quality and security audits.
- **Upgrade Analysis:** Read `agents/odoo-upgrade-analyzer.md` to analyze migration
  compatibility between versions.
- **Context Gathering:** Read `agents/odoo-context-gatherer.md` before generating
  complex code.
- **Skill Discovery:** Read `agents/odoo-skill-finder.md` to navigate the pattern
  library.

## 📚 PATTERN DISCOVERY INDEX

When the user asks for a specific functionality, search the `skills/` directory.

| Intent / Keywords                 | Pattern File                              |
| --------------------------------- | ----------------------------------------- |
| fields, char, many2one, selection | `skills/field-type-reference.md`          |
| computed, depends, inverse        | `skills/computed-field-patterns.md`       |
| constraint, validation, check     | `skills/constraint-patterns.md`           |
| onchange, dynamic, domain         | `skills/onchange-dynamic-patterns.md`     |
| view, form, tree, kanban, search  | `skills/xml-view-patterns.md`             |
| widget, statusbar, badge, image   | `skills/widget-field-patterns.md`         |
| qweb, template, t-if, t-foreach   | `skills/qweb-template-patterns.md`        |
| action, window, server, client    | `skills/action-patterns.md`               |
| menu, navigation, menuitem        | `skills/menu-navigation-patterns.md`      |
| security, access, rule, group     | `skills/odoo-security-guide.md`           |
| workflow, state, statusbar        | `skills/workflow-state-patterns.md`       |
| wizard, transient, dialog         | `skills/wizard-patterns.md`               |
| report, pdf, print                | `skills/report-patterns.md`               |
| cron, scheduled, automation       | `skills/cron-automation-patterns.md`      |
| controller, http, api, rest       | `skills/controller-api-patterns.md`       |
| mail, email, chatter, activity    | `skills/mail-notification-patterns.md`    |
| multi-company, company            | `skills/multi-company-patterns.md`        |
| inherit, extend, override         | `skills/inheritance-patterns.md`          |
| migration, upgrade, version       | `skills/data-migration-patterns.md`       |
| website, portal, public           | `skills/website-integration-patterns.md`  |
| external, api, webhook, sync      | `skills/external-api-patterns.md`         |
| logging, debug, error             | `skills/logging-debugging-patterns.md`    |
| stock, inventory, warehouse       | `skills/stock-inventory-patterns.md`      |
| account, invoice, journal         | `skills/accounting-patterns.md`           |
| sale, order, quotation, crm       | `skills/sale-crm-patterns.md`             |
| hr, employee, contract            | `skills/hr-employee-patterns.md`          |
| domain, filter, search            | `skills/domain-filter-patterns.md`        |
| sequence, numbering               | `skills/sequence-numbering-patterns.md`   |
| purchase, vendor, procurement     | `skills/purchase-procurement-patterns.md` |
| project, task, timesheet          | `skills/project-task-patterns.md`         |
| context, env, sudo                | `skills/context-environment-patterns.md`  |
| portal, token, access             | `skills/portal-access-patterns.md`        |
| settings, config, parameter       | `skills/config-settings-patterns.md`      |
| translation, i18n, language       | `skills/translation-i18n-patterns.md`     |
| assets, js, css, scss             | `skills/assets-bundling-patterns.md`      |
| variant, attribute, product       | `skills/product-variant-patterns.md`      |
| uom, unit, measure                | `skills/uom-patterns.md`                  |
| lot, serial, batch                | `skills/lot-serial-patterns.md`           |
| tax, fiscal, vat                  | `skills/tax-fiscal-patterns.md`           |
| owl, component, frontend          | `skills/odoo-owl-components.md`           |
| test, unittest, integration       | `skills/odoo-test-patterns.md`            |
| manifest, module, depends         | `skills/odoo-module-generator.md`         |
| version, 14, 15, 16, 17, 18, 19   | `skills/odoo-version-knowledge.md`        |
| attachment, binary, file, image   | `skills/attachment-binary-patterns.md`    |
| dashboard, kpi, analytics, graph  | `skills/dashboard-kpi-patterns.md`        |
| exception, error, validation      | `skills/error-handling-patterns.md`       |
| import, export, csv, excel        | `skills/import-export-patterns.md`        |
| pricelist, price, discount        | `skills/pricelist-pricing-patterns.md`    |
| performance, optimize, index      | `skills/odoo-performance-guide.md`        |
| troubleshooting, debug, fix       | `skills/odoo-troubleshooting-guide.md`    |
| quick, snippet, cheatsheet        | `skills/quick-patterns.md`                |
| editions, community, enterprise   | `skills/odoo-editions.md`                 |
| end-to-end, example, full module  | `skills/end-to-end-examples.md`           |
| template, scaffold, boilerplate   | `skills/common-module-templates.md`       |
| module generation, example        | `skills/module-generation-example.md`     |
| model, abstract, transient        | `skills/odoo-model-patterns.md`           |

### Version-Specific Pattern Files

Many patterns have **version-specific variants** following the naming convention
`skills/{pattern}-{version}.md`. When generating code for a specific Odoo version,
always check if a version-specific file exists:

- **Single version:** `skills/{pattern}-{version}.md` (e.g.,
  `skills/odoo-model-patterns-18.md`)
- **Migration guide:** `skills/{pattern}-{sourceV}-{targetV}.md` (e.g.,
  `skills/odoo-model-patterns-17-18.md`)
- **All versions:** `skills/{pattern}-all.md` (e.g.,
  `skills/odoo-model-patterns-all.md`)

Available version-specific pattern families:

- `odoo-version-knowledge-{14..19}.md` and migration guides `{14-15..18-19}.md`
- `odoo-model-patterns-{14..19}.md` and migration guides
- `odoo-module-generator-{14..19}.md` and migration guides
- `odoo-owl-components-{15..19}.md` and migration guides
- `odoo-security-guide-{14..19}.md` and migration guides

**Rule:** Always read the corresponding pattern file using file reading tools before
generating code. DO NOT guess the syntax if you are unsure.

Base directory for this skill: /home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.

<skill_files>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/agents/odoo-skill-finder.md</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/agents/odoo-context-gatherer.md</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/agents/odoo-code-reviewer.md</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/agents/odoo-upgrade-analyzer.md</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/LICENSE</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/README.md</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/skills/logging-debugging-patterns.md</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/skills/odoo-version-knowledge-17.md</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/skills/assets-bundling-patterns.md</file>
<file>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/skills/constraint-patterns.md</file>
</skill_files>
</skill_content>
```

**Tool: websearch**

**Input:**

```json
{
  "query": "tutorial crear reports QWeb PDF Odoo 18 2024 2025",
  "numResults": 10,
  "type": "deep"
}
```

**Output:**

```
Title: Build PDF Reports — Odoo 18.0 documentation
URL: https://www.odoo.com/documentation/18.0/developer/tutorials/pdf_reports.html
Published: N/A
Author: N/A
Highlights:
Build PDF Reports — Odoo 18.0 documentation
...
# Build PDF Reports¶
...
This tutorial is an extension of the Server framework 101 tutorial. Make sure you have completed it and use the`estate` module you have built as a base for the exercises in this tutorial.
...
We were previously introduced to QWeb where it was used to build a kanban view. Now we will expand on one of QWeb’s other main uses: creating PDF reports. A common business requirement is the ability to create documents to send to customers and to use internally. These reports can be used to summarize and display information in an organized template to support the business in different ways. Odoo can additionally add our company’s header and footer to our reports with minimal extra effort.
...
The documentation related to this topic can be found in QWeb Templates, QWeb Reports, and the Report Actions (ir.actions.report) section of the Actions reference.
...
The bulk of a PDF report is its QWeb template. It also typically needs a corresponding`ir.actions.report` to include the report within a module’s business logic. There is no strict rule for the file names or where they are located, but these two parts are typically stored in 2 separate files within a`report` folder at the top level of your module’s directory. If a module has many or multiple long report templates, then they are often organized logically across different files named after the report(s) they contain. All actions for the reports are usually stored in the same file ending with`_reports.xml`, regardless of the number of reports it contains.
...
Don’t forget to add whatever files your template and action view will be into to your`__manifest__.py`. In this case, you will want to add the files to the`data` list and remember that the files listed in a manifest are loaded sequentially!
...
## Basic Report¶
...
Goal: at the end of this section, we will be able to print a report that displays all offers for a property.
...
### Report Data
...
Before we do anything we first need some data to populate our reports or else this tutorial won’t be very interesting. When creating reports, you will need some data to test your report code and check that the resulting look is as expected. It is a good idea to test with data that will cover most or all of your expected use cases. A good representation set for our simple report is:
...
### Minimal Template¶
...
A minimal viable template is viewable under the “Minimal viable template” section of the Report template documentation. We can modify this example to build our minimal property offers template file:
...
the Odoo specific (i.e. non-HTML) items in our file are
...
### Report Action¶
...
Now that we have a template, we need to make it accessible in our app via a`ir.actions.report`. A practical example of`ir.actions.report` is here corresponding to this template. Its contents are all explained in the documentation.
...
An`ir.actions.report` is primarily used via the Print menu of a model’s view. In the practical example, the`binding_model_id` specifies which model’s views the report should show, and Odoo will auto-magically add it for you. Another common use case of the report action is to link it to a button as we learned in Chapter 9: Ready For Some Action?. This is handy for reports that only make sense under specific conditions. For example, if we wanted to make a “Final Sale” report, then we can link it to a “Print Sale Info” button that appears in the form view only when the property is “Sold”.
...
You may have noticed or are wondered why our report template loops through a recordset. When our template is passed more than one record, it can produce one PDF report for all the records. Using the Print menu in the list view with multiple records selected will demonstrate this.
...
### Make a Report¶
...
Finally, you now know where to create your files and how the content of the files should look. Happy report making!
...
Make a report.
...
Add the property offers report from the minimal template subsection to the Print menu of the Property views.
...
Improve the report by adding more data. Refer to the Goal of this section to see what additional data you can add and feel free to add even more.
...
Bonus: Make an extra flexible report by adding in some logic so that when there are no offers on a property then we don’t create a table and instead write something about how there are no offers yet. Hint: you will need to use`t-if` and`t-else`.
...
Remember to check that your PDF reports match your data as expected.
...
## Sub-templates¶
...
Goal: at the end of this section, we will have a sub-template that we use in 2 reports.
...
There are two main reasons for using sub-templates. One is to make the code easier to read when working with extra-long or complicated templates. The other is to reuse code where possible. Our simple property offers report is useful, but listing property offers information can be useful for more than just one report template. One example is a report that lists all of a salesman’s properties’ offers.
...
Split the table portion of the offers into its own template. Remember to check that your original report still prints correctly afterwards.
...
Add a new report for`res.users` that allows you to print all of the Real Estate Properties that are visible in their form view (i.e. in the “Settings” app). Include the offers for each of those saleman’s properties in the same report. Hint: since the`binding_model_id` in this case will not be within the estate module, you will need to use`ref="base.model_res_users"`.
...
## Report Inheritance¶
...
Goal: at the end of this section, we will inherit the property report in the`estate_account` module.
...
Inheritance in QWeb uses the same`xpath` elements as views inheritance. A QWeb template refers to its parent template in a different way though. It is even easier to do by just adding the`inherit_id` attribute to the`template` element and setting it equal to the module.parent_template_id.
...
We didn’t add any new fields to any of the estate models in`estate_account`, but we can still add information to our existing property report. For example, we know that any “Sold” properties will already have an invoice created for them, so we can add this information to our report.
...
## Additional Features¶
...
### Reports are web pages¶
...
You probably are tired of hearing that QWeb creates HTML, but we’re saying it again! One of the neat features of reports being written in QWeb is they can be viewed within the web browser. This can be useful if you want to embed a hyperlink that leads to a specific report. Note that the usual security checks will still apply to prevent unauthorized users from accessing the reports.

---

Title: Build PDF Reports — Odoo saas-18.4 documentation
URL: https://www.odoo.com/documentation/saas-18.4/developer/tutorials/pdf_reports.html
Published: N/A
Author: N/A
Highlights:
Build PDF Reports — Odoo saas-18.4 documentation
...
# Build PDF Reports¶
...
This tutorial is an extension of the Server framework 101 tutorial. Make sure you have completed it and use the`estate` module you have built as a base for the exercises in this tutorial.
...
We were previously introduced to QWeb where it was used to build a kanban view. Now we will expand on one of QWeb’s other main uses: creating PDF reports. A common business requirement is the ability to create documents to send to customers and to use internally. These reports can be used to summarize and display information in an organized template to support the business in different ways. Odoo can additionally add our company’s header and footer to our reports with minimal extra effort.
...
The documentation related to this topic can be found in QWeb Templates, QWeb Reports, and the Report Actions (ir.actions.report) section of the Actions reference.
...
The bulk of a PDF report is its QWeb template. It also typically needs a corresponding`ir.actions.report` to include the report within a module’s business logic. There is no strict rule for the file names or where they are located, but these two parts are typically stored in 2 separate files within a`report` folder at the top level of your module’s directory. If a module has many or multiple long report templates, then they are often organized logically across different files named after the report(s) they contain. All actions for the reports are usually stored in the same file ending with`_reports.xml`, regardless of the number of reports it contains.
...
Don’t forget to add whatever files your template and action view will be into to your`__manifest__.py`. In this case, you will want to add the files to the`data` list and remember that the files listed in a manifest are loaded sequentially!
...
## Basic Report¶
...
Goal: at the end of this section, we will be able to print a report that displays all offers for a property.
...
### Report Data
...
Before we do anything we first need some data to populate our reports or else this tutorial won’t be very interesting. When creating reports, you will need some data to test your report code and check that the resulting look is as expected. It is a good idea to test with data that will cover most or all of your expected use cases. A good representation set for our simple report is:
...
### Minimal Template¶
...
A minimal viable template is viewable under the “Minimal viable template” section of the Report template documentation. We can modify this example to build our minimal property offers template file:
...
the Odoo specific (i.e.
...
-HTML) items in our file
...
### Report Action¶
...
Now that we have a template, we need to make it accessible in our app via a`ir.actions.report`. A practical example of`ir.actions.report` is here corresponding to this template. Its contents are all explained in the documentation.
...
An`ir.actions.report` is primarily used via the Print menu of a model’s view. In the practical example, the`binding_model_id` specifies which model’s views the report should show, and Odoo will auto-magically add it for you. Another common use case of the report action is to link it to a button as we learned in Chapter 9: Ready For Some Action?. This is handy for reports that only make sense under specific conditions. For example, if we wanted to make a “Final Sale” report, then we can link it to a “Print Sale Info” button that appears in the form view only when the property is “Sold”.
...
You may have noticed or are
...
report template loops through a recordset
...
is passed more than one record, it can produce one PDF
...
for all the records
...
the Print menu in
...
view with multiple records selected will
...
### Make a Report¶
...
Finally, you now know where to create your files and how the content of the files should look. Happy report making!
...
Make a report.
...
Add the property offers report from the minimal template subsection to the Print menu of the Property views.
...
Improve the report by adding more data. Refer to the Goal of this section to see what additional data you can add and feel free to add even more.
...
Bonus: Make an extra flexible report by adding in some logic so that when there are no offers on a property then we don’t create a table and instead write something about how there are no offers yet. Hint: you will need to use`t-if` and`t-else`.
...
Remember to check that your PDF reports match your data as expected.
...
## Sub-templates¶
...
Goal: at the end of this section, we will have a sub-template that we use in 2 reports.
...
There are two main reasons for using sub-templates. One is to make the code easier to read when working with extra-long or complicated templates. The other is to reuse code where possible. Our simple property offers report is useful, but listing property offers information can be useful for more than just one report template. One example is a report that lists all of a salesman’s properties’ offers.
...
Split the table portion of the offers into its own template. Remember to check that your original report still prints correctly afterwards.
...
Add a new report for`res.users` that allows you to print all of the Real Estate Properties that are visible in their form view (i.e. in the “Settings” app). Include the offers for each of those saleman’s properties in the same report. Hint: since the`binding_model_id` in this case will not be within the estate module, you will need to use`ref="base.model_res_users"`.
...
## Report Inheritance¶
...
Goal: at the end of this section, we will inherit the property report in the`estate_account` module.
...
Inheritance in QWeb uses the same`xpath` elements as views inheritance. A QWeb template refers to its parent template in a different way though. It is even easier to do by just adding the`inherit_id` attribute to the`template` element and setting it equal to the module.parent_template_id.
...
We didn’t add any new fields to any of the estate models in`estate_account`, but we can still add information to our existing property report. For example, we know that any “Sold” properties will already have an invoice created for them, so we can add this information to our report.
...
## Additional Features¶
...
### Reports are web pages¶
...
You probably are tired of hearing that QWeb creates HTML, but we’re saying it again! One of the neat features of reports being written in QWeb is they can be viewed within the web browser. This can be useful if you want to embed a hyperlink that leads to a specific report. Note that the usual security checks will still apply to prevent unauthorized users from accessing the reports.

---

Title: How to Create a PDF Report in Odoo 18?
URL: https://www.cybrosys.com/blog/how-to-create-a-pdf-report-in-odoo-18
Published: N/A
Author: N/A
Highlights:
How to Create a PDF Report in Odoo 18?
...
# How to Create a PDF Report in Odoo 18?
...
Qweb is Odoo’s powerful templating engine, designed to easily convert XML data into HTML documents. Its feature set includes attribute-based customization, conditional logic, dynamic content insertion, and a range of report template options. This versatility makes Qweb ideal for crafting personalized, visually compelling reports, emails, and documents. From financial statements to invoices and complex business reports, Qweb streamlines the creation process, ensuring that each output is both clear and appealing.
...
In this guide, we will walk through creating a custom PDF report in Odoo 18 for the "hr.expense" model. This process involves building a Qweb template and setting up the corresponding report action, which will allow users to generate a PDF of expense details directly from the Odoo interface.
...
## Step-by-Step Guide to Creating a Custom PDF Report in Odoo 18
...
### * Create the Report Action (XML file)
...
Inside your module's "report" directory, create an XML file for the report action. Let's name it expense_reports.xml. This file will define the report action that binds the report to the model. Below is an example of what the XML file might contain:
...
```

<?xml version="1.0" encoding="UTF-8"?><odoo>    <!--    Report Function in Expense -->    <record id="action_expense_request_report" model="ir.actions.report">        <field name="name">Expense Report</field>        <field name="model">hr.expense</field>        <field name="report_type">qweb-pdf</field>        <field name="report_name">expense_report_odoo.report_expense_report_details</field>        <field name="report_file">expense_report_odoo.report_expense_report_details</field>        <field name="binding_model_id" ref="hr_expense.model_hr_expense"/>        <field name="binding_type">report</field>    </record></odoo>

... In this XML file, we define a report action using the following fields: ...

### Important Fields When Creating Report Actions

...

#### 1. Name (name):

... The name of the report action is specified using the name field. It helps identify
the report within the system. In our example, it’s set to "Expense Report". ...

#### 2. Model (model):

... This field defines the model that the report is associated with. The report
retrieves data from this model. In our case, the model is "hr.expense", which means the
report will display data from the hr expense model. ...

#### 3. Report Type (report_type):

... This specifies the type of report being generated. The available options are: ...

- qweb-pdf: For generating PDF reports using QWeb templates.

- qweb-html: For generating HTML reports using QWeb templates.

- qweb-text: For generating plain text reports using QWeb templates. ... In our example,
  we’re generating a PDF report, so the report_type is set to "qweb-pdf". ...

#### 4. Report Name (report_name):

... This field specifies the internal name of the report template. It links the report
action to the QWeb template that will be used to generate the output. In our case, the
report name is "module_name.report_expense_report_details". ...

#### 5. Report File (report_file):

... The report_file defines the name of the QWeb template file used for the report. This
file contains the XML structure for rendering the report. It’s set to
"module_name.report_expense_report_details". ...

#### 6. Binding Model ID (binding_model_id):

... This is a reference to the model associated with the report action, linking it to
other objects. Here, it references the hr expense model: "hr_expense.model_hr_expense".
...

#### 7. Binding Type (binding_type):

... This defines how the report is bound to the system. The two options are: ...

- action: Binds the report to a specific action.

- report: Binds the report directly to a record of the specified model. ... The report
  action will create a new entry under the "Print" menu of the associated model. In the
  case of the report action mentioned above, it will add a new report option within the
  "Print" menu for the hr.expense model, as demonstrated in the screenshot below. ...

### Create the QWeb Template (XML file)

... Next, we need to create the QWeb template, which defines the structure and layout of
the PDF report. This file should be placed in the report directory and named
expense_report_templates.xml. Below is an example of a simple QWeb template for the
report: ...

```
<?xml version="1.0" encoding="UTF-8" ?><odoo>    <!--    Report Template-->    <template id="report_expense_report_details">        <t t-call="web.html_container">           <t t-foreach="docs" t-as="o">                <t t-call="web.external_layout">                    <div class="page">                        <div class="oe_structure"/>                        <h2>Expense Report</h2>                        <br></br>                        <p>                            Name :                            <span t-field="o.employee_id.name"/>                        </p>                    </div>                </t>            </t>        </t>    </template></odoo>
...
In this QWeb template file, we define a structure using the template ID, which matches the report_name specified in the report action XML. The t-foreach loop iterates through the list of records (docs) and generates a report page for each product. Inside the template, HTML tags and QWeb expressions are used to format and display the data as needed.
...
This basic template will generate a PDF report that includes the expense report details, as shown below.
...
Creating PDF reports in Odoo 18 using Qweb is a straightforward process that combines powerful templating capabilities with a simple XML configuration. By defining a report action and crafting a custom Qweb template, you can generate detailed and well-structured PDF documents tailored to your business needs. This guide provides a foundation to help you create personalized reports that seamlessly integrate into your Odoo workflows, improving data presentation and accessibility.

---

Title: QWeb Reports — Odoo 18.0 documentation
URL: https://www.odoo.com/documentation/18.0/developer/reference/backend/reports.html
Published: N/A
Author: N/A
Highlights:
QWeb Reports — Odoo 18.0 documentation
...
# QWeb Reports¶
...
Reports are written in HTML/QWeb, like website views in Odoo. You can use the usual QWeb control flow tools. The PDF rendering itself is performed by wkhtmltopdf.

Reports are declared using a report action, and a Report template for the action to use.
...
If useful or necessary, it is possible to specify a Paper Format for the report report.
...
## Report template¶
...
Report templates will always provide the following
...
### Minimal viable template¶
...
A minimal template would look like:
...
```

<template id="report_invoice">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    <h2>Report title</h2>
                    <p>This object's name is <span t-field="o.name"/></p>
                </div>
            </t>
        </t>
    </t>
</template>

````
...
Calling`external_layout` will add the default header and footer on your report. The PDF body will be the content inside the` `. The template’s`id` must be the name specified in the report declaration; for example`account.report_invoice` for the above report. Since this is a QWeb template, you can access all the fields of the`docs` objects received by the template.
...
### Translatable Templates¶
...
If you wish to translate reports (to the language of a partner, for example), you need to define two templates:
...
You can then call the translatable document from your main template with the attribute`t-lang` set to a language code (for example`fr` or`en_US`) or to a record field. You will also need to re-browse the related records with the proper context if you use fields that are translatable (like country names, sales conditions, etc.)
...
The main template calls the translatable template with`doc.partner_id.lang` as a`t-lang` parameter, so it will be rendered in the language of the partner. This way, each Sale Order will be printed in the language of the corresponding customer. If you wish to translate only the body of the document, but keep the header and footer in a default language, you could call the report’s external layout this way:
...
## Paper Format¶
...
Paper formats are records of`report.paperformat` and can contain the following attributes:
...
## Custom Reports¶
...
By default, the reporting system builds rendering values based on the target model specified through the`model` field.
...
However, it will first look for a model named`report.module.report_name` and call that model’s`_get_report_values(doc_ids, data)` in order to prepare the rendering data for the template.
...
## Reports are web pages¶

Reports are dynamically generated by the report module and can be accessed directly via URL:

For example, you can access a Sale Order report in html mode by going to http:// /report/html/sale.report_saleorder/38
...
Or you can access the pdf version at http:// /report/pdf/sale.report_saleorder/38

---

Title: Build PDF Reports — Odoo saas-18.3 documentation
URL: https://www.odoo.com/documentation/saas-18.3/developer/tutorials/pdf_reports.html
Published: N/A
Author: N/A
Highlights:
Build PDF Reports — Odoo saas-18.3 documentation
...
# Build PDF Reports¶
...
This tutorial is an extension of the Server framework 101 tutorial. Make sure you have completed it and use the`estate` module you have built as a base for the exercises in this tutorial.
...
We were previously introduced to QWeb where it was used to build a kanban view. Now we will expand on one of QWeb’s other main uses: creating PDF reports. A common business requirement is the ability to create documents to send to customers and to use internally. These reports can be used to summarize and display information in an organized template to support the business in different ways. Odoo can additionally add our company’s header and footer to our reports with minimal extra effort.
...
The documentation related to this topic can be found in QWeb Templates, QWeb Reports, and the Report Actions (ir.actions.report) section of the Actions reference.
...
The bulk of a PDF report is its QWeb template. It also typically needs a corresponding`ir.actions.report` to include the report within a module’s business logic. There is no strict rule for the file names or where they are located, but these two parts are typically stored in 2 separate files within a`report` folder at the top level of your module’s directory. If a module has many or multiple long report templates, then they are often organized logically across different files named after the report(s) they contain. All actions for the reports are usually stored in the same file ending with`_reports.xml`, regardless of the number of reports it contains.
...
Don’t forget to add whatever files your template and action view will be into to your`__manifest__.py`. In this case, you will want to add the files to the`data` list and remember that the files listed in a manifest are loaded sequentially!
...
## Basic Report¶
...
Goal: at the end of this section, we will be able to print a report that displays all offers for a property.
...
### Report Data
...
Before we do anything we first need some data to populate our reports or else this tutorial won’t be very interesting. When creating reports, you will need some data to test your report code and check that the resulting look is as expected. It is a good idea to test with data that will cover most or all of your expected use cases. A good representation set for our simple report is:
...
### Minimal Template¶
...
A minimal viable template is viewable under the “Minimal viable template” section of the Report template documentation. We can modify this example to build our minimal property offers template file:
...
the Odoo specific (i.e. non-HTML) items in our file
...
our template are
...
### Report Action¶
...
Now that we have a template, we need to make it accessible in our app via a`ir.actions.report`. A practical example of`ir.actions.report` is here corresponding to this template. Its contents are all explained in the documentation.
...
An`ir.actions.report` is primarily used via the Print menu of a model’s view. In the practical example, the`binding_model_id` specifies which model’s views the report should show, and Odoo will auto-magically add it for you. Another common use case of the report action is to link it to a button as we learned in Chapter 9: Ready For Some Action?. This is handy for reports that only make sense under specific conditions. For example, if we wanted to make a “Final Sale” report, then we can link it to a “Print Sale Info” button that appears in the form view only when the property is “Sold”.
...
You may have noticed or are wondered why our report template loops through a recordset. When
...
template is passed more than one record, it can produce one PDF report for all the records. Using the Print menu in the list view with multiple records selected will demonstrate this.
...
### Make a Report¶
...
Finally, you now know where to create your files and how the content of the files should look. Happy report making!
...
Make a report.
...
Add the property offers report from the minimal template subsection to the Print menu of the Property views.
...
Improve the report by adding more data. Refer to the Goal of this section to see what additional data you can add and feel free to add even more.
...
Bonus: Make an extra flexible report by adding in some logic so that when there are no offers on a property then we don’t create a table and instead write something about how there are no offers yet. Hint: you will need to use`t-if` and`t-else`.
...
Remember to check that your PDF reports match your data as expected.
...
## Sub-templates¶
...
Goal: at the end of this section, we will have a sub-template that we use in 2 reports.
...
There are two main reasons for using sub-templates. One is to make the code easier to read when working with extra-long or complicated templates. The other is to reuse code where possible. Our simple property offers report is useful, but listing property offers information can be useful for more than just one report template. One example is a report that lists all of a salesman’s properties’ offers.
...
Split the table portion of the offers into its own template. Remember to check that your original report still prints correctly afterwards.
...
Add a new report for`res.users` that allows you to print all of the Real Estate Properties that are visible in their form view (i.e. in the “Settings” app). Include the offers for each of those saleman’s properties in the same report. Hint: since the`binding_model_id` in this case will not be within the estate module, you will need to use`ref="base.model_res_users"`.
...
## Report Inheritance¶
...
Goal: at the end of this section, we will inherit the property report in the`estate_account` module.
...
Inheritance in QWeb uses the same`xpath` elements as views inheritance. A QWeb template refers to its parent template in a different way though. It is even easier to do by just adding the`inherit_id` attribute to the`template` element and setting it equal to the module.parent_template_id.
...
We didn’t add any new fields to any of the estate models in`estate_account`, but we can still add information to our existing property report. For example, we know that any “Sold” properties will already have an invoice created for them, so we can add this information to our report.
...
## Additional Features¶
...
### Reports are web pages¶
...
You probably are tired of hearing that QWeb creates HTML, but we’re saying it again! One of the neat features of reports being written in QWeb is they can be viewed within the web browser. This can be useful if you want to embed a hyperlink that leads to a specific report. Note that the usual security checks will still apply to prevent unauthorized users from accessing the reports.

---

Title: Dynamic Reports in Odoo 18 | Complete Development Guide
URL: https://www.braincuber.com/tutorial/create-dynamic-reports-odoo-18
Published: 2026-02-02T10:22:48.000Z
Author: Mayur Domadiya
Highlights:
# How to Create Dynamic Reports in Odoo 18
...
Static reports are fine when you just need a snapshot of data. But when managers want to slice and dice information—filter by date, group by salesperson, compare categories—you need dynamic reports. In Odoo 18, building these interactive reports means combining OWL JavaScript components with Python backend logic and QWeb templates.
...
This tutorial walks through building a complete dynamic sales report. Users can filter by date range, choose different report views (by order, product, or salesperson), and export to PDF or Excel. The same pattern works for any Odoo model—inventory, accounting, HR, whatever data you need to analyze.
...
## Step 1: Module Setup and Menu
...
```python
{
    'name': 'Dynamic Sales Report',
    'version': '18.0.1.0.0',
    'category': 'Sales/Reporting',
    'summary': 'Interactive dynamic sales reports with filters and export',
    'description': 'Create dynamic, filterable sales reports with PDF and Excel export',
    'author': 'Your Company',
    'depends': ['sale', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'report/sales_report_pdf.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sales_dynamic_report/static/src/js/sales_report.js',
            'sales_dynamic_report/static/src/xml/sales_report_template.xml',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
````

... ="1. ...

## Step 3: The QWeb Template

... The OWL template defines the UI structure—filters, buttons, and data tables. ...

````xml
<?xml version="1.0" encoding="UTF-8"?>
<templates xml:space="preserve">
    <t t-name="SalesDynamicReportTemplate" owl="1">
        <div class="o_sales_dynamic_report">

            <!-- Report Header -->
            <div class="report-header">
                <h1>Sales Analytics Report</h1>
            </div>

            <!-- Filter Section -->
            <div class="filter-section">
                <div class="filter-row">
                    <!-- Export Buttons -->
                    <div class="export-buttons">
                        <button class="btn btn-primary"
                                t-on-click="printPdf">
                            <i class="fa fa-file-pdf-o"/> Export PDF
                        </button>
                        <button class="btn btn-success"
                                t-on-click="exportXlsx">
                            <i class="fa fa-file-excel-o"/> Export Excel
                        </button>
                    </div>

                    <!-- Date Filters -->
                    <div class="date-filters">
                        <div class="filter-group">
                            <label>From:</label>
                            <input type="date" t-ref="date_from"
                                   class="form-control"/>
                        </div>
                        <div class="filter-group">
                            <label>To:</label>
                            <input type="date" t-ref="date_to"
                                   class="form-control"/>
                        </div>
                    </div>

                    <!-- Report Type Selector -->
                    <div class="report-type-selector">
                        <label>Report Type:</label>
                        <select t-ref="report_type" class="form-control">
                            <option value="by_order">By Order</option>
                            <option value="by_product">By Product</option>
                            <option value="by_salesperson">By Salesperson</option>
                            <option value="by_customer">By Customer</option>
                        </select>
                    </div>

                    <button class="btn btn-primary apply-btn"
                            t-on-click="applyFilters">
                        Apply Filters
                    </button>
                </div>
            </div>

            <!-- Summary Cards -->
            <div class="summary-cards">
                <div class="summary-card">
                    <span class="card-label">Total Orders</span>
                    <span class="card-value" t-esc="state.summary.totalOrders"/>
                </div>
                <div class="summary-card">
                    <span class="card-label">Total Quantity</span>
                    <span class="card-value" t-esc="state.summary.totalQty"/>
                </div>
                <div class="summary-card">
                    <span class="card-label">Total Revenue</span>
                    <span class="card-value">
                        $<t t-esc="state.summary.totalAmount"/>
                    </span>
                </div>
            </div>

            <!-- Loading State -->
            <div t-if="state.isLoading" class="loading-overlay">
                <div class="spinner"/>
                <p>Loading report data...</p>
            </div>

            <!-- Report Table: By Order -->
            <div t-if="!state.isLoading && state.reportType === 'by_order'"
                 class="report-table">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Order</th>
                            <th>Date</th>
                            <th>Customer</th>
                            <th>Salesperson</th>
                            <th>Quantity</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        <t t-foreach="state.reportLines" t-as="line"
                           t-key="line.id">
                            <tr>
                                <td>
                                    <a href="#" t-att-data-order-id="line.id"
                                       t-on-click="viewSalesOrder">
                                        <t t-esc="line.name"/>
                                    </a>
                                </td>
                                <td t-esc="line.date_order"/>
                                <td t-esc="line.partner_name"/>
                                <td t-esc="line.salesperson"/>
                                <td t-esc="line.total_qty"/>
                                <td>$<t t-esc="line.amount_total"/></td>
                            </tr>
                        </t>
                    </tbody>
                </table>
            </div>

        </div>
    </t>
</templates>
...
## Step 4: Python Backend Model
...
## Step 5: Excel Export Controller
...
You now have a complete dynamic reporting system: an OWL component handling the UI and interactions, Python backend processing data with raw SQL for performance, and export functionality for both PDF and Excel. This same architecture extends to any Odoo model—just modify the queries and template columns to match your data requirements.
...
A dynamic report in Odoo 18 is an interactive report that allows users to filter, sort, and customize data in real-time without page reloads. Unlike static PDF reports that show fixed data, dynamic reports use OWL JavaScript components to update the display based on user selections like date ranges, grouping options, and filter criteria. They combine a frontend OWL component with Python backend queries.
...
Create an HTTP controller with a route that accepts report data as JSON. Use the xlsxwriter library to create an Excel workbook in memory, write your headers and data rows, then return the file with appropriate Content-Type and Content-Disposition headers. In your OWL component, use the download utility from @web/core/network/download to trigger the file download.

---

Title: Creating and Customizing PDF Reports in Odoo 18.0: A Comprehensive Guide
URL: https://cleverence.com/articles/odoo-documentation/pdf-reports-odoo-18-0-documentation-2186/
Published: 2025-08-11T16:19:57.000Z
Author: N/A
Highlights:
Creating and Customizing PDF Reports in Odoo 18.0: A Comprehensive Guide --
...
# Creating and Customizing PDF Reports in Odoo 18.0: A Comprehensive Guide
...
Are you navigating the intricate maze of generating PDF reports in Odoo 18.0? You're not alone. Reports are like the lifeblood of any business, offering insights and data that help guide decisions. In this article, we'll delve into the world of PDF reports in Odoo 18.0, breaking down everything from basic report generation to advanced customization. Let's make those PDF reports as crisp and informative as they can be!
...
Odoo 18.0
...
Understanding how these reports work involves getting familiar with the underlying data structure and templates in Odoo. You'll find that most reports use QWeb, an XML-based template language, to format and display your data accurately and beautifully.
...
## Setting Up Your First PDF Report
...
Setting up your first PDF report in Odoo is like setting the stage for a show. Start in the Odoo backend, navigating to the report templates. You'll notice each module in Odoo has its set of reports, which can be customized to meet specific needs.
...
The creation process typically involves choosing a base template, defining the report's structure, and specifying the data it will use. In many cases, Odoo provides a skeleton template, which you can flesh out with the specific information you want to present.
...
Once your template is ready, you can directly generate the report. Head over to the report menu and execute, and just like magic, your data transforms into a polished PDF document. Keep in mind that you might need to tweak things like date formats and display settings to perfectly match your requirements.
...
## Customizing PDF Reports
...
Customizing PDF reports is where you can inject a bit of personality into those dry numbers. Odoo's flexibility shines through its customization options, allowing you to tailor reports to reflect your brand's identity.
...
Begin by accessing the QWeb templates, where you can modify existing elements or add new ones. Adjust the layout to better display key data, and don't shy away from adding colors or logos to align the report with your company's branding strategy.
...
## Automating PDF Report Generation
...
Let’s face it: nobody wants to spend hours generating reports. Luckily, Odoo 18.0 offers robust options for automating report generation. It's like setting up a coffee maker to brew your morning cup while you get dressed for work.
...
Automation can be set up using the scheduled actions feature in Odoo. Define triggers based on specific conditions, such as actions occurring in your inventory or sales modules, so that reports generate automatically without manual intervention.
...
Most troubleshooting begins with reviewing the QWeb templates for syntax errors or invalid object calls. Since these templates are XML-based, even minor typos can lead to significant data display problems.
...
- How do I generate a PDF report in Odoo?
...
Navigate to the desired module, select the data you wish to include, and execute the report generation process within the reporting menu.
...
- Can I customize the templates used for PDF reports?
...
Yes, Odoo provides the flexibility to edit QWeb templates, allowing you to modify the layout, format, and content to fit your specific needs.
...
- How can I automate the generation of reports?
...
You can set up automated actions using scheduled tasks in Odoo, which allows reports to be generated at regular intervals or based on specific triggers.
...
You can use CSS to style reports, adjusting elements like font, color, and alignment, and adding visual components like graphs for enhanced aesthetics.
...
First, check for any errors in your XML template. If the issue persists, review the data source configurations in Odoo to ensure all necessary information is being captured correctly.

---

Title: How to Create a Customized Purchase Order Report in Odoo 18?
URL: https://www.netilligence.io/blog/how-to-create-a-customized-purchase-order-report-in-odoo-18/
Published: 2025-08-22T13:55:06.000Z
Author: N/A
Highlights:
How to Create a Customized Purchase Order Report in Odoo 18?
...
- August 22, 2025
...
# How to Create a Customized Purchase Order Report in Odoo 18?
...
Creating a customized Purchase Order report in Odoo 18 isn’t just about changing the look of your documents. It’s about changing your procurement process into something more innovative, sharper, and custom-made for your business. Whether you’re a procurement officer, developer, or business owner, having the ability to generate reports that reflect your unique workflows, data points, and branding can provide a competitive edge.
...
In this guide, we’ll walk you through creating a customized Purchase Order report in Odoo 18, giving you the tools to extract insights, simplify communication, and enhance professional presentation while harnessing the power and flexibility of Odoo’s backend architecture. Let’s dive in and turn your purchase data into a strong business asset.
...
## What is a QWeb Report?
...
QWeb is Odoo’s templating engine for rendering reports. It allows you to write XML-based templates that dynamically insert data from Odoo models. QWeb reports are often used for PDF outputs like invoices and purchase orders.
...
An Odoo report consists of:
...
- A QWeb template (XML)
- A paper format record
- A report action record
- Optional Python helper functions (for complex logic)
...
## Folder Structure for Custom Report
...
## Creating the Template
...
The report’s core is the XML template, which defines how the data is displayed. Here is a working template:
...
PURCHASE ORDER
...
Description
...
VAT 5% Amount
...
## Paper Format XML
...
This defines the layout properties like page size and margins:
...
## Report Action XML
...
This links the model and template to create the report:
...
```xml




Purchase Order
purchase.order
qweb-html
my_module.report_purchase_order
my_module.report_purchase_order

report






````

...

## Explanation of Key Parts

... What it does

Inherits base PDF layout used in Odoo reports

Loops through purchase orders (usually one per report)

image_data_uri(…) ... Embeds the company logo as base64-encoded image ... t-field and
t-esc ... Outputs fields (with or without formatting)

Footer section ... Dynamically renders company contact information ...

## Make Your Reports Work for You

...

- The report is fully dynamic and supports multi-company.
- You can add more fields, conditions, or sections based on business needs.
- Odoo’s templating allows using Python-like expressions inside XML with ease.
- You can replace the basic_layout with custom layouts for more control.

---

Title: 26. Odoo 18 Tutorial: How to Print PDF Reports | QWeb PDF ... URL:
https://www.youtube.com/watch?v=2LSyfJnZACw Published: 2026-03-07T17:04:26.000Z Author:
WOWDOO Highlights:

# 26. Odoo 18 Tutorial: How to Print PDF Reports | QWeb PDF Report in Odoo 18 (Step-by-Step)

... Learn how to generate and print PDF reports in Odoo 18 using QWeb reports. ... In
this tutorial, I will show you step-by-step how to create a PDF report in Odoo 18 and
print it directly from the system. This guide is perfect for Odoo developers, beginners,
and ERP learners who want to understand how the Odoo reporting system works. ... In this
video you will learn:

✅ How the Odoo reporting system works

✅ Creating a QWeb report template

✅ Using report_type="qweb-pdf"

✅ Printing reports in PDF format

✅ Testing the report inside Odoo ... Hello everyone. In the last video, we talked about
compute display name method in OD 18in. In today's video, we are going to talk about how
to print PDF in Odin. ... To create a PDF file, we have to deal with two files. For
that, let's create a uh directory first named report. ... This is just a convention. You
can name it um anything you want. And inside that we have to create two XML files. one
is for the Q web template which basically shows the PDF and a report record in in the
IR.Actions report model we have to create a record which is B which basically works as
the connector between the u between the template and PDU. So let's create the report
file first. I will name the report file as student card student card report doxml and
the second one is the uh the Q web template. So I will name it like student card report
template dot XML. ... First of all, I will create a a record inside the ODUS built-in
IR.Actions.report model. So first of all, let's create the boiler plate code of X of an
XML file of a XML file as you know. So XML and the encoding should be UT F8. ... Okay.
Now we have to we have to mention the report type. ... Report type. There are different
types of report um types like QB, HTML, QB, PDF. But as we are creating a PDF report
here. So we will we will go with the report type as Q web PDF. ... Sorry not underscore
it's hyphen. So this what this QB PDF does it basically means that we are using a Q web
template for our PDF file. Q web- PDF uh basically means that Q web PDF. ... This is the
module name and dot the exact id of the report template file. So give this temp uh this
report name as a student card report template. Later we will be creating a template in
this report template.xml XML file with this a student card report template id. So this
is basically the connection between this report record and our wouldbe created would be
created template doxml file. So this is the connection. Now we have to mention two other
things which is binding model ID and binding type. So let's create that. ... And here we
have to mention the model ID as the ref attributes value. So the first thing we have to
do is we have to use this model prefix and then we have to write the model name like
this a student instead of dot we have to use underscore and the second word. So model a
student card and then the final thing we have to do is we have to mention the binding
type and so we have to mention binding type like this and as the value we have to pass
report. So these two lines basically are needed to uh render our PDF successfully. If we
don't use these two lines, then our report may not be rendered successfully. ... Okay.
Now inside this we have to call a built-in uh a built-in template in ODO which is
already built in ODO and uh we have to call that which is web dot HTML container. ... So
we have to mention the htm we have to use the html container and inside this we have to
use a special object which is docs this is provided by odo so let's use that first we
have to loop through that docs object let's write that first then I will explain what it
is doing basically so t uh t for h t for H equals docs and T as let's say O and inside
this we have to use another uh built-in template which is um web dot external layout. So
we have to call that web web dot external layout. ... This name is coming from this name
attributes value which is print a student card. Now when when we click on this we when
we click on this button what what we will do it will find that template using this ID
and render a Q web temp uh a Q web template um and then it will um uh it will compile
that Q web template to HTML and then the WK HTML to PDF uh PDF renderer engine will uh
convert this HTML ML to a PDF view. So now if we click on this, let's see what happens
if we get any error or not. ...

...10566 bytes truncated...

The tool call succeeded but the output was truncated. Full output saved to:
/home/socger/.local/share/opencode/tool-output/tool_f857dabb1001eA2AqtI10Xjn2f Use the
Task tool to have explore agent process this file with Grep and Read (with
offset/limit). Do NOT read the full file yourself - delegate to save context.

````

---

## Assistant (Odoo-Dev · Big Pickle · 21.8s)

_Thinking:_

El usuario quiere aprender sobre cómo crear reports en Odoo. Voy a cargar el patrón de reports del skill y buscar videos en la web.

Perfecto, ya tengo el skill cargado y he encontrado mucha información. Déjame también leer el patrón de reports específico del skill para darte la información más precisa posible.

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/skills/report-patterns.md"
}
````

**Output:**

````
<path>/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/skills/report-patterns.md</path>
<type>file</type>
<content>
1: # Report Generation Patterns
2:
3: ```
4: ╔══════════════════════════════════════════════════════════════════════════════╗
5: ║  REPORT PATTERNS                                                             ║
6: ║  PDF reports, QWeb templates, and document generation                        ║
7: ║  Use for invoices, delivery slips, quotes, and custom documents              ║
8: ╚══════════════════════════════════════════════════════════════════════════════╝
9: ```
10:
11: ## Report Types
12:
13: | Type  | Use Case            | Technology          |
14: | ----- | ------------------- | ------------------- |
15: | PDF   | Printable documents | QWeb + wkhtmltopdf  |
16: | HTML  | Screen display      | QWeb                |
17: | Excel | Data export         | xlsxwriter/openpyxl |
18:
19: ---
20:
21: ## Basic Report Structure
22:
23: ### File Organization
24:
25: ```
26: my_module/
27: ├── report/
28: │   ├── __init__.py
29: │   ├── my_report.py           # Report logic (optional)
30: │   └── my_report_templates.xml # QWeb templates
31: └── __manifest__.py
32: ```
33:
34: ### Manifest Entry
35:
36: ```python
37: {
38:     'data': [
39:         'report/my_report_templates.xml',
40:     ],
41: }
42: ```
43:
44: ---
45:
46: ## PDF Report Definition
47:
48: ### Report Action (XML)
49:
50: ```xml
51: <?xml version="1.0" encoding="utf-8" ?>
52: <odoo>
53:     <!-- Report Action -->
54:     <record id="report_my_model" model="ir.actions.report">
55:         <field name="name">My Report</field>
56:         <field name="model">my.model</field>
57:         <field name="report_type">qweb-pdf</field>
58:         <field name="report_name">my_module.report_my_model_document</field>
59:         <field name="report_file">my_module.report_my_model_document</field>
60:         <field name="print_report_name">'MyReport - %s' % object.name</field>
61:         <field name="binding_model_id" ref="model_my_model" />
62:         <field name="binding_type">report</field>
63:         <field name="paperformat_id" ref="base.paperformat_euro" />
64:     </record>
65:
66:     <!-- Report Template -->
67:     <template id="report_my_model_document">
68:         <t t-call="web.html_container">
69:             <t t-foreach="docs" t-as="doc">
70:                 <t t-call="web.external_layout">
71:                     <div class="page">
72:                         <h2>
73:                             <span t-field="doc.name" />
74:                         </h2>
75:
76:                         <div class="row mt-4">
77:                             <div class="col-6">
78:                                 <strong>Customer:</strong>
79:                                 <span t-field="doc.partner_id.name" />
80:                             </div>
81:                             <div class="col-6 text-end">
82:                                 <strong>Date:</strong>
83:                                 <span t-field="doc.date" />
84:                             </div>
85:                         </div>
86:
87:                         <table class="table table-sm mt-4">
88:                             <thead>
89:                                 <tr>
90:                                     <th>Description</th>
91:                                     <th class="text-end">Quantity</th>
92:                                     <th class="text-end">Price</th>
93:                                     <th class="text-end">Total</th>
94:                                 </tr>
95:                             </thead>
96:                             <tbody>
97:                                 <t t-foreach="doc.line_ids" t-as="line">
98:                                     <tr>
99:                                         <td><span t-field="line.name" /></td>
100:                                         <td class="text-end">
101:                                             <span t-field="line.quantity" />
102:                                         </td>
103:                                         <td class="text-end">
104:                                             <span
105:                         t-field="line.price_unit"
106:                         t-options='{"widget": "monetary",
107:                                                               "display_currency": doc.currency_id}'
108:                       />
109:                                         </td>
110:                                         <td class="text-end">
111:                                             <span
112:                         t-field="line.subtotal"
113:                         t-options='{"widget": "monetary",
114:                                                               "display_currency": doc.currency_id}'
115:                       />
116:                                         </td>
117:                                     </tr>
118:                                 </t>
119:                             </tbody>
120:                             <tfoot>
121:                                 <tr>
122:                                     <td colspan="3" class="text-end">
123:                                         <strong>Total:</strong>
124:                                     </td>
125:                                     <td class="text-end">
126:                                         <strong>
127:                                             <span
128:                         t-field="doc.amount_total"
129:                         t-options='{"widget": "monetary",
130:                                                               "display_currency": doc.currency_id}'
131:                       />
132:                                         </strong>
133:                                     </td>
134:                                 </tr>
135:                             </tfoot>
136:                         </table>
137:
138:                         <div t-if="doc.notes" class="mt-4">
139:                             <strong>Notes:</strong>
140:                             <p t-field="doc.notes" />
141:                         </div>
142:                     </div>
143:                 </t>
144:             </t>
145:         </t>
146:     </template>
147: </odoo>
148: ```
149:
150: ---
151:
152: ## QWeb Template Syntax
153:
154: ### Basic Output
155:
156: ```xml
157: <!-- Text content -->
158: <span t-field="doc.name"/>
159:
160: <!-- With formatting -->
161: <span t-field="doc.date" t-options='{"format": "dd/MM/yyyy"}'/>
162:
163: <!-- Raw output (no escaping) -->
164: <span t-out="doc.html_content"/>
165:
166: <!-- Escaped output -->
167: <span t-esc="doc.description"/>
168: ```
169:
170: ### Field Widgets
171:
172: ```xml
173: <!-- Monetary -->
174: <span t-field="doc.amount"
175:       t-options='{"widget": "monetary",
176:                   "display_currency": doc.currency_id}'/>
177:
178: <!-- Date -->
179: <span t-field="doc.date"
180:       t-options='{"format": "MMMM dd, yyyy"}'/>
181:
182: <!-- Float precision -->
183: <span t-field="doc.quantity"
184:       t-options='{"precision": 2}'/>
185:
186: <!-- Duration -->
187: <span t-field="doc.duration"
188:       t-options='{"widget": "duration",
189:                   "unit": "hour"}'/>
190:
191: <!-- Image -->
192: <img t-att-src="image_data_uri(doc.image)"
193:      style="max-width: 200px;"/>
194:
195: <!-- Barcode -->
196: <img t-att-src="'/report/barcode/?barcode_type=Code128&amp;value=%s&amp;width=200&amp;height=50' % doc.code"/>
197: ```
198:
199: ### Conditionals
200:
201: ```xml
202: <!-- If -->
203: <div t-if="doc.state == 'draft'">
204:     <span class="badge bg-secondary">Draft</span>
205: </div>
206:
207: <!-- If-Else -->
208: <t t-if="doc.amount > 0">
209:     <span class="text-success" t-field="doc.amount"/>
210: </t>
211: <t t-else="">
212:     <span class="text-muted">0.00</span>
213: </t>
214:
215: <!-- If-Elif-Else -->
216: <t t-if="doc.state == 'done'">Done</t>
217: <t t-elif="doc.state == 'cancel'">Cancelled</t>
218: <t t-else="">In Progress</t>
219: ```
220:
221: ### Loops
222:
223: ```xml
224: <!-- Basic loop -->
225: <t t-foreach="doc.line_ids" t-as="line">
226:     <tr>
227:         <td t-esc="line.name"/>
228:         <td t-esc="line.quantity"/>
229:     </tr>
230: </t>
231:
232: <!-- Loop with index -->
233: <t t-foreach="doc.line_ids" t-as="line">
234:     <tr>
235:         <td t-esc="line_index + 1"/>  <!-- 0-based index -->
236:         <td t-esc="line.name"/>
237:     </tr>
238: </t>
239:
240: <!-- Loop variables -->
241: <!-- line_index: current index (0-based) -->
242: <!-- line_first: True if first iteration -->
243: <!-- line_last: True if last iteration -->
244: <!-- line_odd: True if odd iteration (1-based) -->
245: <!-- line_even: True if even iteration -->
246: <!-- line_size: total items -->
247: ```
248:
249: ### Attributes
250:
251: ```xml
252: <!-- Dynamic class -->
253: <tr t-att-class="'table-danger' if line.amount &lt; 0 else ''">
254:
255: <!-- Dynamic style -->
256: <span t-att-style="'color: red;' if doc.overdue else ''"/>
257:
258: <!-- Multiple attributes -->
259: <div t-attf-class="alert alert-#{doc.state == 'done' and 'success' or 'warning'}"/>
260: ```
261:
262: ### Variables
263:
264: ```xml
265: <!-- Set variable -->
266: <t t-set="total" t-value="sum(doc.line_ids.mapped('amount'))"/>
267: <span t-esc="total"/>
268:
269: <!-- String formatting -->
270: <t t-set="title" t-value="'Invoice %s' % doc.name"/>
271: ```
272:
273: ---
274:
275: ## External Layout
276:
277: ### Using Company Header/Footer
278:
279: ```xml
280: <template id="report_my_document">
281:     <t t-call="web.html_container">
282:         <t t-foreach="docs" t-as="doc">
283:             <!-- Uses company letterhead -->
284:             <t t-call="web.external_layout">
285:                 <div class="page">
286:                     <!-- Your content here -->
287:                 </div>
288:             </t>
289:         </t>
290:     </t>
291: </template>
292: ```
293:
294: ### Minimal Layout (No Header/Footer)
295:
296: ```xml
297: <template id="report_my_document">
298:     <t t-call="web.html_container">
299:         <t t-foreach="docs" t-as="doc">
300:             <t t-call="web.basic_layout">
301:                 <div class="page">
302:                     <!-- Your content here -->
303:                 </div>
304:             </t>
305:         </t>
306:     </t>
307: </template>
308: ```
309:
310: ---
311:
312: ## Custom Report Logic
313:
314: ### Python Report Model
315:
316: ```python
317: # report/my_report.py
318: from odoo import api, models
319:
320:
321: class MyReport(models.AbstractModel):
322:     _name = 'report.my_module.report_my_model_document'
323:     _description = 'My Report'
324:
325:     @api.model
326:     def _get_report_values(self, docids, data=None):
327:         """Prepare report data."""
328:         docs = self.env['my.model'].browse(docids)
329:
330:         # Calculate totals
331:         totals = {
332:             'amount': sum(docs.mapped('amount_total')),
333:             'count': len(docs),
334:         }
335:
336:         # Get additional data
337:         categories = docs.mapped('category_id')
338:
339:         return {
340:             'doc_ids': docids,
341:             'doc_model': 'my.model',
342:             'docs': docs,
343:             'data': data,
344:             'totals': totals,
345:             'categories': categories,
346:             'company': self.env.company,
347:             'format_amount': self._format_amount,
348:         }
349:
350:     def _format_amount(self, amount, currency):
351:         """Format amount with currency."""
352:         return currency.format(amount)
353: ```
354:
355: ### Using Custom Values in Template
356:
357: ```xml
358: <template id="report_my_model_document">
359:     <t t-call="web.html_container">
360:         <t t-foreach="docs" t-as="doc">
361:             <t t-call="web.external_layout">
362:                 <div class="page">
363:                     <!-- Use custom values -->
364:                     <p>Total Records: <t t-esc="totals['count']" /></p>
365:                     <p>Grand Total: <t
366:               t-esc="format_amount(totals['amount'], doc.currency_id)"
367:             /></p>
368:
369:                     <!-- Access categories -->
370:                     <ul>
371:                         <t t-foreach="categories" t-as="cat">
372:                             <li t-esc="cat.name" />
373:                         </t>
374:                     </ul>
375:                 </div>
376:             </t>
377:         </t>
378:     </t>
379: </template>
380: ```
381:
382: ---
383:
384: ## Paper Format
385:
386: ### Define Custom Paper Format
387:
388: ```xml
389: <record id="paperformat_custom" model="report.paperformat">
390:     <field name="name">Custom Format</field>
391:     <field name="default" eval="False"/>
392:     <field name="format">A4</field>
393:     <field name="orientation">Portrait</field>
394:     <field name="margin_top">40</field>
395:     <field name="margin_bottom">20</field>
396:     <field name="margin_left">7</field>
397:     <field name="margin_right">7</field>
398:     <field name="header_line" eval="False"/>
399:     <field name="header_spacing">35</field>
400:     <field name="dpi">90</field>
401: </record>
402:
403: <!-- Use in report -->
404: <record id="report_my_model" model="ir.actions.report">
405:     <field name="paperformat_id" ref="paperformat_custom"/>
406: </record>
407: ```
408:
409: ### Standard Paper Formats
410:
411: - `base.paperformat_euro` - A4 Portrait
412: - `base.paperformat_us` - Letter Portrait
413:
414: ---
415:
416: ## Print from Python
417:
418: ### Single Record
419:
420: ```python
421: def action_print(self):
422:     """Print report for current record."""
423:     return self.env.ref('my_module.report_my_model').report_action(self)
424: ```
425:
426: ### Multiple Records
427:
428: ```python
429: def action_print_selected(self):
430:     """Print report for selected records."""
431:     return self.env.ref('my_module.report_my_model').report_action(self.ids)
432: ```
433:
434: ### With Custom Data
435:
436: ```python
437: def action_print_with_data(self):
438:     """Print with custom parameters."""
439:     data = {
440:         'date_from': self.date_from,
441:         'date_to': self.date_to,
442:         'include_draft': self.include_draft,
443:     }
444:     return self.env.ref('my_module.report_my_model').report_action(
445:         self, data=data
446:     )
447: ```
448:
449: ---
450:
451: ## CSS Styling
452:
453: ### Inline Styles
454:
455: ```xml
456: <style>
457:     .my-report-table {
458:         width: 100%;
459:         border-collapse: collapse;
460:     }
461:     .my-report-table th {
462:         background-color: #f5f5f5;
463:         border-bottom: 2px solid #333;
464:     }
465:     .my-report-table td {
466:         border-bottom: 1px solid #ddd;
467:         padding: 8px;
468:     }
469:     .page-break {
470:         page-break-after: always;
471:     }
472: </style>
473: ```
474:
475: ### External Stylesheet
476:
477: ```xml
478: <!-- In manifest assets -->
479: 'assets': {
480:     'web.report_assets_common': [
481:         'my_module/static/src/scss/report.scss',
482:     ],
483: },
484: ```
485:
486: ---
487:
488: ## Multi-Page Reports
489:
490: ### Page Breaks
491:
492: ```xml
493: <t t-foreach="docs" t-as="doc">
494:     <div class="page">
495:         <!-- Page content -->
496:     </div>
497:     <t t-if="not doc_last">
498:         <div class="page-break" />
499:     </t>
500: </t>
501: ```
502:
503: ### Grouped Reports
504:
505: ```xml
506: <t t-set="grouped" t-value="docs.grouped('category_id')"/>
507: <t t-foreach="grouped.items()" t-as="group">
508:     <div class="page">
509:         <h2 t-esc="group[0].name or 'Uncategorized'"/>
510:         <t t-foreach="group[1]" t-as="doc">
511:             <!-- Document content -->
512:         </t>
513:     </div>
514: </t>
515: ```
516:
517: ---
518:
519: ## Report Inheritance
520:
521: ### Extend Existing Report
522:
523: ```xml
524: <template
525:   id="report_invoice_document_inherit"
526:   inherit_id="account.report_invoice_document"
527: >
528:     <xpath expr="//div[@name='invoice_address']" position="after">
529:         <div class="col-6">
530:             <strong>Custom Field:</strong>
531:             <span t-field="o.x_custom_field" />
532:         </div>
533:     </xpath>
534: </template>
535: ```
536:
537: ---
538:
539: ## Best Practices
540:
541: 1. **Use external_layout** for professional documents with company header
542: 2. **Test PDF rendering** - wkhtmltopdf may render differently than browser
543: 3. **Handle empty data** - Use `t-if` to check before displaying
544: 4. **Format currencies properly** - Always use monetary widget with currency
545: 5. **Escape user content** - Use `t-esc` or `t-field` to prevent XSS
546: 6. **Add page breaks** - Use CSS `page-break-after: always` between records
547: 7. **Optimize images** - Resize before including in reports
548: 8. **Test multi-record** - Verify reports work with multiple records

(End of file - total 548 lines)
</content>
````

**Tool: websearch**

**Input:**

```json
{
  "query": "tutorial crear reports QWeb PDF Odoo 18 youtube 2024 2025 paso a paso",
  "numResults": 10,
  "type": "deep"
}
```

**Output:**

```
Title: 26. Odoo 18 Tutorial: How to Print PDF Reports | QWeb PDF Report in ...
URL: https://www.youtube.com/watch?v=2LSyfJnZACw
Published: 2026-03-07T17:04:26.000Z
Author: WOWDOO
Highlights:
# 26. Odoo 18 Tutorial: How to Print PDF Reports | QWeb PDF Report in Odoo 18 (Step-by-Step)
...
Learn how to generate and print PDF reports in Odoo 18 using QWeb reports.
...
In this tutorial, I will show you step-by-step how to create a PDF report in Odoo 18 and print it directly from the system. This guide is perfect for Odoo developers, beginners, and ERP learners who want to understand how the Odoo reporting system works.
...
In this video you will learn:

✅ How the Odoo reporting system works

✅ Creating a QWeb report template

✅ Using report_type="qweb-pdf"

✅ Printing reports in PDF format

✅ Testing the report inside Odoo
...
Hello everyone. In the last video, we talked about compute display name method in OD 18in. In today's video, we are going to talk about how to print PDF in Odin.
...
To create a PDF file, we have to deal with two files. For that, let's create a uh directory first named report.
...
This is just a convention. You can name it um anything you want. And inside that we have to create two XML files. one is for the Q web template which basically shows the PDF and a report record in in the IR.Actions report model we have to create a record which is B which basically works as the connector between the u between the template and PDU. So let's create the report file first. I will name the report file as student card student card report doxml and the second one is the uh the Q web template. So I will name it like student card report template dot XML.
...
First of all, I will create a a record inside the ODUS built-in IR.Actions.report model. So first of all, let's create the boiler plate code of X of an XML file of a XML file as you know. So XML and the encoding should be UT F8.
...
Okay. Now we have to we have to mention the report type.
...
Report type. There are different types of report um types like QB, HTML, QB, PDF. But as we are creating a PDF report here. So we will we will go with the report type as Q web PDF.
...
This is the module name and dot the exact id of the report template file. So give this temp uh this report name as a student card report template. Later we will be creating a template in this report template.xml XML file with this a student card report template id. So this is basically the connection between this report record and our wouldbe created would be created template doxml file. So this is the connection. Now we have to mention two other things which is binding model ID and binding type. So let's create that.
...
And here we have to mention the model ID as the ref attributes value. So the first thing we have to do is we have to use this model prefix and then we have to write the model name like this a student instead of dot we have to use underscore and the second word. So model a student card and then the final thing we have to do is we have to mention the binding type and so we have to mention binding type like this and as the value we have to pass report. So these two lines basically are needed to uh render our PDF successfully. If we don't use these two lines, then our report may not be rendered successfully.
...
Okay. Now inside this we have to call a built-in uh a built-in template in ODO which is already built in ODO and uh we have to call that which is web dot HTML container.
...
So we have to mention the htm we have to use the html container and inside this we have to use a special object which is docs this is provided by odo so let's use that first we have to loop through that docs object let's write that first then I will explain what it is doing basically so t uh t for h t for H equals docs and T as let's say O and inside this we have to use another uh built-in template which is um web dot external layout. So we have to call that web web dot external layout.
...
It will take some time. Now if we go here in this in this form view and refresh the page. Now if you click on this gear icon we will see a third option for printing a PDF. Let's click.
...
This name is coming from this name attributes value which is print a student card. Now when when we click on this we when we click on this button what what we will do it will find that template using this ID and render a Q web temp uh a Q web template um and then it will um uh it will compile that Q web template to HTML and then the WK HTML to PDF uh PDF renderer engine will uh convert this HTML ML to a PDF view. So now if we click on this, let's see what happens if we get any error or not.
...
But we cannot uh do it like um in HTML. In HTML we just mention the path like um something the u the path and image dotpng. We we cannot do this here because in odo the image file is not loaded as a file. It's it's it it it's basically loaded as a character or base 64 string. So we have to uh we have to make our uh browser understand that u this is uh something that um this is something that that that is not like a uh direct image file. This is a base 64 string. So we have to make that thing to our browser and u tell our browser that you need to convert this thing as a PNG image. So now what uh the first thing uh that we have to do is we have to write a data colon image / PNZ base 64 and after this we will have we will have our exact image object. So um before that we have to um place this string inside another uh quotation another single quotation and inside in in the place of this percentage s we will have our actual image object. So where is our um uh where is our main student record inside this O this O object. So we can refer to this student object using o and uh access to the image uh field using dot the field name which is image okay image now image sorry not here image but let's say um we don't have a uh image for a student then what it will do it will get an error uh so we have to check this this thing also If the O do image exists then and only then do this thing otherwise we will use a built-in image of ODO which uh we can use from the web module if we go to the add-ons and go to this web module and inside this if we go to this static and go to the um image then here we can see that there is a image uh image named placeholder placeholder.png PNG. So we will use this. So we have to go to the web module web module and inside that we have to go to the static folder or directory and inside that we have the img directory and inside that we have a we have the placeholder placeholder.png file. Now there is one thing which is left to do. We are we are um we are just passing the image of object itself inside this uh string uh in the place of this percentages. But we have to the image is encoded with the basics string.
...
First of all we have to decode that um encoded image file uh using UTF8. So decode dot decode call the dot uh decode method on this image object and inside that we have to mention UTF8.
...
Okay. Now, what we have to do? We have to like H1 we we can use the H1 tag here to render the name and we can use the TSC directive ESC directive to print the value of an of a field. So O dot name the field name is name.
...
Now we can see that we have the image, we have the name, we have the age and we have the gender value. Now let's style this whole thing. We will style our card exactly like this. Okay. So now first of all let's let's place all these contents all of these contents inside a div named um with a class named student_c card inside this place all of this let's format at it. Now this content, let's place these three um elements inside another div uh with a class named card body.
...
That's it. And the image let's and the image should have exact the same width of its parent which is a student card. So let's use the image tag and let's mention the width as 100% of its parent and then work with the card body class.
...
And there it is. We have got this exact thing. These two things are exactly the same. So this is it. We have seen how to create a PDF file in UDO 18. How to create a card in ODO 18. So this is it for today.

---

Title: QWeb Odoo 📄 ¿Qué Son y Cómo funcionan? | Acciones de Reporte con ir.actions.report | De Acción a PDF - YouTube
URL: https://www.youtube.com/watch?v=YhEu2ueX-Fk
Published: 2026-02-25T12:00:00.000Z
Author: N/A
Highlights:
QWeb Odoo 📄 ¿Qué Son y Cómo funcionan? | Acciones de Reporte con ir.actions.report | De Acción a PDF - YouTube
...
QWeb Odoo 📄 ¿Qué Son y Cómo funcionan? | Acciones de Reporte con ir.actions.report | De Acción a PDF - YouTube

---

Title: Build PDF Reports — Odoo 18.0 documentation
URL: https://www.odoo.com/documentation/18.0/developer/tutorials/pdf_reports.html
Published: N/A
Author: N/A
Highlights:
Build PDF Reports — Odoo 18.0 documentation
...
# Build PDF Reports¶
...
This tutorial is an extension of the Server framework 101 tutorial. Make sure you have completed it and use the`estate` module you have built as a base for the exercises in this tutorial.
...
We were previously introduced to QWeb where it was used to build a kanban view. Now we will expand on one of QWeb’s other main uses: creating PDF reports. A common business requirement is the ability to create documents to send to customers and to use internally. These reports can be used to summarize and display information in an organized template to support the business in different ways. Odoo can additionally add our company’s header and footer to our reports with minimal extra effort.
...
The documentation related to this topic can be found in QWeb Templates, QWeb Reports, and the Report Actions (ir.actions.report) section of the Actions reference.
...
The bulk of a PDF report is its QWeb template. It also typically needs a corresponding`ir.actions.report` to include the report within a module’s business logic. There is no strict rule for the file names or where they are located, but these two parts are typically stored in 2 separate files within a`report` folder at the top level of your module’s directory. If a module has many or multiple long report templates, then they are often organized logically across different files named after the report(s) they contain. All actions for the reports are usually stored in the same file ending with`_reports.xml`, regardless of the number of reports it contains.
...
Don’t forget to add whatever files your template and action view will be into to your`__manifest__.py`. In this case, you will want to add the files to the`data` list and remember that the files listed in a manifest are loaded sequentially!
...
## Basic Report¶
...
Goal: at the end of this section, we will be able to print a report that displays all offers for a property.
...
Before we do anything we first need some data to populate our reports or else this tutorial won’t be very interesting. When creating reports, you will need some data to test your report code and check that the resulting look is as expected. It is a good idea to test with data that will cover most or all of your expected use cases. A good representation set for our simple report is:
...
Copy this data file into a new directory (data) in your estate module and copy these lines into your __manifest__.py file (you may need to
...
a new database to load in the demo data).
...
### Minimal Template¶
...
A minimal viable template is viewable under the “Minimal viable template” section of the Report template documentation. We can modify this example to build our minimal property offers template file:
...
the Odoo
...
### Report Action¶
...
Now that we have a template, we need to make it accessible in our app via a`ir.actions.report`. A practical example of`ir.actions.report` is here corresponding to this template. Its contents are all explained in the documentation.
...
An`ir.actions.report` is primarily used via the Print menu of a model’s view. In the practical example, the`binding_model_id` specifies which model’s views the report should show, and Odoo will auto-magically add it for you. Another common use case of the report action is to link it to a button as we learned in Chapter 9: Ready For Some Action?. This is handy for reports that only make sense under specific conditions. For example, if we wanted to make a “Final Sale” report, then we can link it to a “Print Sale Info” button that appears in the form view only when the property is “Sold”.
...
### Make a Report¶
...
Finally, you now know where to create your files and how the content of the files should look. Happy report making!
...
Make a report.
...
Add the property offers report from the minimal template subsection to the Print menu of the Property views.
...
Improve the report by adding more data. Refer to the Goal of this section to see what additional data you can add and feel free to add even more.
...
Bonus: Make an extra flexible report by adding in some logic so that when there are no offers on a property then we don’t create a table and instead write something about how there are no offers yet. Hint: you will need to use`t-if` and`t-else`.
...
Remember to check that your PDF reports match your data as expected.
...
## Sub-templates¶
...
Goal: at the end of this section, we will have a sub-template that we use in 2 reports.
...
There are two main reasons for
...
. One is
...
-long or complicated
...
property offers information
...
. One example
...
Create and use a sub-template.
...
Split the table portion of the offers into its own template. Remember to check that your original report still prints correctly afterwards.
...
Add a new report for`res.users` that allows you to print all of the Real Estate Properties that are visible in their form view (i.e. in the “Settings” app). Include the offers for each of those saleman’s properties in the same report. Hint: since the`binding_model_id` in this case will not be within the estate module, you will need to use`ref="base.model_res_users"`.
...
## Report Inheritance¶
...
Goal: at the end of this section, we will inherit the property report in the`estate_account` module.
...
Inheritance in QWeb uses the same`xpath` elements as views inheritance. A QWeb template refers to its parent template in a different way though. It is even easier to do by just adding the`inherit_id` attribute to the`template` element and setting it equal to the module.parent_template_id.
...
Additional Features¶
...
### Reports are web pages¶
...
You probably are tired of hearing that QWeb creates HTML, but we’re saying it again! One of the neat features of reports being written in QWeb is they can be viewed within the web browser. This can be useful if you want to embed a hyperlink that leads to a specific report. Note that the usual security checks will still apply to prevent unauthorized users from accessing the reports.

---

Title: How to Create a PDF Report in Odoo 18?
URL: https://www.cybrosys.com/blog/how-to-create-a-pdf-report-in-odoo-18
Published: N/A
Author: N/A
Highlights:
How to Create a PDF Report in Odoo 18?
...
# How to Create a PDF Report in Odoo 18?
...
Qweb is Odoo’s powerful templating engine, designed to easily convert XML data into HTML documents. Its feature set includes attribute-based customization, conditional logic, dynamic content insertion, and a range of report template options. This versatility makes Qweb ideal for crafting personalized, visually compelling reports, emails, and documents. From financial statements to invoices and complex business reports, Qweb streamlines the creation process, ensuring that each output is both clear and appealing.
...
In this guide, we will walk through creating a custom PDF report in Odoo 18 for the "hr.expense" model. This process involves building a Qweb template and setting up the corresponding report action, which will allow users to generate a PDF of expense details directly from the Odoo interface.
...
## Step-by-Step Guide to Creating a Custom PDF Report in Odoo 18
...
### * Create the Report Action (XML file)
...
Inside your module's "report" directory, create an XML file for the report action. Let's name it expense_reports.xml. This file will define the report action that binds the report to the model. Below is an example of what the XML file might contain:
...
```

<?xml version="1.0" encoding="UTF-8"?><odoo>    <!--    Report Function in Expense -->    <record id="action_expense_request_report" model="ir.actions.report">        <field name="name">Expense Report</field>        <field name="model">hr.expense</field>        <field name="report_type">qweb-pdf</field>        <field name="report_name">expense_report_odoo.report_expense_report_details</field>        <field name="report_file">expense_report_odoo.report_expense_report_details</field>        <field name="binding_model_id" ref="hr_expense.model_hr_expense"/>        <field name="binding_type">report</field>    </record></odoo>

... In this XML file, we define a report action using the following fields: ...

#### 1. Name (name):

... The name of the report action is specified using the name field. It helps identify
the report within the system. In our example, it’s set to "Expense Report". ...

#### 2. Model (model):

... This field defines the model that the report is associated with. The report
retrieves data from this model. In our case, the model is "hr.expense", which means the
report will display data from the hr expense model. ...

#### 3. Report Type (report_type):

... This specifies the type of report being generated. The available options are: ...

- qweb-pdf: For generating PDF reports using QWeb templates.

- qweb-html: For generating HTML reports using QWeb templates.

- qweb-text: For generating plain text reports using QWeb templates. ... In our example,
  we’re generating a PDF report, so the report_type is set to "qweb-pdf". ...

#### 4. Report Name (report_name):

... This field specifies the internal name of the report template. It links the report
action to the QWeb template that will be used to generate the output. In our case, the
report name is "module_name.report_expense_report_details". ...

#### 5. Report File (report_file):

... The report_file defines the name of the QWeb template file used for the report. This
file contains the XML structure for rendering the report. It’s set to
"module_name.report_expense_report_details". ...

#### 6. Binding Model ID (binding_model_id):

... This is a reference to the model associated with the report action, linking it to
other objects. Here, it references the hr expense model: "hr_expense.model_hr_expense".
...

#### 7. Binding Type (binding_type):

... This defines how the ... is bound to the system. The two options are: ...

- action: Binds the report to a specific action.

- report: Binds the report directly to a record of the specified model. ... the case of
  the ... , it will ... a new report option ... " menu for ... .expense model ... as
  demonstrated in the screenshot below. ...

### Create the QWeb Template (XML file)

... Next, we need to create the QWeb template, which defines the structure and layout of
the PDF report. This file should be placed in the report directory and named
expense_report_templates.xml. Below is an example of a simple QWeb template for the
report: ...

```
<?xml version="1.0" encoding="UTF-8" ?><odoo>    <!--    Report Template-->    <template id="report_expense_report_details">        <t t-call="web.html_container">           <t t-foreach="docs" t-as="o">                <t t-call="web.external_layout">                    <div class="page">                        <div class="oe_structure"/>                        <h2>Expense Report</h2>                        <br></br>                        <p>                            Name :                            <span t-field="o.employee_id.name"/>                        </p>                    </div>                </t>            </t>        </t>    </template></odoo>
...
In this QWeb template file, we define a structure using the template ID, which matches the report_name specified in the report action XML. The t-foreach loop iterates through the list of records (docs) and generates a report page for each product. Inside the template, HTML tags and QWeb expressions are used to format and display the data as needed.
...
This basic template will generate a PDF report that includes the expense report details, as shown below.
...
Creating PDF reports in Odoo 18 using Qweb is a straightforward process that combines powerful templating capabilities with a simple XML configuration. By defining a report action and crafting a custom Qweb template, you can generate detailed and well-structured PDF documents tailored to your business needs. This guide provides a foundation to help you create personalized reports that seamlessly integrate into your Odoo workflows, improving data presentation and accessibility.

---

Title: Creación de Plantillas QWeb | Reportes en Odoo #odoocustomization #xml #template "#qweb #odoosupport
URL: https://www.youtube.com/watch?v=wDUCOwAfNtk
Published: 2026-03-06T12:00:00.000Z
Author: Josuhe Uh
Highlights:
# Creación de Plantillas QWeb | Reportes en Odoo #odoocustomization #xml #template "#qweb #odoosupport
...
Parte de un video donde explico la estructura XML que compone un informe QWEB en Odoo.
...
▶ Video completo: https://youtu.be/FjpOBMMcKHU
...
▶ Curso completo: https://www.youtube.com/playlist?list=PLXwzJRuH--eZKw4KLwGbCKAHmKUlPhT_X
...
Lo que vamos a ver en este video es justamente esta parte, la creación de la plantilla QB que posteriormente va a generar el HTML dinámico. Para definir una plantilla Qeb se usa la etiqueta template. Este se define en un documento XML. Tenemos el documento reporte.xml y aquí va a estar nuestra plantilla Qweb. En este documento se va a encontrar la etiqueta template.

---

Title: Build PDF Reports — documentación de Odoo - saas-18.4
URL: https://www.odoo.com/documentation/saas-18.4/es/developer/tutorials/pdf_reports.html
Published: N/A
Author: N/A
Highlights:
Build PDF Reports — documentación de Odoo - saas-18.4
...
# Build PDF Reports¶
...
This tutorial is an extension of the Server framework 101 tutorial. Make sure you have completed it and use the`estate` module you have built as a base for the exercises in this tutorial.
...
We were previously introduced to QWeb where it was used to build a kanban view. Now we will expand on one of QWeb’s other main uses: creating PDF reports. A common business requirement is the ability to create documents to send to customers and to use internally. These reports can be used to summarize and display information in an organized template to support the business in different ways. Odoo can additionally add our company’s header and footer to our reports with minimal extra effort.
...
The documentation related to this topic can be found in QWeb Templates, QWeb Reports, and the Report Actions (ir.actions.report) section of the Actions reference.
...
The bulk of a PDF report is its QWeb template. It also typically needs a corresponding`ir.actions.report` to include the report within a module’s business logic. There is no strict rule for the file names or where they are located, but these two parts are typically stored in 2 separate files within a`report` folder at the top level of your module’s directory. If a module has many or multiple long report templates, then they are often organized logically across different files named after the report(s) they contain. All actions for the reports are usually stored in the same file ending with`_reports.xml`, regardless of the number of reports it contains.
...
Don’t forget to add whatever files your template and action view will be into to your`__manifest__.py`. In this case, you will want to add the files to the`data` list and remember that the files listed in a manifest are loaded sequentially!
...
## Basic Report¶
...
Goal: at the end of this section, we will be able to print a report that displays all offers for a property.
...
Before we do anything we first need some data to populate our reports or else this tutorial won’t be very interesting. When creating reports, you will need some data to test your report code and check that the resulting look is as expected. It is a good idea to test with data that will cover most or all of your expected use cases. A good representation set for our simple report is:
...
Complete the Define module data tutorial (if you haven’t done so already) and add the extra cases to your
...
data (you
...
Copy this data file into a new directory (data) in your estate module and copy these lines into your __manifest__.py file (you may need to create a new database to load in the demo data).
...
### Minimal Template¶
...
A minimal viable template is viewable under the «Minimal viable template» section of the Report template documentation. We can modify this example to build our minimal property offers template file:
...
the Odoo
...
(i.e. non-HTML) items
...
### Report Action¶
...
Now that we have a template, we need to make it accessible in our app via a`ir.actions.report`. A practical example of`ir.actions.report` is here corresponding to this template. Its contents are all explained in the documentation.
...
An`ir.actions.report` is primarily used via the Print menu of a model’s view. In the practical example, the`binding_model_id` specifies which model’s views the report should show, and Odoo will auto-magically add it for you. Another common use case of the report action is to link it to a button as we learned in Chapter 9: Ready For Some Action?. This is handy for reports that only make sense under specific conditions. For example, if we wanted to make a «Final Sale» report, then we can link it to a «Print Sale Info» button that appears in the form view only when the property is «Sold».
...
### Make a Report¶
...
Finally, you now know where to create your files and how the content of the files should look. Happy report making!
...
Make a report.
...
Add the property offers report from the minimal template subsection to the Print menu of the Property views.
...
Improve the report by adding more data. Refer to the Goal of this section to see what additional data you can add and feel free to add even more.
...
Bonus: Make an extra flexible report by adding in some logic so that when there are no offers on a property then we don’t create a table and instead write something about how there are no offers yet. Hint: you will need to use`t-if` and`t-else`.
...
Remember to check that your PDF reports match your data as expected.
...
## Sub-templates¶
...
Goal: at the end of this section, we will have a sub-template that we use in 2 reports.
...
There are two main reasons
...
Create and use a sub-template.
...
Split the table portion of the offers into its own template. Remember to check that your original report still prints correctly afterwards.
...
Add a new report for`res.users` that allows you to print all of the Real Estate Properties that are visible in their form view (i.e. in the «Settings» app). Include the offers for each of those saleman’s properties in the same report. Hint: since the`binding_model_id` in this case will not be within the estate module, you will need to use`ref="base.model_res_users"`.
...
## Report Inheritance¶
...
Goal: at the end of this section, we will inherit the property report in the`estate_account` module.
...
Inheritance in QWeb uses the same`xpath` elements as views inheritance. A QWeb template refers to its parent template in a different way though. It is even easier to do by just adding the`inherit_id` attribute to the`template` element and setting it equal to the module.parent_template_id.
...
## Additional Features¶
...
### Reports are web pages¶
...
You probably are tired of hearing that QWeb creates HTML, but we’re saying it again! One of the neat features of reports being written in QWeb is they can be viewed within the web browser. This can be useful if you want to embed a hyperlink that leads to a specific report. Note that the usual security checks will still apply to prevent unauthorized users from accessing the reports.

---

Title: Día 21: Creación de Informes PDF con QWeb — Documentos Imprimibles | Angel Moya
URL: https://angelmoya.es/blog/odoo/dia-21-creacion-de-informes-pdf-con-qweb-documentos-imprimibles/
Published: 2025-12-21T06:00:00.000Z
Author: Angel Moya
Highlights:
Día 21: Creación de Informes PDF con QWeb — Documentos Imprimibles | Angel Moya
...
final del reto
...
En Odoo (V19), los informes PDF se basan en una estructura de tres partes: una Acción de Reporte que invoca el informe, un Motor de Plantillas (QWeb) que renderiza el contenido, y el uso de Wkhtmltopdf (un motor de renderizado de HTML a PDF).
...
Hemos añadido el código XML necesario para definir la acción de reporte y la vista de plantilla QWeb que formará el cuerpo de nuestro PDF.
...
### 1. La Acción de Reporte (ir.actions.report)
...
Esta acción de XML es el punto de inicio para la generación del informe. Define los metadatos del PDF:
...
- model: El modelo en el que se basa el informe.
- report_type: Generalmente qweb-pdf.
- report_name: El nombre técnico de la plantilla QWeb que contiene el diseño.
- name: El nombre que aparece en el menú de impresión y en el nombre del archivo PDF.
...
### 2. La Plantilla QWeb
...
QWeb es el lenguaje de plantillas que utiliza sintaxis HTML enriquecida con directivas Odoo (t-if, t-foreach, t-field). Esta plantilla es la que diseña el contenido.
...
- Estructura: La plantilla debe heredar o incluir las estructuras base de Odoo para obtener los estilos, el header y el footer (si no, el PDF saldrá sin ellos).
- Acceso a Datos: Dentro de QWeb, los registros del modelo se acceden a través de la variable docs.
- Ejemplo Básico: … para iterar sobre los registros seleccionados.
...
### 3. El Botón de Impresión
...
Para que el usuario pueda generar el PDF desde el formulario, añadimos un botón especial en la vista Formulario:
...
- type=»report»: Indica que este botón debe ejecutar una acción de reporte.
- name: Debe ser el ID externo de la ir.actions.report.
...
## Explicación
...
allada en Vídeo
...
En el siguiente vídeo, te muestro la sintaxis de ir.actions.report, cómo estructurar la plantilla QWeb básica y cómo se accede a los campos de tu registro (o.campo_x) dentro del HTML.
...
Puedes consultar el código fuente completo de esta lección, con la definición de la acción de reporte y la plantilla QWeb de ejemplo, directamente en nuestro repositorio.
...
➡️ Ver el Código en GitLab: https://github.com/angelmoya/calendario-adviento-curso-tecnico-odoo-19/tree/d9d7e5ccded32a06ca86c11daa23758c60077e78
...
YouTube: ¡No olvides suscribirte al canal para no perderte ninguna lección! http://www.youtube.com/@AngelMoya-Odoo

---

Title: How to Create a PDF Report in Odoo 18 - Odoo  Slides | PPTX
URL: https://www.slideshare.net/slideshow/how-to-create-a-pdf-report-in-odoo-18-odoo-slides/281357232
Published: 2025-07-07T06:47:15.000Z
Author: N/A
Highlights:
How to Create a PDF Report in Odoo 18 - Odoo Slides | PPTX
...
# How to Create a PDF Report in Odoo 18 - Odoo Slides
...
In Odoo 18, creating a PDF report involves defining a report template using QWeb, linking it to a model, and customizing its structure. The process includes setting up an XML report definition, designing the layout with a QWeb template, and integrating it into your module.

---

Title: How to create pdf report in Odoo | Custom Report | Qweb PDF Report ...
URL: https://www.youtube.com/watch?v=uF4VkNFoDOI
Published: 2022-06-17T08:30:13.000Z
Author: WebLearns
Highlights:
# How to create pdf report in Odoo | Custom Report | Qweb PDF Report Tutorial
...
- Channel: WebLearns
- Length: 16:57
- Views: 8.1K
- Likes: 56
- Published: 2022-06-17T01:30:13-07:00
- Category: Education
- Keywords: odoo qweb pdf report, odoo qweb report tutorial, qweb report in odoo, simple pdf report generate in odoo, odoo pdf report create, odoo qweb, qweb template engine odoo, odoo qweb pdf, odoo qweb template, odoo qweb template engine pdf, odoo report qweb, how to generate pdf report in odoo, odoo qweb tutorial, odoo qweb pdf tutorial, generate pdf report in odoo, create pdf report in odoo, custom pdf report in odoo, custom qweb pdf report odoo, pdf report in odoo
...
- Language: en
...
How to create custom pdf report in Odoo? Generate qweb pdf report Odoo, design student card using qweb pdf report. Here in this tutorial you will going to see how to create simple pdf report using qweb report engine and here we will use odoo 14 community version. Please check till end of this discussion you will learn more about qweb pdf report.

In case you missed previous discussion about what is paper format and how to implement in qweb pdf report for different report size. Please check below link.

---

Title: QWeb Reports — Odoo 18.0 documentation
URL: https://www.odoo.com/documentation/18.0/th/developer/reference/backend/reports.html
Published: N/A
Author: N/A
Highlights:
QWeb Reports — Odoo 18.0 documentation
...
# QWeb Reports¶
...
Reports are written in HTML/QWeb, like website views in Odoo. You can use the usual QWeb control flow tools. The PDF rendering itself is performed by wkhtmltopdf.

Reports are declared using a report action, and a Report template for the action to use.
...
If useful or necessary, it is possible to specify a Paper Format for the report report.
...
## Report template¶
...
### Minimal viable template¶
...
A minimal template would look like:
...
```

<template id="report_invoice">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    <h2>Report title</h2>
                    <p>This object's name is <span t-field="o.name"/></p>
                </div>
            </t>
        </t>
    </t>
</template>
...
Calling`external_layout` will add the default header and footer on your report. The PDF body will be the content inside the` `. The template's`id` must be the name specified in the report declaration; for example`account.report_invoice` for the above report. Since this is a QWeb template, you can access all the fields of the`docs` objects received by the template.
...
### Translatable Templates¶
...
If you wish to translate reports (to the language of a partner, for example), you need to define two templates:
...
You can then call the translatable document from your main template with the attribute`t-lang` set to a language code (for example`fr` or`en_US`) or to a record field. You will also need to re-browse the related records with the proper context if you use fields that are translatable (like country names, sales conditions, etc.)
...
The main template calls the translatable template with`doc.partner_id.lang` as a`t-lang` parameter, so it will be rendered in the language of the partner. This way, each Sale Order will be printed in the language of the
...
customer. If you wish to translate only the body of the document, but keep the header and
...
in a default language, you could call the report'
...
external layout this way:
...
## Paper Format¶
...
Paper formats are records of`report.paperformat` and can contain
...
following attributes:
...
## Custom Reports¶
...
By default, the
...
system builds rendering values based on
...
specified through the
...
model` field.
...
However, it will first look for a model named`report.module.report
...
name` and call that model's`_get_report_values(doc_ids, data)` in order to prepare
...
rendering data for the template.
...
## Reports are web pages¶

Reports are dynamically generated by the report module and can be accessed directly via
URL:

For example, you can access a Sale Order report in html mode by going to http://
/report/html/sale.report_saleorder/38

Or you can access the pdf version at http:// /report/pdf/sale.report_saleorder/38

```

---

## Assistant (Odoo-Dev · Big Pickle · 53.7s)

_Thinking:_

Ahora tengo toda la información que necesito. Voy a proporcionar una explicación completa sobre cómo crear reports en Odoo 18, junto con enlaces a videos tutoriales en español.

Perfecto, ya tengo toda la información. Te voy a explicar cómo crear reports en Odoo 18 de forma clara y ordenada, y al final te dejo los mejores videos tutoriales que he encontrado.

---

## Guía para crear Reports en Odoo 18

### Estructura básica de un report

Un report en Odoo consta de **3 partes fundamentales**:

1. **Una acción de reporte** (`ir.actions.report`) — define los metadatos y conecta el report con el modelo
2. **Una plantilla QWeb** — define el diseño/contenido del PDF usando XML con sintaxis especial
3. **(Opcional) Un modelo Python** — para lógica personalizada de datos

### Estructura de archivos recomendada

```

mi_modulo/ ├── report/ │ ├── **init**.py │ ├── mi_report.py # Lógica Python (opcional) │
├── mi_report_action.xml # Acción ir.actions.report │ └── mi_report_templates.xml #
Plantilla QWeb └── **manifest**.py

````

### Paso 1: Definir la Acción del Reporte (XML)

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <!-- Acción del reporte -->
    <record id="report_mi_modelo" model="ir.actions.report">
        <field name="name">Mi Reporte</field>
        <field name="model">mi.modelo</field>
        <field name="report_type">qweb-pdf</field>
        <field name="report_name">mi_modulo.report_mi_modelo_plantilla</field>
        <field name="report_file">mi_modulo.report_mi_modelo_plantilla</field>
        <field name="print_report_name">'Mi Reporte - %s' % object.name</field>
        <field name="binding_model_id" ref="model_mi_modelo" />
        <field name="binding_type">report</field>
        <field name="paperformat_id" ref="base.paperformat_euro" />
    </record>
</odoo>
````

**Campos importantes:**

- `report_type`: `qweb-pdf` (PDF), `qweb-html` (HTML), o `qweb-text` (texto plano)
- `report_name`: referencia a la plantilla QWeb (formato: `modulo.plantilla_id`)
- `binding_model_id`: enlaza el report con el modelo, aparecerá en el menú "Imprimir"
- `binding_type`: `report` (aparece en menú) o `action`

### Paso 2: Crear la Plantilla QWeb (XML)

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <template id="report_mi_modelo_plantilla">
        <t t-call="web.html_container">
            <t t-foreach="docs" t-as="doc">
                <t t-call="web.external_layout">
                    <div class="page">
                        <h2>Mi Reporte</h2>

                        <div class="row mt-4">
                            <div class="col-6">
                                <strong>Nombre:</strong>
                                <span t-field="doc.name" />
                            </div>
                            <div class="col-6 text-end">
                                <strong>Fecha:</strong>
                                <span t-field="doc.date" />
                            </div>
                        </div>

                        <table class="table table-sm mt-4">
                            <thead>
                                <tr>
                                    <th>Descripción</th>
                                    <th class="text-end">Cantidad</th>
                                    <th class="text-end">Precio</th>
                                </tr>
                            </thead>
                            <tbody>
                                <t t-foreach="doc.line_ids" t-as="line">
                                    <tr>
                                        <td><span t-field="line.name" /></td>
                                        <td class="text-end">
                                            <span t-field="line.quantity" />
                                        </td>
                                        <td class="text-end">
                                            <span t-field="line.price_unit" />
                                        </td>
                                    </tr>
                                </t>
                            </tbody>
                        </table>
                    </div>
                </t>
            </t>
        </t>
    </template>
</odoo>
```

**Elementos QWeb clave:**

- `t-call="web.html_container"` — contenedor base del report
- `t-call="web.external_layout"` — añade cabecera/pie de empresa
- `t-foreach="docs" t-as="doc"` — itera sobre los registros seleccionados
- `t-field="doc.name"` — muestra el valor de un campo con formato
- `t-esc="doc.name"` — muestra el valor sin formato
- `t-if`, `t-else`, `t-elif` — condicionales
- `t-attf-class` — atributos dinámicos

### Paso 3: Actualizar el manifest

```python
{
    'data': [
        'report/mi_report_action.xml',
        'report/mi_report_templates.xml',
    ],
}
```

### Paso 4 (Opcional): Lógica Python personalizada

Si necesitas procesar datos antes de pasarlos al template:

```python
from odoo import api, models

class MiReport(models.AbstractModel):
    _name = 'report.mi_modulo.report_mi_modelo_plantilla'
    _description = 'Mi Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['mi.modelo'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': 'mi.modelo',
            'docs': docs,
            'company': self.env.company,
        }
```

### Formato de papel personalizado

```xml
<record id="paperformat_custom" model="report.paperformat">
    <field name="name">Formato Personalizado</field>
    <field name="format">A4</field>
    <field name="orientation">Portrait</field>
    <field name="margin_top">40</field>
    <field name="margin_bottom">20</field>
    <field name="margin_left">7</field>
    <field name="margin_right">7</field>
    <field name="dpi">90</field>
</record>
```

---

## Videos Tutoriales recomendados (en español)

1. **"QWeb Odoo - Qué Son y Cómo funcionan | Acciones de Reporte con
   ir.actions.report"**

   - https://www.youtube.com/watch?v=YhEu2ueX-Fk
   - Explica QWeb y las acciones de reporte desde cero

2. **"Creación de Plantillas QWeb | Reportes en Odoo"** (Josuhe Uh)

   - https://www.youtube.com/watch?v=wDUCOwAfNtk
   - Parte de un curso completo, explica la estructura XML de los informes QWeb
   - Curso completo:
     https://www.youtube.com/playlist?list=PLXwzJRuH--eZKw4KLwGbCKAHmKUlPhT_X

3. **"Día 21: Creación de Informes PDF con QWeb"** (Angel Moya - Calendario Adviento
   Odoo)

   - Blog:
     https://angelmoya.es/blog/odoo/dia-21-creacion-de-informes-pdf-con-qweb-documentos-imprimibles/
   - Código fuente:
     https://github.com/angelmoya/calendario-adviento-curso-tecnico-odoo-19

4. **"Odoo 18 Tutorial: How to Print PDF Reports | QWeb PDF Report"** (WOWDOO) — en
   inglés pero muy visual

   - https://www.youtube.com/watch?v=2LSyfJnZACw
   - Paso a paso completo con ejemplo de tarjeta de estudiante

5. **Documentación oficial Odoo 18** (tutorial interactivo con ejercicios)
   - https://www.odoo.com/documentation/18.0/developer/tutorials/pdf_reports.html
   - https://www.odoo.com/documentation/18.0/developer/reference/backend/reports.html

---

## Tips importantes

- **Usa `external_layout`** para documentos profesionales con cabecera/pie de empresa
- **Prueba el PDF** directamente — wkhtmltopdf puede renderizar diferente al navegador
- **Maneja datos vacíos** — usa `t-if` antes de mostrar tablas
- **Formatea monedas** siempre con el widget monetary y la moneda del registro
- **Escapa contenido de usuario** — usa `t-esc` o `t-field` para prevenir XSS
- **Añade saltos de página** entre registros con CSS `page-break-after: always`

Si quieres que te ayude a crear un report concreto para alguno de tus módulos (como
`socger_hospital` o `glv_basic_module`), ¡solo dime y lo hacemos juntos!

---

## User

Existe alguna herramienta de diseño de reportes que luego lo convierta a reporte
entendido por Odoo?

---

## Assistant (Odoo-Dev · Big Pickle · 11.0s)

_Thinking:_

El usuario pregunta si existen herramientas de diseño visual de reportes que puedan
generar código compatible con Odoo. Voy a buscar información sobre esto, ya que existen
algunas herramientas como QWeb Designer, report designers de Odoo Studio, y posiblemente
herramientas de terceros.

**Tool: websearch**

**Input:**

```json
{
  "query": "herramientas diseño visual reportes Odoo QWeb designer tool WYSIWYG 2024 2025",
  "numResults": 10,
  "type": "deep"
}
```

**Output:**

```
Title: Report Drag & Drop Builder (Advanced) | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/report_dragdrop
Published: N/A
Author: N/A
Highlights:
# Report Drag & Drop Builder (Advanced)
...
# Advanced Report Builder
...
## Drag & Drop QWeb Report Designer for Odoo 19
...
Create professional Odoo reports in minutes, without custom development. Empower your team to design, preview, and publish PDF or Word reports using a simple visual drag-and-drop builder.
...
Build professional reports visually without hardcoding templates. This module provides a complete report-building workflow with dynamic fields, one2many table designer, advanced styling controls, and separate print publishing for PDF and Word.
...
1. Published actions appear directly in Odoo print menu
2. Create template and choose target model (e.g.`account.move`,`sale.order`).
3. Open Advanced Builder.
4. Drag blocks to canvas and style each block from Properties panel.
5. Use /// autocomplete to insert dynamic model fields quickly.
6. Insert one2many tables and pick columns using relation-based selector.
7. Preview on real record ID to validate output data.
8. Save template.
9. Publish PDF and/or Word print action as needed.
10. Print directly from document Print menu.
...
Drag blocks into the canvas and build full report layouts visually.
...
#### One2many
...
#### Advanced Properties Panel
...
Control typography, spacing, borders, direction, and visual styling per block.
...
# Advanced Report Builder (Odoo 19)
...
This module provides a modern visual builder for creating QWeb-ready report templates in Odoo. It is designed for business teams that need flexible report design with developer-level output quality.
...
1. Visual block editor (drag and drop)
2. Dynamic data bindings (t-field, t-esc)
3. One2many table field picker
4. Rich properties panel for typography, spacing, border, and layout
5. Publish print actions independently: - PDF action - Word action
6. In-record print wizard with format choice
...
1. Create a new template and select target model.
2. Open Advanced Builder.
3. Add and style blocks.
4. Preview using a real record.
5. Save template.
6. Publish PDF and/or Word action.
7. Print from records directly.
...
- Templates are model-aware and validated before rendering.
- Published actions can be unpublished independently.
- Word output is generated from the rendered template HTML.

---

Title: Report Designer | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/vis_report_designer
Published: N/A
Author: N/A
Highlights:
Report Designer | Odoo Apps Store
...
# Report Designer
...
Odoo 19 Visual Designer ReportLab PDF
...
# Report Designer
...
A pixel-perfect, drag-and-drop PDF report builder for Odoo. Design professional documents visually — no QWeb, no XML, no code required. Bind any Odoo model field, build dynamic tables, add images, barcodes, watermarks and preview real data instantly inside the designer.
...
## Everything you need to design PDF reports visually
...
Stop fighting with QWeb templates. Report Designer gives your team a full visual canvas with real-time field binding, expression logic, and instant PDF preview.
...
Text, Field, Image, Rectangle, Line, Section, Table, Page Break, Watermark — all draggable onto the canvas.
...
Bind tables to One2many / Many2many data sources. Per-column Text, Image, or Barcode content with custom widths and visibility expressions.
...
Dedicated canvas zones that repeat on every page of multi-page documents. Configurable height, independent element sets.
...
Write Python-style expressions with a built-in function library (String, Math, Date, Type Conversion) and guided field insertion.
...
### Instant PDF Preview
...
Select any real record from the designer and generate a live PDF preview without leaving the editor.
...
Install vis_report_designer from the Apps menu. Then run`pip install reportlab` on the Odoo server and restart the service.
...
Click Open Designer. Drag elements from the left sidebar (Text, Field, Image, Table, …) onto the canvas. Resize and reposition with your mouse. Use the right panel to style each element and bind Odoo fields.
...
Select a Field element → right panel → Browse Fields tab. Navigate the model's field tree (relations expand to sub-fields) and click any field to bind it instantly. Use the Expression Editor for computed values like`partner_id.name`.
...
Drag a Table element onto the canvas. In the right panel choose a Data Source (any One2many / Many2many field, e.g.`order_line`). Click Add Column and pick the field to display in each column.
...
## Pixel-Perfect Visual Canvas
...
A WYSIWYG canvas built on Fabric.js. Drag elements from the sidebar, position them freely, resize with handles, and configure every style property in the right panel — all in real time.
...
Tables are first-class citizens. Bind them to any One2many or Many2many relation, then configure each column independently — header, content type, field expression, width, and visibility.
...
Three focused tabs keep the workspace organised: a component palette to drag new elements, a live field browser for your model's data, and a page manager for multi-page documents.
...
Repeating Header &
...
Switch between Header, Content, and Footer zones with a single click. Header and footer elements repeat on every page automatically — ideal for company branding, page numbers, and legal text.
...
## Expression Editor with Function Library
...
Write powerful dynamic expressions with a guided editor. Browse model fields in the left panel, insert functions from categorised snippets on the right, and get instant syntax validation.
...
## Live PDF Preview — No Context Switching
...
Click Preview directly inside the designer, pick a real record, and generate a pixel-perfect PDF instantly. Renders actual field data, images, tables, and barcodes — exactly as it will print.
...
No XML knowledge required. From install to first PDF in under 5 minutes.
...
`reportlab`(
...
Design visuallyClick Open Designer. Drag elements from the sidebar, bind model fields, style everything from the right panel.
...
Preview with real dataClick Preview in the toolbar, select any existing record, and generate a live PDF instantly.
...
## Technical Requirements
...
| Requirement | Details |
| --- | --- |
| Odoo Version | 19.0 Community or Enterprise |
| Python | 3.10+ (matches Odoo 19 requirement) |
| Python Packages | `reportlab`≥ 3.6 — pip install reportlab |
| Odoo Depends | base, web, mail, account, sale |
| Browser | Any modern browser (Chrome, Firefox, Safari, Edge) |

---

Title: Report Studio | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/td_report_studio
Published: N/A
Author: N/A
Highlights:
# REPORT STUDIO
...
Design professional reports without writing a single line of code
...
QWeb Builder Excel Builder
...
100% visual â no programming required
...
## TWO POWERFUL BUILDERS
...
### QWEB BUILDER
...
Visual drag & drop editor for PDF and HTML reports
...
- WYSIWYG live preview editing
- 18 drag & drop components
- Dynamic field binding from any Odoo model
- 8 style presets + 20 page backgrounds
- Conditional visibility (if / elif / else)
...
QWeb Builder â Drag & drop report editor
...
## QWEB BUILDER
...
### VISUAL EDITOR
...
#### WYSIWYG Live Preview
...
Edit directly on the rendered report. Click to select any element, hover to highlight with type label. Inline text editing and parent hierarchy tree navigation.
...
#### Zoom & Layout
...
Zoom 50%â200% with Ctrl+/- shortcuts. 3-panel layout with templates, editor, and properties side by side. Collapsible panels, fullscreen mode, dark mode.
...
#### Right-Click Context Menu
...
Right-click any element to edit properties, delete, duplicate, move up/down, add before/after, or wrap in container. Fast element manipulation without leaving the editor.
...
### 18 COMPONENTS
...
Smart drop targeting auto-finds the best insert point. Conditional chain protection keeps if/elif/else blocks intact. All components support drag & drop from the side panel.
...
### STYLING & DESIGN
...
##### 30+ CSS Properties
...
Font, color, padding, margin, border, radius, opacity, background, display, class editor
...
##### 9 Style Presets
...
Brutalism, Cartoon, Corporate, Elegant, Memphis, Minimalist, Pop Art, Swiss
...
##### 20 Backgrounds
...
11 geometric + 9 artistic SVG patterns, or custom image upload
...
### DOCUMENT LAYOUT
...
Odoo's
...
#### Page Background
...
Pick from 20 SVG patterns (geometric + artistic) or upload a custom image. Backgrounds render correctly in both editor and exported PDF.
...
### PREVIEW & EXPORT
...
#### Live Preview
...
Toggle Design/Preview mode. See actual Odoo data in
...
grid with a specific record.
...
## SHARED FEATURES
...
Available in both QWeb Builder and Excel Builder
...
#### No Code
...
100% visual point & click. No programming, no XML, no Python required.
...
#### Dark Mode
...
Full dark theme with CSS variables. Grid dark mode. Full
...
#### 3-Panel Layout
...
### REPORT STUDIO
...
No-code report builder for Odoo 19
...
Version 19.0.1.0.0

---

Title: Qweb PDF Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/report_builder_visual
Published: N/A
Author: N/A
Highlights:
Qweb PDF Report Builder | Odoo Apps Store
...
# Qweb PDF Report Builder
...
Direct Design - No XML Development
...
# Visual Report Builder. Design Directly. Bypass Code. Live PDF. One-Click Publish.
...
Stop wasting hours writing QWeb XML, modifying paper formats in code, and compiling PDFs. Visual Report Builder enables functional consultants, administrators, and developers to drag, drop, and publish pixel-perfect reports directly in the Odoo interface.
...
Drag-and-Drop Canvas Upcoming: AI Layout Builder No XML Coding Required 3-Level Field Picker Real-time PDF Preview Version & Snapshot History
...
## Direct Design vs. Traditional Coding
...
Stop making Odoo reports "the old way." Let's compare how this visual designer changes everything for developers and businesses alike.
...
#### Direct Visual Builder Style
...
- Drag & Drop: Place tables, text, barcodes, and lines on an intuitive grid
- Zero Restarts: Apply edits live, save drafts, and publish instantly
- Visual Configuration: Set font family, size, colors, and margins via sidebar UI
- Live Rendering: Generate real PDF preview with actual records as you design
- Empower Business Users: Let administrators manage layout, logos, and terms
- Safe Logic Sandbox: Auto-built Jinja2 expressions are linted before saving
...
## Upcoming: AI Layout Builder
...
In our upcoming version, designing custom reports is completely streamlined. Just upload a PDF or an image of your target report design, and watch the AI convert it directly into a layout JSON file. Upload that file into Odoo, and your report configuration is fully complete and ready to print!
...
1. Upload Reference: Provide a PDF file or an image/screenshot of your target report design.
2. Generate Layout File: The AI converts your uploaded visual format into a structured JSON file automatically.
3. Import JSON File: Upload the generated JSON directly in Odoo.
4. Done! The report is instantly generated with correct spacing, margins, and headers.
...
The AI-powered layout builder (JSON generation & auto-formatting) is under active development. Once released in version 2.0, the module price will increase. Purchase the module today at the current rate to secure your license, and receive the AI upgrade 100% free of charge!
...
## How the Builder Works
...
From report record to published view in 5 intuitive steps. Let's look at the lifecycle.
...
#### Native Launch
...
Open any report form (Invoices, Picking lists) and click Edit Layout to open the custom canvas.
...
#### Visual Arranging
...
Drag/resize labels, shapes, tables, and images. Align to a clean mm-scale grid reflecting actual page sizes.
...
#### Field Mapping
...
Open the Field Picker to browse relational models 3 levels deep. Drop variables directly into elements.
...
#### Real-time Preview
...
Click Preview to generate a real PDF in seconds. Review text positioning and tables with actual record data.
...
#### One-Click Publish
...
Publish to auto-generate underlying QWeb XML view overrides. Revert to draft or restore older history anytime.
...
## See the Canvas in Action
...
Explore the layout builder features. Build layouts visually, browse database fields, perform instant previews, and import structures.
...
Click the Edit Layout button directly inside Odoo's native action report view. The system instantly initializes the canvas using the linked Paper Format (margins, width, and height).
...
2. Drag-and-Drop Canvas & Zones
...
Arrange elements inside dynamic zones (Header, Body, Footer) on a precise millimeter-scale layout grid. Elements automatically stack, line up, or support absolute coordinate placements for billing headers and custom zones.
...
3. Insert Elements, Smart Fields & Snippets
...
Use the newly redesigned 3-column insert menu card to instantly drop static text, shapes, database-bound fields, barcodes, and smart fields (page number, print date) or advanced pre-styled snippets directly into the canvas.
...
4. Relational Field Picker
...
Select any text block and click the Field Picker. Browse Odoo database fields, including relational fields (up to 3 levels deep like`invoice_line_ids.product_id.name`), and inject dynamic tags with a click.
...
5. Convert PDF/Image to Layout JSON (Upcoming)
...
Simply upload a PDF or image of your desired report layout. The AI converts it into a structured JSON fileâthen just upload the file and the layout is fully built!
...
6. Instant Server-Side PDF Preview
...
No client-side approximations. Click Preview to let Odoo render a real PDF using active database records, giving you a 100% accurate visual representation of the printed document.
...
7. Native Report Selection & Print Execution
...
Once published, the customized report automatically registers in the Odoo Action framework. Standard users can generate the pixel-perfect layout with a single click from the standard native form view's Print menu.
...
## Ultimate Design Control
...
Experience direct report development inside Odoo with capabilities designed for both business professionals and developers.
...
##### Drag & Drop Editor
...
Place and scale text fields, dynamic tables, lines, shapes, and images visually. Custom grids ensure millimetric alignment.
...
##### Roadmap: AI Layouts
...
Convert PDF/Image layouts to JSON using AI, then upload them directly to auto-compile your visual reports. (Free upcoming update v2.0).
...
##### 3-Level Field Picker
...
No need to memorize Odoo database field strings. Drill down through related records (M2O, O2M) up to 3 layers deep automatically.
...
##### Zone Management
...
Manage headers, footers, and body sections independently. Visual dimensions automatically scale to the report's paper orientation.
...
##### Version Snapshot History
...
Rollback layout changes instantly. Review visual differences between drafts and published versions, protecting layouts from loss.
...
##### Jinja2 Logic Linter
...
Need custom visibility or logic conditions? Use the developer mode expression panel, fortified with an on-the-fly syntax linter.
...
Banish slow manual QWeb coding cycles. Empower your team to modify invoice formats, quotation layouts, picking templates, and barcode labels visually inside Odoo.
...
© 2026 Synodica Solutions PVT. LTD. - Qweb PDF Report Builder for Odoo 18

---

Title: Omni Designer - Visual Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/omni_designer
Published: N/A
Author: N/A
Highlights:
Omni Designer - Visual Report Builder | Odoo Apps Store
...
# Omni Designer - Visual Report Builder
...
# Omni Designer
...
### Visual Report Designer & Client-Side PDF Engine
...
Design professional PDF reports visually with integrated client-side PDF generation. No server-side rendering required.
...
Drag-and-drop interface with pixel-perfect precision. No coding, no XML, just design.
...
## Professional Visual Designer
...
### Design Reports Like a Pro
...
| Rulers & Grid Professional layout tools |
...
| Multi-Page
...
Create and manage multi-page report templates. |
...
- Undo/Redo - Full history with keyboard shortcuts
- Copy/Paste - Including right-click positioned paste
- Zoom - Flexible zoom levels for precision work
- Layer Ordering - Bring to front/back control
- Keyboard Shortcuts - Speed up your workflow
...
## Rich Component Library
...
- Field - Field selector, expression, format (HTML, date, number, currency)
- QR Code, Code128, EAN13 and more
- Table - WYSIWYG design, conditional columns, header repeat
- Section - Data-driven repeating blocks
- Shape - Rectangle, Ellipse, Triangle, Star
- Line & Frame - Visual separators
- Page Break - Control pagination
- Image Library - Drag-drop upload, manage and preview resources
...
## Compare with Alternatives
...
#### vs QWeb Reports
...
- No XML coding
- Instant preview
- Precise positioning
- Any layout
...
Why this happens: Omni Designer ships as two separate modules, each with its own rendering engine: omni_designer (the visual designer, including the live preview) and omni_report (the engine used for printing and PDF export). The Designer preview is rendered by the omni_designer engine, while printing and export are rendered by the omni_report engine. If you update only omni_designer (for example to a version that supports multi-
...
while omni_report stays on an older version, the two engines render differently - the preview can look correct while the printed PDF is wrong, such as a multi-page
...
Visual drag-and-drop report builder for thermal POS receipts. No QWeb coding required.
...
## Release Notes
...
19.0.1.0.5 - Share the same PDF generation backend as omni_report_server.
...
- Added support for multi-page template layout and upgraded the Outline tab to a Pages tab.
...
- Improved field drag-and-drop: dropping a binary field onto the canvas now creates an Image component automatically.
...
- Upgraded the designer engine and updated asset loading.
...
Availability | Odoo Online Odoo.sh On Prem
...
--- | ---
...
Apps Dependencies |
...
Omni Report - PDF Report Engine |
...
of code | 3
...
34 |
...
| Technical Name | `
 omni_designer` |
...
| License | OPL-1 |
...
| Website | https://omni-byte.com/ |

---

Title: BJET Print Form Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/bjet_print_form_builder
Published: N/A
Author: N/A
Highlights:
## Bjet Print Form Builder makes Odoo reports dynamic, flexible, and business-friendly.
...
### Design, Customize, and Print Like a Pro
...
Create, customize, and print professional business documents in Odoo - without coding. Design invoices, offers, and other forms directly in the Odoo interface. Fully compatible with Odoo Community and Enterprise editions.
...
Built-in HTML/WYSIWYG editor - allowing users to design templates visually.
...
### Design Your Odoo Print Forms Smarter with AI
...
Our AI assistant creates QWeb templates for BJet Print Form Builder - from invoices to delivery notes. Always verify and test your code.
...
### HTML / WYSIWYG Editor
...
- Design templates with a user-friendly interface.
- Supports text formatting, tables, images, lists, and hyperlinks.
- Access to HTML source view for advanced users.
- Live preview with real data.
...
Dynamic Data Insertion
...
Use Odoo QWeb expressions directly in templates with support for nested fields, custom methods, and data formatting.
...
- Toggle between "Code" and "Preview" views without losing changes.
- Select from standard Odoo print layouts or create your own print format.
- Render documents in real A4 layout - ready for PDF export.
...
### Interactive Preview & Print
...
- Toggle between "Code" and "Preview" views without losing changes.
- Select from standard Odoo print layouts or create your own print format.
- Render documents in real A4 layout - ready for PDF export.

---

Title: Introducing Omni Designer: The Visual Report Builder Odoo Has Been Missing | Omni Byte
URL: https://omni-byte.com/blog/introducing-omni-designer-faster-way-to-build-odoo-reports-without-qweb/
Published: 2026-03-26T00:00:00.000Z
Author: Omni Byte Team
Highlights:
Introducing Omni Designer: The Visual Report Builder Odoo Has Been Missing | Omni Byte
...
We built Omni Designer to replace that workflow.
...
Omni Designer is a visual, drag-and-drop report builder that runs directly inside your Odoo instance. Instead of editing QWeb XML and refreshing to see results, you design on a canvas and see the layout take shape in real time.
...
It handles the full report lifecycle: layout, data binding, conditional logic, and PDF rendering - all without leaving the browser and without writing a single line of template code.
...
From any report template in Odoo, click Design. The full workspace loads inside your browser - a toolbar at the top, a component sidebar on the left, your canvas in the center, and a property panel on the right.
...
Open the Components tab and drag a Text element onto the canvas for your header. Need a company logo? Drag an Image element and point it at a static URL or bind it to a binary field.
...
Now switch to the Data tab. You will see the full field schema of your report model -`sale.order` in this case. Expand`partner_id` to reveal`name`,`email`,`street`. Drag`partner_id.name` onto the canvas, and Omni Designer automatically creates a properly bound Field element. No expression syntax to memorize.
...
Here is where it gets interesting. Drag`order_line`(a One2many field) from the Data tab. Omni Designer recognizes it as a collection and can automatically create a repeating Section bound to that dataset. Every element you place inside the section will repeat for each order line.
...
- right-click column operations (insert, delete, copy, paste)
- draggable column borders for resizing
- switchable cell content types (text, image, barcode)
- footer rows with colspan for totals and summaries
...
Select any element and the property panel shows its full configuration: position, size, font, color, background, borders, and padding - each side individually.
...
For pixel-perfect alignment, elements automatically snap to page margins and to the edges and centers of nearby elements as you drag them. Select multiple elements and use the toolbar to align or distribute them evenly, or use keyboard shortcuts like`Ctrl+Shift+Arrow` for quick alignment.
...
Every element has a Visibility property. Set a condition like`state == 'sale'` and that element only renders when the condition is met. Hide discount columns when there is no discount. Show tax disclaimers only for international orders.
...
Beyond visibility, Dynamic Styles let you apply conditional formatting: turn text red when`amount < 0`, highlight a row yellow when`priority == 'urgent'`. Rules are expression-driven and evaluated in order.
...
Click the Preview button. Select which records to render against. Omni Designer generates a pixel-accurate PDF directly in your browser and opens it immediately.
...
Omni Designer is not a typical JavaScript web app. Like Figma, it uses WebAssembly to run a compiled, high-performance rendering engine directly in the browser.
...
This matters for reports because the same layout engine that calculates text measurement, line breaks, page splitting, and element positioning at design time is the exact same engine that produces the final PDF. There is no “preview looks different from output” problem. What you see on canvas is what ends up on paper.
...
Because the entire engine runs client-side, PDF generation is fast and does not depend on server resources. Even complex multi-page reports with tables, sections, and images render in seconds.
...
Omni Designer includes a built-in expression engine with over 30 functions. You are not limited to simple field references:
...
Reports are international. Omni Designer includes fallback fonts for CJK, Arabic, Hebrew, Thai, Devanagari, and Cyrillic scripts. Mixed-language documents render correctly without manual font configuration.
...
The component library covers what real business documents actually require:
...
- Text and Field elements with full typography control
- Images with static, URL, or Odoo binary field sources
- Tables with header, data, and footer rows
- Sections for repeating data (order lines, invoice lines)
- Barcodes and QR Codes (EAN-13, Code 128, Code 39, and more)
- Shapes (rectangle, ellipse, triangle, star) and Lines
- Frames for grouping elements
- Page Breaks for manual pagination control
...
Every element supports lock/unlock, conditional visibility, dynamic styles, and precise positioning.
...
Omni Designer is built for teams that need custom Odoo reports but cannot afford to turn every layout change into a development task.
...
Omni Designer is available on the Odoo App Store and supports Odoo 16, 17, 18, and 19.
...
1. Install the`omni_designer` module in your Odoo instance.
2. Navigate to any report template and click Open Designer.
3. Drag, bind, style, preview, save. That is the whole workflow.
...
We built Omni Designer because report design in Odoo deserved better tooling. If you have been spending hours in QWeb templates for changes that should take minutes, give it a try.

---

Title: Report Drag & Drop Builder (Advanced) | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/17.0/report_dragdrop
Published: N/A
Author: N/A
Highlights:
& Drop Builder
...
# Advanced Report Builder
...
## Drag & Drop QWeb Report Designer for Odoo 19
...
Create professional Odoo reports in minutes, without custom development. Empower your team to design, preview, and publish PDF or Word reports using a simple visual drag-and-drop builder.
...
Build professional reports visually without hardcoding templates. This module provides a complete report-building workflow with dynamic fields, one2many table designer, advanced styling controls, and separate print publishing for PDF and Word.
...
1. Published actions appear directly in Odoo print menu
2. Create template and choose target model (e.g.`account.move`,`sale.order`).
3. Open Advanced Builder.
4. Drag blocks to canvas and style each block from Properties panel.
5. Use /// autocomplete to insert dynamic model fields quickly.
6. Insert one2many tables and pick columns using relation-based selector.
7. Preview on real record ID to validate output data.
8. Save template.
9. Publish PDF and/or Word print action as needed.
10. Print directly from document Print menu.
...
Drag blocks into the canvas and build full report layouts visually.
...
#### One2many Table Column Picker
...
Select relation columns
...
#### Advanced Properties Panel
...
Control typography, spacing, borders, direction, and visual styling per block.
...
# Advanced Report Builder (Odoo 19)
...
This module provides a modern visual builder for creating QWeb-ready report templates in Odoo. It is designed for business teams that need flexible report design with developer-level output quality.
...
1. Visual block editor (drag and drop)
2. Dynamic data bindings (t-field, t-esc)
3. One2many table field picker
4. Rich properties panel for typography, spacing, border, and layout
5. Publish print actions independently: - PDF action - Word action
6. In-record print wizard with format choice
...
1. Create a new template and select target model.
2. Open Advanced Builder.
3. Add and style blocks.
4. Preview using a real record.
5. Save template.
6. Publish PDF and/or Word action.
7. Print from records directly.
...
- Templates are model-aware and validated before rendering.
- Published actions can be unpublished independently.
- Word output is generated from the rendered template HTML.

---

Title: Building Custom Reports in Odoo 19: From Basic to Advanced
URL: https://bytelegions.com/build-custom-reports-odoo19-from-basic-to-advanced/
Published: 2026-01-08T06:29:46.000Z
Author: N/A
Highlights:
Customizing reports in Odoo 19 involves several methods, including using Odoo Studio for simpler customizations and developer tools for more advanced setups. Odoo offers built-in tools for report customization, but understanding how to navigate them is crucial for unlocking their full potential. The report builder in Odoo Studio is an intuitive drag-and-drop tool, while more advanced users can leverage the XML-based template engine for deeper customizations.
...
Odoo Studio is one of the easiest ways to customize reports without writing code. It’s a visual editor that allows users to create custom PDF reports by simply dragging and dropping elements onto a layout. Whether you’re generating sales reports, invoices, or any other document, Odoo Studio provides an easy interface to tweak reports according to your needs.
...
## QWeb Template Customization in Odoo
...
When you need more flexibility, Odoo provides advanced customization methods for reports.
...
Extending Default Odoo Reports:Sometimes, the default reports do not meet all business needs. You can extend or adjust them using the Odoo development environment by creating new report actions or modifying existing ones. The ir.actions.report model controls how reports are generated, and by overriding it, you can define more complex behaviors.
...
Adding Custom Fields to Reports:To further personalize reports, Odoo allows you to add custom fields. Whether it’s adding a specific tax field, a user-defined discount, or any other custom data, Odoo’s developer tools allow you to modify the report templates and include custom fields seamlessly.
...
Customizing Headers and Footers in Reports:Customizing the header and footer of your reports allows for branding and consistency across all reports. You can include company logos, contact information, or legal disclaimers, ensuring that every document carries your corporate identity.
...
### Working with XML and XPath for Custom Reports
...
For those looking for deep customization, working with XML and XPath is essential. XML is used to define the structure of the report, while XPath allows you to navigate and select data dynamically. Customizing reports with XML and XPath gives developers more control over what data is shown and how it is displayed.
...
For example, to extract and display specific data from a complex relational model, XPath expressions can be used within QWeb templates to filter and show only relevant results.
...
Odoo QWeb vs Spreadsheet Reports:While QWeb reports are great for formatted PDF documents, spreadsheet exports provide businesses with more flexibility when it comes to analyzing data. Odoo offers tools to export reports in Excel or CSV formats, allowing for deeper data manipulation. You can generate custom spreadsheets directly from your reports, enabling you to perform further analysis.
...
Use Odoo Studio for simple customizations or modify QWeb templates for more complex reports. Enable developer mode for deeper access to Odoo’s backend features.
...
QWeb reports are ideal for PDF-based documents, while spreadsheet exports are better suited for data analysis and manipulation in Excel or CSV formats.
...
Yes, you can add custom fields by modifying report templates and leveraging Odoo’s developer tools.
...
Customizing reports in Odoo 19 involves several methods, including using Odoo Studio for simpler customizations and developer tools for more advanced setups. Odoo offers built-in tools for report customization, but understanding how to navigate them is crucial for unlocking their full potential. The report builder in Odoo Studio is an intuitive drag-and-drop tool, while more advanced users can leverage the XML-based template engine for deeper customizations.
...
Odoo Studio is one of the easiest ways to customize reports without writing code. It’s a visual editor that allows users to create custom PDF reports by simply dragging and dropping elements onto a layout. Whether you’re generating sales reports, invoices, or any other document, Odoo Studio provides an easy interface to tweak reports according to your needs.
...
## QWeb Template Customization in Odoo
...
When you need more flexibility, Odoo provides advanced customization methods for reports.
...
Extending Default Odoo Reports:Sometimes, the default reports do not meet all business needs. You can extend or adjust them using the Odoo development environment by creating new report actions or modifying existing ones. The ir.actions.report model controls how reports are generated, and by overriding it, you can define more complex behaviors.
...
Adding Custom Fields to Reports:To further personalize reports, Odoo allows you to add custom fields. Whether it’s adding a specific tax field, a user-defined discount, or any other custom data, Odoo’s developer tools allow you to modify the report templates and include custom fields seamlessly.
...
Customizing Headers and Footers in Reports:Customizing the header and footer of your reports allows for branding and consistency across all reports. You can include company logos, contact information, or legal disclaimers, ensuring that every document carries your corporate identity.
...
### Working with XML and XPath for Custom Reports
...
For those looking for deep customization, working with XML and XPath is essential. XML is used to define the structure of the report, while XPath allows you to navigate and select data dynamically. Customizing reports with XML and XPath gives developers more control over what data is shown and how it is displayed.
...
For example, to extract and display specific data from a complex relational model, XPath expressions can be used within QWeb templates to filter and show only relevant results.
...
options, including exporting custom
...
spreadsheets for easy analysis and
...
with other business systems
...
Odoo QWeb vs Spreadsheet Reports:While QWeb reports are great for formatted PDF documents, spreadsheet exports provide businesses with more flexibility when it comes to analyzing data. Odoo offers tools to export reports in Excel or CSV formats, allowing for deeper data manipulation. You can generate custom spreadsheets directly from your reports, enabling you to perform further analysis.
...
Whether you are
...
delving into XML
...
, Odoo offers
...
. At Byte Legions, we specialize in
...
out of their O
...
Use Odoo Studio for simple customizations or modify QWeb templates for more complex reports. Enable developer mode for deeper access to Odoo’s backend features.
...
QWeb reports are ideal for PDF-based documents, while spreadsheet exports are better suited for data analysis and manipulation in Excel or CSV formats.
...
Yes, you can add custom fields by modifying report templates and leveraging Odoo’s developer tools.
...
Odoo 19 developer mode Odoo
...
19 report customization Odoo reporting
...
Odoo reporting for
...
statements. Odoo Studio Odoo XML report templates QWeb templates

---

Title: Report Designer - Word & Excel Template Engine | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/sm_report_designer
Published: N/A
Author: N/A
Highlights:
Report Designer - Word & Excel Template Engine | Odoo Apps Store
...
# Report Designer - Word & Excel Template Engine
...
## Report Designer — Word & Excel Template Engine
...
#### Design professional Odoo 19 reports from .docx and .xlsx templates — no developer needed
...
✓ DOCX & XLSX ✓ Multi-Format Output ✓ Python Expressions ✓ Image & Conditionals ✓ Cover Page & PDF Merge
...
### 1 Word & Excel templates
...
Upload`.docx` or`.xlsx` files as templates. Design your report layout in Microsoft Word, LibreOffice, or Google Docs — the tools you already know. Use`{{field_name}}` placeholders and they get replaced with real Odoo data when you print.
...
Click Parse Template and all`{{placeholder}}` patterns are detected automatically. Map each placeholder to an Odoo field via dropdown selectors — supports dot notation for relational fields like`{{partner_id.name}}`. Zero coding required.
...
### 3 Multi-format output
...
Generate reports as PDF, DOCX, XLSX, HTML, ODT, or RTF. PDF conversion is powered by LibreOffice headless for pixel-perfect output. Keep the original format or convert to any supported format with one click.
...
### 8 Image support
...
Insert images from binary fields with`{{img:company_id.logo}}` or`{{img:partner_id.image_128}}`. Images are auto-resized with preserved aspect ratio (max 15cm × 10cm). Supports PNG, JPEG, GIF, WEBP, and BMP formats.
...
### 9 PDF merge & cover page
...
Select multiple records and generate a single merged PDF. Upload an optional DOCX cover page template — it renders with the same record data and gets prepended as the first page automatically. Perfect for batch-printing invoices, quotations, or delivery slips.
...
### 10 Domain-based template selection
...
Set domain conditions per template. The system auto-selects the right template based on record data — different layouts for different customer types, order amounts, or any other criteria. Fully configurable from the UI.
...
### 11 PDF preview in browser
...
Preview reports inline in the browser before downloading. Quick verification without leaving Odoo. Accessible via button or direct URL endpoint.
...
## How It Works
...
✓ Odoo 19 Community or Enterprise
...
✓ LibreOffice installed on server (for PDF/HTML/ODT/RTF conversion)
...
# Report Designer — Word & Excel Template Engine for Odoo 19
...
## 2. Creating Your First Template
...
Open Microsoft Word, LibreOffice Writer, or Google Docs and create your report layout. Use {{field_name}} placeholders wherever you want Odoo data to appear.
...
- Name: e.g., "Sales Order Quotation"
- Model: Select the target Odoo model (e.g., sale.order)
- Template File: Upload your .docx or .xlsx file
- Output Format: Choose PDF, Original, HTML, ODT, or RTF
...
1. Go to the Field Mappings tab
2. Click the Parse Template button
3. All {{placeholder}} patterns are auto-detected
4. For each placeholder, select the correct Odoo field from the dropdown
5. Use dot notation for relational fields: partner_id.name, company_id.logo
...
1. Open any record of the target model (e.g., a Sale Order)
2. Click Action menu → select your report template
3. The report is generated and downloaded automatically
...
### Image Insertion
...
## 4. Advanced Features
...
### Cover Page
...
### PDF Preview
...
## 5. Output Formats
...
| Format | File Extension | Notes |
| --- | --- | --- |
| Original | .docx / .xlsx | Keeps the template format as-is |
| PDF | .pdf | Requires LibreOffice. Supports merge & cover |
| HTML | .html | Requires LibreOffice for conversion |
| ODT | .odt | OpenDocument format.
...
LibreOffice |
| RTF | .rtf | Rich Text Format. Requires LibreOffice |
...
## 7. Changelog
...
### Version 19.0.3.0.0
...
- Added Python expressions {{=expr}}
- Added conditional blocks {{#if}}/{{#else}}/{{/if}}
- Added format pipes {{field|format}} (currency, date, datetime, number, upper, lower, title)
- Added image support {{img:field}} for DOCX and XLSX
- Added cover page support (PDF only)
...
- Added PDF merge for multiple records
- Added domain-based template selection
- Added PDF preview in browser
- Added direct URL endpoints for preview and download
...
### Version 19.0.1.0.0
...
- Initial release
- Word (.docx) and Excel (.xlsx) template support
- Auto-detect placeholders
- Field mapping via UI
- Table row loops for One2many fields
- Multi-format output (PDF, HTML, ODT, RTF)
- One-click print action
- Batch generation with ZIP download
```

**Tool: websearch**

**Input:**

```json
{
  "query": "Odoo report design tools visual builder QWeb generator third party",
  "numResults": 10,
  "type": "deep"
}
```

**Output:**

```
Title: Report Drag & Drop Builder (Advanced) | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/report_dragdrop
Published: N/A
Author: N/A
Highlights:
v 19.0 Third Party
...
# Advanced Report Builder
...
## Drag & Drop QWeb Report Designer for Odoo 19
...
Create professional Odoo reports in minutes, without custom development. Empower your team to design, preview, and publish PDF or Word reports using a simple visual drag-and-drop builder.
...
Build professional reports visually without hardcoding templates. This module provides a complete report-building workflow with dynamic fields, one2many table designer, advanced styling controls, and separate print publishing for PDF and Word.
...
1. Published actions appear directly in Odoo print menu
2. Create template and choose target model (e.g.`account.move`,`sale.order`).
3. Open Advanced Builder.
4. Drag blocks to canvas and style each block from Properties panel.
5. Use /// autocomplete to insert dynamic model fields quickly.
6. Insert one2many tables and pick columns using relation-based selector.
7. Preview on real record ID to validate output data.
8. Save template.
9. Publish PDF and/or Word print action as needed.
10. Print directly from document Print menu.
...
# Advanced Report Builder (Odoo 19)
...
This module provides a modern visual builder for creating QWeb-ready report templates in Odoo. It is designed for business teams that need flexible report design with developer-level output quality.
...
1. Visual block editor (drag and drop)
2. Dynamic data bindings (t-field, t-esc)
3. One2many table field picker
4. Rich properties panel for typography, spacing, border, and layout
5. Publish print actions independently: - PDF action - Word action
6. In-record print wizard with format choice
...
1. Create a new template and select target model.
2. Open Advanced Builder.
3. Add and style blocks.
4. Preview using a real record.
5. Save template.
6. Publish PDF and/or Word action.
7. Print from records directly.
...
- Templates are model-aware and validated before rendering.
- Published actions can be unpublished independently.
- Word output is generated from the rendered template HTML.

---

Title: Omni Designer - Visual Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/omni_designer
Published: N/A
Author: N/A
Highlights:
Omni Designer - Visual Report Builder | Odoo Apps Store
...
# Omni Designer - Visual Report Builder
...
| Availability | Odoo Online Odoo.sh On Premise |
| --- | --- |
| Community Apps Dependencies | Show Omni Report - PDF Report Engine |
| Lines of code | 3134 |
| Technical Name | `
 omni_designer` |
| License | OPL-1 |
| Website | https://omni-byte.com/ |
...
### Visual Report Designer & Client-Side PDF Engine
...
Design professional PDF reports visually with integrated client-side PDF generation. No server-side rendering required.
...
Drag-and-drop interface with pixel-perfect precision. No coding, no XML, just design.
...
Preview PDF in real-time directly in your browser. Client-side generation reduces server load.
...
## Professional Visual Designer
...
## Compare with Alternatives
...
#### vs QWeb Reports
...
- No XML coding
- Instant preview
- Precise positioning
- Any layout
...
- Single vendor
- Cross-platform
- Active development
- Professional support
...
Why this happens: Omni Designer ships as two separate modules, each with its own rendering engine: omni_designer (the visual designer, including the live preview) and omni_report (the engine used for printing and PDF export). The Designer preview is rendered by the omni_designer engine, while printing and export are rendered by the omni_report engine. If you update only omni_designer (for example to a version that supports multi-
...
layout) while omni_report stays on an older version, the two engines render differently - the preview can
...
correct while the printed PDF is wrong, such as
...
##### Omni Report
...
Visual drag-and-drop report builder for thermal POS receipts. No QWeb coding required.
...
19.0.

---

Title: Report Studio | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/td_report_studio
Published: N/A
Author: N/A
Highlights:
Party 1
...
# REPORT STUDIO
...
Design professional reports without writing a single line of code
...
QWeb Builder Excel Builder
...
100% visual â no programming required
...
## TWO POWERFUL BUILDERS
...
### QWEB BUILDER
...
Visual drag & drop editor for PDF and HTML reports
...
- WYSIWYG live preview editing
- 18 drag & drop components
- Dynamic field binding from any Odoo model
- 8 style presets + 20 page backgrounds
- Conditional visibility (if / elif / else)
...
QWeb Builder â Drag & drop report editor
...
## QWEB BUILDER
...
### VISUAL EDITOR
...
#### WYSIWYG Live Preview
...
Edit directly on the rendered report. Click to select any element, hover to highlight with type label. Inline text editing and parent hierarchy tree navigation.
...
Zoom 50%â200% with Ctrl+/- shortcuts. 3-panel layout with templates, editor, and properties side by side. Collapsible panels, fullscreen mode, dark mode.
...
Click Context Menu
...
Right-click any element to edit properties, delete, duplicate, move up/down, add before/
...
, or wrap in container. Fast element manipulation without
...
the editor.
...
### 18 COMPONENTS
...
Smart drop targeting auto-finds the best insert point. Conditional chain protection keeps if/elif/else blocks intact. All
...
support drag & drop from the
...
### STYLING & DESIGN
...
## SHARED FEATURES
...
Available in both QWeb Builder and Excel Builder
...
#### No Code
...
100% visual point & click. No programming, no XML, no Python required.
...
### REPORT STUDIO
...
No-code report builder for Odoo 19
...
| Availability | Odoo Online Odoo.sh On Premise |
| --- | --- |
| Lines of code | 24407 |
| Technical Name | `
 td_report_studio` |
| License | LGPL-3 |
| Website | http://micheal.nguyen291996@gmail.com |

---

Title: Report Designer | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/vis_report_designer
Published: N/A
Author: N/A
Highlights:
v 19.0 Third Party
...
| Availability |
...
| --- |
...
| Odoo Apps Dependencies | • Discuss (mail) • Invoicing (account) |
...
| Lines of code
...
4803 |
...
| Technical Name | `
 vis_report_designer` |
| License | OPL-1 |
...
A pixel-perfect, drag-and-drop PDF report builder for Odoo. Design professional documents visually — no QWeb, no XML, no code required. Bind any Odoo model field, build dynamic tables, add images, barcodes, watermarks and preview real data instantly inside the designer.
...
Stop fighting with QWeb templates. Report Designer gives your team a full visual canvas with real-time field binding, expression logic, and instant PDF preview.
...
A WYSIWYG canvas built on Fabric.js. Drag elements from the sidebar, position them freely, resize with handles, and configure every style property in the right panel — all in real time.
...
Click Preview directly inside the designer, pick a real record, and generate a pixel-perfect PDF instantly. Renders actual field data, images, tables, and barcodes — exactly as it will print.
...
| Requirement | Details |
| --- | --- |
| Odoo Version | 19.0 Community or Enterprise |
| Python | 3.10+ (matches Odoo 19 requirement) |
| Python Packages | `reportlab`≥ 3.6 — pip install reportlab |
| Odoo Depends | base, web, mail, account, sale |
| Browser | Any modern browser (Chrome, Firefox, Safari, Edge) |
...
account) |

---

Title: Qweb PDF Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/report_builder_visual
Published: N/A
Author: N/A
Highlights:
Qweb PDF Report Builder | Odoo Apps Store
...
# Qweb PDF Report Builder
...
v 18.0 Third Party
...
| Availability |
| --- |
| Lines of code | 6708 |
| Technical Name | `
 report_builder_visual` |
| License | OPL-1 |
| Website | https://synodica.com |
...
| Availability |
| --- |
| Lines of code | 6708 |
| Technical Name | `
 report_builder_visual` |
| License | OPL-1 |
| Website | https://synodica.com |
...
Direct Design - No XML Development
...
# Visual Report Builder. Design Directly. Bypass Code. Live PDF. One-Click Publish.
...
Stop wasting hours writing QWeb XML, modifying paper formats in code, and compiling PDFs. Visual Report Builder enables functional consultants, administrators, and developers to drag, drop, and publish pixel-perfect reports directly in the Odoo interface.
...
Zero external APIs or heavy rendering
...
#### Direct Visual Builder Style
...
- Drag & Drop: Place tables, text, barcodes, and lines on an intuitive grid
- Zero Restarts: Apply edits live, save drafts, and publish instantly
- Visual Configuration: Set font family, size, colors, and margins via sidebar UI
- Live Rendering: Generate real PDF preview with actual records as you design
- Empower Business Users: Let administrators manage layout, logos, and terms
- Safe Logic Sandbox: Auto-built Jinja2 expressions are linted before saving
...
## Upcoming: AI Layout Builder
...
In our upcoming version, designing custom reports is completely streamlined. Just upload a PDF or an image of your target report design, and watch the AI convert it directly into a layout JSON file. Upload that file into Odoo, and your report configuration is fully complete and ready to print!
...
1. Upload Reference: Provide a PDF file or an image/screenshot of your target report design.
2. Generate Layout File: The AI converts your uploaded visual format into a structured JSON file automatically.
3. Import JSON File: Upload the generated JSON directly in Odoo.
4. Done! The report is instantly generated with correct spacing, margins, and headers.
...
The AI-powered layout builder (JSON generation & auto-formatting) is under active development. Once released in version 2.0, the module price will increase. Purchase the module today at the current rate to secure your license, and receive the AI upgrade 100% free of charge!
...
## How the Builder Works
...
Click Preview to generate a real PDF in seconds. Review text positioning and tables with actual record data.
...
One-Click Publish
...
Publish to auto-generate underlying QWeb XML view overrides. Revert to draft or restore older history anytime.
...
Explore the layout builder features. Build layouts
...
, browse database
...
5. Convert PDF/Image to Layout JSON (Upcoming)
...
Simply upload a PDF or image of your desired report layout. The AI converts it into a structured JSON fileâthen just upload the file and the layout is fully built!
...
6. Instant Server-Side PDF Preview
...
No client-side approximations. Click Preview to let Odoo render a real PDF using active database records, giving you a 100% accurate visual representation of the printed document.
...
Once published, the customized report automatically registers in the Odoo Action framework. Standard users can generate the pixel-perfect layout with a single click from the standard native form view's Print menu.
...
## Ultimate Design Control
...
Experience direct report development inside Odoo with capabilities designed for both business professionals and developers
...
& Drop Editor
...
Place and scale text fields, dynamic tables,
...
, shapes, and images visually. Custom grids ensure
...
##### Roadmap: AI Layouts
...
Convert PDF/Image layouts to JSON using AI, then upload them directly to auto-compile your visual reports. (Free upcoming update v2.0).
...
Banish slow manual QWeb coding cycles. Empower your team to modify invoice formats, quotation layouts, picking templates, and barcode labels visually inside Odoo.
...
© 2026 Synodica Solutions PVT. LTD. - Qweb PDF Report Builder for Odoo 18

---

Title: BJET Print Form Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/bjet_print_form_builder
Published: N/A
Author: N/A
Highlights:
## Bjet Print Form Builder makes Odoo reports dynamic, flexible, and business-friendly.
...
### Design, Customize,
...
Create, customize, and print professional business documents in Odoo - without coding. Design invoices, offers, and other forms directly in the Odoo interface. Fully compatible with Odoo Community and Enterprise editions.
...
Built-in HTML/WYSIWYG editor - allowing users to design templates visually.
...
### Design Your Odoo Print Forms Smarter with AI
...
Our AI assistant creates QWeb templates for BJet Print Form Builder - from invoices to delivery notes. Always verify and test your code.
...
### HTML / WYSIWYG Editor
...
- Design templates with a user-friendly interface.
- Supports text formatting, tables, images, lists, and hyperlinks.
- Access to HTML source view for advanced users.
- Live preview with real data.
...
### Dynamic Data Insertion
...
Use Odoo QWeb expressions directly in templates with support for nested fields, custom methods, and data formatting.
...
- Toggle between "Code" and
...
Preview" views
...
- Select from
...
Odoo print layouts or create your own print format.
...
- Render documents in real A4 layout - ready for PDF export.
...
Interactive Preview & Print
...
- Toggle between "Code" and "Preview" views without losing changes.
- Select from standard Odoo print layouts or create your own print format.
- Render documents in real A4 layout - ready for PDF export.

---

Title: Omni Designer Overview | Omni Byte
URL: https://omni-byte.com/docs/omni-designer/
Published: N/A
Author: Omni Byte
Highlights:
Omni Designer is a powerful drag-and-drop visual report generator built as the modern alternative to complex QWeb coding. Effortlessly create pixel-perfect layouts with zero server-side dependencies. It achieves flawless native integration for your modern workflows, providing lightning-fast preview and rendering directly in your browser.
...
Drag-and-Drop Editor
...
Intuitive visual interface for building reports without coding.
...
Client-Side Rendering
...
Instant PDF preview directly in the client browser.
...
Odoo Data Binding
...
Seamlessly browse and bind Odoo fields, including relational and computed fields.
...
Includes Text, Images, Tables, Barcodes, QR Codes, Shapes, and more.
...
Interface Guide Navigate the designer workspace, panels, and tools.
...
Data Binding & Expressions Bind Odoo data to your report design.

---

Title: Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/ubx_report_builder
Published: N/A
Author: N/A
Highlights:
Report Builder | Odoo Apps Store
...
# Report Builder
...
v 18.0 Third Party 214
...
# 🚀 Report Builder
...
Professional Dynamic Report Generation for Odoo 18
...
Transform the way you create reports in Odoo! Report Builder is a powerful, user-friendly module that empowers users to design custom reports without any programming knowledge. With an intuitive drag-and-drop interface, advanced filtering capabilities, and professional export options, you can generate exactly the reports your business needs in minutes.
...
✨ Key Features
...
#### Drag & Drop Interface
...
#### Advanced Filtering
...
#### PDF Export
...
Generate professional PDF reports with proper formatting, headers, and your filtered data preserved.
...
#### Excel Export
...
#### Responsive Design
...
Modern, mobile-friendly interface that works perfectly on desktops, tablets, and smartphones.
...
#### Column Customization
...
Odoo 18.0 OWL Framework Python 3.10+ JavaScript ES6+ ReportLab PDF XlsxWriter Excel PostgreSQL Responsive CSS
...
- Odoo 18.0 Community or Enterprise Edition
- Python 3.10 or higher
- ReportLab library (for PDF generation)
- Modern web browser (Chrome, Firefox, Safari, Edge)
...
- base (Odoo Core)
- web (Odoo Web Framework)
- base_setup (Odoo Setup)
...
- reportlab (
...
auto-installed)
...
## 🎨 User Interface Highlights
...
- Modern, clean interface with intuitive navigation
- Three-panel layout: Models → Available Fields → Selected Fields
- Real-time search and filtering of fields
- Visual icons for different field types
- Color-coded relational fields with expand/collapse
- Responsive design works on all screen sizes
- Dark mode compatible
- Accessibility features for screen readers
...
| Availability | Odoo Online Odoo.sh On Premise |
| --- | --- |
| Lines of code | 6350 |
| Technical Name | `
 ubx_report_builder` |
| License | LGPL-3 |
| Website | https://urbexlabs.com |

---

Title: PDF Report Designer | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/ld_pdf_report_designer
Published: N/A
Author: N/A
Highlights:
PDF Report Designer | Odoo Apps Store
...
# PDF Report Designer
...
v 18.0 Third Party
...
| Availability |
| --- |
| Odoo Apps Dependencies | Discuss (mail) |
| Lines of code | 2400 |
| Technical Name | `
 ld_pdf_report_designer` |
| License | OPL-1 |
| Website | https://lutfi.dev |
...
# PDF Report Designer
...
Design beautiful PDF reports without writing a single line of XML or code.
...
Features (FREE): - Visual drag-drop canvas designer (like Canva / Figma simplified) - Basic elements: text, image, line, rectangle, page number, date - Bind dynamic fields from any Odoo model - Live preview with sample data - A4 / Letter / Custom page size - Up to 2 customizable report templates
...
Features (PRO version): - Unlimited report templates - Advanced elements: table (line items), barcode/QR code, watermark, signature block - Conditional visibility logic (show/hide based on field value) - Theme system: Corporate, Modern, Minimal, Elegant presets - Per-company template support - Export/import templates (JSON) - Multi-language report versions

---

Title: Odoo Report Studio Module– Generate 10X Better Reports Without Coding
URL: https://codersfort.com/odoo-report-studio-module/
Published: 2026-06-17T03:13:20.000Z
Author: N/A
Highlights:
# Odoo Report Studio Module
...
## No. 1 PDF report designer for Odoo Community — design, edit, and customize reports without writing code
...
Odoo Report Studio is a no-code PDF report designer module developed by CodersFort, exclusively for the Odoo Community Edition. It enables business users to edit existing reports, create new ones from scratch, and customize report design — including layout, font size, images, logos, tables, address blocks, and headers — without any developer involvement. Compatible with All Odoo versions.
...
Odoo Report Studio gives you complete control over your business documents without writing a single line of code. Using a simple drag-and-drop report designer, you can quickly create, edit, and print professional reports tailored to your business needs.
...
Control visual elements including font size, layout, logos, headers, images, tables, address blocks, and color — all visually, without code.
...
Odoo Report Studio is a feature within the Odoo Community Edition that allows users to customize and create PDF business reports. It provides tools to edit existing reports such as invoices and quotations, build entirely new reports from scratch, and control visual design elements — all without requiring programming skills.
...
Odoo Report Studio lets you create, edit, and customize PDF reports using a visual drag-and-drop interface. Instead of modifying QWeb templates manually, business users and consultants can design invoices, quotations, purchase orders, delivery slips, and other reports directly within Odoo.
...
Getting started with Odoo Report Studio is simple. Create professional PDF reports from scratch using an intuitive visual editor—no programming or QWeb knowledge required. Just follow these steps to start building reports tailored to your business needs.
...
Your report is ready to customize with dynamic fields, tables, images, company branding, and formatting options—all without writing a single line of code.
...
The visual editor makes report design simple—no coding or QWeb knowledge is required.
...
Installing the Odoo Report Studio module takes under five minutes and requires no coding knowledge. Download the module from the CodersFort app store or the official Odoo Apps marketplace, upload it to your custom addons directory, enable developer mode, and install it from the Apps list. Follow the six steps below to get Odoo Report Studio running on your Odoo instance and start customizing PDF reports right away.
...
Whether you need to build a report from scratch or improve an existing one, Odoo Report Studio provides a flexible way to work with layouts, fields, and design elements. It is
...
development time,
...
Build and modify reports without writing code. Odoo Report Studio allows users to create professional report layouts through a visual interface, making it easier for non-technical users to manage report design.
...
Add report components such as text blocks, tables, columns, images, address fields, and data values using a simple drag-and-drop workflow. This makes report customization faster and more accessible.
...
CodersFort develops and maintains a growing library of 1,000+ Odoo modules designed to extend and enhance the standard Odoo ERP platform. Each module is built by certified Odoo developers, fully tested, and ready to integrate with any Odoo version.
...
Odoo Report Studio empowers business users to create, customize, and modify professional PDF reports without writing code. Whether you need to edit invoices, quotations, delivery slips, or build entirely new report templates, Report Studio gives every department complete control over report design.
...
Create reusable report templates for clients, customize existing reports, and deploy branded PDF documents without writing complex QWeb code. Reduce implementation time and simplify client customization.
...
Odoo Report Studio enables businesses to create, customize, and manage professional PDF reports without coding. From invoices and quotations to delivery slips and purchase orders, you can design reports visually, apply company branding, and modify layouts in minutes.
...
Business users can create and customize reports using a drag-and-drop interface without writing QWeb, XML, or Python code.
...
Odoo Report Builder is developed and maintained by CodersFort — an Odoo-certified development partner based in Kollam, Kerala, India. With over 7 years of Odoo ERP experience and more than 1000 published Odoo modules, CodersFort has helped businesses across manufacturing, trading, retail, healthcare, and logistics implement and customise Odoo for their specific needs.
...
We help you install and configure Odoo Report Studio in your Odoo instance and customize report templates to match your business needs. Whether you need branded invoices, quotations, delivery slips, purchase orders, or custom PDF reports, our team can tailor layouts, add custom fields, and optimize report designs without disrupting your workflow. We typically respond to support requests within one business day during Indian business hours (Mon–Fri).
...
Odoo Report Studio is a no-code report designer that allows you to create, edit, and customize PDF reports directly within Odoo. You can modify invoices, quotations, purchase orders, delivery slips, and other business documents using a visual drag-and-drop interface without writing QWeb or XML code.
...
No. Odoo Report Studio is designed for business users, consultants, and administrators. Reports can be created and customized using a visual editor without programming knowledge.
...
Yes. Odoo Report Studio lets you modify existing Odoo reports, including layouts, logos, headers, footers, tables, fonts, colors, and dynamic fields without recreating the report from scratch.
...
Yes. You can insert custom Odoo fields, calculated values, dynamic tables, barcodes, QR codes, images, and other data directly into your reports using the visual editor.
...
CodersFort provides installation, configuration, customization, and ongoing support for Odoo Report Studio. Our experts can tailor report layouts, implement business-specific requirements, integrate custom fields, and help you build professional reports that match your operational workflows.
...
Yes. Odoo Report Studio allows you to create brand-new PDF reports from scratch using a visual editor. You can choose a report layout, add dynamic fields, insert tables, and design reports that meet your business requirements.
...
Yes. You can customize report layouts, add company branding, include custom fields, control element visibility, and create reports tailored to your specific business processes without modifying the core Odoo code.
```

---

## Assistant (Odoo-Dev · Big Pickle · 45.4s)

_Thinking:_

The user is asking if there are any report design tools that can then convert the design
into a report understood by Odoo. I found quite a few options from the search results.
Let me summarize them clearly.

¡Sí! Existen **varias herramientas** de diseño visual de reportes que generan código
compatible con Odoo. Te las clasifico por categorías:

---

## 🎨 Herramientas de Diseño Visual (Drag & Drop) para Odoo

### 1. **Omni Designer** (⭐ Muy recomendado)

- **Web:** https://omni-byte.com
- **Odoo App Store:** https://apps.odoo.com/apps/modules/19.0/omni_designer
- **Compatibilidad:** Odoo 16, 17, 18 y 19
- **Qué hace:** Editor visual drag-and-drop con motor de renderizado PDF client-side
  (WebAssembly)
- **Características:**
  - Diseñador visual con reglas y cuadrícula
  - Previsualización PDF en tiempo real en el navegador
  - Bind de campos de Odoo arrastrando desde el árbol de datos
  - Soporte para tablas, imágenes, códigos de barras, QR, secciones repetitivas
  - Lógica condicional de visibilidad
  - **Sin necesidad de escribir XML/QWeb**
- **Requiere:** Módulo `omni_report` (motor de renderizado) como dependencia

### 2. **Report Studio** (QWeb Builder + Excel Builder)

- **Odoo App Store:** https://apps.odoo.com/apps/modules/18.0/td_report_studio
- **Compatibilidad:** Odoo 18 y 19
- **Qué hace:** Dos builders en uno — QWeb Builder (PDF/HTML) y Excel Builder
- **Características:**
  - Editor WYSIWYG con previsualización en vivo
  - 18 componentes drag-and-drop
  - Bind dinámico de campos desde cualquier modelo Odoo
  - 8 presets de estilo + 20 fondos de página
  - Visibilidad condicional (if/elif/else)
  - Modo oscuro, zoom 50%-200%, layout de 3 paneles

### 3. **Report Designer** (por VIS - Visual Innovation Studio)

- **Odoo App Store:** https://apps.odoo.com/apps/modules/19.0/vis_report_designer
- **Compatibilidad:** Odoo 19
- **Qué hace:** Constructor de reports PDF pixel-perfect con canvas WYSIWYG basado en
  Fabric.js
- **Características:**
  - Arrastra texto, campo, imagen, tabla, línea, código de barras, etc.
  - Tablas con fuente One2many/Many2many
  - Zonas de Header/Footer que se repiten en cada página
  - Editor de expresiones con biblioteca de funciones (String, Math, Date...)
  - Previsualización PDF instantánea con datos reales
- **Requiere:** `pip install reportlab`

### 4. **Report Drag & Drop Builder (Advanced)**

- **Odoo App Store:** https://apps.odoo.com/apps/modules/19.0/report_dragdrop
- **Compatibilidad:** Odoo 17, 18, 19
- **Qué hace:** Constructor visual de plantillas QWeb listas para usar
- **Características:**
  - Editor de bloques visual drag-and-drop
  - Bind dinámico de campos (t-field, t-esc)
  - Diseñador de tablas One2many
  - Panel de propiedades avanzado (tipografía, espaciado, bordes...)
  - Publicación independiente de acciones PDF y Word

### 5. **Qweb PDF Report Builder** (por Synodica)

- **Odoo App Store:** https://apps.odoo.com/apps/modules/18.0/report_builder_visual
- **Compatibilidad:** Odoo 18
- **Qué hace:** Constructor visual que genera QWeb XML automáticamente
- **Características:**
  - Drag & drop de tablas, texto, códigos de barras, líneas
  - Field Picker de 3 niveles (relaciones anidadas)
  - Vista previa PDF real desde el servidor
  - **Próximamente:** Conversión de PDF/imagen a layout JSON con IA 🤖
  - One-Click Publish que genera el QWeb XML subyacente

### 6. **PDF Report Designer** (Versión FREE disponible)

- **Odoo App Store:** https://apps.odoo.com/apps/modules/18.0/ld_pdf_report_designer
- **Compatibilidad:** Odoo 18
- **Qué hace:** Diseñador visual tipo Canva/Figma simplificado para reports
- **Versión FREE:** Hasta 2 plantillas, elementos básicos (texto, imagen, línea,
  rectángulo)
- **Versión PRO:** Tablas, barcode/QR, watermark, lógica condicional, temas predefinidos

---

## 📝 Herramienta tipo Word/Excel Template Engine

### 7. **Report Designer - Word & Excel Template Engine**

- **Odoo App Store:** https://apps.odoo.com/apps/modules/19.0/sm_report_designer
- **Compatibilidad:** Odoo 19
- **Qué hace:** Diseña en Word/LibreOffice/Google Docs con placeholders `{{campo}}`, y
  Odoo lo convierte a PDF
- **Características:**
  - Usa `.docx` o `.xlsx` como plantilla
  - Placeholders tipo `{{partner_id.name}}`
  - Soporte de imágenes con `{{img:company_id.logo}}`
  - Condiciones `{{#if}}/{{#else}}/{{/if}}`
  - Salida en PDF, DOCX, XLSX, HTML, ODT, RTF
  - Merge de PDF para múltiples registros

---

## 🏢 Odoo Studio (Enterprise)

Si tienes **Odoo Enterprise**, **Odoo Studio** incluye un report builder integrado:

- Arrastrar y soltar elementos
- Bind de campos desde cualquier modelo
- Previsualización en vivo
- Genera QWeb XML automáticamente
- Sin necesidad de módulos adicionales

---

## Tabla Comparativa Rápida

| Herramienta               | Tipo                | Versión Odoo | Precio   | Código generado      |
| ------------------------- | ------------------- | ------------ | -------- | -------------------- |
| **Omni Designer**         | Visual canvas       | 16-19        | De pago  | Propio (client-side) |
| **Report Studio**         | Visual WYSIWYG      | 18-19        | De pago  | QWeb XML             |
| **Report Designer (VIS)** | Visual canvas       | 19           | De pago  | ReportLab PDF        |
| **Drag & Drop Builder**   | Visual bloques      | 17-19        | De pago  | QWeb XML             |
| **Qweb PDF Builder**      | Visual + AI         | 18           | De pago  | QWeb XML             |
| **PDF Report Designer**   | Visual (FREE tier)  | 18           | FREE/Pro | Propio               |
| **Word/Excel Engine**     | Template Word/Excel | 19           | De pago  | DOCX/XLSX → PDF      |
| **Odoo Studio**           | Visual integrado    | Enterprise   | Incluido | QWeb XML             |

---

## Mi recomendación

Para tu caso (estás aprendiendo Odoo 18 en un entorno de desarrollo con Doodba):

1. **Si quieres aprender el proceso "real"**: quédate con QWeb/XML manual — es lo que
   todo desarrollador Odoo debe saber
2. **Si quieres eficiencia para reports simples**: prueba **PDF Report Designer** (tiene
   versión FREE)
3. **Si quieres el mejor equilibrio visual + potencia**: **Omni Designer** o **Report
   Studio** son las opciones más completas
4. **Si tu equipo no es técnico**: **Report Designer - Word & Excel Engine** es ideal
   porque diseñan en Word/Excel y Odoo lo convierte

¿Te interesa que profundice en alguna de estas herramientas en particular?

---

## User

Se podría crear un generador de reportes visual (al más puro estilo parecido a jasper
Report) para Odoo en React, que pudiera leer la estructura de las tablas y que
pudieramos hacer con ellos generación de Qweb/XML?

---

## Assistant (Odoo-Dev · Big Pickle · 18.8s)

_Thinking:_

El usuario pregunta si se podría crear un generador de reportes visual estilo
JasperReport para Odoo, pero usando React, que leyera la estructura de tablas de Odoo y
generara QWeb/XML. Esto es una pregunta de arquitectura/diseño técnico. Voy a investigar
un poco sobre cómo funciona Odoo internamente con los reports, las APIs disponibles, y
si ya existen soluciones similares que puedan servir de referencia.

**Tool: websearch**

**Input:**

```json
{
  "query": "Odoo QWeb report generator visual tool React frontend API model fields introspection XML generation",
  "numResults": 8,
  "type": "deep"
}
```

**Output:**

```
Title: Report Designer | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/vis_report_designer
Published: N/A
Author: N/A
Highlights:
A pixel-perfect, drag-and-drop PDF report builder for Odoo. Design professional documents visually — no QWeb, no XML, no code required. Bind any Odoo model field, build dynamic tables, add images, barcodes, watermarks and preview real data instantly inside the designer.
...
Stop fighting with QWeb templates. Report Designer gives your team a full visual canvas with real-time field binding, expression logic, and instant PDF preview.
...
Navigate your Odoo model's fields with full relation traversal, type badges, and one-click insertion.
...
Write Python-style expressions with a built-in function library (String, Math, Date, Type Conversion) and guided field insertion.
...
Select any real record from the designer and generate a live PDF preview without leaving the editor.
...
Click Open Designer. Drag elements from the left sidebar (Text, Field, Image, Table, …) onto the canvas. Resize and reposition with your mouse. Use the right panel to style each element and bind Odoo fields.
...
Select a Field element → right panel → Browse Fields tab. Navigate the model's field tree (relations expand to sub-fields) and click any field to bind it instantly. Use the Expression Editor for computed values like`partner_id.name`.
...
Drag a Table element onto the canvas. In the right panel choose a Data Source (any One2many / Many2many field, e.g.`order_line`). Click Add Column and pick the field to display in each column.
...
Click the Preview button (top toolbar) → enter a record ID → the PDF renders immediately inside the
...
real values from your database
...
A WYSIWYG canvas built on Fabric.js. Drag elements from the sidebar, position them freely, resize with handles, and configure every style property in the right panel — all in real time.
...
Tables are first-class citizens. Bind them to any One2many or Many2many relation, then configure each column independently — header, content type, field expression, width, and visibility.
...
Three focused tabs keep the workspace organised: a component palette to drag new elements, a live field browser for your model's data, and a page manager for multi-page documents.
...
## Expression Editor with Function Library
...
Write powerful dynamic expressions with a guided editor. Browse model fields in the left panel, insert functions from categorised snippets on the right, and get instant syntax validation.
...
Click Preview directly inside the designer, pick a real record, and generate a pixel-perfect PDF instantly. Renders actual field data, images, tables, and barcodes — exactly as it will print.
...
No XML knowledge required. From install to first PDF in under 5 minutes.
...
Design visuallyClick Open Designer. Drag elements from the sidebar, bind model fields, style everything from the right panel.
...
Preview with real dataClick Preview in the toolbar, select any existing record, and generate a live PDF instantly.
...
| --- | --- |
...
| Odoo Version | 19.0 Community or Enterprise
...
| Python | 3.10+
...
matches Odoo 19 requirement) |
...
| Python Packages | `reportlab`≥ 3.6 — pip install reportlab |
...
| Odoo Depends | base, web, mail, account, sale |
...
| Browser | Any modern browser (Chrome, Firefox, Safari, Edge) |

---

Title: odoo-introspection | odoo-toolbox
URL: https://www.marcfargas.com/~odoo-toolbox/packages/odoo-introspection
Published: N/A
Author: N/A
Highlights:
TypeScript introspection and code generation for Odoo models.
...
- Runtime Introspection: Query Odoo's`ir.model` and`ir.model.fields` to discover models and their schemas
- Type Generation: Automatically generate TypeScript interfaces from live Odoo metadata
- Field Type Mapping: Intelligent mapping of Odoo field types to TypeScript types
- Caching: Built-in caching to minimize RPC calls
- CLI Tool: Command-line tool for easy code generation
...
{ createClient } from '@marcfargas/odoo-client';
import { Introspector } from '@marcfargas/odoo-introspection';
...
// Create introspector
const introspector = new Introspector(client);
...
// Get all models
const models = await introspector.getModels();
console.log(models.map(m => m.model)); // ['res.partner', 'sale.order', ...]
...
// Get fields for a model
const fields = await introspector.getFields('res.partner');
...
// Get complete metadata
const metadata = await introspector.getModelMetadata('res.partner');
console.log(metadata.model.name);    // 'Contact'
console.log(metadata.fields.length); // 50+
...
oo-introspect
...
8069
...
\
...
output src/
...
## API ​
...
##### getModels(options?) ​
...
```

const models = await introspector.getModels({ includeTransient: false, // Include wizard
models modules: ['sale'], // Filter by modules bypassCache: false // Force fresh query
}); ...

##### getFields(modelName, options?) ​

... Retrieve all fields for a model. ... introspector.getFields ...

##### getModelMetadata(modelName, options?) ​

... Retrieve complete metadata (model + fields ...

### CodeGenerator Class ​

... Generate TypeScript interfaces from Odoo schemas. ...

```
import { CodeGenerator } from '@marcfargas/odoo-introspection';
...
const generator = new CodeGenerator(client);
...
const code = await generator.generate({
  outputDir: './src/models',
  includeTransient: false,
  modules: undefined,
  bypassCache: false
});
```

...

## Generated Code ​

... The code generator produces TypeScript interfaces like: ...

````
/**
 * Contact
 *
 * Odoo Model: res.partner
 */
export interface ResPartner {
  /**
   * Name
   * @required
   */
  name: string;

  /**
   * Email
   */
  email?: string;

  /**
   * Customer
   */
  customer: boolean;

  // ... more fields
}
...
## Type Mapping ​
...
Odoo field types are mapped to TypeScript as follows:
...
| Odoo Type | TypeScript Type |
| --- | --- |
| `char`,`text`,`html` | `string` |
| `integer` | `number` |
| `float`,`monetary` | `number` |
| `boolean` | `boolean` |
| `date`,`datetime` | `string`(ISO 8601) |
| `many2one` | `number` |
| `one2many`,`many2many` | `number[]` |
| `selection` | `string` |
| `binary` | `string` |
...
## Caching ​
...
Introspection results are cached in memory to minimize RPC overhead. Cache is automatically managed:
...
- Models are cached after the first`getModels()` call
- Fields are cached per-model after each`getFields()` call
- Combined metadata is cached after`getModelMetadata()` calls
...
Use`bypassCache: true` to force a fresh query, or call`clearCache()` to reset all caches.

---

Title: @kodeme-io/next-core-codegen v0.8.4
URL: https://registry.npmjs.org/%40kodeme-io%2Fnext-core-codegen
Published: 2025-10-07T11:53:26.000Z
Author: N/A
Highlights:
TypeScript code generation utilities for next-core framework with React Query hooks and API client generation
...
TypeScript code generation utilities for next-core framework, specifically designed to generate type-safe interfaces from Odoo models.
...
- 🚀 **Automatic Type Generation** - Generate TypeScript interfaces from any Odoo model
- 🔍 **Native Odoo Integration** - Uses Odoo's built-in `fields_get()` API
- 📝 **Zero Configuration** - Works out of the box with sensible defaults
- 🎯 **Type Safety** - Prevents runtime errors through compile-time checking
- 🔄 **Regenerate Anytime** - Types stay in sync with your Odoo schema
- 📦 **Framework Agnostic** - Works with any Odoo project using next-core
...
```json
{
  "odoo": {
    "url": "${ODOO_URL}",
    "db": "${ODOO_DB}",
    "username": "${ODOO_USERNAME}",
    "password": "${ODOO_PASSWORD}"
  },
  "models": [
    "res.partner",
    "res.users",
    "product.product",
    "sale.order",
    "sfa.visit"
  ],
  "output": "src/types/odoo.ts",
  "exclude": [
    "ir.*",
    "mail.*",
    "base.*"
  ]
}
...
```bash
...
# Discover and generate all available
...
npx next-core-codegen types --discover
...
# Generate specific models
npx next-core-codegen types --models res.partner,sale.order
...
: ResPartner[]
...
## Field Type Mapping
...
The generator maps Odoo field types to TypeScript types:

| Odoo Type | TypeScript Type | Example |
| --- | --- | --- |
| `char` | `string` | `name: string` |
| `text` | `string` | `description: string` |
| `html` | `string` | `content: string` |
| `integer` | `number` | `quantity: number` |
| `float` | `number` | `price: number` |
| `monetary` | `number` | `amount: number` |
| `boolean` | `boolean` | `active: boolean` |
| `date` | `string` | `date_order: string` |
| `datetime` | `string` | `create_date: string` |
| `binary` | `string` | `image: string` |
| `many2one` | `Many2one` | `partner_id: Many2one` |
| `one2many` | `One2many` | `order_ids: One2many` |
| `many2many` | `Many2many` | `tag_ids: Many2many` |
| `selection` | Union Type | `state: 'draft' \ | 'done'` |
...
## API Usage
...
You can also use the codegen utilities programmatically:
...
```typescript
import { OdooIntrospector, TypeScriptGenerator } from '@kodeme-io/next-core-codegen'
import { OdooClient } from '@kodeme-io/next-core-odoo-api'
...
// Connect to Odoo
...
const odoo = new OdooClient
...
url
...
db
...
username
...
_password'
})
...
await odoo.connect()
...
// Introspect models
const introspector = new OdooIntrospector(odoo)
const schemas = await introspector.introspectModels(['res.partner', 'sale.order'])

// Generate TypeScript
const generator = new TypeScriptGenerator()
const typescript = generator.generate(schemas)
...
// Save to file
import fs from
...
fs'
fs.writeFileSync('src/types/odoo
...
ts', typescript)

---

Title: Qweb PDF Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/report_builder_visual
Published: N/A
Author: N/A
Highlights:
Direct Design - No XML Development
...
# Visual Report Builder. Design Directly. Bypass Code. Live PDF. One-Click Publish.
...
Stop wasting hours writing QWeb XML, modifying paper formats in code, and compiling PDFs. Visual Report Builder enables functional consultants, administrators, and developers to drag, drop, and publish pixel-perfect reports directly in the Odoo interface.
...
Drag-and-Drop Canvas Upcoming: AI Layout Builder No XML Coding Required 3-Level Field Picker Real-time PDF Preview Version & Snapshot History
...
Zero external APIs or heavy rendering
...
Write complex Qweb XML inheritance blocks
...
apply changes
...
Manually define tables
...
columns, borders
...
margins in code
...
- Drag & Drop: Place tables, text, barcodes, and lines on an intuitive grid
- Zero Restarts: Apply edits live, save drafts, and publish instantly
- Visual Configuration: Set font family, size, colors, and margins via sidebar UI
- Live Rendering: Generate real PDF preview with actual records as you design
- Empower Business Users: Let administrators manage layout, logos, and terms
- Safe Logic Sandbox: Auto-built Jinja2 expressions are linted before saving
...
In our upcoming version, designing custom reports is completely streamlined. Just upload a PDF or an image of your target report design, and watch the AI convert it directly into a layout JSON file. Upload that file into Odoo, and your report configuration is fully complete and ready to print!
...
1. Upload Reference: Provide a PDF file or an image/screenshot of your target report design.
2. Generate Layout File: The AI converts your uploaded visual format into a structured JSON file automatically.
3. Import JSON File: Upload the generated JSON directly in Odoo.
4. Done! The report is instantly generated with correct spacing, margins, and headers.
...
The AI-powered layout builder (JSON generation & auto-formatting) is under active development. Once released in version 2.0, the module price will increase. Purchase the module today at the current rate to secure your license, and receive the AI upgrade 100% free of charge!
...
#### Field Mapping
...
Open the Field Picker to browse relational models 3 levels deep. Drop variables directly into elements.
...
Click Preview to generate a real PDF in seconds. Review text positioning and tables with actual record data.
...
Publish to auto-generate underlying QWeb XML view overrides. Revert to draft or restore older history anytime.
...
Explore the layout builder features. Build layouts visually, browse database fields, perform instant previews, and import structures.
...
3. Insert Elements, Smart Fields & Snippets
...
Use the newly redesigned 3-column insert menu card to instantly drop static text, shapes, database-bound fields, barcodes, and smart fields (page number, print date) or advanced pre-styled snippets directly into the canvas.
...
4. Relational Field Picker
...
Select any text block and click the Field Picker. Browse Odoo database fields, including relational fields (up to 3 levels deep like`invoice_line_ids.product_id.name`), and inject dynamic tags with a click.
...
5. Convert PDF/Image to Layout JSON (Upcoming)
...
Simply upload a PDF or image of your desired report layout. The AI converts it into a structured JSON fileâthen just upload the file and the layout is fully built!
...
Layout JSON Parser & Schema Generator Dialog
...
No client-side approximations. Click Preview to let Odoo render a real PDF using active database records, giving you a 100% accurate visual representation of the printed document.
...
Once published, the customized report automatically registers in the Odoo Action framework. Standard users can generate the pixel-perfect layout with a single click from the standard native form view's Print menu.
...
Convert PDF/Image layouts to JSON using AI, then upload them directly to auto-compile your visual reports. (Free upcoming update v2.0).
...
##### 3-Level Field Picker
...
No need to memorize Odoo database field strings. Drill down through related records (M2O, O2M) up to 3 layers deep automatically.
...
##### Jinja2 Logic Linter
...
Need custom visibility or logic conditions? Use the developer mode expression panel, fortified with an on-the-fly syntax linter.
...
Odoo.

---

Title: Report Drag & Drop Builder (Advanced) | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/report_dragdrop
Published: N/A
Author: N/A
Highlights:
# Advanced Report Builder
...
## Drag & Drop QWeb Report Designer for Odoo 19
...
Create professional Odoo reports in minutes, without custom development. Empower your team to design, preview, and publish PDF or Word reports using a simple visual drag-and-drop builder.
...
Build professional reports visually without hardcoding templates. This module provides a complete report-building workflow with dynamic fields, one2many table designer, advanced styling controls, and separate print publishing for PDF and Word.
...
1. Published actions appear directly in Odoo print menu
2. Create template and choose target model (e.g.`account.move`,`sale.order`).
3. Open Advanced Builder.
4. Drag blocks to canvas and style each block from Properties panel.
5. Use /// autocomplete to insert dynamic model fields quickly.
6. Insert one2many tables and pick columns using relation-based selector.
7. Preview on real record ID to validate output data.
8. Save template.
9. Publish PDF and/or Word print action as needed.
10. Print directly from document Print menu.
...
#### Smart Field Autocomplete (///)
...
Type /// to open model fields and insert dynamic values instantly.
...
#### One2many Table
...
Select relation columns, rename headers, and generate table layout in seconds.
...
This module provides a modern visual builder for creating QWeb-ready report templates in Odoo. It is designed for business teams that need flexible report design with developer-level output quality.
...
1. Visual block editor (drag and drop)
2. Dynamic data bindings (t-field, t-esc)
3. One2many table field picker
4. Rich properties panel for typography, spacing, border, and layout
5. Publish print actions independently: - PDF action - Word action
6. In-record print wizard with format choice
...
1. Create a new template and select target model.
2. Open Advanced Builder.
3. Add and style blocks.
4. Preview using a real record.
5. Save template.
6. Publish PDF and/or Word action.
7. Print from records directly.
...
- Templates are model-aware and validated before rendering.
- Published actions can be unpublished independently.
- Word output is generated from the rendered template HTML.

---

Title: Omni Designer - Visual Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/omni_designer
Published: N/A
Author: N/A
Highlights:
### Visual Report Designer & Client-Side PDF Engine
...
Design professional PDF reports visually with integrated client-side PDF generation. No server-side rendering required.
...
Drag-and-drop interface with pixel-perfect precision. No coding, no XML, just design.
...
Seamlessly binds to any Odoo model. Appears in print menus alongside standard reports.
...
- Client-side PDF Generation - Faster rendering by offloading PDF generation to browser
...
- Smart Data Transfer - Only required fields sent
...
LRU cache with compression
...
## Rich Component Library
...
- Field - Field selector, expression, format (HTML, date, number, currency)
- QR Code, Code128, EAN13 and more
- Table - WYSIWYG design, conditional columns, header repeat
- Section - Data-driven repeating blocks
- Shape - Rectangle, Ellipse, Triangle, Star
- Line & Frame - Visual separators
- Page Break - Control pagination
- Image Library - Drag-drop upload, manage and preview resources
...
## Powerful Data Binding & Expressions
...
Bind Any Odoo Data
...
| Field Picker Browse and select from model fields |
| --- |
...
- Conditional Styles - Change colors based on data values
- Record Picker - Select specific records for preview
- Nested Relations - Access partner_id.name, order_line.product_id
...
#### vs QWeb Reports
...
- No XML coding
- Instant preview
- Precise positioning
- Any layout
...
i_designer
...
Visual drag-and-drop report builder for thermal POS receipts. No QWeb coding required.
...
19.0.1.
...
5 - Share the same PDF
...
_report_server.
...
- Improved field drag-and-drop: dropping a binary field onto the canvas now creates an Image component automatically.

---

Title: QWeb Reports — Odoo 19.0 documentation
URL: https://www.odoo.com/documentation/19.0/developer/reference/backend/reports.html
Published: N/A
Author: N/A
Highlights:
Reports are written in HTML/QWeb, like website views in Odoo. You can use the usual QWeb control flow tools. The PDF rendering itself is performed by wkhtmltopdf.

Reports are declared using a report action, and a Report template for the action to use.
...
Report templates will always provide the following variables:
...
Calling`external_layout` will add the default header and footer on your report. The PDF body will be the content inside the` `. The template’s`id` must be the name specified in the report declaration; for example`account.report_invoice` for the above report. Since this is a QWeb template, you can access all the fields of the`docs` objects received by the template.
...
By default, the rendering context will also expose the following items:
...
`docs`
...
records for the current report
...
`doc_ids`
...
`doc_model`
...
model for the`docs` records
...
If you wish to access other records/models in the template, you will need a custom report, however in that case you will have to provide the items above if you need them.
...
You can then call the translatable document from your main template with the attribute`t-lang` set to a language code (for example`fr` or`en_US`) or to a record field. You will also need to re-browse the related records with the proper context if you use fields that are translatable (like country names, sales conditions, etc.)
...
## Paper Format¶
...
Paper formats are records of`report.paperformat` and can contain the following attributes:
...
## Custom Reports¶
...
By default, the reporting system builds rendering values based on the target model specified through the`model` field.

However, it will first look for a model named`report.{module.report_name}` and call that model’s`_get_report_values(doc_ids, data)` in order to prepare the rendering data for the template.

This can be used to include arbitrary items to use or display while rendering the template, such as data from additional models:
...
````

from odoo import api, models ... class ParticularReport(models.AbstractModel): \_name =
'report.module.report_name'

    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        report = self.env['ir.actions.report']._get_report_from_name('module.report_name')
        # get the records selected for this rendering of the report
        obj = self.env[report.model].browse(docids)
        # return a custom rendering context
        return {
            'lines': docids.get_lines()
        }

```
...
When using a custom report, the “default” document-related items (`doc_ids`,`doc_model` and`docs`) will not be included. If you want them, you will need to include them yourself.
...
In the example above, the rendering context will contain the “global” values as well as the`lines` we put in there but nothing else.
...
## Reports are web pages¶
...
Reports are dynamically generated by the report module and can be accessed directly via URL:
...
For example, you can access a Sale Order report in html mode by going to http:// /report/html/sale.report_saleorder/38
...
pdf version at http:// /report

---

Title: Advanced Odoo MCP Studio - AI Builder for React Apps, Odoo Modules, Reports, Emails & Charts | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/eb_odoo_mcp_server_studio
Published: N/A
Author: N/A
Highlights:
Odoo MCP Server Studio turns Odoo into a real AI execution platform, not just a chatbot connection. Connect your supported MCP clients and let AI handle live data queries, bulk create and update, file import, custom field creation, module generation from scratch, React customer portals, PDF report building, website snippet creation, email template workflows, and live Apache ECharts dashboards directly inside Odoo.
...
Build printable reports for any Odoo module. Generate polished output and deliver it to business users without long development cycles.
...
Generate models, fields, views, menus, and security rules from business instructions. Create real Odoo modules far faster.
...
Launch full React-based customer portals and multi-page business apps connected to live Odoo data. Public share URLs, custom API endpoints, and portal user redirect — no separate hosting needed.
...
Add business-ready fields to any
...
safely without hand-coding a
...
custom module or touching Python
...
. Ask what fields a
...
has, and AI can use odoo_list_models odoo_get_fields instantly
...
Use odoo
...
module to turn business requirements into a real odoo
...
8, 19 module with models, views,
...
output instead of stopping
...
##### Launch React Portals and Self-Service Experiences from Odoo
...
Use odoo_manage_webapp to create React 18 web applications served directly from Odoo, giving teams a faster path to customer, vendor, employee, or field-service portals.
...
Each app gets its own route at`/mcp/app/ `, can include multiple pages and custom API endpoints, and can fetch server-side Odoo data through safe handlers. Portal-aware context
...
the right information
...
##### Report Builder
...
Use odoo_manage_report to create QWeb PDF or HTML reports that become part of standard Odoo printing workflows.
...
Choose the target model, define the layout, generate the template, preview it, and install it. Once live, users see the report directly in the Print menu of the related records.
...
###### Report Builder Screenshots
...
Ask AI to generate a professional, custom PDF report for a specific Odoo model.
...
The report configuration, architecture, and views are instantly created.
...
Review the generated XML layout and QWeb templates directly in the MCP Studio.
...
Manage your report's underlying components and linked actions seamlessly.
...
odoo_manage_webapp - deploy React web apps
...
odoo_manage_report - create PDF reports
```

**Tool: websearch**

**Input:**

```json
{
  "query": "JasperReport alternative Odoo integration visual designer QWeb template generator",
  "numResults": 8,
  "type": "deep"
}
```

**Output:**

```
Title: Omni Designer - Visual Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/omni_designer
Published: N/A
Author: N/A
Highlights:
### Visual Report Designer & Client-Side PDF Engine
...
Design professional PDF reports visually with integrated client-side PDF generation. No server-side rendering required.
...
#### Native Odoo Integration
...
Seamlessly binds to any Odoo model. Appears in print menus alongside standard reports.
...
| Multi-Page Templates Create and manage multi-page report templates. |
| --- |
...
## Odoo Integration
...
- Batch Export - Export multiple templates as
...
- Thumbnails - Visual preview in template list
...
- Omni Print - Direct print integration without download
...
## Compare with Alternatives
...
#### vs QWeb Reports
...
- No XML coding
- Instant preview
- Precise positioning
- Any layout
...
#### vs Jasper Reports
...
- No external server
- No Java required
- Native Odoo
- Modern UI
...
Visual drag-and-drop report builder for thermal POS receipts. No QWeb coding required.
...
- Added support for multi-page template layout and upgraded the Outline tab to a Pages tab.

---

Title: Report Designer | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/vis_report_designer
Published: N/A
Author: N/A
Highlights:
A pixel-perfect, drag-and-drop PDF report builder for Odoo. Design professional documents visually — no QWeb, no XML, no code required. Bind any Odoo model field, build dynamic tables, add images, barcodes, watermarks and preview real data instantly inside the designer.
...
Stop fighting with QWeb templates. Report Designer gives your team a full visual canvas with real-time field binding, expression logic, and instant PDF preview.
...
Manage all templates from a visual kanban board with one-click Design, Duplicate, Export, and Print Menu binding.
...
Open the Report Designer app → click New. Enter a name, choose the Target Model (e.g. Sale Order), select a paper format, then Save.
...
Click Open Designer. Drag elements from the left sidebar (Text, Field, Image, Table, …) onto the canvas. Resize and reposition with your mouse. Use the right panel to style each element and bind Odoo fields.
...
From a Sale Order (or any target model record), use the ⚙ Action menu → Print with Visual Template. Select the template and download the PDF. Alternatively, use Add to Print Menu from the template card to bind it as a permanent action button on the target model.
...
All your report templates in one visual board. Each card shows the target model, last-modified date, and a quick-action menu for Preview, Duplicate, Export, and one-click Print Menu registration.
...
A WYSIWYG canvas built on Fabric.js. Drag elements from the sidebar, position them freely, resize with handles, and configure every style property in the right panel — all in real time.
...
## Live PDF Preview — No
...
Click Preview directly inside the designer, pick a real record, and generate a pixel-perfect PDF instantly. Renders actual field data, images, tables, and barcodes — exactly as it will print.
...
Create a templateGo to Report Designer → Templates → New. Choose the target Odoo model (Sale Order, Invoice, etc.).
...
Design visuallyClick Open Designer. Drag elements from the sidebar, bind model fields, style everything from the right panel.
...
Preview with real dataClick Preview in the toolbar, select any existing record, and generate a live PDF instantly.
...
MenuUse the kanban card
...
→ Add to Print
...
to expose the template in the
...
s Action menu
...
Odoo Version | 19.0 Community
...
matches Odoo
...
19 requirement) |
...
`reportlab
...
pip install reportlab |
...
Odoo Depends |
...
Any modern browser (Chrome, Firefox, Safari, Edge) |

---

Title: Qweb PDF Report Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/report_builder_visual
Published: N/A
Author: N/A
Highlights:
# Qweb PDF Report Builder
...
Direct Design - No XML Development
...
# Visual Report Builder. Design Directly. Bypass Code. Live PDF. One-Click Publish.
...
Stop wasting hours writing QWeb XML, modifying paper formats in code, and compiling PDFs. Visual Report Builder enables functional consultants, administrators, and developers to drag, drop, and publish pixel-perfect reports directly in the Odoo interface.
...
## Direct Design vs. Traditional Coding
...
Stop making Odoo reports "the old way." Let's compare how this visual designer changes everything for developers and businesses alike.
...
- Write complex Qweb XML inheritance blocks by hand
- Restart Odoo service and upgrade modules to apply changes
- Manually define tables, columns, borders, and margins in code
- No visual reference; guess pixel sizes and compile repeatedly
- Requires professional Odoo developers for tiny updates or text tweaks
- Risk syntax/evaluation errors that crash document printouts entirely
...
#### Direct Visual Builder Style
...
- Drag & Drop: Place tables, text, barcodes, and lines on an intuitive grid
- Zero Restarts: Apply edits live, save drafts, and publish instantly
- Visual Configuration: Set font family, size, colors, and margins via sidebar UI
- Live Rendering: Generate real PDF preview with actual records as you design
- Empower Business Users: Let administrators manage layout, logos, and terms
- Safe Logic Sandbox: Auto-built Jinja2 expressions are linted before saving
...
## Upcoming: AI Layout Builder
...
In our upcoming version, designing custom reports is completely streamlined. Just upload a PDF or an image of your target report design, and watch the AI convert it directly into a layout JSON file. Upload that file into Odoo, and your report configuration is fully complete and ready to print!
...
1. Upload Reference: Provide a PDF file or an image/screenshot of your target report design.
2. Generate Layout File: The AI converts your uploaded visual format into a structured JSON file automatically.
3. Import JSON File: Upload the generated JSON directly in Odoo.
4. Done! The report is instantly generated with correct spacing, margins, and headers.
...
The AI-powered layout builder (JSON generation & auto-formatting) is under active development. Once released in version 2.0, the module price will increase. Purchase the module today at the current rate to secure your license, and receive the AI upgrade 100% free of charge!
...
## How the Builder Works
...
Drag/resize labels, shapes, tables, and images. Align to a clean mm-scale grid reflecting actual page sizes.
...
Click Preview to generate a real PDF in seconds. Review text positioning and tables with actual record data.
...
Publish to auto-generate underlying QWeb XML view overrides. Revert to draft or restore older history anytime.
...
Explore the layout builder features. Build layouts visually, browse database fields, perform instant previews, and import structures.
...
inside dynamic zones (Header, Body, Footer) on a precise millimeter-scale layout grid. Elements
...
stack, line up, or support absolute coordinate placements for billing headers and custom zones.
...
3-column insert
...
, database-bound
...
, barcodes, and smart
...
number, print date
...
-styled snippets directly into the canvas.
...
5. Convert PDF/Image to Layout JSON (Upcoming)
...
Simply upload a PDF or image of your desired report layout. The AI converts it into a structured JSON fileâthen just upload the file and the layout is fully built!
...
No client-side approximations. Click Preview to let Odoo render a real PDF using active database records, giving you a 100% accurate visual representation of the printed document.
...
Once published, the customized report automatically registers in the Odoo Action framework. Standard users can generate the pixel-perfect layout with a single click from the standard native form view's Print menu.
...
Experience direct report development inside Odoo with capabilities designed
...
both business professionals and developers.
...
Drag & Drop Editor
...
Place and scale text fields, dynamic tables, lines, shapes, and images visually. Custom grids ensure millimetric alignment.
...
##### Roadmap: AI Layouts
...
Convert PDF/Image layouts to JSON using AI, then upload them directly to auto-compile your visual reports. (Free upcoming update v2.0).
...
We build, customize, and maintain Odoo solutions for businesses worldwide - from implementation to
...
Banish slow manual QWeb coding cycles. Empower your team to modify invoice formats, quotation layouts, picking templates, and barcode labels visually inside Odoo.

---

Title: Report Drag & Drop Builder (Advanced) | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/17.0/report_dragdrop
Published: N/A
Author: N/A
Highlights:
# Advanced Report Builder
...
## Drag & Drop QWeb Report Designer for Odoo 19
...
Create professional Odoo reports in minutes, without custom development. Empower your team to design, preview, and publish PDF or Word reports using a simple visual drag-and-drop builder.
...
Build professional reports visually without hardcoding templates. This module provides a complete report-building workflow with dynamic fields, one2many table designer, advanced styling controls, and separate print publishing for PDF and Word.
...
1. Published actions appear directly in Odoo print menu
2. Create template and choose target model (e.g.`account.move`,`sale.order`).
3. Open Advanced Builder.
4. Drag blocks to canvas and style each block from Properties panel.
5. Use /// autocomplete to insert dynamic model fields quickly.
6. Insert one2many tables and pick columns using relation-based selector.
7. Preview on real record ID to validate output data.
8. Save template.
9. Publish PDF and/or Word print action as needed.
10. Print directly from document Print menu.
...
Drag blocks into the canvas and build full report layouts visually.
...
Control typography, spacing, borders, direction, and visual styling per block.
...
# Advanced Report Builder (Odoo
...
19)
...
This module provides a modern visual builder for creating QWeb-ready report templates in Odoo. It is designed for business teams that need flexible report design with developer-level output quality.
...
1. Visual block editor (drag and drop)
2. Dynamic data bindings (t-field, t-esc)
3. One2many table field picker
4. Rich properties panel for typography, spacing, border, and layout
5. Publish print actions independently: - PDF action - Word action
6. In-record print wizard with format choice
...
1. Create a new template and select target model.
2. Open Advanced Builder.
3. Add and style blocks.
4. Preview using a real record.
5. Save template.
6. Publish PDF and/or Word action.
7. Print from records directly.
...
- Templates are model-aware and validated before rendering.
- Published actions can be unpublished independently.
- Word output is generated from the rendered template HTML.

---

Title: Report Studio | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/18.0/td_report_studio
Published: N/A
Author: N/A
Highlights:
Design professional reports without writing a single line of code
...
QWeb Builder Excel Builder
...
100% visual â no programming required
...
### QWEB BUILDER
...
Visual drag & drop editor for PDF and HTML reports
...
- WYSIWYG live preview editing
- 18 drag & drop components
- Dynamic field binding from any Odoo model
- 8 style presets + 20 page backgrounds
- Conditional visibility (if / elif / else)
...
### EXCEL BUILDER
...
- Familiar Excel-like grid interface
- 5 cell types: Text, Field, Formula, Image, Link
- Dynamic tables with auto data loops
...
- 6 chart types linked to data tables
- 5 template presets (List, Detail, Summary...)
- Download pixel-perfect XLSX files
...
## QWEB BUILDER
...
### VISUAL EDITOR
...
#### WYSIWYG Live Preview
...
Edit directly on the rendered report. Click to select any element, hover to highlight with type label. Inline text editing and parent hierarchy tree navigation.
...
Zoom 50%â200% with Ctrl+/- shortcuts. 3-panel layout with templates, editor, and properties side by side. Collapsible panels, fullscreen mode, dark mode.
...
### 18 COMPONENTS
...
Smart drop targeting auto-finds the best insert point. Conditional chain protection keeps if/elif/else blocks intact. All components support drag & drop from the side panel.
...
### STYLING & DESIGN
...
Font, color, padding, margin, border, radius, opacity, background, display, class editor
...
20
...
both editor and
...
#### Template Manager
...
Create, duplicate, delete report templates. Quick create with model selector.
...
## SHARED FEATURES
...
Available in both QWeb Builder and Excel Builder
...
#### No Code
...
100% visual point & click. No programming, no XML, no Python required.
...
#### Odoo Native
...
Deep Odoo integration. Access any model, field, relation. Standard ORM & security.
...
#### 3-Panel Layout
...
Template list + editor + properties panel side by side. Collapsible left panel.
...
No-code report builder for Odoo 19

---

Title: Omni Designer Overview | Omni Byte
URL: https://omni-byte.com/docs/omni-designer/
Published: N/A
Author: Omni Byte
Highlights:
Omni Designer is a powerful drag-and-drop visual report generator built as the modern alternative to complex QWeb coding. Effortlessly create pixel-perfect layouts with zero server-side dependencies. It achieves flawless native integration for your modern workflows, providing lightning-fast preview and rendering directly in your browser.
...
Intuitive visual interface for building reports without coding.
...
PDF preview directly in the client browser.
...
Odoo Data Binding
...
Seamlessly browse and bind Odoo fields, including relational and computed fields.
...
Includes Text, Images, Tables, Barcodes, QR Codes, Shapes, and more.
...
Quick Start Learn the basics of creating a report template.
...
Data Binding & Expressions Bind Odoo data to your report design.

---

Title: BJET Print Form Builder | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/bjet_print_form_builder
Published: N/A
Author: N/A
Highlights:
## Bjet Print Form Builder makes Odoo reports dynamic, flexible, and business-friendly.
...
##### Seamless Odoo Integration
...
Create, customize, and print professional business documents in Odoo - without coding. Design invoices, offers, and other forms directly in the Odoo interface. Fully compatible with Odoo Community and Enterprise editions.
...
Built-in HTML/WYSIWYG editor - allowing users to design templates visually.
...
Design Your Odoo Print Forms Smarter with AI
...
Our AI assistant creates QWeb templates for BJet Print Form Builder - from invoices to delivery notes. Always verify and test your code.
...
### HTML / WYSIWYG Editor
...
- Design templates with a user-friendly interface.
- Supports text formatting, tables, images, lists, and hyperlinks.
- Access to HTML source view for advanced users.
- Live preview with real data.
...
### Dynamic Data Insertion
...
Use Odoo QWeb expressions directly in templates with support for nested fields, custom methods, and data formatting.

---

Title: Dynamic Report Templates & PDF Layouts | Odoo Apps Store
URL: https://apps.odoo.com/apps/modules/19.0/nz_dynamic_report
Published: N/A
Author: N/A
Highlights:
Design and print professional PDF reports directly from Odoo — without touching any XML or Python file. Pick any model, build field placeholders visually, write your HTML template, choose a layout and paper format, and generate pixel-perfect PDFs with one click.
...
This module lets you create fully custom PDF reports for any Odoo model — all from within the Odoo interface, with no developer files required. Define a report name, pick your target model, choose a report layout (Basic, External, or HTML Container) and a paper format, then write free-form HTML using {{field_name}} placeholders. The visual Field Placeholder Builder lets you navigate relational fields up to 5 levels deep and automatically generates the correct placeholder expression. Repeating sections (order lines, attendees, etc.) are handled with {{#each field}}...{{/each}} loops. A Variables panel keeps all your registered placeholders in one list with one-click append. Saving a report automatically creates a Server Action bound to the target model, so the report appears instantly in the model's Print menu. A live rendered preview shows the template populated with real record data before printing.
...
Choose from web.html_container (minimal wrapper), web.basic_layout (header & footer), or web.external_layout (company-branded letterhead) per report.
...
The Report Layout dropdown showing the three available layout options: web.html_container (minimal HTML wrapper — full control over the page), web.basic_layout (adds a standard Odoo header and footer), and web.external_layout (uses the company-branded external letterhead with logo and address).
...
The Template tab contains a full rich-text HTML editor (widget=html). The editor shows a sample report template with`{{name}}`,`{{partner_id.name}}`, and a loop block rendering order lines. You can type raw HTML, paste content from an external editor, or append placeholders directly from the Variables panel above.
...
The generated PDF using web.basic_layout: the standard Odoo header (company name, date, page number) and footer are added automatically around the custom HTML content. Field values like the order number, customer name, and order lines are fully rendered with the correct data from the record.
...
The same report rendered with web.external_layout: the company letterhead is applied with the company logo, address, and contact details. The custom HTML body sits inside the branded frame — ideal for customer-facing documents like offers, delivery notes, or certificates.
...
Because the Target Model is fully configurable, the same module works for any Odoo model — Sale Orders, Purchase Orders, Invoices, Employees, Projects, custom models, and more. Each report is independently configured with its own layout, paper format, and HTML template, giving complete flexibility across all business documents.
...
Visual Field Placeholder Builder: Browse model fields through a guided 5-level picker and generate`{{placeholder}}` expressions without writing any code.
...
Free-form HTML template editor: Write or paste any HTML in the rich-text editor — full control over layout, styling, tables, images, and custom CSS.
...
3 report layouts: Choose between web.html_container (raw wrapper), web.basic_layout (standard header/footer), or web.external_layout (company letterhead) per report.
...
No. Everything is configured inside Odoo — you pick the model, build placeholders with the visual field picker, write the HTML template in the editor, and save. The module automatically creates all the required Odoo records (report action, server action) behind the scenes.
...
Yes. The template editor accepts any valid HTML including inline` ` blocks, external CSS classes, and images. Relative image URLs (like`/web/image/product.product/1/image_1920`) are automatically resolved to absolute URLs before PDF generation so images render correctly.
...
The module is compatible with Odoo 19 Community and Enterprise on On-Premise, Odoo Online, and Odoo.sh deployments. It depends only on base and web, so it has minimal dependencies.
...
- Custom HTML report templates for any Odoo model
- Visual Field Placeholder Builder with up to 5-level relational traversal
- {{#each}} / {{/each}} loop support for One2many and Many2many fields
- Variables panel with one-click Append to template
- 3 report layouts: web.html_container, web.basic_layout, web.external_layout
- Custom paper format selection per report
- Auto-creation and auto-update of bound ir.actions.server (Print menu integration)
- Live rendered content preview field with real record data
- Multi-record PDF generation with automatic page breaks
- Absolute URL resolution for images and lazy-load fix for wkhtmltopdf
- UTF-8 encoding flag automatically added to wkhtmltopdf arguments
- Cascade deletion of server action when report is deleted
- Unique report name constraint to prevent duplicate server actions
```

---

## Assistant (Odoo-Dev · Big Pickle · 86.5s)

_Thinking:_

El usuario pregunta si se podría crear un generador de reportes visual estilo
JasperReport para Odoo, pero usando React, que leyera la estructura de las tablas y
pudiera generar QWeb/XML. Esta es una pregunta arquitectónica/técnica muy interesante.

Voy a analizar la viabilidad técnica de esto:

1. **Introspección de modelos Odoo**: Odoo expone `ir.model` y `ir.model.fields` que
   permiten descubrir la estructura de todos los modelos y campos. Ya existen librerías
   como `odoo-introspection` que hacen esto.

2. **El frontend React**: Se puede crear un diseñador visual con canvas drag-and-drop
   (similar a lo que hacen Omni Designer con WebAssembly/Fabric.js, o Report Designer
   con Fabric.js).

3. **Generación de QWeb/XML**: El designer visual necesitaría un "translator" que
   convierta el diseño visual en XML QWeb válido.

4. **Publicación en Odoo**: El módulo Odoo recibiría el XML generado y lo guardaría como
   plantilla QWeb + ir.actions.report.

Esto es totalmente viable y de hecho varios de los módulos que encontré ya implementan
partes de esto. La arquitectura sería:

- Frontend: React app con canvas visual (usando algo como Fabric.js, Konva.js, o React
  DnD)
- Backend Odoo: Módulo Python que:
  - Expone API para introspección de modelos
  - Recibe el diseño JSON/visual del frontend
  - Genera el XML QWeb correspondiente
  - Crea la ir.actions.report
  - Publica el report

Voy a dar una respuesta técnica completa sobre cómo se podría arquitecturar esto.

¡Excelente pregunta! **Sí, es totalmente viable** y de hecho ya existen módulos que
implementan partes de esta arquitectura. Te explico cómo se podría diseñar un sistema
así desde cero:

---

## 🏗️ Arquitectura Propuesta: Report Designer Visual para Odoo

### Vista general del sistema

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (React)                      │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Canvas Visual (Fabric.js / Konva.js)             │  │
│  │  • Drag & Drop de elementos                       │  │
│  │  • Propiedades de estilo (panel derecho)          │  │
│  │  • Tree view de elementos                         │  │
│  └───────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Field Picker (introspección de modelos Odoo)     │  │
│  │  • Árbol de campos del modelo seleccionado        │  │
│  │  • Navegación relacional (Many2one → campos)      │  │
│  │  • Drag desde field picker al canvas              │  │
│  └───────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Transistor Visual → QWeb XML                     │  │
│  │  • Genera JSON intermedio del diseño              │  │
│  │  • Convierte JSON → QWeb XML válido               │  │
│  │  • Preview en tiempo real via API                  │  │
│  └───────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────┘
                        │ API (XML-RPC / JSON-RPC)
┌───────────────────────▼─────────────────────────────────┐
│               BACKEND (Módulo Odoo Python)               │
│  ┌───────────────────────────────────────────────────┐  │
│  │  API Controller                                   │  │
│  │  • GET /api/models → lista de modelos disponibles │  │
│  │  • GET /api/fields/{model} → campos del modelo    │  │
│  │  • POST /api/report/publish → publica el report   │  │
│  │  • POST /api/report/preview → preview PDF         │  │
│  └───────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────┐  │
│  │  QWeb Generator (Motor de traducción)             │  │
│  │  • JSON Layout → QWeb XML template                │  │
│  │  • Genera ir.actions.report                       │  │
│  │  • Maneja herencia, sub-templates, etc.           │  │
│  └───────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Report Publisher                                 │  │
│  │  • Guarda plantilla QWeb en ir.ui.view            │  │
│  │  • Crea/actualiza ir.actions.report               │  │
│  │  • Actualiza __manifest__.py data files           │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

### 📐 Componente 1: Introspección de Modelos Odoo

Esto ya existe como librería independiente. Odoo expone los metadatos vía RPC:

```typescript
// Ejemplo usando la API de Odoo
// GET /web/dataset/call_kw → ir.model.fields.fields_get()

interface OdooField {
  type:
    | "char"
    | "integer"
    | "float"
    | "monetary"
    | "boolean"
    | "date"
    | "datetime"
    | "text"
    | "html"
    | "binary"
    | "many2one"
    | "one2many"
    | "many2many"
    | "selection";
  string: string; // Nombre legible
  required: boolean;
  readonly: boolean;
  relation?: string; // Modelo relacionado (M2O, O2M, M2M)
  selection_options?: [string, string][]; // Para selection fields
  help?: string;
  // ... otros atributos
}

// Ejemplo de uso en React
const fetchModelFields = async (modelName: string): Promise<OdooField[]> => {
  const response = await odooRpc("fields_get", {
    model: modelName,
    attributes: [
      "string",
      "type",
      "relation",
      "required",
      "readonly",
      "selection",
      "help",
    ],
  });
  return response;
};
```

**Referencia existente:** `@marcfargas/odoo-introspection` — ya hace exactamente esto:

```typescript
import {Introspector} from "@marcfargas/odoo-introspection";

const introspector = new Introspector(client);
const fields = await introspector.getFields("sale.order");
// → [{ name: 'partner_id', type: 'many2one', relation: 'res.partner', ... }, ...]
```

---

### 📐 Componente 2: El Canvas Visual (React + Fabric.js)

```tsx
// Estructura conceptual del designer
interface ReportElement {
  id: string;
  type: "text" | "field" | "table" | "image" | "line" | "barcode" | "shape";
  x: number;
  y: number;
  width: number;
  height: number;
  style: {
    fontSize: number;
    fontFamily: string;
    fontWeight: string;
    color: string;
    backgroundColor?: string;
    border?: string;
    padding?: number;
    textAlign?: "left" | "center" | "right";
  };
  // Para elementos tipo campo
  fieldBinding?: {
    model: string; // 'sale.order'
    fieldPath: string; // 'partner_id.name'
    format?: string; // 'monetary', 'date', etc.
  };
  // Para tablas (One2many)
  tableConfig?: {
    dataSource: string; // 'order_line' (campo O2M)
    columns: TableColumn[];
    headerStyle?: ElementStyle;
    rowStyle?: ElementStyle;
  };
  // Para elementos tipo texto estático
  content?: string;
  // Visibilidad condicional
  condition?: string; // "record.state == 'sale'"
}

interface TableColumn {
  header: string;
  fieldPath: string; // 'product_id.name'
  width: number;
  alignment: "left" | "center" | "right";
  format?: string;
}

interface ReportLayout {
  id: string;
  name: string;
  targetModel: string;
  paperFormat: {
    format: "A4" | "Letter" | "A3" | "Legal";
    orientation: "Portrait" | "Landscape";
    margin: {top: number; bottom: number; left: number; right: number};
  };
  elements: ReportElement[];
  // Zonas del report
  zones: {
    header?: ReportElement[];
    body: ReportElement[];
    footer?: ReportElement[];
  };
}
```

---

### 📐 Componente 3: Transistor Visual → QWeb XML

Este es el **corazón** del sistema. Convierte el JSON del diseño en QWeb XML válido:

```typescript
class QWebGenerator {
  generate(layout: ReportLayout): string {
    const lines: string[] = [];

    lines.push(`<?xml version="1.0" encoding="utf-8"?>`);
    lines.push(`<odoo>`);

    // 1. Generar la ir.actions.report
    lines.push(this.generateReportAction(layout));

    // 2. Generar la plantilla QWeb
    lines.push(this.generateTemplate(layout));

    lines.push(`</odoo>`);
    return lines.join("\n");
  }

  private generateReportAction(layout: ReportLayout): string {
    const reportName = `report_${layout.targetModel.replace(".", "_")}_${layout.id}`;
    return `
    <record id="${reportName}_action" model="ir.actions.report">
        <field name="name">${layout.name}</field>
        <field name="model">${layout.targetModel}</field>
        <field name="report_type">qweb-pdf</field>
        <field name="report_name">${reportName}_template</field>
        <field name="report_file">${reportName}_template</field>
        <field name="binding_model_id" ref="model_${layout.targetModel.replace(
          ".",
          "_"
        )}"/>
        <field name="binding_type">report</field>
        <field name="paperformat_id" ref="base.paperformat_euro"/>
    </record>`;
  }

  private generateTemplate(layout: ReportLayout): string {
    const lines: string[] = [];

    lines.push(`    <template id="${layout.id}_template">`);
    lines.push(`        <t t-call="web.html_container">`);
    lines.push(`            <t t-foreach="docs" t-as="o">`);
    lines.push(`                <t t-call="web.external_layout">`);
    lines.push(`                    <div class="page">`);

    // Renderizar cada elemento del body
    for (const element of layout.zones.body) {
      lines.push(this.renderElement(element, "o"));
    }

    lines.push(`                    </div>`);
    lines.push(`                </t>`);
    lines.push(`            </t>`);
    lines.push(`        </t>`);
    lines.push(`    </template>`);

    return lines.join("\n");
  }

  private renderElement(element: ReportElement, recordVar: string): string {
    switch (element.type) {
      case "text":
        return this.renderText(element);
      case "field":
        return this.renderField(element, recordVar);
      case "table":
        return this.renderTable(element, recordVar);
      case "image":
        return this.renderImage(element, recordVar);
      case "line":
        return this.renderLine(element);
      default:
        return "";
    }
  }

  private renderField(element: ReportElement, recordVar: string): string {
    const fieldPath = `${recordVar}.${element.fieldBinding!.fieldPath}`;
    const indent = "                    ";

    let xml = `${indent}`;

    // Aplicar estilos
    const styles = this.buildStyleString(element.style);
    if (styles) {
      xml += `<div style="${styles}">`;
    }

    // Formato según tipo de campo
    if (element.fieldBinding?.format === "monetary") {
      xml += `<span t-field="${fieldPath}"
                t-options='{"widget": "monetary",
                           "display_currency": ${recordVar}.currency_id}'/>`;
    } else if (element.fieldBinding?.format === "date") {
      xml += `<span t-field="${fieldPath}"
                t-options='{"format": "dd/MM/yyyy"}'/>`;
    } else {
      xml += `<span t-field="${fieldPath}"/>`;
    }

    if (styles) {
      xml += `</div>`;
    }

    return xml;
  }

  private renderTable(element: ReportElement, recordVar: string): string {
    const table = element.tableConfig!;
    const dataSource = `${recordVar}.${table.dataSource}`;
    const indent = "                    ";

    let xml = `${indent}<table class="table table-sm">`;

    // Cabecera
    xml += `${indent}  <thead><tr>`;
    for (const col of table.columns) {
      xml += `<th>${col.header}</th>`;
    }
    xml += `</tr></thead>`;

    // Cuerpo con loop
    xml += `${indent}  <tbody>`;
    xml += `${indent}    <t t-foreach="${dataSource}" t-as="line">`;
    xml += `${indent}      <tr>`;

    for (const col of table.columns) {
      const fieldPath = `line.${col.fieldPath}`;
      xml += `${indent}        <td>`;

      if (col.format === "monetary") {
        xml += `<span t-field="${fieldPath}"
                  t-options='{"widget": "monetary",
                             "display_currency": ${recordVar}.currency_id}'/>`;
      } else {
        xml += `<span t-field="${fieldPath}"/>`;
      }

      xml += `</td>`;
    }

    xml += `${indent}      </tr>`;
    xml += `${indent}    </t>`;
    xml += `${indent}  </tbody>`;
    xml += `${indent}</table>`;

    return xml;
  }

  private renderText(element: ReportElement): string {
    const styles = this.buildStyleString(element.style);
    return `<div style="${styles}">${element.content || ""}</div>`;
  }

  private renderLine(element: ReportElement): string {
    return `<hr style="border-top: ${element.style.border || "1px solid #ccc"}"/>`;
  }

  private renderImage(element: ReportElement, recordVar: string): string {
    if (element.fieldBinding) {
      const fieldPath = `${recordVar}.${element.fieldBinding.fieldPath}`;
      return `<img t-att-src="image_data_uri(${fieldPath})"
                style="max-width: ${element.width}px; max-height: ${element.height}px;"/>`;
    }
    return `<img src="/web/image/${element.id}"
              style="max-width: ${element.width}px;"/>`;
  }

  private buildStyleString(style: ReportElement["style"]): string {
    const parts: string[] = [];
    if (style.fontSize) parts.push(`font-size: ${style.fontSize}pt`);
    if (style.fontFamily) parts.push(`font-family: ${style.fontFamily}`);
    if (style.fontWeight) parts.push(`font-weight: ${style.fontWeight}`);
    if (style.color) parts.push(`color: ${style.color}`);
    if (style.backgroundColor) parts.push(`background-color: ${style.backgroundColor}`);
    if (style.textAlign) parts.push(`text-align: ${style.textAlign}`);
    if (style.padding) parts.push(`padding: ${style.padding}px`);
    return parts.join("; ");
  }
}
```

---

### 📐 Componente 4: Publicador en Odoo

```python
# report_publisher.py (Módulo Odoo)
from odoo import models, api
from lxml import etree


class ReportPublisher(models.AbstractModel):
    _name = 'report.designer.publisher'
    _description = 'Report Designer Publisher'

    @api.model
    def publish_report(self, layout_json):
        """Publica un report desde el JSON del diseñador visual."""

        # 1. Generar el XML QWeb desde el JSON
        qweb_xml = self.env['report.designer.generator']\
            .generate_qweb_xml(layout_json)

        # 2. Guardar la plantilla QWeb
        template_xml_id = f"report_designer.{layout_json['id']}_template"
        existing_view = self.env['ir.ui.view'].search([
            ('xml_id', '=', template_xml_id)
        ])

        if existing_view:
            existing_view.write({
                'arch': qweb_xml['template'],
            })
        else:
            self.env['ir.ui.view'].create({
                'name': f"Report: {layout_json['name']}",
                'type': 'qweb',
                'xml_id': template_xml_id,
                'arch': qweb_xml['template'],
            })

        # 3. Crear/actualizar la ir.actions.report
        report_action_xml_id = f"report_designer.{layout_json['id']}_action"
        existing_action = self.env['ir.actions.report'].search([
            ('xml_id', '=', report_action_xml_id)
        ])

        model_id = self.env['ir.model']._get(layout_json['targetModel']).id

        vals = {
            'name': layout_json['name'],
            'model': layout_json['targetModel'],
            'report_type': 'qweb-pdf',
            'report_name': f"report_designer.{layout_json['id']}_template",
            'report_file': f"report_designer.{layout_json['id']}_template",
            'binding_model_id': model_id,
            'binding_type

---

## User

Pero se podrían elegir los elementos(campos de tablas) y soltarlos (drag & drop) sobre una plantilla en la que iríamos diseñando el reporte?

---

## Assistant (Plan · Big Pickle · 87.4s)

_Thinking:_

The user is asking specifically about whether they could select elements (table fields) and drag & drop them onto a template where they would design the report. They want to understand the feasibility and how it would work from a UX/technical perspective.

Since I'm in plan mode, I should answer this question and help them understand the architecture and feasibility. Let me research a bit more about how the existing tools implement this and what technologies are commonly used for this kind of visual designer.

**¡Sí, absolutamente!** Esa es exactamente la idea central de un generador visual tipo JasperReport. Te explico cómo funcionaría el flujo de interacción y las tecnologías que lo hacen posible:

---

## 🎯 Flujo de Interacción del Usuario

### Paso 1: Seleccionar el modelo
```

┌─────────────────────────────────────┐ │ Target Model: [sale.order ▼] │ │ │ │ Cuando
seleccionas un modelo, │ │ se carga su estructura de campos │ │ en el panel lateral │
└─────────────────────────────────────┘

```

### Paso 2: Panel lateral con los campos (Field Picker)
```

┌──────────────────┐ ┌─────────────────────────────────┐ │ 📋 Field Picker │ │ │ │ │ │
CANVAS DEL REPORTE │ │ ▼ sale.order │ │ │ │ ├── name │ │ [ Arrastrar elementos aquí ] │
│ ├── partner_id ─┼──► │ │ │ │ ├── name │ │ │ │ │ ├── email │ │ │ │ │ └── phone │ │ │ │
├── date_order │ │ │ │ ├── amount_tax │ │ │ │ ├── order_line ◄────┼── (tabla O2M que se
puede │ │ │ ├── name │ │ arrastrar como bloque) │ │ │ ├── qty │ │ │ │ │ ├── price │ │ │
│ │ └── total │ │ │ │ └── state │ │ │ └──────────────────┘
└─────────────────────────────────┘ ▲ ▲ │ DRAG & DROP │ └────────────────────────┘

```

### Paso 3: Soltar un campo → Se convierte en un elemento visual
```

Al soltar "partner_id.name" en el canvas:

- Se crea un elemento "Field" en esa posición
- Se muestra con un placeholder: {{partner_id.name}}
- Panel derecho muestra propiedades editables
- Se puede redimensionar, mover, cambiar estilo

````

---

## 🛠️ Tecnologías para Implementar Esto

### Opción A: Canvas con Fabric.js (la más usada)

```tsx
// React + Fabric.js — el canvas visual
import { fabric } from 'fabric';

const ReportCanvas: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [fabricCanvas, setFabricCanvas] = useState<fabric.Canvas | null>(null);

  useEffect(() => {
    if (canvasRef.current) {
      const canvas = new fabric.Canvas(canvasRef.current, {
        width: 794,   // A4 width en px (210mm @ 96dpi)
        height: 1123, // A4 height en px (297mm @ 96dpi)
        backgroundColor: '#fff',
      });
      setFabricCanvas(canvas);
    }
  }, []);

  // Handler cuando sueltas un campo del Field Picker
  const handleFieldDrop = (field: OdooField, position: { x: number; y: number }) => {
    const fieldText = new fabric.IText(`{{${field.name}}}`, {
      left: position.x,
      top: position.y,
      fontSize: 12,
      fontFamily: 'Arial',
      fill: '#333',
      // Guardamos metadata del campo vinculado
      data: {
        type: 'field',
        fieldName: field.name,
        fieldType: field.type,
        fieldRelation: field.relation,
      },
    });

    fabricCanvas?.add(fieldText);
    fabricCanvas?.renderAll();
  };

  // Handler para soltar una tabla O2M
  const handleTableDrop = (field: OdooField, position: { x: number; y: number }) => {
    // Crear grupo con header + filas de ejemplo
    const headerText = new fabric.IText(field.string, {
      left: position.x,
      top: position.y,
      fontSize: 14,
      fontWeight: 'bold',
      fill: '#fff',
      backgroundColor: '#333',
      data: { type: 'table_header', parentTable: field.name },
    });

    const tableGroup = new fabric.Group([headerText], {
      left: position.x,
      top: position.y,
      data: {
        type: 'table',
        dataSource: field.name,
        columns: [],  // Se configuran después
      },
    });

    fabricCanvas?.add(tableGroup);
  };

  return (
    <div className="report-designer">
      <FieldPicker
        model="sale.order"
        onFieldDrag={handleFieldDrop}
        onTableDrag={handleTableDrop}
      />
      <canvas ref={canvasRef} />
      <PropertiesPanel
        selectedElement={fabricCanvas?.getActiveObject()}
      />
    </div>
  );
};
````

### Opción B: React DnD + HTML/CSS (más flexible)

```tsx
// Usando react-dnd para el drag & drop nativo
import {useDrag, useDrop, DndProvider} from "react-dnd";

// Componente del Field Picker (panel lateral)
const FieldItem: React.FC<{field: OdooField}> = ({field}) => {
  const [{isDragging}, drag] = useDrag({
    type: "FIELD",
    item: {field},
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
  });

  return (
    <div ref={drag} className={`field-item ${isDragging ? "dragging" : ""}`}>
      <span className="field-icon">{getFieldIcon(field.type)}</span>
      <span className="field-name">{field.string}</span>
      {field.relation && <span className="relation-badge">→</span>}
    </div>
  );
};

// Componente del Canvas (zona de drop)
const ReportCanvas: React.FC = () => {
  const [elements, setElements] = useState<ReportElement[]>([]);

  const [{isOver}, drop] = useDrop({
    accept: "FIELD",
    drop: (item: {field: OdooField}, monitor) => {
      const offset = monitor.getClientOffset();
      const canvasRect = document
        .getElementById("report-canvas")
        ?.getBoundingClientRect();

      if (offset && canvasRect) {
        const newElement: ReportElement = {
          id: generateId(),
          type: item.field.type === "one2many" ? "table" : "field",
          x: offset.x - canvasRect.left,
          y: offset.y - canvasRect.top,
          fieldBinding: {
            model: "sale.order",
            fieldPath: item.field.name,
          },
          style: {fontSize: 12, fontFamily: "Arial", color: "#333"},
        };
        setElements([...elements, newElement]);
      }
    },
    collect: (monitor) => ({
      isOver: monitor.isOver(),
    }),
  });

  return (
    <div ref={drop} id="report-canvas" className={isOver ? "drop-active" : ""}>
      {elements.map((el) => (
        <ReportElementComponent
          key={el.id}
          element={el}
          onUpdate={(updated) => updateElement(el.id, updated)}
          onDelete={() => removeElement(el.id)}
        />
      ))}
    </div>
  );
};

// Renderizado de cada elemento en el canvas
const ReportElementComponent: React.FC<{
  element: ReportElement;
  onUpdate: (el: ReportElement) => void;
  onDelete: () => void;
}> = ({element, onUpdate, onDelete}) => {
  const [isDragging, setIsDragging] = useState(false);
  const [isResizing, setIsResizing] = useState(false);

  return (
    <div
      className={`report-element ${isDragging ? "dragging" : ""}`}
      style={{
        position: "absolute",
        left: element.x,
        top: element.y,
        minWidth: 100,
        border: "1px dashed #ccc",
        padding: "4px 8px",
        cursor: "move",
      }}
      onMouseDown={() => setIsDragging(true)}
      onMouseUp={() => setIsDragging(false)}
    >
      {element.type === "field" && (
        <div className="field-placeholder">
          <span className="field-label">{element.fieldBinding?.fieldPath}</span>
          <span className="field-format-hint">[t-field]</span>
        </div>
      )}

      {element.type === "table" && <TablePreview element={element} />}

      <button className="delete-btn" onClick={onDelete}>
        ×
      </button>
    </div>
  );
};
```

---

## 🔄 Pipeline Completo: Visual → QWeb XML → Odoo

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐     ┌─────────────┐
│  USUARIO    │     │   REACT      │     │  BACKEND     │     │   ODOO      │
│  (Browser)  │     │   FRONTEND   │     │  (Python)    │     │   CORE      │
└──────┬──────┘     └──────┬───────┘     └──────┬───────┘     └──────┬──────┘
       │                   │                     │                     │
       │  1. Select Model  │                     │                     │
       │──────────────────►│  2. RPC: fields_get │                     │
       │                   │────────────────────►│                     │
       │                   │  3. Fields[]         │                     │
       │                   │◄────────────────────│                     │
       │                   │                     │                     │
       │  4. Drag & Drop   │                     │                     │
       │  campos al canvas │                     │                     │
       │──────────────────►│                     │                     │
       │                   │  5. Genera JSON     │                     │
       │                   │  layout del diseño  │                     │
       │                   │                     │                     │
       │  6. Click Preview │                     │                     │
       │──────────────────►│  7. POST layout_json│                    │
       │                   │────────────────────►│                     │
       │                   │                     │  8. Genera QWeb XML │
       │                   │                     │  9. Guarda template │
       │                   │                     │     + action report │
       │                   │                     │                     │
       │                   │  10. Devuelve PDF   │  11. Renderiza PDF  │
       │                   │◄────────────────────│◄────────────────────│
       │  12. Preview PDF  │                     │                     │
       │◄──────────────────│                     │                     │
       │                   │                     │                     │
       │  13. Click Publish│                     │                     │
       │──────────────────►│  14. POST publish   │                     │
       │                   │────────────────────►│  15. ir.actions.report│
       │                   │                     │     created/updated │
       │                   │                     │                     │
       │                   │  16. OK + URL       │  17. Report avail.  │
       │                   │◄────────────────────│     in Print menu   │
       │  18. Success!     │                     │                     │
       │◄──────────────────│                     │                     │
```

---

## 📋 Estructura JSON del Diseño (Formato Intermedio)

Este es el **corazón** del sistema — el JSON que conecta el visual con la generación de
XML:

```json
{
  "id": "sale_order_custom_report",
  "name": "Orden de Venta - Mi Empresa",
  "targetModel": "sale.order",
  "paperFormat": {
    "format": "A4",
    "orientation": "portrait",
    "margins": {"top": 40, "bottom": 20, "left": 15, "right": 15}
  },
  "zones": {
    "body": [
      {
        "id": "el_001",
        "type": "text",
        "content": "ORDEN DE VENTA",
        "x": 200,
        "y": 30,
        "style": {"fontSize": 24, "fontWeight": "bold", "textAlign": "center"}
      },
      {
        "id": "el_002",
        "type": "field",
        "fieldBinding": {"model": "sale.order", "fieldPath": "name", "format": "char"},
        "x": 50,
        "y": 80,
        "label": "Número:",
        "style": {"fontSize": 12}
      },
      {
        "id": "el_003",
        "type": "field",
        "fieldBinding": {"model": "sale.order", "fieldPath": "partner_id.name"},
        "x": 50,
        "y": 110,
        "label": "Cliente:",
        "style": {"fontSize": 12}
      },
      {
        "id": "el_004",
        "type": "field",
        "fieldBinding": {
          "model": "sale.order",
          "fieldPath": "date_order",
          "format": "date"
        },
        "x": 400,
        "y": 80,
        "label": "Fecha:",
        "style": {"fontSize": 12}
      },
      {
        "id": "el_005",
        "type": "table",
        "dataSource": "order_line",
        "x": 50,
        "y": 160,
        "width": 700,
        "columns": [
          {"header": "Producto", "fieldPath": "product_id.name", "width": 250},
          {
            "header": "Cantidad",
            "fieldPath": "product_uom_qty",
            "width": 100,
            "alignment": "center"
          },
          {
            "header": "Precio",
            "fieldPath": "price_unit",
            "width": 120,
            "alignment": "right",
            "format": "monetary"
          },
          {
            "header": "Total",
            "fieldPath": "price_subtotal",
            "width": 120,
            "alignment": "right",
            "format": "monetary"
          }
        ],
        "style": {"headerBg": "#333", "headerColor": "#fff", "borderColor": "#ddd"}
      },
      {
        "id": "el_006",
        "type": "field",
        "fieldBinding": {
          "model": "sale.order",
          "fieldPath": "amount_total",
          "format": "monetary"
        },
        "x": 500,
        "y": 450,
        "label": "Total:",
        "style": {"fontSize": 16, "fontWeight": "bold"}
      }
    ]
  }
}
```

---

## 🔌 API del Backend Odoo

```python
# controllers/main.py
from odoo import http
from odoo.http import request
import json


class ReportDesignerController(http.Controller):

    @http.route('/api/report-designer/models', type='json', auth='user')
    def get_models(self, **kwargs):
        """Devuelve lista de modelos disponibles para reports."""
        models = request.env['ir.model'].search([
            ('transient', '=', False),
            ('name', '!=', False),
        ])
        return [{
            'id': m.id,
            'model': m.model,
            'name': m.name,
        } for m in models]

    @http.route('/api/report-designer/fields/<model_name>', type='json', auth='user')
    def get_fields(self, model_name, **kwargs):
        """Devuelve los campos de un modelo con su estructura."""
        try:
            model = request.env[model_name]
        except KeyError:
            return {'error': f'Model {model_name} not found'}

        fields = model.fields_get()
        result = []

        for fname, fdata in fields.items():
            result.append({
                'name': fname,
                'string': fdata.get('string', fname),
                'type': fdata.get('type'),
                'required': fdata.get('required', False),
                'relation': fdata.get('relation'),
                'selection': fdata.get('selection'),
                'help': fdata.get('help'),
            })

        return result

    @http.route('/api/report-designer/preview', type='json', auth='user')
    def preview_report(self, layout_json, record_id=None, **kwargs):
        """Genera preview del report como PDF."""
        # 1. Generar QWeb XML desde el JSON
        generator = request.env['report.designer.generator']
        qweb_data = generator.generate_from_json(layout_json)

        # 2. Crear/actualizar template temporal
        template_id = f"report_designer_preview_{layout_json['id']}"
        # ... crear vista QWeb temporal

        # 3. Renderizar el report
        report_model = layout_json['targetModel']

        if record_id:
            records = request.env[report_model].browse(record_id)
        else:
            records = request.env[report_model].search([], limit=1)

        # 4. Generar PDF
        pdf_content, _ = request.env['ir.actions.report']._render_qweb_pdf(
            template_id, records.ids
        )

        return {
            'pdf_base64': pdf_content.encode('base64').decode(),
            'record_count': len(records),
        }

    @http.route('/api/report-designer/publish', type='json', auth='user')
    def publish_report(self, layout_json, **kwargs):
        """Publica el report permanentemente en Odoo."""
        publisher = request.env['report.designer.publisher']
        result = publisher.publish_from_json(layout_json)

        return {
            'success': True,
            'report_xml_id': result['xml_id],
            'message': 'Report publicado correctamente. Aparecerá en el menú Imprimir.'
        }
```

---

## 📊 Resumen de Viabilidad

| Aspecto                         | Viabilidad  | Detalles                                       |
| ------------------------------- | ----------- | ---------------------------------------------- |
| **Introspección de modelos**    | ✅ Total    | Odoo expone `fields_get()` vía RPC             |
| **Canvas visual drag & drop**   | ✅ Total    | Fabric.js, Konva.js, o React DnD               |
| **Field picker con relaciones** | ✅ Total    | Árbol navegable con Many2one → campos          |
| **Generación QWeb XML**         | ✅ Total    | Traductor JSON → XML (ya existen patrones)     |
| **Preview en tiempo real**      | ✅ Total    | API que renderiza PDF vía Odoo                 |
| **Publicación en Odoo**         | ✅ Total    | ir.actions.report + ir.ui.view vía ORM         |
| **Tablas O2M arrastrables**     | ✅ Total    | Reconocer `one2many` → generar `<t t-foreach>` |
| **Condiciones visuales**        | ✅ Total    | Expresiones QWeb (t-if) en el editor           |
| **Herencia de reports**         | ⚠️ Complejo | Requiere manejo de `inherit_id` + xpath        |

**Conclusión:** Es un proyecto **completamente viable** técnicamente. De hecho, los
módulos que encontré en el Odoo App Store (Omni Designer, Report Studio, Qweb PDF
Builder) implementan exactamente esta arquitectura, aunque cada uno con sus propias
restricciones. Crear una versión open-source en React sería un proyecto muy interesante.

¿Te gustaría que profundice en algún componente específico, o que investigue las
licencias y RESTricciones de las soluciones existentes para poder reutilizar partes de
su código?

---

## User

Quiero que crees un plan de trabajo para empezar a trabajar en esta idea. Que la crees
por fases, diciéndome lo que vas a hacer en cada una de ellas y sugiéreme en cada una de
esas fases (porque serían con diferentes lenguajes de programación) que modelo de IA
elegimos y Si uso el modo Build o Odoo-Dev para proceder a crear la fase. Debes de
separarme las tareas por fases como te comenté y elegirme cuales son las primeras con
las que debes de trabajar. Por lo que estoy viendo, tendrás que ponerte en el rol de
desarrollador de Odoo en algunas de las fases y en otras como desarrollador en React.

---

## Assistant (Odoo-Dev · Big Pickle · 4.4s)

---

## User

Quiero que crees un plan de trabajo para empezar a trabajar en esta idea. Que la crees
por fases, diciéndome lo que vas a hacer en cada una de ellas y sugiéreme en cada una de
esas fases (porque serían con diferentes lenguajes de programación) que modelo de IA
elegimos y Si uso el modo Build o Odoo-Dev para proceder a crear la fase. Debes de
separarme las tareas por fases como te comenté y elegirme cuales son las primeras con
las que debes de trabajar. Por lo que estoy viendo, tendrás que ponerte en el rol de
desarrollador de Odoo en algunas de las fases y en otras como desarrollador en React.

---

## Assistant (Plan · Big Pickle · 114.7s)

_Thinking:_

El usuario me está pidiendo que cree un plan de trabajo detallado por fases para
desarrollar un generador de reportes visual estilo JasperReport para Odoo, usando React
como frontend y un módulo Odoo como backend.Necesito:

1. Estructurar el proyecto en fases claras
2. Para cada fase indicar qué se hace, qué tecnologías se usan
3. Sugerir qué modelo de IA usar para cada fase (Build mode vs Odoo-Dev mode)
4. Indicar qué rol tomo en cada fase (desarrollador Odoo o desarrollador React)
5. Marcar cuáles son las primeras fases en las que trabajar

Déjame pensar en las fases lógicas de este proyecto:

**Fase 0**: Setup del proyecto y arquitectura base **Fase 1**: Backend Odoo - API de
introspección de modelos **Fase 2**: Frontend React - Field Picker (panel lateral con
campos) **Fase 3**: Frontend React - Canvas visual drag & drop **Fase 4**: Backend
Odoo - Generador QWeb XML desde JSON **Fase 5**: Integración Frontend-Backend - Preview
de reports **Fase 6**: Backend Odoo - Publicador de reports (ir.actions.report) **Fase
7**: Frontend React - Editor de propiedades (panel derecho) **Fase 8**: Frontend React -
Manejo de tablas O2M **Fase 9**: Frontend React - Condiciones visuales y estilos

**Fase 10**: Testing y refinamiento

Ahora debo considerar qué capacidades de IA están disponibles para cada fase. El modo
Build es ideal para generar código React rápido y componentes visuales, mientras que el
modo Odoo-Dev es mejor para lógica backend y configuración de módulos Odoo. Necesito
asignar estas herramientas estratégicamente a cada fase del proyecto.

Antes de presentar el plan al usuario, debo investigar más sobre cómo están
estructurados estos proyectos y qué configuraciones son necesarias para cada fase.

**Tool: task**

**Input:**

```json
{
  "description": "Explore Odoo project structure",
  "prompt": "Explore the Odoo project structure at /home/socger/trabajo/galvintec/odoo/tutorial to understand:\n1. What modules exist in odoo/custom/src/private/\n2. How existing modules are structured (look at one example)\n3. Check if there's any existing React/JavaScript setup in the project\n4. Look at tasks.py to understand available invoke commands\n5. Check the manifest of one of the private modules to understand versioning and structure\n\nReturn a summary of findings including:\n- List of existing private modules\n- Typical module structure (files, directories)\n- Any JavaScript/React tooling already in place\n- Available invoke commands for development",
  "subagent_type": "explore"
}
```

**Output:**

```
<task id="ses_07a5635b7ffelPhKpojaige2Z5" state="completed">
<task_result>
Here is a comprehensive summary of the findings:

---

## 1. Existing Private Modules

There are **3 private modules** in `/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/private/`:

| Module | Name | Version | Depends on | License | Has tests |
|--------|------|---------|------------|---------|-----------|
| `socger_hospital` | Hospital management system | `18.0.0.1.0` | `base`, `mail`, `product`, `account` | LGPL-3 | Yes (2 test files) |
| `glv_basic_module` | Basic module | `18.0.0.1.0` | `base` | LGPL-3 | No |
| `socger_expand_fleet` | Socger Expand Fleet | `18.0.0.9.0` | `fleet` | LGPL-3 | Yes (7 test files) |

---

## 2. Typical Module Structure

Using `socger_hospital` as the canonical example, the standard layout is:

```

socger_hospital/ **init**.py # Top-level Python imports (from . import models)
**manifest**.py # Module manifest (version 18.0.x.y.z) models/ **init**.py # Imports all
model files patient.py patient_tag.py appointment.py account_move.py views/
patient_views.xml patient_readonly_views.xml appointment_views.xml
appointment_line_views.xml patient_tag_views.xml account_move_views.xml menu.xml #
Always loaded LAST (references actions from other view files) security/ security.xml #
Record rules / group definitions (wrapped in <odoo><data noupdate="0">)
ir.model.access.csv # Access control list data/ sequence.xml # Data records (sequences,
etc.) tests/ **init**.py test_patient.py test_appointment.py static/ description/
index.html # Auto-generated by pre-commit hook icon.png readme/ DESCRIPTION.md #
Fragments used to auto-generate README.rst USAGE.md README.rst # Auto-generated -- DO
NOT edit manually

```

**Manifest conventions:**
- Version format: `18.0.x.y.z` (major.minor.patch.major.minor)
- `license`: `LGPL-3`
- `application`: `True` for standalone apps, `False` for extensions
- `data` load order: `security` -> `ir.model.access.csv` -> `data` -> `views` -> `menu.xml` (last)

---

## 3. JavaScript/React Tooling

**There is no React or custom JS build tooling in this project.** Specifically:

- **No `package.json`** exists anywhere in the repository.
- **`npm.txt`** (at `odoo/custom/dependencies/npm.txt`) is **empty** -- no npm dependencies are installed.
- **No React, webpack, babel, or similar frontend build tools** are present.

**What does exist for frontend work** is standard **Odoo 18 OWL (Odoo Web Library)** JavaScript, found only in `socger_expand_fleet`:

| File | Purpose |
|------|---------|
| `static/src/components/attachment_preview.esm.js` | OWL Component using `@odoo/owl` |
| `static/src/components/attachment_preview.xml` | OWL QWeb template |
| `static/src/components/attachment_preview.scss` | SCSS styling |
| `static/src/widgets/attachment_preview_field.esm.js` | Field widget registered via `@web/core/registry` |
| `static/src/widgets/attachment_preview_field.xml` | Widget template |

These are loaded through the `"assets"` key in `__manifest__.py` under `"web.assets_backend"`. This is the standard Odoo 18 pattern for frontend customization -- plain JS modules using the `/** @odoo-module **/` directive, OWL components, and Odoo's built-in asset bundling. There is no separate JS build pipeline.

---

## 4. Available Invoke Commands

All commands are run from the project root via `invoke <task>`. Here is the full list extracted from `tasks.py` (1408 lines):

| Command | Description | Key Options |
|---------|-------------|-------------|
| `invoke develop` | Set up basic dev environment (git init, symlinks, pre-commit install, workspace file) | -- |
| `invoke start` | Start Docker Compose environment (Odoo on `127.0.0.1:18069`) | `--detach` (default True), `--debugpy`, `--port-prefix` |
| `invoke stop` | Stop environment | `--purge` (remove containers, networks, images, volumes) |
| `invoke restart` | Restart odoo containers | `--quick` (default True, uses `-t0`) |
| `invoke install` | Install Odoo addon(s) | `-m <modules>`, `--cur-file`, `--core`, `--extra`, `--private`, `--enterprise` |
| `invoke uninstall` | Uninstall Odoo addon(s) | `-m <modules>`, `--cur-file` |
| `invoke test` | Run Odoo tests | `-m <modules>`, `--mode init/update`, `--debugpy`, `--tags`, `--skip`, `--cur-file`, `--db-filter` |
| `invoke lint` | Run `pre-commit run --all-files` | `--verbose` |
| `invoke resetdb` | Drop and recreate DB with specified modules | `-m <modules>`, `--dbname` (default `devel`), `--populate`, `--dependencies` |
| `invoke img_build` | Build Docker image | `--pull` (default True) |
| `invoke img_pull` | Pull Docker images | -- |
| `invoke git_aggregate` | Download Odoo & addons git code via git-aggregator | -- |
| `invoke logs` | View container logs | `--tail N`, `--no-follow`, `--container NAME` |
| `invoke snapshot` | Snapshot current DB + filestore | `--source-db`, `--destination-db` |
| `invoke restore_snapshot` | Restore DB snapshot | `--snapshot-name`, `--destination-db` |
| `invoke updatepot` | Update POT translation files | `-m <module>`, `--all`, `-r <repo>` |
| `invoke preparedb` | Populate DB with helpful config (v11+) | -- |
| `invoke scaffold` | Scaffold a new Odoo module via `odoo scaffold` | `module_name` (required), `--path` |
| `invoke after_update` | Post-copier-update actions | -- |
| `invoke write_code_workspace_file` | Generate `.code-workspace` file for VSCode | `--cw-path` |
| `invoke closed_prs` | Test closed PRs from repos.yaml | -- |

---

## 5. Development Tooling Summary

| Category | Tool | Notes |
|----------|------|-------|
| **Linting/Formatting** | `pre-commit` via `invoke lint` | Includes `ruff`, `ruff-format`, `prettier` (with XML plugin), `pylint_odoo`, `eslint`, OCA checks |
| **Python config** | `.ruff.toml` | Ruff linter/formatter config |
| **JS/CSS formatting** | Prettier 2.7.1 | Fixed version with `@prettier/plugin-xml@v2.2.0` |
| **Python deps** | `pip.txt` | `openupgradelib`, `unicodecsv`, `unidecode` |
| **NPM deps** | `npm.txt` | Empty |
| **Docker** | Doodba scaffolding | Odoo 18.0, Postgres 18, Traefik 2 |
| **Database** | `devel` | User `odoo`, password `odoopassword` |
</task_result>
</task>
```

**Tool: task**

**Input:**

```json
{
  "description": "Explore available AI modes",
  "prompt": "Search the current project for information about:\n1. Available AI modes or build modes (check .opencode/ directory, opencode.json, or similar config files)\n2. What \"Build mode\" vs \"Odoo-Dev mode\" means in this context\n3. Any agent configurations or model settings\n4. Check if there's a way to switch between different AI development modes\n\nLook in:\n- /home/socger/trabajo/galvintec/odoo/tutorial/.opencode/\n- /home/socger/trabajo/galvintec/odoo/tutorial/opencode.json\n- /home/socger/trabajo/galvintec/odoo/tutorial/.opencode.json\n- /home/socger/trabajo/galvintec/odoo/tutorial/.config/\n- Any JSON or YAML config files in the root\n\nReturn findings about available modes and how they work.",
  "subagent_type": "explore"
}
```

**Output:**

```
<task id="ses_07a562491ffe00QqMFe1vT45ly" state="completed">
<task_result>
Here are my findings, organized by each of your questions:

---

## 1. Available AI Modes / Build Modes

**This project does NOT have explicit "Build mode" vs "Odoo-Dev mode" as toggleable modes.** Instead, it has a single configured AI agent with skill-based context switching. The relevant configuration files are:

### `/home/socger/trabajo/galvintec/odoo/tutorial/opencode.json`
This is the main OpenCode configuration file. It defines:
- **`default_agent`: `"odoo-dev"`** -- The single default agent for the project.
- **`permission.edit`** -- Granular edit permissions:
  - `*` (any file): `allow` (auto-approve)
  - `odoo/custom/src/private/**`: `ask` (prompt user before editing)
  - `odoo/custom/src/oca/**`: `ask`
  - `odoo/custom/src/odoo/**`: `ask`

### `/home/socger/trabajo/galvintec/odoo/tutorial/.opencode/agent/odoo-dev.md`
This is the **only agent definition** in the project. It is a markdown-based agent configuration with YAML frontmatter:
- **`mode: primary`** -- This agent is the primary/default agent.
- **`description`**: "Agente primario para desarrollo Odoo 18 en este proyecto. Carga OBLIGATORIA del skill odoo-development-skill antes de cualquier edit en odoo/custom/src/**."
- **`permission`** block mirrors `opencode.json` (edit permissions).

There is **no separate "Build mode" agent**. The only defined agent is `odoo-dev`.

---

## 2. What "Build mode" vs "Odoo-Dev mode" Means

**There is no "Build mode" configuration anywhere in this project.** Based on my search:

- The `.opencode/` directory contains only one agent: `odoo-dev.md` (with `mode: primary`).
- The `opencode.json` sets `default_agent` to `"odoo-dev"`.
- The `AGENTS.md` file (loaded automatically as project instructions) defines the overall agent behavior but does not mention multiple modes.

What exists instead is a **skill-based system** rather than a mode-based system. The `odoo-dev` agent operates with two complementary skills:

| Skill | Location | Purpose |
|-------|----------|---------|
| `odoo-development-skill` | `.agents/skills/odoo-development-skill/` | Universal skill with strict OCA standards, 114 pattern files, version-specific guides for Odoo 14-19. This is the **canonical** skill. |
| `odoo-development` | `.agents/skills/odoo-development/` | A simpler, general guidance skill for Odoo development. Supplementary only. |

The `odoo-dev` agent has an **absolute rule** (defined in `.opencode/agent/odoo-dev.md`): before ANY edit to `odoo/custom/src/**`, it MUST:
1. Load the `odoo-development-skill` via the `skill` tool.
2. Detect the Odoo version from `__manifest__.py`.
3. Read the relevant pattern file from the skills library.
4. Only then proceed with the edit.

---

## 3. Agent Configurations and Model Settings

### Agent: `odoo-dev` (the only agent)
- **File**: `/home/socger/trabajo/galvintec/odoo/tutorial/.opencode/agent/odoo-dev.md`
- **Mode**: `primary`
- **Permissions**: Edit `*` auto-allowed; edit to `odoo/custom/src/**` paths requires user confirmation.

### Specialized Sub-Agents (loaded on-demand via skill reading)
The `odoo-development-skill` includes 4 specialized agent workflows under `/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/agents/`:

| Agent File | Name | Purpose |
|------------|------|---------|
| `odoo-code-reviewer.md` | `odoo-code-reviewer` | Comprehensive code review for quality, security, performance, and version compliance. Produces star-rated assessments across 5 categories. |
| `odoo-context-gatherer.md` | `odoo-context-gatherer` | Gathers ALL relevant patterns and version-specific context BEFORE code generation. MANDATORY for complex tasks. |
| `odoo-skill-finder.md` | `odoo-skill-finder` | Targeted pattern lookup. Returns file path + line range + max 50 lines of relevant code from the 114-pattern library. |
| `odoo-upgrade-analyzer.md` | `odoo-upgrade-analyzer` | Analyzes Odoo module upgrade compatibility between versions and generates migration plans with breaking change identification. |

### Skills Library (114 pattern files)
Located at `/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/skills/`, these include:
- Version-specific patterns: `odoo-model-patterns-{14..19}.md`, `odoo-module-generator-{14..19}.md`, `odoo-owl-components-{15..19}.md`, `odoo-security-guide-{14..19}.md`, `odoo-version-knowledge-{14..19}.md`
- Migration guides: `odoo-model-patterns-{14-15..18-19}.md`, etc.
- Domain patterns: `field-type-reference.md`, `xml-view-patterns.md`, `wizard-patterns.md`, `report-patterns.md`, `controller-api-patterns.md`, `cron-automation-patterns.md`, `mail-notification-patterns.md`, and many more.

### Model/Provider Settings
There are **no AI model/provider settings** (e.g., which LLM to use, temperature, etc.) in any configuration file. The `opencode.json` schema (`https://opencode.ai/config.json`) does not contain model selection. The `.opencode/package.json` only has the `@opencode-ai/plugin` dependency (v1.17.20).

---

## 4. Switching Between AI Development Modes

**There is no explicit mode-switching mechanism.** The project is designed to work with a single agent (`odoo-dev`) that loads different skills/patterns on-demand. The switching happens implicitly:

### How context is switched:
1. **Automatic skill loading**: The `odoo-dev` agent's instructions mandate loading `odoo-development-skill` before any Odoo edit.
2. **Version detection**: The agent reads `__manifest__.py` to determine the Odoo version (14-19), then loads version-specific pattern files.
3. **On-demand specialized agents**: When a task requires code review, upgrade analysis, complex context gathering, or pattern discovery, the agent reads the corresponding specialized agent file from `.agents/skills/odoo-development-skill/agents/`.
4. **Pattern file selection**: The `SKILL.md` file provides a lookup table mapping keywords/intents to specific skill files (e.g., "wizard, transient, dialog" maps to `skills/wizard-patterns.md`).

### What you could do to add modes:
If you wanted to add a "Build mode" (non-Odoo general development), you would:
- Create a new agent markdown file in `.opencode/agent/` (e.g., `build.md`) with `mode: build` or similar.
- Set `"default_agent": "build"` in `opencode.json` or switch via the OpenCode UI.
- Remove or relax the Odoo-specific skill-loading requirements for that agent.

### Summary of all config files found:

| File | Purpose |
|------|---------|
| `/home/socger/trabajo/galvintec/odoo/tutorial/opencode.json` | Main OpenCode config: default agent + permissions |
| `/home/socger/trabajo/galvintec/odoo/tutorial/.opencode/agent/odoo-dev.md` | Agent definition (the only one) |
| `/home/socger/trabajo/galvintec/odoo/tutorial/.opencode/package.json` | OpenCode plugin dependency |
| `/home/socger/trabajo/galvintec/odoo/tutorial/AGENTS.md` | Project-wide agent instructions (auto-loaded) |
| `/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/SKILL.md` | Canonical skill entry point |
| `/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development/SKILL.md` | Supplementary general skill |
| `/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/agents/*.md` | 4 specialized sub-agent workflows |
| `/home/socger/trabajo/galvintec/odoo/tutorial/.agents/skills/odoo-development-skill/skills/*.md` | 114 pattern files for Odoo development |

**Bottom line**: This project has a single AI agent (`odoo-dev`) configured in "primary" mode, with a rich skill library for Odoo 18 development. There is no "Build mode" vs "Odoo-Dev mode" toggle -- the entire AI setup is purpose-built for Odoo development with version-aware pattern loading.
</task_result>
</task>
```

---

## Assistant (Plan · Big Pickle · 97.6s)

_Thinking:_

Ahora tengo información completa sobre:

1. La estructura del proyecto Odoo (módulos privados existentes, sin tooling React)
2. Los modos de IA disponibles (solo existe el agente `odoo-dev`, no hay "Build mode"
   separado)

Ahora necesito crear un plan de trabajo detallado por fases. Dado que no existe un
"Build mode" separado, el usuario podría estar confundiendo con opciones que no están
disponibles, o quizás se refiere a simplemente cambiar de contexto entre desarrollo Odoo
y desarrollo React.

Voy a crear un plan que:

1. Sea claro y estructurado por fases
2. Indique en cada fase qué rol tomo (Odoo dev o React dev)
3. Indique qué configuración de IA usar (en este caso, será el agente `odoo-dev` para
   todo lo relacionado con Odoo, y para React será trabajo fuera del contexto de Odoo)
4. Sea realista sobre lo que se puede hacer

Dado que no hay un "Build mode" separado, voy a aclarar esto al usuario y proponer una
alternativa práctica: usar el agente `odoo-dev` para las fases de Odoo, y trabajar
directamente en modo "desarrollador general" para las fases de React (ya que no hay un
agente configurado para React).

El plan tendrá estas fases principales:

1. Fase 0: Setup y Arquitectura
2. Fase 1: Backend Odoo - API de Introspección
3. Fase 2: Frontend React - Field Picker
4. Fase 3: Frontend React - Canvas Visual
5. Fase 4: Backend Odoo - Generador QWeb

6. Fase 5: Integración y Preview
7. Fase 6: Backend Odoo - Publicador
8. Fase 7: Frontend React - Editor de Propiedades
9. Fase 8: Frontend React - Tablas O2M
10. Fase 9: Testing y Refinamiento

Perfecto, ya tengo toda la información del proyecto. Aquí va el plan de trabajo
completo:

---

## 📋 PLAN DE TRABAJO: Generador Visual de Reports para Odoo

### ⚠️ Aclaración sobre los Modos de IA

**No existe un "Build mode" separado en tu proyecto.** Solo tienes configurado el agente
`odoo-dev` como agente primario. Para este proyecto propongo:

| Contexto                                | Agente/Modo           | Uso                                         |
| --------------------------------------- | --------------------- | ------------------------------------------- |
| **Desarrollo Odoo** (Python, XML, QWeb) | `odoo-dev`            | Con skill `odoo-development-skill` cargado  |
| **Desarrollo React** (JS/TS, CSS, HTML) | Sin agente específico | Trabajo directo sin restricciones Odoo      |
| **Arquitectura/Configuración**          | `odoo-dev`            | Para decisiones de diseño que afectan ambos |

---

## 🏗️ FASE 0: Setup del Proyecto y Arquitectura Base

**🎯 Objetivo:** Preparar el entorno de desarrollo para ambos mundos (Odoo + React)

| Tarea                                                                         | Tecnología       | Rol        | Agente IA  |
| ----------------------------------------------------------------------------- | ---------------- | ---------- | ---------- |
| 0.1 Crear estructura de directorios para el módulo Odoo `report_designer`     | Python/Odoo      | Odoo Dev   | `odoo-dev` |
| 0.2 Definir arquitectura del proyecto (carpetas, dependencias)                | Arquitectura     | Arquitecto | `odoo-dev` |
| 0.3 Setup de React app (create-react-app o Vite) en `report_designer/static/` | React/TypeScript | React Dev  | Directo    |
| 0.4 Configurar package.json con dependencias (Fabric.js, react-dnd, etc.)     | NPM              | React Dev  | Directo    |
| 0.5 Crear manifest básico del módulo Odoo                                     | Python           | Odoo Dev   | `odoo-dev` |
| 0.6 Configurar proxy en Odoo para API calls al backend                        | Python           | Odoo Dev   | `odoo-dev` |

**📁 Estructura resultante:**

```
odoo/custom/src/private/report_designer/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── report_layout.py          # Modelo para guardar diseños
├── controllers/
│   ├── __init__.py
│   └── main.py                   # API REST para el frontend
├── views/
│   ├── report_layout_views.xml
│   └── menu.xml
├── security/
│   ├── security.xml
│   └── ir.model.access.csv
├── static/
│   ├── src/
│   │   ├── react-app/            # React app embebida
│   │   │   ├── package.json
│   │   │   ├── src/
│   │   │   │   ├── App.tsx
│   │   │   │   ├── components/
│   │   │   │   ├── services/
│   │   │   │   └── types/
│   │   │   └── ...
│   │   └── description/
│   │       └── index.html
│   └── ...
└── README.rst
```

**✅ Entregable:** Módulo Odoo instalable + React app buildeable

---

## 🔌 FASE 1: Backend Odoo - API de Introspección

**🎯 Objetivo:** Crear las APIs que exponen la estructura de modelos y campos de Odoo al
frontend React

| Tarea                                                                  | Tecnología        | Rol      | Agente IA  |
| ---------------------------------------------------------------------- | ----------------- | -------- | ---------- |
| 1.1 Crear modelo `report.layout` para guardar diseños JSON             | Python/Odoo       | Odoo Dev | `odoo-dev` |
| 1.2 API: `GET /api/report-designer/models` - Lista modelos disponibles | Python/Controller | Odoo Dev | `odoo-dev` |
| 1.3 API: `GET /api/report-designer/fields/<model>` - Campos del modelo | Python/Controller | Odoo Dev | `odoo-dev` |
| 1.4 API: `POST /api/report-designer/save` - Guardar diseño             | Python/Controller | Odoo Dev | `odoo-dev` |
| 1.5 API: `GET /api/report-designer/list` - Listar diseños guardados    | Python/Controller | Odoo Dev | `odoo-dev` |
| 1.6 Crear security XML y CSV de acceso                                 | XML/CSV           | Odoo Dev | `odoo-dev` |
| 1.7 Tests del backend                                                  | Python/Unittest   | Odoo Dev | `odoo-dev` |

**📋 Modelo de datos:**

```python
class ReportLayout(models.Model):
    _name = 'report.layout'
    _description = 'Report Designer Layout'

    name = fields.Char(string='Name', required=True)
    target_model = fields.Char(string='Target Model', required=True)
    layout_json = fields.Text(string='Layout JSON')
    paper_format = fields.Selection([
        ('a4', 'A4'), ('letter', 'Letter'), ('legal', 'Legal')
    ], default='a4')
    paper_orientation = fields.Selection([
        ('portrait', 'Portrait'), ('landscape', 'Landscape')
    ], default='portrait')
    state = fields.Selection([
        ('draft', 'Draft'), ('published', 'Published')
    ], default='draft')
    report_action_id = fields.Many2one('ir.actions.report', string='Report Action')
```

**✅ Entregable:** API REST funcional que devuelve modelos, campos y guarda diseños

---

## 🎨 FASE 2: Frontend React - Field Picker

**🎯 Objetivo:** Crear el panel lateral izquierdo que muestra los campos del modelo
seleccionado y permite arrastrarlos

| Tarea                                                        | Tecnología | Rol       | Agente IA |
| ------------------------------------------------------------ | ---------- | --------- | --------- |
| 2.1 Servicio de conexión a Odoo API (axios/fetch wrapper)    | TypeScript | React Dev | Directo   |
| 2.2 Componente `ModelSelector` - Dropdown para elegir modelo | React      | React Dev | Directo   |
| 2.3 Componente `FieldPicker` - Árbol de campos navegable     | React      | React Dev | Directo   |
| 2.4 Componente `FieldItem` - Campo individual arrastrable    | React/DnD  | React Dev | Directo   |
| 2.5 Manejo de relaciones Many2one (expandir → campos hijas)  | React      | React Dev | Directo   |
| 2.6 Indicadores visuales por tipo de campo (iconos)          | React/CSS  | React Dev | Directo   |
| 2.7 Estados de carga y manejo de errores                     | React      | React Dev | Directo   |

**📋 Estructura del Field Picker:**

```
┌────────────────────────────┐
│ 🔍 Search fields...        │
├────────────────────────────┤
│ 📦 sale.order              │
│   ├── 📝 name              │
│   ├── 👤 partner_id ──────┼──► res.partner
│   │   ├── 📝 name          │
│   │   ├── 📧 email         │
│   │   └── 📱 phone         │
│   ├── 📅 date_order        │
│   ├── 💰 amount_total      │
│   ├── 📋 order_line ──────┼──► sale.order.line
│   │   ├── 📝 name          │
│   │   ├── 🔢 product_uom_qty│
│   │   └── 💰 price_unit   │
│   └── 📊 state             │
└────────────────────────────┘
```

**✅ Entregable:** Panel lateral funcional con campos arrastrables

---

## 🖼️ FASE 3: Frontend React - Canvas Visual

**🎯 Objetivo:** Crear el editor visual principal donde se diseñan los reports con drag
& drop

| Tarea                                                 | Tecnología       | Rol       | Agente IA |
| ----------------------------------------------------- | ---------------- | --------- | --------- |
| 3.1 Configurar canvas con Fabric.js o Konva.js        | React/TypeScript | React Dev | Directo   |
| 3.2 Componente `ReportCanvas` - Canvas principal      | React            | React Dev | Directo   |
| 3.3 Componente `CanvasElement` - Wrapper de elementos | React            | React Dev | Directo   |
| 3.4 Drag & Drop desde Field Picker al canvas          | React/DnD        | React Dev | Directo   |
| 3.5 Mover elementos dentro del canvas                 | React/Fabric     | React Dev | Directo   |
| 3.6 Redimensionar elementos con handles               | React/Fabric     | React Dev | Directo   |
| 3.7 Snap to grid (alineación a cuadrícula)            | React            | React Dev | Directo   |
| 3.8 Componente `TextField` - Campo de texto dinámico  | React            | React Dev | Directo   |
| 3.9 Componente `StaticText` - Texto estático          | React            | React Dev | Directo   |
| 3.10 Componente `ImageElement` - Imágenes             | React            | React Dev | Directo   |
| 3.11 Componente `LineElement` - Líneas separadoras    | React            | React Dev | Directo   |
| 3.12 Zoom in/out del canvas                           | React            | React Dev | Directo   |
| 3.13 Undo/Redo de acciones                            | React            | React Dev | Directo   |

**📋 Elementos del canvas:**

```
┌─────────────────────────────────────────────────────────┐
│ 📄 Canvas (A4 simulado)                                 │
│  ┌─────────────────────────────────────────────────┐   │
│  │                                                 │   │
│  │   ┌─────────────────────┐                       │   │
│  │   │ ORDEN DE VENTA      │  ← StaticText        │   │
│  │   └─────────────────────┘                       │   │
│  │                                                 │   │
│  │   Cliente: [partner_id.name]  ← TextField      │   │
│  │   Fecha:   [date_order]       ← TextField      │   │
│  │                                                 │   │
│  │   ┌─────────────────────────────────────────┐   │   │
│  │   │ Producto │ Cantidad │ Precio │ Total    │   │   │
│  │   ├──────────┼──────────┼────────┼──────────┤   │   │
│  │   │ [name]   │ [qty]    │ [price]│ [total]  │   │   │
│  │   │ ...      │ ...      │ ...    │ ...      │   │   │
│  │   └─────────────────────────────────────────┘   │   │
│  │                                   ← TableElement│   │
│  │   Total: [amount_total]          ← TextField   │   │
│  │                                                 │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

**✅ Entregable:** Canvas visual funcional con elementos interactivos

---

## ⚙️ FASE 4: Backend Odoo - Generador QWeb XML

**🎯 Objetivo:** Crear el motor que traduce el JSON del diseño visual a QWeb XML válido
para Odoo

| Tarea                                                 | Tecnología        | Rol      | Agente IA  |
| ----------------------------------------------------- | ----------------- | -------- | ---------- |
| 4.1 Clase `QWebGenerator` - Generador base            | Python            | Odoo Dev | `odoo-dev` |
| 4.2 Generación de `ir.actions.report` desde JSON      | Python            | Odoo Dev | `odoo-dev` |
| 4.3 Generación de template QWeb desde JSON            | Python            | Odoo Dev | `odoo-dev` |
| 4.4 Manejo de campos simples (char, int, float, etc.) | Python            | Odoo Dev | `odoo-dev` |
| 4.5 Manejo de Many2one (relaciones)                   | Python            | Odoo Dev | `odoo-dev` |
| 4.6 Manejo de One2many (tablas con loop)              | Python            | Odoo Dev | `odoo-dev` |
| 4.7 Manejo de Many2many                               | Python            | Odoo Dev | `odoo-dev` |
| 4.8 Formateo de campos (monetary, date, duration)     | Python            | Odoo Dev | `odoo-dev` |
| 4.9 Manejo de Paper Format personalizado              | Python            | Odoo Dev | `odoo-dev` |
| 4.10 Validación del XML generado                      | Python            | Odoo Dev | `odoo-dev` |
| 4.11 API: `POST /api/report-designer/generate-xml`    | Python/Controller | Odoo Dev | `odoo-dev` |

**📋 Ejemplo de traducción JSON → QWeb:**

```json
// INPUT (JSON del diseñador)
{
  "type": "table",
  "dataSource": "order_line",
  "columns": [
    {"header": "Producto", "fieldPath": "product_id.name"},
    {"header": "Cantidad", "fieldPath": "product_uom_qty"}
  ]
}
```

```xml
<!-- OUTPUT (QWeb XML generado) -->
<table class="table table-sm">
  <thead>
    <tr>
      <th>Producto</th>
      <th>Cantidad</th>
    </tr>
  </thead>
  <tbody>
    <t t-foreach="o.order_line" t-as="line">
      <tr>
        <td><span t-field="line.product_id.name" /></td>
        <td><span t-field="line.product_uom_qty" /></td>
      </tr>
    </t>
  </tbody>
</table>
```

**✅ Entregable:** Generador QWeb funcional con cobertura de tipos de campo

---

## 🔗 FASE 5: Integración Frontend-Backend

**🎯 Objetivo:** Conectar React con Odoo para previsualización en tiempo real

| Tarea                                                             | Tecnología        | Rol       | Agente IA  |
| ----------------------------------------------------------------- | ----------------- | --------- | ---------- |
| 5.1 API: `POST /api/report-designer/preview` - Genera PDF preview | Python/Controller | Odoo Dev  | `odoo-dev` |
| 5.2 Componente `PreviewPanel` - Muestra PDF generado              | React             | React Dev | Directo    |
| 5.3 Botón "Preview" en la toolbar                                 | React             | React Dev | Directo    |
| 5.4 Selector de registro para preview                             | React             | React Dev | Directo    |
| 5.5 Auto-refresh del preview al cambiar diseño                    | React             | React Dev | Directo    |
| 5.6 Manejo de loading states                                      | React             | React Dev | Directo    |
| 5.7 Cache de previews                                             | React             | React Dev | Directo    |

**✅ Entregable:** Preview funcional que muestra el PDF real generado por Odoo

---

## 📤 FASE 6: Backend Odoo - Publicador de Reports

**🎯 Objetivo:** Publicar el report permanentemente en Odoo (aparece en menú Imprimir)

| Tarea                                              | Tecnología        | Rol      | Agente IA  |
| -------------------------------------------------- | ----------------- | -------- | ---------- |
| 6.1 API: `POST /api/report-designer/publish`       | Python/Controller | Odoo Dev | `odoo-dev` |
| 6.2 Crear/actualizar `ir.actions.report`           | Python            | Odoo Dev | `odoo-dev` |
| 6.3 Crear/actualizar template QWeb en `ir.ui.view` | Python            | Odoo Dev | `odoo-dev` |
| 6.4 Asignar Paper Format al report                 | Python            | Odoo Dev | `odoo-dev` |
| 6.5 Bind del report al modelo (`binding_model_id`) | Python            | Odoo Dev | `odoo-dev` |
| 6.6 Despublicar reports (eliminar action)          | Python            | Odoo Dev | `odoo-dev` |
| 6.7 Historial de versiones de reports              | Python            | Odoo Dev | `odoo-dev` |

**✅ Entregable:** Reports publicables que aparecen en el menú Imprimir de Odoo

---

## 🎛️ FASE 7: Frontend React - Editor de Propiedades

**🎯 Objetivo:** Panel derecho para editar propiedades del elemento seleccionado

| Tarea                                                     | Tecnología | Rol       | Agente IA |
| --------------------------------------------------------- | ---------- | --------- | --------- |
| 7.1 Componente `PropertiesPanel` - Panel lateral derecho  | React      | React Dev | Directo   |
| 7.2 Propiedades de posición (x, y, width, height)         | React      | React Dev | Directo   |
| 7.3 Propiedades de tipografía (font, size, weight, color) | React      | React Dev | Directo   |
| 7.4 Propiedades de alineación (text-align)                | React      | React Dev | Directo   |
| 7.5 Propiedades de fondo y bordes                         | React      | React Dev | Directo   |
| 7.6 Propiedades de padding/margin                         | React      | React Dev | Directo   |
| 7.7 Editor de condiciones de visibilidad (t-if)           | React      | React Dev | Directo   |
| 7.8 Binding de campo (qué campo mostrar)                  | React      | React Dev | Directo   |
| 7.9 Formato del campo (monetary, date, etc.)              | React      | React Dev | Directo   |
| 7.10 Previsualización de cambios en tiempo real           | React      | React Dev | Directo   |

**✅ Entregable:** Panel de propiedades completo y funcional

---

## 📊 FASE 8: Frontend React - Tablas O2M

**🎯 Objetivo:** Soporte completo para tablas de One2many/Many2many

| Tarea                                                  | Tecnología | Rol       | Agente IA |
| ------------------------------------------------------ | ---------- | --------- | --------- |
| 8.1 Componente `TableElement` - Tabla visual en canvas | React      | React Dev | Directo   |
| 8.2 Configuración de fuente de datos (O2M/M2M field)   | React      | React Dev | Directo   |
| 8.3 Editor de columnas (agregar, eliminar, reordenar)  | React      | React Dev | Directo   |
| 8.4 Selector de campos por columna                     | React      | React Dev | Directo   |
| 8.5 Estilo de cabecera (colores, fuente)               | React      | React Dev | Directo   |
| 8.6 Estilo de filas (zebra striping, bordes)           | React      | React Dev | Directo   |
| 8.7 Filas de totales (footer)                          | React      | React Dev | Directo   |
| 8.8 Preview de tabla con datos reales                  | React      | React Dev | Directo   |

**✅ Entregable:** Tablas funcionales con editor visual de columnas

---

## 🧪 FASE 9: Testing y Refinamiento

**🎯 Objetivo:** Asegurar calidad y pulir la experiencia de usuario

| Tarea                                               | Tecnología   | Rol       | Agente IA  |
| --------------------------------------------------- | ------------ | --------- | ---------- |
| 9.1 Tests unitarios del backend (pytest)            | Python       | Odoo Dev  | `odoo-dev` |
| 9.2 Tests de integración (API calls)                | Python       | Odoo Dev  | `odoo-dev` |
| 9.3 Tests del frontend (Jest/React Testing Library) | TypeScript   | React Dev | Directo    |
| 9.4 Tests E2E (Cypress/Playwright)                  | TypeScript   | React Dev | Directo    |
| 9.5 UI/UX polish (animaciones, feedback)            | React/CSS    | React Dev | Directo    |
| 9.6 Responsive design (tablets)                     | React/CSS    | React Dev | Directo    |
| 9.7 Keyboard shortcuts                              | React        | React Dev | Directo    |
| 9.8 Performance optimization                        | React/Python | Both      | Directo    |
| 9.9 Documentation (README, usage guide)             | Markdown     | Both      | Directo    |
| 9.10 `invoke lint` y fix de todos los warnings      | Python       | Odoo Dev  | `odoo-dev` |

**✅ Entregable:** Producto final testado y pulido

---

## 🚀 ORDEN DE EJECUCIÓN RECOMENDADO

```
FASE 0 ──► FASE 1 ──► FASE 2 ──► FASE 3
   │           │           │           │
   │           │           │           ▼
   │           │           │      FASE 4
   │           │           │           │
   │           │           │           ▼
   │           │           │      FASE 5 ◄── Primer MVP funcional
   │           │           │           │
   │           │           │           ▼
   │           │           │      FASE 6
   │           │           │           │
   │           │           │           ▼
   │           │           │      FASE 7 ──► FASE 8 ──► FASE 9
```

**📌 Para empezar HOY, las primeras fases serían:**

1. **FASE 0** (Setup) - ~2-3 horas
2. **FASE 1** (API Introspección) - ~4-6 horas
3. **FASE 2** (Field Picker) - ~4-6 horas
4. **FASE 3** (Canvas Visual) - ~8-12 horas

**Total estimado hasta MVP (Fase 5):** ~30-40 horas de desarrollo

---

¿Quieres que empiece con la **FASE 0** (Setup del proyecto)? O si prefieres, puedo
profundizar en alguna fase específica antes de comenzar.

---

## User

Empieza en el orden que tú veas más conveniente, hazlo por fases, pero dime antes que
fase vas a realizar y en que modo pongo al OpenCode. Es decir, si para esa fase lo pongo
en modo Build o en modo Odoo-Dev. Cuando termines una fase debes de preguntarme si
procedes con la siguiente fase y decirme en que modo debo de ponerme para esa fase.

---

## Assistant (Plan · Big Pickle · 134.7s)

_Thinking:_

El usuario me está pidiendo que cree un plan de trabajo para desarrollar un generador de
reportes visual estilo JasperReport para Odoo, usando React como frontend. Quiere que:

1. Divida el trabajo en fases
2. En cada fase le diga qué voy a hacer
3. Le sugiera qué modelo de IA usar (Build mode o Odoo-Dev mode)
4. Cuando termine una fase, le pregunte si procedo con la siguiente
5. Le diga en qué modo debe poner OpenCode

Sin embargo, estoy en modo READ-ONLY (Plan Mode), por lo que NO puedo hacer ediciones.
Solo puedo planificar, investigar y analizar.

El usuario parece querer que empiece a trabajar, pero primero necesito:

1. Aclarar que estoy en modo planificación (solo lectura)
2. Crear un plan detallado de las fases
3. Explicarle sobre los modos de IA disponiblesPrimero debo investigar:

- Qué modos de IA están disponibles en OpenCode
- Cómo funciona el modo Build vs Odoo-Dev
- La estructura actual del proyecto para saber dónde encajaría este nuevo módulo

Voy a usar herramientas de exploración para entender mejor el entorno y luego
presentarle un plan completo.

Entendido. Estoy en modo **Plan Mode** (solo lectura), por lo que solo puedo analizar,
investigar y planificar. Voy a crear un plan completo para este proyecto de generador
visual de reports.

Primero, déjame investigar el entorno actual y los modos de IA disponibles:

**Tool: task**

**Input:**

```json
{
  "subagent_type": "explore",
  "description": "Explore Odoo project structure",
  "prompt": "Explore the current Odoo project structure at /home/socger/trabajo/galvintec/odoo/tutorial to understand:\n\n1. What modules exist in odoo/custom/src/private/\n2. The structure of existing modules (especially any that use React or JavaScript)\n3. Check the __manifest__.py files to understand module conventions\n4. Look for any existing React/JavaScript setup in the project\n5. Check if there's a package.json or any frontend build system\n6. Look at the tasks.py file to understand available development commands\n\nBe thorough - I need to understand the project layout to plan where to place a new React-based report designer module."
}
```

**Output:**

```
<task id="ses_07a4f0506ffeYFvg0PfQo2wl3E" state="completed">
<task_result>
Here is a comprehensive analysis of the project structure for planning a new React-based report designer module.

---

## 1. Project Overview

This is a **Doodba (Docker-based Odoo) 18.0** scaffolded project running entirely in Docker Compose. The root is at `/home/socger/trabajo/galvintec/odoo/tutorial`. All custom development goes in `/odoo/custom/src/private/`.

---

## 2. Modules in `odoo/custom/src/private/`

There are **3 modules**:

### a) `socger_hospital` (the most complete module)
- **Path:** `/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/private/socger_hospital/`
- **Purpose:** Hospital management system (patients, appointments, tags, account move integration)
- **Version:** `18.0.0.1.0`
- **License:** LGPL-3
- **Depends:** `base`, `mail`, `product`, `account`
- **Structure:**
```

socger_hospital/ **init**.py (imports models) **manifest**.py models/ **init**.py
(patient, appointment, patient_tag, account_move) patient.py appointment.py
patient_tag.py account_move.py views/ patient_views.xml patient_readonly_views.xml
appointment_views.xml appointment_line_views.xml patient_tag_views.xml
account_move_views.xml menu.xml (loaded LAST in manifest data list) security/
security.xml (groups: Receptionists, Doctors; record rules) ir.model.access.csv data/
sequence.xml static/ description/ icon.png, icon.svg, icon_2.png, index.html tests/
**init**.py test_patient.py (TransactionCase, @tagged('post_install', '-at_install'))
test_appointment.py readme/ (for auto-generated README)

```
- **No frontend/JS assets** in this module.

### b) `socger_expand_fleet` (has JS/OWL frontend code)
- **Path:** `/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/private/socger_expand_fleet/`
- **Purpose:** Fleet vehicle expansion (types, features, cost/budget concepts, document previews)
- **Version:** `18.0.0.9.0`
- **License:** LGPL-3
- **Depends:** `fleet`
- **Structure:**
```

socger_expand_fleet/ **init**.py (imports models) **manifest**.py (has "assets" block!)
models/ (8 Python model files) views/ (8 XML view files + menu.xml) security/
ir.model.access.csv static/ description/ icon.png, index.html src/ components/
attachment_preview.esm.js (OWL Component) attachment_preview.xml (OWL QWeb template)
attachment_preview.scss (SCSS styles) widgets/ attachment_preview_field.esm.js (OWL
field widget) attachment_preview_field.xml tests/ (7 test files) readme/

````
- **This is the key reference** for how frontend code is organized in this project.

### c) `glv_basic_module` (empty/skeleton)
- **Path:** `/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/private/glv_basic_module/`
- **Purpose:** Basic module template (all data/views commented out in manifest)
- **Version:** `18.0.0.1.0`
- **License:** LGPL-3
- **Depends:** `base`
- Contains only `__init__.py` and `__manifest__.py` -- essentially an empty shell.

---

## 3. Module Conventions (from `__manifest__.py` analysis)

All modules follow this pattern:

```python
{
  "name": "...",
  "summary": "...",
  "version": "18.0.x.y.z",       # Always 18.0 prefix
  "category": "...",
  "website": "...",
  "author": "...",
  "license": "LGPL-3",
  "depends": [...],
  "data": [
      "security/security.xml",
      "security/ir.model.access.csv",
      "data/sequence.xml",          # if needed
      "views/xxx_views.xml",
      ...
      "views/menu.xml",            # ALWAYS LAST (references actions above)
  ],
  "assets": {                      # Only if module has frontend code
      "web.assets_backend": [
          "module_name/static/src/components/xxx.esm.js",
          "module_name/static/src/components/xxx.xml",
          "module_name/static/src/components/xxx.scss",
      ],
  },
  "installable": True,
  "application": True/False,
  "auto_install": False,
}
````

**Key conventions:**

- `menu.xml` is always the last entry in `data` (referencing actions defined above).
- Security XML wraps records in `<odoo><data noupdate="0">...</data></odoo>`.
- Access CSV naming: `access_<model>_<group>`.
- `__init__.py` at root level imports `from . import models`.
- Tests use `TransactionCase` with `@tagged('post_install', '-at_install')`.

---

## 4. Existing JavaScript/OWL Setup

**There is NO React in this project.** The only frontend code is **Odoo OWL (Odoo Web
Library)** -- the native Odoo 18 component framework. Found in `socger_expand_fleet`:

- **OWL Component:** `attachment_preview.esm.js` -- imports from `@odoo/owl`, uses
  `Component` class, `setup()`, `get` properties.
- **OWL QWeb templates:** `.xml` files with `<t t-name="module.TemplateName">` syntax.
- **Field Widget:** `attachment_preview_field.esm.js` -- uses
  `registry.category("fields").add(...)` to register.
- **SCSS:** Standard SCSS with Odoo Bootstrap variables (`$spacer`, `$border-color`,
  `$primary`, etc.).
- **Assets declaration** in `__manifest__.py` under `"web.assets_backend"` key.
- **File naming:** `*.esm.js` extension (Odoo ESM module format).

The `@odoo-module` pragma at the top of each JS file marks it as an Odoo ES module:

```js
/** @odoo-module **/
import {Component} from "@odoo/owl";
```

---

## 5. Frontend Build System / package.json

**There is NO frontend build system in this project.** Specifically:

- **No `package.json`** anywhere in the project root or addon directories (only
  `.opencode/package.json` for the OpenCode AI tool, unrelated).
- **No `webpack.config.*`** anywhere.
- **No `vite.config.*`** anywhere.
- **No `.jsx` or `.tsx` files** anywhere.
- **No React, Vue, or any other SPA framework** installed.
- `odoo/custom/dependencies/npm.txt` is **empty** -- no npm dependencies are injected
  into the Docker image.

Odoo 18's frontend works differently from a typical SPA: the JS files in `static/src/`
are **loaded directly by the Odoo web client** via the `assets` manifest declaration.
There is no separate build step. OWL components are served as ES modules by Odoo's asset
pipeline. SCSS is compiled by Odoo's built-in asset controller.

---

## 6. Available Development Commands (`tasks.py`)

The project uses **`invoke`** (Python task runner). All commands wrap `docker compose`:

| Command                       | Purpose                                                          |
| ----------------------------- | ---------------------------------------------------------------- |
| `invoke develop`              | One-time setup (git init, symlinks, pre-commit install)          |
| `invoke img_build`            | Build Docker image (rebuild after dependency/Dockerfile changes) |
| `invoke start`                | Start environment (detached); Odoo at `127.0.0.1:18069`          |
| `invoke stop [--purge]`       | Stop containers (optional: remove volumes/images)                |
| `invoke restart`              | Quick restart of odoo + proxy containers                         |
| `invoke install [-m MODULE]`  | Install an Odoo module (infers from CWD if no -m)                |
| `invoke test [-m MODULE]`     | Run tests (supports `--mode init/update`, `--debugpy`, `--tags`) |
| `invoke resetdb`              | Drop + recreate `devel` database                                 |
| `invoke lint`                 | Run `pre-commit run --all-files` (Python/JS/XML lint+format)     |
| `invoke logs`                 | View container logs                                              |
| `invoke scaffold MODULE_NAME` | Scaffold a new Odoo module skeleton                              |
| `invoke updatepot`            | Update POT translation files                                     |
| `invoke snapshot`             | Snapshot DB + filestore                                          |
| `invoke restore_snapshot`     | Restore a DB snapshot                                            |

**Lint stack** (pre-commit hooks):

- **Python:** ruff (lint+format), pylint_odoo (mandatory + optional rcfiles)
- **JS:** eslint (v8.49.0, with `.eslintrc.yml` config for Odoo globals like `owl`,
  `odoo`, etc.)
- **XML/JSON/SCSS:** prettier v2.7.1 with `@prettier/plugin-xml@v2.2.0`
- **OCA checks:** `oca-checks-odoo-module`, `oca-checks-po`
- **README:** auto-generated by `oca-gen-addon-readme`

**Node version:** pinned to `18.17.1` in `.pre-commit-config.yaml`.

---

## 7. Key Implications for a React-Based Report Designer Module

Based on this analysis, here are the critical architectural considerations:

### Where to place the module

- **Path:** `odoo/custom/src/private/socger_report_designer/` (or similar name).
- This is the only correct location for custom private modules.

### No existing React toolchain

- **React is not present** anywhere in the project. There is no `package.json`, no
  webpack, no vite, no npm dependencies.
- You will need to **add a build system** for React (likely webpack or vite) and
  integrate it with Odoo's asset pipeline.
- The `odoo/custom/dependencies/npm.txt` file exists and is empty -- npm dependencies
  installed here are baked into the Docker image at build time.

### Two viable approaches for React integration

**Approach A: Build React externally, bundle as static assets**

- Create a `package.json` inside the module (e.g.,
  `static/src/report_designer/package.json`).
- Use webpack/vite to build a standalone JS bundle.
- Place the built bundle in `static/src/dist/` or `static/lib/`.
- Reference the bundle in the `__manifest__.py` assets section.
- The React app communicates with Odoo via RPC (`@web/core/utils/rpc` or standard
  `fetch`).

**Approach B: Use React-OWL bridge**

- Use a library like `@nicollite/owl-to-react` or similar bridge to mount React
  components inside OWL.
- This allows deeper integration with Odoo's view system but adds complexity.

### Reference module for frontend patterns

- `socger_expand_fleet` is the **only** module with frontend code. Its structure
  (`static/src/components/`, `static/src/widgets/`) and manifest `assets` block is the
  pattern to follow for any Odoo-native frontend work.
- OWL components use `@odoo/owl` imports, `/** @odoo-module **/` pragma, `.esm.js`
  extension, and XML QWeb templates.

### Lint compliance

- Any new JS files must pass **eslint** (`.eslintrc.yml` -- browser env, ES2022, Odoo
  globals).
- Any new SCSS/XML must pass **prettier** with the XML plugin.
- Any new Python must pass **ruff** and **pylint_odoo**.
- Files must be `git add`-ed before `invoke lint` to actually be checked.

### Docker consideration

- The `odoo/custom` directory is mounted **read-only** in the container (`:ro,z` in
  `devel.yaml`).
- Hot-reload is enabled via `--dev=reload,qweb,werkzeug,xml`.
- If you need npm build tools **inside** the container, add them to
  `odoo/custom/dependencies/npm.txt` and run `invoke img_build`. </task_result> </task>

````

**Tool: task**

**Input:**
```json
{
  "subagent_type": "explore",
  "description": "Explore OpenCode AI modes",
  "prompt": "Search for information about OpenCode's AI modes, specifically:\n\n1. Look in /home/socger/trabajo/galvintec/odoo/tutorial/ for any opencode configuration files\n2. Search for files like .opencode.json, opencode.json, .agents/, .opencode/ or similar\n3. Check if there are any agent definitions or mode configurations\n4. Look for any documentation about \"Build mode\" vs \"Odoo-Dev mode\"\n5. Search in the current directory and parent directories for opencode configuration\n\nI need to understand what AI modes are available and how to switch between them for different types of development work (React frontend vs Odoo backend)."
}
````

**Output:**

````
<task id="ses_07a4ef26fffeEe88o9RLgAoPkW" state="completed">
<task_result>
Here is a comprehensive summary of the OpenCode AI configuration in this project:

---

## Files Found

### 1. Main OpenCode Configuration
**`/home/socger/trabajo/galvintec/odoo/tutorial/opencode.json`**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "odoo-dev",
  "permission": {
    "edit": {
      "*": "allow",
      "odoo/custom/src/private/**": "ask",
      "odoo/custom/src/oca/**": "ask",
      "odoo/custom/src/odoo/**": "ask"
    }
  }
}
````

This sets `odoo-dev` as the **default agent** and defines edit permissions: full access
everywhere, but asks for confirmation before modifying files under `odoo/custom/src/`.

---

### 2. Agent Definition

**`/home/socger/trabajo/galvintec/odoo/tutorial/.opencode/agent/odoo-dev.md`**

This is the only custom agent defined. Its YAML frontmatter specifies:

```yaml
description: Agente primario para desarrollo Odoo 18 en este proyecto...
mode: primary
permission:
  edit:
    "*": "allow"
    "odoo/custom/src/private/**": "ask"
    "odoo/custom/src/oca/**": "ask"
    "odoo/custom/src/odoo/**": "ask"
```

Key points:

- **`mode: primary`** -- This agent runs as the default/primary agent for the session.
- It mandates loading the `odoo-development-skill` before any edit under
  `odoo/custom/src/**`.
- It references `AGENTS.md` (loaded automatically) for all project conventions.

There are **no other agents** defined in `.opencode/agent/` -- only `odoo-dev.md`.

---

### 3. Skills (`.agents/skills/`)

Two skills are installed:

| Skill                    | Path                                             | Purpose                                                                                    |
| ------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `odoo-development-skill` | `.agents/skills/odoo-development-skill/SKILL.md` | Universal Odoo dev skill (OCA standards, versions 14-19, 123+ pattern files, 4 sub-agents) |
| `odoo-development`       | `.agents/skills/odoo-development/SKILL.md`       | Simpler/general Odoo dev guidance (older, less comprehensive)                              |

The `odoo-development-skill` includes **4 specialized sub-agents** (loaded on demand
from within the skill):

- `odoo-code-reviewer.md`
- `odoo-upgrade-analyzer.md`
- `odoo-context-gatherer.md`
- `odoo-skill-finder.md`

---

### 4. What is NOT present

- **No "Build mode" or "Odoo-Dev mode" toggle concept** exists in this project's
  configuration. The terms "Build mode" and "React frontend mode" do not appear anywhere
  in the project files.
- **No React frontend agent or mode** is defined. There is no agent configuration for
  React/frontend development.
- **No mode switching mechanism** exists. The project has a single agent (`odoo-dev`)
  set as `mode: primary`. There is no configuration for switching between different AI
  modes for different types of work.
- **No parent-directory `.opencode/` configurations** were found outside this project
  root.

---

### 5. How it actually works

OpenCode's architecture in this project is:

1. **`opencode.json`** at the project root is the main config file. It selects
   `odoo-dev` as the default agent.
2. **`.opencode/agent/odoo-dev.md`** defines the agent's behavior, permissions, and
   mandatory workflow (load skill, detect version, read pattern, then edit).
3. **`AGENTS.md`** at the project root is auto-loaded as persistent context (it defines
   the full stack, commands, conventions, and "things not to do").
4. **`.agents/skills/`** provides the pattern library the agent consults before
   generating code.

---

### Regarding switching between React frontend vs Odoo backend

This project does **not** have a built-in mode-switching mechanism. If you want the AI
to handle React frontend work differently from Odoo backend work, you would need to
either:

1. **Create additional agent files** in `.opencode/agent/` (e.g., `react-frontend.md`
   with `mode: primary` or a different designation) and update `opencode.json` to
   reference it or set it as default.
2. **Use natural language instructions** in your prompts to tell the agent to behave
   differently for frontend tasks (the `odoo-development-skill` already includes
   OWL/frontend patterns in its skill files like `odoo-owl-components-18.md`,
   `assets-bundling-patterns.md`, etc.).
3. **Add a second skill** under `.agents/skills/` focused on React/frontend development
   (this project currently has no such skill).

The OpenCode agent system supports multiple agent definition files in
`.opencode/agent/`, but only one (`odoo-dev`) exists here. </task_result> </task>

```

---

## Assistant (Plan · Big Pickle · 70.3s)

_Thinking:_

Ahora tengo toda la información necesaria para crear un plan de trabajo completo. Voy a resumir lo que he descubierto:

1. **Proyecto Odoo 18** con Doodba (Docker)
2. **3 módulos privados** existentes: `socger_hospital`, `socger_expand_fleet`, `glv_basic_module`
3. **No hay React** en el proyecto - solo OWL (Odoo Web Library)
4. **No hay Build mode** configurado - solo existe el agente `odoo-dev`
5. **Ubicación correcta**: `odoo/custom/src/private/`
6. **Herramientas de linting**: pre-commit con ruff, eslint, prettier

Dado que no existe un "Build mode" ni un agente de React configurado, voy a:
1. Proponer la creación de un agente de React si es necesario
2. Explicar que trabajaremos con el agente `odoo-dev` para todo lo que sea Odoo
3. Para React, simplemente trabajaremos sin un agente específico (o podemos crear uno)

Voy a crear un plan de trabajo detallado por fases.

Perfecto, ya tengo toda la información del entorno. Aquí va mi análisis y plan de trabajo:

---

## 📊 ANÁLISIS DEL ENTORNO ACTUAL

| Aspecto | Estado |
|---------|--------|
| **Proyecto** | Odoo 18 con Doodba (Docker) |
| **Módulos privados** | 3 existentes (`socger_hospital`, `socger_expand_fleet`, `glv_basic_module`) |
| **Frontend actual** | Solo OWL (nativo Odoo), **NO hay React** |
| **Build tools** | **No hay** webpack/vite/npm configurados |
| **Agente IA disponible** | Solo `odoo-dev` (no existe "Build mode") |
| **Ubicación módulos** | `odoo/custom/src/private/` |

### ⚠️ Aclaración importante sobre los modos de IA

**No existe un "Build mode" en tu proyecto.** Solo tienes configurado el agente `odoo-dev`. Para este proyecto propongo:

| Tipo de trabajo | Modo/Agente | Descripción |
|-----------------|-------------|-------------|
| **Desarrollo Odoo** (Python, XML, QWeb, modelos, vistas) | `odoo-dev` | Usa el skill `odoo-development-skill` con estándares OCA |
| **Desarrollo React** (Componentes UI, canvas, drag & drop) | Sin agente específico | Trabajo directo sin restricciones de Odoo |
| **Configuración/Arquitectura** | `odoo-dev` | Para decisiones que afectan ambos mundos |

---

## 🗂️ PLAN DE TRABAJO POR FASES

### **FASE 0: Configuración del Entorno y Arquitectura Base**
**⏱️ Duración estimada:** 2-3 horas
**👤 Modo de OpenCode:** `odoo-dev`
**🎯 Objetivo:** Preparar el entorno de desarrollo

| # | Tarea | Responsable |
|---|-------|-------------|
| 0.1 | Crear estructura del módulo `socger_report_designer` | Odoo-Dev |
| 0.2 | Configurar `__manifest__.py` con dependencias | Odoo-Dev |
| 0.3 | Crear modelos base (`report.layout`) | Odoo-Dev |
| 0.4 | Configurar sistema de seguridad (grupos, permisos) | Odoo-Dev |
| 0.5 | Preparar estructura de directorios para React en `static/` | Odoo-Dev |

**📁 Estructura resultante:**
```

odoo/custom/src/private/socger_report_designer/ ├── **init**.py ├── **manifest**.py ├──
models/ │ ├── **init**.py │ └── report_layout.py ├── security/ │ ├── security.xml │ └──
ir.model.access.csv ├── views/ │ ├── report_layout_views.xml │ └── menu.xml ├──
controllers/ │ ├── **init**.py │ └── main.py └── static/ └── src/ └── description/

```

**✅ Entregable:** Módulo Odoo instalable con modelos básicos

---

### **FASE 1: API Backend para Introspección de Modelos**
**⏱️ Duración estimada:** 3-4 horas
**👤 Modo de OpenCode:** `odoo-dev`
**🎯 Objetivo:** Crear APIs que expongan la estructura de modelos de Odoo

| # | Tarea | Responsable |
|---|-------|-------------|
| 1.1 | Crear controller REST para listar modelos | Odoo-Dev |
| 1.2 | Crear endpoint para obtener campos de un modelo | Odoo-Dev |
| 1.3 | Implementar lógica de introspección (`fields_get`) | Odoo-Dev |
| 1.4 | Crear endpoints para operaciones CRUD de layouts | Odoo-Dev |
| 1.5 | Documentar APIs (postman/swagger básico) | Odoo-Dev |

**🔌 APIs a crear:**
```

GET /api/report-designer/models → Lista modelos disponibles GET
/api/report-designer/fields/<model> → Campos del modelo POST
/api/report-designer/layouts → Crear layout GET /api/report-designer/layouts → Listar
layouts PUT /api/report-designer/layouts/<id> → Actualizar layout POST
/api/report-designer/layouts/<id>/publish → Publicar report

```

**✅ Entregable:** API REST funcional para introspección de modelos

---

### **FASE 2: Frontend React - Field Picker (Panel de Campos)**
**⏱️ Duración estimada:** 4-6 horas
**👤 Modo de OpenCode:** Sin agente específico (React directo)
**🎯 Objetivo:** Panel lateral que muestra campos del modelo y permite arrastrar

| # | Tarea | Responsable |
|---|-------|-------------|
| 2.1 | Configurar React app (Vite + TypeScript) | React Dev |
| 2.2 | Crear servicio de conexión a API Odoo | React Dev |
| 2.3 | Componente `ModelSelector` - Selector de modelo | React Dev |
| 2.4 | Componente `FieldPicker` - Árbol de campos | React Dev |
| 2.5 | Componente `FieldItem` - Campo arrastrable (DnD) | React Dev |
| 2.6 | Manejo de relaciones Many2one → campos anidados | React Dev |
| 2.7 | Iconos y indicadores por tipo de campo | React Dev |

**🎨 UI del Field Picker:**
```

┌────────────────────────────┐ │ 🔍 Buscar campos... │ ├────────────────────────────┤ │
📦 sale.order │ │ ├── 📝 name │ │ ├── 👤 partner_id ──────┼──► res.partner │ │ ├── 📝
name │ │ │ ├── 📧 email │ │ │ └── 📱 phone │ │ ├── 📅 date_order │ │ ├── 💰 amount_total
│ │ └── 📋 order_line ──────┼──► sale.order.line │ ├── 📝 name │ │ ├── 🔢 qty │ │ └── 💰
price_unit │ └────────────────────────────┘

```

**✅ Entregable:** Panel de campos funcional con drag & drop

---

### **FASE 3: Frontend React - Canvas Visual**
**⏱️ Duración estimada:** 8-12 horas
**👤 Modo de OpenCode:** Sin agente específico (React Dev)
**🎯 Objetivo:** Editor visual principal para diseñar reports

| # | Tarea | Responsable |
|---|-------|-------------|
| 3.1 | Configurar canvas con Fabric.js/Konva.js | React Dev |
| 3.2 | Componente `ReportCanvas` - Lienzo principal | React Dev |
| 3.3 | Drag & drop desde Field Picker al canvas | React Dev |
| 3.4 | Mover y redimensionar elementos | React Dev |
| 3.5 | Snap to grid (alineación) | React Dev |
| 3.6 | Componente `TextField` - Campo dinámico | React Dev |
| 3.7 | Componente `StaticText` - Texto estático | React Dev |
| 3.8 | Componente `ImageElement` - Imágenes | React Dev |
| 3.9 | Componente `LineElement` - Líneas | React Dev |
| 3.10 | Zoom in/out | React Dev |
| 3.11 | Undo/Redo | React Dev |

**🖼️ Estructura del Canvas:**
```

┌─────────────────────────────────────────────────────────┐ │ 📄 Canvas (A4 simulado) │
│ ┌─────────────────────────────────────────────────┐ │ │ │ │ │ │ │
┌─────────────────────┐ │ │ │ │ │ ORDEN DE VENTA │ ← StaticText │ │ │ │
└─────────────────────┘ │ │ │ │ │ │ │ │ Cliente: [partner_id.name] ← TextField │ │ │ │
Fecha: [date_order] ← TextField │ │ │ │ │ │ │ │
┌─────────────────────────────────────────┐ │ │ │ │ │ Producto │ Cantidad │ Precio │
Total │ │ │ │ │ ├──────────┼──────────┼────────┼──────────┤ │ │ │ │ │ [name] │ [qty] │
[price]│ [total] │ │ │ │ │ └─────────────────────────────────────────┘ │ │ │ │ ←
TableElement│ │ │ │ Total: [amount_total] ← TextField │ │ │
└─────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘

````

**✅ Entregable:** Canvas visual con elementos interactivos

---

### **FASE 4: Backend - Generador QWeb XML**
**⏱️ Duración estimada:** 6-8 horas
**👤 Modo de OpenCode:** `odoo-dev`
**🎯 Objetivo:** Motor que traduce JSON del diseñador a QWeb XML

| # | Tarea | Responsable |
|---|-------|-------------|
| 4.1 | Clase `QWebGenerator` - Generador base | Odoo-Dev |
| 4.2 | Generación de `ir.actions.report` | Odoo-Dev |
| 4.3 | Generación de template QWeb | Odoo-Dev |
| 4.4 | Manejo de campos simples | Odoo-Dev |
| 4.5 | Manejo de Many2one (relaciones) | Odoo-Dev |
| 4.6 | Manejo de One2many (tablas con loop) | Odoo-Dev |
| 4.7 | Formateo de campos (monetary, date) | Odoo-Dev |
| 4.8 | Validación del XML generado | Odoo-Dev |

**🔄 Ejemplo de traducción:**
```json
// INPUT (JSON del diseñador)
{
  "type": "table",
  "dataSource": "order_line",
  "columns": [
    {"header": "Producto", "fieldPath": "product_id.name"},
    {"header": "Cantidad", "fieldPath": "product_uom_qty"}
  ]
}
````

```xml
<!-- OUTPUT (QWeb XML) -->
<table class="table table-sm">
  <thead>
    <tr>
      <th>Producto</th>
      <th>Cantidad</th>
    </tr>
  </thead>
  <tbody>
    <t t-foreach="o.order_line" t-as="line">
      <tr>
        <td><span t-field="line.product_id.name" /></td>
        <td><span t-field="line.product_uom_qty" /></td>
      </tr>
    </t>
  </tbody>
</table>
```

**✅ Entregable:** Generador QWeb funcional

---

### **FASE 5: Integración Frontend-Backend (Preview)**

**⏱️ Duración estimada:** 4-6 horas **👤 Modo de OpenCode:** Mixto (`odoo-dev` para
API + React Dev para UI) **🎯 Objetivo:** Preview en tiempo real del report

| #   | Tarea                             | Responsable |
| --- | --------------------------------- | ----------- |
| 5.1 | API de preview en backend         | Odoo-Dev    |
| 5.2 | Componente `PreviewPanel`         | React Dev   |
| 5.3 | Botón "Preview" en toolbar        | React Dev   |
| 5.4 | Selector de registro para preview | React Dev   |
| 5.5 | Auto-refresh al cambiar diseño    | React Dev   |
| 5.6 | Loading states                    | React Dev   |

**✅ Entregable:** Preview funcional con PDF real

---

### **FASE 6: Backend - Publicador de Reports**

**⏱️ Duración estimada:** 4-5 horas **👤 Modo de OpenCode:** `odoo-dev` **🎯 Objetivo:**
Publicar reports permanentemente en Odoo

| #   | Tarea                                | Responsable |
| --- | ------------------------------------ | ----------- |
| 6.1 | API de publicación                   | Odoo-Dev    |
| 6.2 | Crear/actualizar `ir.actions.report` | Odoo-Dev    |
| 6.3 | Crear/actualizar template QWeb       | Odoo-Dev    |
| 6.4 | Asignar Paper Format                 | Odoo-Dev    |
| 6.5 | Bind al modelo (`binding_model_id`)  | Odoo-Dev    |

**✅ Entregable:** Reports que aparecen en menú Imprimir

---

### **FASE 7: Frontend - Editor de Propiedades**

**⏱️ Duración estimada:** 6-8 horas **👤 Modo de OpenCode:** React Dev **🎯 Objetivo:**
Panel derecho para editar elementos

| #   | Tarea                                | Responsable |
| --- | ------------------------------------ | ----------- |
| 7.1 | Componente `PropertiesPanel`         | React Dev   |
| 7.2 | Propiedades de posición (x, y, w, h) | React Dev   |
| 7.3 | Propiedades de tipografía            | React Dev   |
| 7.4 | Propiedades de alineación            | React Dev   |
| 7.5 | Propiedades de fondo/bordes          | React Dev   |
| 7.6 | Editor de condiciones (t-if)         | React Dev   |
| 7.7 | Binding de campo                     | React Dev   |

**✅ Entregable:** Panel de propiedades completo

---

### **FASE 8: Frontend - Tablas O2M**

**⏱️ Duración estimada:** 6-8 horas **👤 Modo de OpenCode:** React Dev **🎯 Objetivo:**
Soporte completo para tablas One2many/Many2many

| #   | Tarea                            | Responsable |
| --- | -------------------------------- | ----------- |
| 8.1 | Componente `TableElement`        | React Dev   |
| 8.2 | Configuración de fuente de datos | React Dev   |
| 8.3 | Editor de columnas               | React Dev   |
| 8.4 | Selector de campos por columna   | React Dev   |
| 8.5 | Estilo de cabecera/filas         | React Dev   |
| 8.6 | Filas de totales                 | React Dev   |

**✅ Entregable:** Tablas funcionales con editor visual

---

### **FASE 9: Testing y Refinamiento**

**⏱️ Duración estimada:** 6-8 horas **👤 Modo de OpenCode:** Mixto **🎯 Objetivo:**
Asegurar calidad y pulir UX

| #   | Tarea                        | Responsable |
| --- | ---------------------------- | ----------- |
| 9.1 | Tests unitarios backend      | Odoo-Dev    |
| 9.2 | Tests de integración API     | Odoo-Dev    |
| 9.3 | Tests frontend (Jest)        | React Dev   |
| 9.4 | Tests E2E (Cypress)          | React Dev   |
| 9.5 | UI/UX polish                 | React Dev   |
| 9.6 | Keyboard shortcuts           | React Dev   |
| 9.7 | Performance optimization     | Mixto       |
| 9.8 | Documentation                | Mixto       |
| 9.9 | `invoke lint` - fix warnings | Odoo-Dev    |

**✅ Entregable:** Producto final testado y pulido

---

## 🚀 ORDEN DE EJECUCIÓN

```
FASE 0 ──► FASE 1 ──► FASE 2 ──► FASE 3
   │           │           │           │
   │           │           │           ▼
   │           │           │      FASE 4
   │           │           │           │
   │           │           │           ▼
   │           │           │      FASE 5 ◄── MVP FUNCIONAL
   │           │           │           │
   │           │           │           ▼
   │           │           │      FASE 6
   │           │           │           │
   │           │           │           ▼
   │           │           │      FASE 7 ──► FASE 8 ──► FASE 9
```

---

## 📋 RESUMEN DE MODOS POR FASE

| Fase       | Modo OpenCode       | Tipo Desarrollo    |
| ---------- | ------------------- | ------------------ |
| **FASE 0** | `odoo-dev`          | Odoo Backend       |
| **FASE 1** | `odoo-dev`          | Odoo Backend       |
| **FASE 2** | React Dev (directo) | React Frontend     |
| **FASE 3** | React Dev (directo) | React Frontend     |
| **FASE 4** | `odoo-dev`          | Odoo Backend       |
| **FASE 5** | Mixto               | Backend + Frontend |
| **FASE 6** | `odoo-dev`          | Odoo Backend       |
| **FASE 7** | React Dev (directo) | React Frontend     |
| **FASE 8** | React Dev (directo) | React Frontend     |
| **FASE 9** | Mixto               | Testing completo   |

---

## ⏱️ ESTIMACIÓN TOTAL

| Fase      | Horas Estimadas |
| --------- | --------------- |
| FASE 0    | 2-3 h           |
| FASE 1    | 3-4 h           |
| FASE 2    | 4-6 h           |
| FASE 3    | 8-12 h          |
| FASE 4    | 6-8 h           |
| FASE 5    | 4-6 h           |
| FASE 6    | 4-5 h           |
| FASE 7    | 6-8 h           |
| FASE 8    | 6-8 h           |
| FASE 9    | 6-8 h           |
| **TOTAL** | **49-68 horas** |

---

¿Te parece bien este plan? ¿Quieres que comience con la **FASE 0** (Configuración del
Entorno)? Si es así, déjame saber y procederé a crear la estructura base del módulo.

---

## User

Todo lo que vas a desarrollar lo vas a crear en un nuevo addon para Odoo?, En que path
lo vas a crear?, Que nombre le pondrás?

---

## Assistant (Plan · Big Pickle · 35.9s)

_Thinking:_

El usuario me está preguntando sobre los detalles del plan que he propuesto:

1. Si todo se creará en un nuevo addon para Odoo
2. En qué path se creará
3. Qué nombre se le pondrá

Estoy en modo READ-ONLY (Plan Mode), por lo que solo puedo responder con información y
planificación, sin hacer cambios.

Voy a responder a estas preguntas basándome en el análisis previo que hice del proyecto.

Exacto, voy a aclarar estos puntos importantes:

---

## 📁 Estructura del Addon

### Path donde se creará:

```
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/private/socger_report_designer/
```

### Nombre del addon:

**`socger_report_designer`**

(Siguiendo la convención de los módulos existentes: `socger_hospital`,
`socger_expand_fleet`)

---

## 🗂️ Estructura Completa del Addon

```
odoo/custom/src/private/socger_report_designer/
│
├── 📄 __init__.py                     # Importa models y controllers
├── 📄 __manifest__.py                 # Manifest Odoo 18
│
├── 📁 models/
│   ├── 📄 __init__.py
│   └── 📄 report_layout.py            # Modelo para guardar diseños
│
├── 📁 controllers/
│   ├── 📄 __init__.py
│   └── 📄 main.py                     # API REST para React
│
├── 📁 views/
│   ├── 📄 report_layout_views.xml     # Vistas del modelo
│   └── 📄 menu.xml                    # Menús
│
├── 📁 security/
│   ├── 📄 security.xml                # Grupos de seguridad
│   └── 📄 ir.model.access.csv         # Permisos
│
├── 📁 data/
│   └── 📄 paper_formats.xml           # Formatos de papel personalizados
│
├── 📁 static/
│   └── 📁 src/
│       ├── 📁 react-app/              # ← React app (build externo)
│       │   ├── 📄 package.json
│       │   ├── 📄 vite.config.ts
│       │   ├── 📁 src/
│       │   │   ├── 📄 App.tsx
│       │   │   ├── 📁 components/
│       │   │   │   ├── 📄 FieldPicker.tsx
│       │   │   │   ├── 📄 ReportCanvas.tsx
│       │   │   │   ├── 📄 PropertiesPanel.tsx
│       │   │   │   └── 📄 PreviewPanel.tsx
│       │   │   ├── 📁 services/
│       │   │   │   └── 📄 odooApi.ts
│       │   │   └── 📁 types/
│       │   │       └── 📄 index.ts
│       │   └── 📁 dist/               # Build output (generado)
│       │       └── 📄 bundle.js
│       │
│       └── 📁 description/
│           └── 📄 index.html          # Icono y descripción del módulo
│
├── 📁 tests/
│   ├── 📄 __init__.py
│   └── 📄 test_report_layout.py
│
└── 📄 README.rst                      # Auto-generado por pre-commit
```

---

## 🤔 Preguntas para ti antes de comenzar

### 1. **¿Qué nombre prefieres para el addon?**

Opciones:

- `socger_report_designer` (mi recomendación)
- `report_designer_visual`
- `glv_report_designer`
- Otro que prefieras

### 2. **¿Dónde almacenará Odoo los diseños JSON?**

Opciones:

- **Opción A:** En el campo `layout_json` del modelo (más simple)
- **Opción B:** Como archivos XML en `data/` (versionable con git)
- **Opción C:** Ambos (JSON editable + exportable a XML)

### 3. **¿El React app se buildea dentro del contenedor Docker o fuera?**

- **Dentro:** Más integrado, pero necesitas npm en el Dockerfile
- **Fuera:** Build local + copiar el `dist/` al `static/` (más flexible)

### 4. **¿Quieres que el report se pueda previsualizar en tiempo real (API de preview) o solo al publicar?**

- Preview en tiempo real = más complejo pero mejor UX
- Solo publicar = más rápido de desarrollar

### 5. **¿Qué nivel de personalización visual necesitas?**

- **Básico:** Solo campos de texto + tablas simples
- **Medio:** + imágenes, líneas, colores, fuentes
- **Avanzado:** + condiciones visuales, sub-templates, herencia

---

## 📊 Comparativa con Soluciones Existentes

| Característica                 | Tu addon | Omni Designer  | Report Studio |
| ------------------------------ | -------- | -------------- | ------------- |
| **Introspección de modelos**   | ✅ Sí    | ✅ Sí          | ✅ Sí         |
| **Canvas visual**              | ✅ Sí    | ✅ Sí          | ✅ Sí         |
| **Genera QWeb XML**            | ✅ Sí    | ❌ No (propio) | ✅ Sí         |
| **Compatible con Odoo nativo** | ✅ Sí    | ⚠️ Parcial     | ✅ Sí         |
| **Coste**                      | Gratis   | ~$200-500      | ~$100-300     |
| **Personalización total**      | ✅ Sí    | ❌ Limitada    | ⚠️ Media      |

---

¿Qué prefieres para estas decisiones de diseño? Una vez que me confirmes, podré ajustar
el plan y comenzar con la **FASE 0**.

---

## User

Me preguntaste lo siguiente:

1. ¿Qué nombre prefieres para el addon? Opciones:

- socger_report_designer (mi recomendación)
- report_designer_visual
- glv_report_designer
- Otro que prefieras CONTESTACION: socger_report_designer

2. ¿Dónde almacenará Odoo los diseños JSON? Opciones:

- Opción A: En el campo layout_json del modelo (más simple)
- Opción B: Como archivos XML en data/ (versionable con git)
- Opción C: Ambos (JSON editable + exportable a XML) CONTESTACION: Creo que la opción B,
  pero aconséjame lo que tú veas mejor.

3. ¿El React app se buildea dentro del contenedor Docker o fuera?

- Dentro: Más integrado, pero necesitas npm en el Dockerfile
- Fuera: Build local + copiar el dist/ al static/ (más flexible) CONTESTACION: Dentro y
  añade lo que necesites al Dockerfile, pero ten en cuenta de que no estorbe para nada a
  Odoo.

4. ¿Quieres que el report se pueda previsualizar en tiempo real (API de preview) o solo
   al publicar?

- Preview en tiempo real = más complejo pero mejor UX
- Solo publicar = más rápido de desarrollar CONTESTACION: Preview en tiempo real

5. ¿Qué nivel de personalización visual necesitas?

- Básico: Solo campos de texto + tablas simples
- Medio: + imágenes, líneas, colores, fuentes
- Avanzado: + condiciones visuales, sub-templates, herencia CONTESTACION: Avanzado

---

## Assistant (Plan · Big Pickle · 39.5s)

_Thinking:_

El usuario me ha respondido a las 5 preguntas que le hice. Ahora debo actualizar mi plan
con sus decisiones:

1. **Nombre del addon**: `socger_report_designer` ✅
2. **Almacenamiento**: Opción B (archivos XML en data/) - pero me pide que le aconseje.
   Voy a recomendarle la opción C (ambos) por las ventajas que ofrece.
3. **Build de React**: Dentro del contenedor Docker✅
4. **Preview**: En tiempo real ✅
5. **Nivel de personalización**: Avanzado ✅

Estoy en modo READ-ONLY (Plan Mode), por lo que solo puedo:

- Analizar
- Investigar
- Hacer preguntas
- Crear un plan

NO puedo hacer ediciones.

Voy a actualizar mi plan con estas decisiones y darle mi recomendación sobre el punto 2
(almacenamiento).

Perfecto, tengo todas tus respuestas. Voy a actualizar el plan con tus decisiones y
darte mi recomendación sobre el punto 2:

---

## ✅ Decisiones Confirmadas

| Decisión                   | Tu elección                  | Mi recomendación                |
| -------------------------- | ---------------------------- | ------------------------------- |
| **1. Nombre del addon**    | `socger_report_designer`     | ✅ Correcto                     |
| **2. Almacenamiento JSON** | Opción B (XML en data/)      | **Recomiendo Opción C (Ambos)** |
| **3. Build React**         | Dentro del contenedor Docker | ✅ Correcto                     |
| **4. Preview**             | Tiempo real                  | ✅ Correcto (mejor UX)          |
| **5. Personalización**     | Avanzado                     | ✅ Completo                     |

---

## 💡 Mi Recomendación sobre el Almacenamiento (Punto 2)

**Te recomiendo la Opción C (Ambos)**, y te explico por qué:

### Opción A: Solo `layout_json` en el modelo

```
Ventajas: Simple, rápido de implementar
Desventajas: No versionable con git, pierde cambios si se borra la BD
```

### Opción B: Solo archivos XML en `data/`

```
Ventajas: Versionable con git, integrado con Odoo
Desventajas: Edición menos fluida, requiere upgrade del módulo para cambios
```

### **Opción C: Ambos (JSON + XML) - MI RECOMENDACIÓN**

```
┌─────────────────────────────────────────────────────────┐
│                    FLUJO DE TRABAJO                      │
└─────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────┐
│ 1. DISEÑO VISUAL    │  El usuario diseña en React
│    (React Canvas)   │  Se guarda como JSON en memoria
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ 2. GUARDADO         │  JSON se guarda en BD (campo del modelo)
│    (Auto-save)      │  → Rápido, sin perder cambios
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ 3. PUBLICACIÓN      │  Se genera QWeb XML y se guarda en ir.ui.view
│    (Publish)        │  → Se carga en data/ del módulo
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ 4. EXPORTACIÓN      │  Opcional: exportar JSON para compartir/importar
│    (Import/Export)  │  → Permite sharing entre instancias
└─────────────────────┘
```

### ¿Por qué Opción C?

| Ventaja            | Descripción                                       |
| ------------------ | ------------------------------------------------- |
| **Rapidez**        | Auto-guardado en BD (sin recargar página)         |
| **Versionado**     | Al publicar, el XML se versiona con git           |
| **Portabilidad**   | Puedes exportar JSON e importar en otra instancia |
| **Rollback**       | Puedes volver a versiones anteriores del XML      |
| **Compatibilidad** | El XML generado funciona con Odoo nativo          |

---

## 📋 Plan Actualizado con tus Decisiones

### Estructura del Modelo de Datos

```python
class ReportLayout(models.Model):
    _name = 'report.layout'
    _description = 'Report Designer Layout'

    # Identificación
    name = fields.Char(string='Name', required=True)
    target_model = fields.Char(string='Target Model', required=True)

    # Diseño (JSON editable en React)
    layout_json = fields.Text(string='Layout JSON')

    # Publicación (XML generado)
    qweb_template_id = fields.Many2one('ir.ui.view', string='QWeb Template')
    report_action_id = fields.Many2one('ir.actions.report', string='Report Action')
    paper_format_id = fields.Many2one('report.paperformat', string='Paper Format')

    # Estado
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published')
    ], default='draft')

    # Metadatos
    version = fields.Integer(string='Version', default=1)
    last_publish_date = fields.Datetime(string='Last Published')
    create_uid = fields.Many2one('res.users', string='Created by')
```

---

## 🗂️ Estructura Actualizada del Addon

```
odoo/custom/src/private/socger_report_designer/
│
├── 📄 __init__.py
├── 📄 __manifest__.py                  # Depends: base, web
│
├── 📁 models/
│   ├── 📄 __init__.py
│   ├── 📄 report_layout.py             # Modelo principal
│   └── 📄 report_generator.py          # Motor de generación QWeb
│
├── 📁 controllers/
│   ├── 📄 __init__.py
│   └── 📄 main.py                      # API REST para React
│       ├── GET  /api/models            # Introspección
│       ├── GET  /api/fields/<model>
│       ├── POST /api/layouts           # CRUD layouts
│       ├── POST /api/preview           # Preview PDF
│       └── POST /api/publish           # Publicar report
│
├── 📁 views/
│   ├── 📄 report_layout_views.xml
│   └── 📄 menu.xml
│
├── 📁 security/
│   ├── 📄 security.xml                 # Grupo: Report Designers
│   └── 📄 ir.model.access.csv
│
├── 📁 data/
│   └── 📄 paper_formats.xml            # Formatos de papel default
│
├── 📁 static/
│   └── 📁 src/
│       ├── 📁 react-app/               # React app (Vite + TS)
│       │   ├── 📄 package.json
│       │   ├── 📄 vite.config.ts
│       │   ├── 📄 tsconfig.json
│       │   ├── 📁 src/
│       │   │   ├── 📄 App.tsx
│       │   │   ├── 📁 components/
│       │   │   │   ├── 📄 FieldPicker.tsx
│       │   │   │   ├── 📄 ReportCanvas.tsx
│       │   │   │   ├── 📄 PropertiesPanel.tsx
│       │   │   │   ├── 📄 PreviewPanel.tsx
│       │   │   │   └── 📄 Toolbar.tsx
│       │   │   ├── 📁 services/
│       │   │   │   └── 📄 odooApi.ts
│       │   │   ├── 📁 hooks/
│       │   │   │   ├── 📄 useCanvas.ts
│       │   │   │   └── 📄 useFieldPicker.ts
│       │   │   └── 📁 types/
│       │   │       └── 📄 index.ts
│       │   └── 📁 dist/                # Build output
│       │       ├── 📄 index.html
│       │       └── 📄 assets/
│       │
│       └── 📁 description/
│           └── 📄 index.html
│
├── 📁 tests/
│   ├── 📄 __init__.py
│   ├── 📄 test_report_layout.py
│   └── 📄 test_qweb_generator.py
│
└── 📄 README.rst
```

---

## 🔧 Dependencias del Dockerfile

Para el build de React dentro del contenedor, necesitaremos agregar a
`odoo/custom/dependencies/npm.txt`:

```
# Dependencias para el Report Designer React app
vite
@vitejs/plugin-react
typescript
react
react-dom
fabric
react-dnd
react-dnd-html5-backend
axios
```

Y potencialmente un script de build en `odoo/custom/build.d/` o
`odoo/custom/entrypoint.d/`.

---

## 📊 Plan Final por Fases (Actualizado)

| Fase  | Nombre                      | Modo OpenCode | Dependencias |
| ----- | --------------------------- | ------------- | ------------ |
| **0** | Setup Entorno + Modelo Base | `odoo-dev`    | Ninguna      |
| **1** | API Backend Introspección   | `odoo-dev`    | Fase 0       |
| **2** | React - Field Picker        | React Dev     | Fase 1       |
| **3** | React - Canvas Visual       | React Dev     | Fase 2       |
| **4** | Backend - Generador QWeb    | `odoo-dev`    | Fase 1       |
| **5** | Integración Preview         | Mixto         | Fase 3 + 4   |
| **6** | Backend - Publicador        | `odoo-dev`    | Fase 5       |
| **7** | React - Editor Propiedades  | React Dev     | Fase 5       |
| **8** | React - Tablas O2M          | React Dev     | Fase 7       |
| **9** | Testing + Refinamiento      | Mixto         | Todas        |

---

¿Te parece bien la **Opción C** para el almacenamiento? ¿O prefieres mantener la Opción
B?

Si estás de acuerdo con todo, cuando quieras puedo comenzar con la **FASE 0** (Setup del
Entorno y Modelo Base).

---

## User

Me parece bien la Opción C para el almacenamiento

---

## Assistant (Plan · Big Pickle · 31.1s)

_Thinking:_

El usuario ha aceptado la Opción C para el almacenamiento (ambos: JSON en BD + XML
publicado). Ahora estoy en modo Plan Mode (READ-ONLY), por lo que no puedo hacer
ediciones, solo planificar.

Debo confirmar que la decisión está tomada y preguntarle si quiere que comience con la
FASE 0, o si tiene alguna pregunta adicional antes de empezar.

Dado que estoy en modo plan, solo debo confirmar el plan final y preguntar si está listo
para comenzar la implementación (cuando salga del modo plan).

Perfecto, **Opción C confirmada** (JSON en BD + XML publicado).

---

## ✅ Plan Final Confirmado

| Decisión             | Valor                                             |
| -------------------- | ------------------------------------------------- |
| **Nombre del addon** | `socger_report_designer`                          |
| **Ubicación**        | `odoo/custom/src/private/socger_report_designer/` |
| **Almacenamiento**   | Opción C (JSON editable + XML versionado)         |
| **Build React**      | Dentro del contenedor Docker                      |
| **Preview**          | Tiempo real                                       |
| **Personalización**  | Avanzado (condiciones, herencia, sub-templates)   |

---

## 📋 Resumen del Proyecto

```
┌─────────────────────────────────────────────────────────────────┐
│            SOCGER REPORT DESIGNER - RESUMEN                     │
├─────────────────────────────────────────────────────────────────┤
│  Addon Odoo 18 con React embebido para diseño visual de reports │
├─────────────────────────────────────────────────────────────────┤
│  ✓ Introspección de modelos Odoo                                │
│  ✓ Canvas visual drag & drop (Fabric.js)                        │
│  ✓ Field Picker con relaciones Many2one/O2M/M2M                 │
│  ✓ Editor de propiedades (estilos, condiciones)                 │
│  ✓ Tablas dinámicas para One2many/Many2many                     │
│  ✓ Preview PDF en tiempo real                                   │
│  ✓ Generación automática QWeb XML                               │
│  ✓ Publicación en menú Imprimir de Odoo                         │
│  ✓ Almacenamiento dual (JSON + XML)                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Siguiente Paso

Cuando quieras comenzar la implementación, tendrás que **salir del modo Plan** para que
yo pueda:

1. Crear la estructura de archivos del addon
2. Escribir el código Python (modelos, controllers)
3. Configurar el build de React
4. Crear las vistas XML

**¿Estás listo para que comience con la FASE 0?**

Si es así, cuando salgas del modo plan, empezaré creando:

- El `__manifest__.py` del addon
- El modelo `report.layout`
- La estructura de directorios
- Las dependencias de npm

¿Alguna pregunta adicional antes de comenzar?

---
