from odoo.exceptions import UserError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestHospitalAppointment(TransactionCase):
    """Unit tests for hospital.appointment."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Patient = cls.env["hospital.patient"]
        cls.Appointment = cls.env["hospital.appointment"]
        cls.Line = cls.env["hospital.appointment.line"]
        cls.Product = cls.env["product.product"]
        cls.patient = cls.Patient.create({"name": "Jane Doe"})
        cls.product = cls.Product.create({"name": "Consultation"})

    def test_create_appointment_default_reference(self):
        """Test that a new appointment gets a sequence reference."""
        appointment = self.Appointment.create({"patient_id": self.patient.id})
        self.assertNotEqual(appointment.reference, "New")
        self.assertTrue(appointment.reference)

    def test_create_appointment_explicit_reference(self):
        """Test that an explicit reference is kept."""
        appointment = self.Appointment.create(
            {"reference": "CUSTOM", "patient_id": self.patient.id}
        )
        self.assertEqual(appointment.reference, "CUSTOM")

    def test_state_workflow(self):
        """Test the full state workflow draft -> confirmed -> ongoing -> done."""
        appointment = self.Appointment.create({"patient_id": self.patient.id})
        self.assertEqual(appointment.state, "draft")

        appointment.action_confirm()
        self.assertEqual(appointment.state, "confirmed")

        appointment.action_ongoing()
        self.assertEqual(appointment.state, "ongoing")

        appointment.action_done()
        self.assertEqual(appointment.state, "done")

    def test_cancel_from_draft(self):
        """Test cancelling a draft appointment."""
        appointment = self.Appointment.create({"patient_id": self.patient.id})
        appointment.action_cancelled()
        self.assertEqual(appointment.state, "cancelled")

    def test_cancel_done_raises(self):
        """Test that a done appointment cannot be cancelled."""
        appointment = self.Appointment.create({"patient_id": self.patient.id})
        appointment.action_confirm()
        appointment.action_ongoing()
        appointment.action_done()
        with self.assertRaises(UserError):
            appointment.action_cancelled()

    def test_confirm_non_draft_raises(self):
        """Test that only draft appointments can be confirmed."""
        appointment = self.Appointment.create({"patient_id": self.patient.id})
        appointment.action_confirm()
        with self.assertRaises(UserError):
            appointment.action_confirm()

    def test_compute_total_qty(self):
        """Test total quantity computation from lines."""
        appointment = self.Appointment.create({"patient_id": self.patient.id})
        self.Line.create(
            {
                "appointment_id": appointment.id,
                "product_id": self.product.id,
                "qty": 3.0,
            }
        )
        self.Line.create(
            {
                "appointment_id": appointment.id,
                "product_id": self.product.id,
                "qty": 2.0,
            }
        )
        self.assertEqual(appointment.total_qty, 5.0)

    def test_display_name(self):
        """Test display name is built from reference and patient."""
        appointment = self.Appointment.create({"patient_id": self.patient.id})
        self.assertIn(appointment.reference, appointment.display_name)
        self.assertIn(self.patient.name, appointment.display_name)

    def test_line_cascade_delete(self):
        """Test that lines are deleted when the appointment is deleted."""
        appointment = self.Appointment.create({"patient_id": self.patient.id})
        line = self.Line.create(
            {
                "appointment_id": appointment.id,
                "product_id": self.product.id,
                "qty": 1.0,
            }
        )
        line_id = line.id
        appointment.unlink()
        self.assertFalse(self.Line.browse(line_id).exists())
