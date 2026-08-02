from odoo.exceptions import UserError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestFleetGarage(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.ref("base.main_company")
        cls.partner = cls.env["res.partner"].create({"name": "Contacto Cochera"})

    def _create_garage(self, name="Cochera Norte", **kwargs):
        vals = {"name": name, "res_company_id": self.company.id}
        vals.update(kwargs)
        return self.env["fleet.garage"].create(vals)

    def test_create_garage(self):
        garage = self._create_garage(
            street="Calle Mayor 1",
            city="Madrid",
            zip="28001",
            phone="912345678",
            email="cochera@example.com",
            contact=self.partner.id,
        )
        self.assertEqual(garage.name, "Cochera Norte")
        self.assertEqual(garage.res_company_id, self.company)
        self.assertEqual(garage.street, "Calle Mayor 1")
        self.assertEqual(garage.city, "Madrid")
        self.assertEqual(garage.zip, "28001")
        self.assertEqual(garage.contact, self.partner)

    def test_unique_constraint_on_create(self):
        self._create_garage()
        with self.assertRaises(UserError):
            self._create_garage()

    def test_unique_constraint_allows_same_name_in_other_company(self):
        self._create_garage()
        other_company = self.env["res.company"].create({"name": "Other Garage Company"})
        garage = self._create_garage(
            name="Cochera Norte", res_company_id=other_company.id
        )
        self.assertEqual(garage.res_company_id, other_company)

    def test_unique_constraint_on_write(self):
        self._create_garage()
        other = self._create_garage(name="Cochera Sur")
        with self.assertRaises(UserError):
            other.name = "Cochera Norte"
