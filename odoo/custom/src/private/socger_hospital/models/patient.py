from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread"]
    _description = "Patient master"
    _rec_name = "name"

    name = fields.Char(required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of Birth", tracking=True)
    gender = fields.Selection(
        selection=[("male", "Male"), ("female", "Female")],
        tracking=True,
    )
    # age es un campo calculado; si se marca store=True, el valor se almacena en
    # la base de datos y podrá usarse en filtros y búsquedas.
    # Al poner store=True, el campo age no se recalculará si el método
    # _compute_age no tiene el decorador @api.depends() adecuado.
    age = fields.Float(
        compute="_compute_age",
        store=False,
    )

    # ----------------------------------------------------------------------
    # Puedo crear tag_ids de las dos maneras que aparecen abajo (la
    # comentada y la no comentada). La comentada es la forma tradicional de
    # hacerlo, pero la no comentada es la forma más simple y moderna.
    # ----------------------------------------------------------------------
    # Ambas formas son válidas y funcionan correctamente en Odoo.
    # ----------------------------------------------------------------------
    # Los campos de la comentada son:
    # - Nombre del modelo: "patient.tag"
    # - Nombre de la tabla relacional: "patient_tag_rel"
    # - Nombre del campo de la tabla relacional que hace referencia al
    #   modelo actual: "patient_id"
    # - Nombre del campo de la tabla relacional que hace referencia al
    #   modelo relacionado: "tag_id"
    # - Etiqueta del campo: "Tags"
    # ----------------------------------------------------------------------
    # tag_ids = fields.Many2many(
    #     "patient.tag", "patient_tag_rel", "patient_id", "tag_id", string="Tags"
    # )
    tag_ids = fields.Many2many(
        "patient.tag",
        string="Tags",
        tracking=True,
    )

    # ----------------------------------------------------------------------
    # Otra muestra de como crear un field Many2many, en este caso para
    # relacionar productos con pacientes.
    # ----------------------------------------------------------------------
    # product_ids = fields.Many2many(
    #     "product.product",
    #     string="Products",
    #     tracking=True,
    # )

    def _compute_age(self):
        for patient in self:
            if patient.date_of_birth:
                today = fields.Date.today()
                age = today.year - patient.date_of_birth.year
                if today.month < patient.date_of_birth.month or (
                    today.month == patient.date_of_birth.month
                    and today.day < patient.date_of_birth.day
                ):
                    age -= 1
                patient.age = age
            else:
                patient.age = 0

    # Este método unlink se ejecuta cuando se intenta borrar un registro de
    # paciente, para ejecutar código antes del delete.
    # def unlink(self):
    #     for patient in self:
    #         domain = [("patient_id", "=", patient.id)]
    #         appintments = self.env["hospital.appointment"].search(domain)
    #         if appintments:
    #             # La diferencia entre UserError y ValidationError es que
    #             # UserError se usa para mostrar un mensaje de error al
    #             # usuario cuando se produce un error en la lógica de
    #             # negocio, mientras que ValidationError se usa para mostrar
    #             # un mensaje de error al usuario cuando se produce un error
    #             # en la validación de datos. En este caso, como estamos
    #             # validando si el paciente tiene citas asociadas antes de
    #             # borrarlo, es más apropiado usar ValidationError.
    #             # raise UserError(
    #             raise ValidationError(
    #                 _(
    #                     "You cannot delete the patient '%s' \n"
    #                     "because it has appointments associated."
    #                 )
    #                 % patient.name
    #             )
    #     return super().unlink()

    # Este método check_patient_appointments se puede utilizar para validar
    # si un paciente tiene citas asociadas antes de realizar alguna acción,
    # como por ejemplo, cambiar el estado del paciente o realizar alguna
    # operación que requiera que el paciente no tenga citas asociadas.
    # Si el paciente tiene citas asociadas, se lanzará una excepción
    # ValidationError con un mensaje indicando que no se puede realizar la
    # acción porque el paciente tiene citas asociadas.
    # Es el mismo código que el método unlink, pero en este caso no se está
    # borrando el paciente, sino que se está validando si tiene citas
    # asociadas antes de realizar alguna acción.
    # Pero es necesario el uso del @api.ondelete(at_uninstall=False)
    @api.ondelete(at_uninstall=False)
    def check_patient_appointments(self):
        for patient in self:
            domain = [("patient_id", "=", patient.id)]
            appintments = self.env["hospital.appointment"].search(domain)
            if appintments:
                raise ValidationError(
                    _(
                        "The patient: '%s' ... has appointments associated.",
                        patient.name,
                    )
                )
