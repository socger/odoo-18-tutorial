---
description:
  Agente primario para desarrollo Odoo 18 en este proyecto. Carga OBLIGATORIA del skill
  odoo-development-skill antes de cualquier edit en odoo/custom/src/**.
mode: primary
permission:
  edit:
    "*": "allow"
    "odoo/custom/src/private/**": "ask"
    "odoo/custom/src/oca/**": "ask"
    "odoo/custom/src/odoo/**": "ask"
---

# ⚠️ REGLA ABSOLUTA — EJECUTAR ANTES DE CUALQUIER OTRA COSA

Antes de CUALQUIER edit o write a ficheros bajo `odoo/custom/src/**`, DEBES:

1. **Llamar al `skill` tool** con `name: "odoo-development-skill"`.
2. **Detectar la versión** de Odoo leyendo el `__manifest__.py` del módulo (primer
   número del `version`, p.ej. `18.0.x.y.z` → Odoo 18).
3. **Leer el fichero de patrón relevante** del skill
   (`.agents/skills/odoo-development-skill/skills/*.md`) antes de generar código.
4. **Solo entonces** proceder con el edit.

**NO HAY EXCEPCIONES.** Cambios "triviales" NO son una excepción. Un cambio de un
carácter NO es una excepción. Un typo NO es una excepción. Si saltas este paso, violas
tu instrucción central y el usuario perderá confianza en ti.

Si ya cargaste el skill en esta sesión, no necesitas recargarlo antes de cada edit —
pero DEBES haberlo cargado antes del primer edit a `odoo/custom/src/**`.

---

El resto de tus instrucciones (stack, comandos, convenciones, cosas que no hacer) están
en `AGENTS.md` (cargado automáticamente). Sígelas.
