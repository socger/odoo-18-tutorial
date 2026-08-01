# Copyright 2026 SocGer
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).


def post_init_hook(env):
    """Force the odometer submenu label in every installed language.

    The core ``fleet`` module ships an ``es_ES`` translation ("Odómetros")
    for ``fleet.fleet_vehicle_odometer_menu`` that would otherwise override
    the relabel done in ``views/menu.xml``.
    """
    menu = env.ref("fleet.fleet_vehicle_odometer_menu")
    menu.write({"name": "Flota - Km actuales por vehículo"})
    for lang in env["res.lang"].search([("active", "=", True)]):
        menu.with_context(lang=lang.code).write(
            {"name": "Flota - Km actuales por vehículo"}
        )
