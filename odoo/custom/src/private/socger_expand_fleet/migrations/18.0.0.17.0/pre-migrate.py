"""Replace the core "Odómetros" translation of the odometer submenu.

The core ``fleet`` module ships an ``es_ES`` translation ("Odómetros") for
``fleet.fleet_vehicle_odometer_menu`` that would otherwise override the
relabel done in ``views/menu.xml``.
"""


def migrate(cr, version):
    cr.execute(
        """
        UPDATE ir_ui_menu m
        SET name = jsonb_set(
                jsonb_set(
                    m.name,
                    '{en_US}',
                    '"Km actuales por vehículo"',
                    false
                ),
                '{es_ES}',
                '"Km actuales por vehículo"',
                false
            )
        FROM ir_model_data imd
        WHERE imd.model = 'ir.ui.menu'
          AND imd.module = 'fleet'
          AND imd.name = 'fleet_vehicle_odometer_menu'
          AND imd.res_id = m.id
        """
    )
