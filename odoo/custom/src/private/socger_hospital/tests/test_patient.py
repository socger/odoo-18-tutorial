from psycopg2 import IntegrityError

from odoo.exceptions import ValidationError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestHospitalPatient(TransactionCase):
    """Unit tests for hospital.patient."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Patient = cls.env["hospital.patient"]
        cls.Tag = cls.env["patient.tag"]
        cls.tag = cls.Tag.create({"name": "Diabetes"})
        cls.patient = cls.Patient.create(
            {
                "name": "John Doe",
                "date_of_birth": "1990-05-15",
                "gender": "male",
                "tag_ids": [(4, cls.tag.id)],
            }
        )

    def test_create_patient(self):
        """Test basic patient creation."""
        self.assertTrue(self.patient.id)
        self.assertEqual(self.patient.name, "John Doe")
        self.assertEqual(self.patient.gender, "male")

    def test_compute_age(self):
        """Test age computation from date of birth."""
        self.assertGreaterEqual(self.patient.age, 0)
        patient_no_dob = self.Patient.create({"name": "No DOB"})
        self.assertEqual(patient_no_dob.age, 0)

    def test_name_required(self):
        """Test that name is required."""
        with self.assertRaises(IntegrityError):
            self.Patient.create({})

    def test_delete_patient_with_appointment(self):
        """Test that a patient with appointments cannot be deleted."""
        self.env["hospital.appointment"].create({"patient_id": self.patient.id})
        with self.assertRaises(ValidationError):
            self.patient.unlink()

    def test_delete_patient_without_appointment(self):
        """Test that a patient without appointments can be deleted."""
        patient = self.Patient.create({"name": "To Delete"})
        patient.unlink()
        self.assertFalse(patient.exists())

    def test_delete_tag_with_patients(self):
        """Test that a tag used by patients cannot be deleted."""
        with self.assertRaises(ValidationError):
            self.tag.unlink()
