from odoo import _, api, fields, models
from odoo.exceptions import UserError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread"]
    _description = "Hospital appointment"
    _rec_names_search = ["reference", "patient_id"]
    _rec_name = "reference"
    _order = "date_appointment desc, id"

    # reference = fields.Char(
    #     string="Reference", required=True, copy=False, readonly=True,
    #     index=True, default=lambda self: ("New"),
    # )
    reference = fields.Char(
        default="New",
        copy=False,
        readonly=True,
    )
    patient_id = fields.Many2one(
        "hospital.patient",
        string="Patient",
        # Con required=True, el campo patient_id es obligatorio y no se puede
        # dejar vacío. Si se intenta guardar un registro de cita sin
        # seleccionar un paciente, Odoo mostrará un mensaje de error
        # indicando que el campo es obligatorio.
        # required=True,
        #
        # con required=False, el campo patient_id no es obligatorio y se
        # puede dejar vacío. Si se intenta guardar un registro de cita sin
        # seleccionar un paciente, Odoo permitirá guardar el registro sin
        # mostrar ningún mensaje de error.
        # Pero ocurre más, si intentamos borrar un paciente que tiene citas
        # asociadas, Odoo mostrará un mensaje de aviso indicando que no se
        # debe de borrar el paciente porque tiene citas asociadas. Pero lo
        # permite a no ser que usemos ondelete="restrict", que es lo que se
        # hace en este caso.
        required=False,
        # Con ondelete="restrict", si se intenta borrar un paciente que tiene
        # citas asociadas, Odoo mostrará un mensaje de error indicando que no
        # se puede borrar el paciente porque tiene citas asociadas. Esto
        # evita que se borren pacientes que tienen citas asociadas y
        # garantiza la integridad de los datos.
        ondelete="restrict",
        # Con ondelete="cascade", si se borra un paciente, todas las citas
        # asociadas a ese paciente también se borrarán automáticamente. Esto
        # puede ser útil en algunos casos, pero hay que tener cuidado porque
        # se pueden perder datos importantes si se borra un paciente por
        # error.
        # ondelete="cascade",
        # Si se borra un paciente, el campo patient_id de las citas
        # asociadas a ese paciente se establecerá en null (vacío). Esto puede
        # ser útil en algunos casos, pero hay que tener cuidado porque se
        # pueden perder datos importantes si se borra un paciente por error.
        # ondelete="set null",
    )
    date_appointment = fields.Date(string="Date")
    note = fields.Text()
    additional_note = fields.Text(string="Additional note")
    state = fields.Selection(
        string="Status",
        selection=[
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("ongoing", "Ongoing"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        tracking=True,
    )
    appointment_line_ids = fields.One2many(
        "hospital.appointment.line",
        "appointment_id",
        string="Lines",
    )

    # total_qty es un campo calculado; si se marca store=True, el valor se
    # almacena en la base de datos y podrá usarse en filtros y búsquedas.
    # Al poner store=True, el campo total_qty no se recalculará si el método
    # _compute_total_qty no tiene el decorador @api.depends() adecuado.
    total_qty = fields.Float(
        compute="_compute_total_qty",
        string="Total quantity",
        store=True,
    )
    date_of_birth = fields.Date(
        related="patient_id.date_of_birth",
        # No es necesario poner string="Date of Birth" porque al ser un campo
        # relacionado, Odoo automáticamente toma el string del campo
        # relacionado.
        # string="Date of Birth",
        # date_of_birth es un campo relacionado; si se marca store=True, el
        # valor se almacena en la base de datos y podrá usarse en filtros y
        # búsquedas.
        # Al poner store=True no se necesita poner ningún tipo de decorador,
        # como es el caso de los campos calculados que queremos guardar su
        # valor en BD.
        store=True,
        # con el groups de abajo, el campo date_of_birth solo será visible
        # para los usuarios que pertenezcan al grupo
        # socger_hospital.group_hospital_doctors.
        # Los usuarios que no pertenezcan a ese grupo no podrán ver ni
        # acceder a ese campo en la vista de formulario, lista o kanban.
        groups="socger_hospital.group_hospital_doctors",
    )

    @api.model_create_multi
    def create(self, vals_list: list[dict]) -> "HospitalAppointment":
        """Override create to assign the appointment reference sequence."""
        for vals in vals_list:
            # if vals.get("reference", "New") == "New":
            #     vals["reference"] = self.env["ir.sequence"].next_by_code(
            #         "hospital.appointment"
            #     ) or "New"
            if not vals.get("reference") or vals["reference"] == "New":
                vals["reference"] = self.env["ir.sequence"].next_by_code(
                    "hospital.appointment.sequence"
                )
        return super().create(vals_list)

    @api.depends("appointment_line_ids", "appointment_line_ids.qty")
    def _compute_total_qty(self) -> None:
        """Compute the total quantity from the appointment lines."""
        for rec in self:
            # print(rec.appointment_line_ids.mapped("qty"))
            # for line in rec.appointment_line_ids:
            #     rec.total_qty += line.qty

            # rec.total_qty = sum(line.qty for line in rec.appointment_line_ids)
            rec.total_qty = sum(rec.appointment_line_ids.mapped("qty"))

    @api.depends("reference", "patient_id")
    def _compute_display_name(self) -> None:
        """Compute the display name from reference and patient."""
        for rec in self:
            rec.display_name = f"[{rec.reference}] - {rec.patient_id.name or ''}"

    def action_confirm(self) -> None:
        """Move appointments from draft to confirmed."""
        for rec in self:
            if rec.state != "draft":
                raise UserError(_("Only draft appointments can be confirmed."))
        self.write({"state": "confirmed"})

    def action_ongoing(self) -> None:
        """Move appointments from confirmed to ongoing."""
        for rec in self:
            if rec.state != "confirmed":
                raise UserError(_("Only confirmed appointments can be set as ongoing."))
        self.write({"state": "ongoing"})

    def action_done(self) -> None:
        """Move appointments from ongoing to done."""
        for rec in self:
            if rec.state != "ongoing":
                raise UserError(_("Only ongoing appointments can be completed."))
        self.write({"state": "done"})

    def action_cancelled(self) -> None:
        """Cancel appointments that are not yet done."""
        for rec in self:
            if rec.state == "done":
                raise UserError(_("Done appointments cannot be cancelled."))
        self.write({"state": "cancelled"})


class HospitalAppointmentLine(models.Model):
    _name = "hospital.appointment.line"
    _description = "Hospital appointment line"
    _order = "sequence, id"

    appointment_id = fields.Many2one(
        "hospital.appointment",
        string="Appointment",
        required=True,
        ondelete="cascade",
        index=True,
    )
    product_id = fields.Many2one(
        "product.product",
        string="Product",
        required=True,
    )
    qty = fields.Float(string="Quantity", default=1.0)
    sequence = fields.Integer(default=10)
