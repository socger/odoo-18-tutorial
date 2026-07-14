Description
===========

Sistema de gestión hospitalaria. Añade el modelo ``hospital.patient``
con datos demográficos (fecha de nacimiento, género), cálculo automático
de la edad, etiquetas clasificatorias (``patient.tag``) y seguimiento
de cambios mediante ``mail.thread``.

Incluye además la gestión de citas (``hospital.appointment`` y sus
líneas) e integra los movimientos contables (``account.move``) para
asociar facturas a los pacientes.

Usage
=====

1. Vaya a *Hospital > Patients* y cree un paciente.
2. Rellene la fecha de nacimiento; el campo *Age* se calcula
   automáticamente.
3. Asigne etiquetas desde *Patient > Tags* para clasificar pacientes.
4. Cree citas desde *Hospital > Appointments* y añada líneas con los
   productos/servicios asociados.
