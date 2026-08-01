"""Rename the odometer submenu to "Flota - Km actuales por vehículo".

Follow-up of the ``18.0.0.17.0`` migration that set the label to
"Km actuales por vehículo"; the final label now includes the "Flota -"
prefix.
"""


def migrate(cr, version):
    cr.execute(
        """
        UPDATE ir_ui_menu m
        SET name = jsonb_set(
                jsonb_set(
                    m.name,
                    '{en_US}',
                    '"Flota - Km actuales por vehículo"',
                    false
                ),
                '{es_ES}',
                '"Flota - Km actuales por vehículo"',
                false
            )
        FROM ir_model_data imd
        WHERE imd.model = 'ir.ui.menu'
          AND imd.module = 'fleet'
          AND imd.name = 'fleet_vehicle_odometer_menu'
          AND imd.res_id = m.id
        """
    )
