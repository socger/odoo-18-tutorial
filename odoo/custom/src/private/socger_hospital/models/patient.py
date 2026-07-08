from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread"]
    _description = "Patient master"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of Birth", tracking=True)
    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female")],
        tracking=True,
    )

    # ----------------------------------------------------------------------------------------------
    # Puedo crear tag_ids de las dos maneras que aparecen abajo (la comentada y la no comentada)
    # La comentada es la forma tradicional de hacerlo, pero la no comentada es la forma más simple y
    # moderna de hacerlo.
    # ----------------------------------------------------------------------------------------------
    # Ambas formas son válidas y funcionan correctamente en Odoo.
    # ----------------------------------------------------------------------------------------------
    # Los campos de la comentada son:
    # - Nombre del modelo: "patient.tag"
    # - Nombre de la tabla relacional: "patient_tag_rel"
    # - Nombre del campo de la tabla relacional que hace referencia al modelo actual: "patient_id"
    # - Nombre del campo de la tabla relacional que hace referencia al modelo relacionado: "tag_id"
    # - Etiqueta del campo: "Tags"
    # ----------------------------------------------------------------------------------------------
    # tag_ids = fields.Many2many(
    #     "patient.tag", "patient_tag_rel", "patient_id", "tag_id", string="Tags"
    # )
    tag_ids = fields.Many2many(
        "patient.tag",
        string="Tags",
        tracking=True,
    )

    # ----------------------------------------------------------------------------------------------
    # Otra muestra de como crear un field Many2many, en este caso para relacionar productos con
    # pacientes.
    # ----------------------------------------------------------------------------------------------
    # product_ids = fields.Many2many(
    #     "product.product",
    #     string="Products",
    #     tracking=True,
    # )

    # Este método unlink se ejecuta cuando se intenta borrar un registro de paciente, para ejecutar código antes del delete.
    def unlink(self):
        for patient in self:
            domain = [("patient_id", "=", patient.id)]
            appintments = self.env["hospital.appointment"].search(domain)
            if appintments:
                # La diferencia entre usar UserError y ValidationError es que UserError se utiliza para mostrar un mensaje de error al usuario cuando se produce un error en la lógica de negocio, mientras que ValidationError se utiliza para mostrar un mensaje de error al usuario cuando se produce un error en la validación de datos. En este caso, como estamos validando si el paciente tiene citas asociadas antes de borrarlo, es más apropiado usar ValidationError.
                # raise UserError(
                raise ValidationError(
                    _(
                        "You cannot delete the patient '%s' \nbecause it has appointments associated."
                    )
                    % patient.name
                )
        return super().unlink()
