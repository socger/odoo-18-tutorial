from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"
    _rec_name = "name"
    _order = "sequence, id"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)

    # Este método check_patient_tags se puede utilizar para validar si un tag
    # tiene citas asociadas antes de realizar alguna acción, como por ejemplo,
    # cambiar el estado del paciente o realizar alguna operación que requiera
    # que el paciente no tenga citas asociadas. Si el paciente tiene citas
    # asociadas, se lanzará una excepción ValidationError con un mensaje
    # indicando que no se puede realizar la acción porque el paciente tiene
    # citas asociadas.
    # Es el mismo código que el método unlink, pero en este caso no se está
    # borrando el paciente, sino que se está validando si tiene citas
    # asociadas antes de realizar alguna acción.
    # Pero es necesario el uso del @api.ondelete(at_uninstall=False)
    @api.ondelete(at_uninstall=False)
    def _check_patient_tags(self) -> None:
        """Prevent deletion when the tag is still used by patients."""
        patients = self.env["hospital.patient"].search([("tag_ids", "in", self.ids)])
        if patients:
            tag_names = self.mapped("name")
            raise ValidationError(
                _(
                    "The tag(s): %(names)s ... has patients associated.",
                    names=", ".join(tag_names),
                )
            )
