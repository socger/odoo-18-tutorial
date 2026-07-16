# AGENTS.md

Guía para agentes de OpenCode que trabajan en este proyecto Odoo 18 scaffoldizado con
Doodba.

## Comportamiento del agente (preferencia persistente)

- **Tareas de desarrollo Odoo**: al recibir cualquier tarea de desarrollo Odoo (crear
  modelos, vistas, seguridad, wizards, reports, controladores, migraciones, etc.), el
  agente **debe cargar automáticamente el skill `odoo-development-skill`** y aplicar los
  estándares OCA estrictos que este define:
  1. **Detectar la versión** de Odoo leyendo `__manifest__.py` (primer número del
     `version`, p.ej. `18.0.x.y.z` → Odoo 18) antes de aplicar cualquier patrón.
  2. **No reinventar la rueda**: buscar primero en Odoo core
     (`odoo/custom/src/odoo/addons/`), luego en OCA (`odoo/custom/src/oca/` y GitHub
     upstream), antes de desarrollar desde cero. Heredar/extender si existe algo
     similar.
  3. **Usar el patrón correspondiente** del librerario en
     `.agents/skills/odoo-development-skill/skills/` (ver índice en el `SKILL.md` del
     skill). Para Odoo 18, priorizar las variantes `-18.md` y las guías de migración
     `*-17-18.md`. Leer el fichero de patrón con herramientas de lectura antes de
     generar código; no adivinar la sintaxis.
  4. **Comunicación con el usuario en español**; código, variables y docstrings en
     inglés (igual que el resto del repo).
  5. **Verificar** con `invoke lint` (= `pre-commit run --all-files`) antes de dar una
     tarea por terminada, y validar XML de datos con
     `xmllint --relaxng odoo/custom/src/odoo/odoo/import_xml.rng <file>` si la
     actualización falla con aserción "extra content" (ver sección "Pega conocida de
     XML" más abajo).
- Los **4 agentes especializados** del skill (`agents/odoo-code-reviewer.md`,
  `odoo-upgrade-analyzer.md`, `odoo-context-gatherer.md`, `odoo-skill-finder.md`) se
  cargan bajo demanda cuando la tarea lo requiera (code review, análisis de migración,
  contexto complejo, navegación de patrones).
- El skill `odoo-development` (guía general) puede cargarse adicionalmente para
  refrescar principios ORM/vistas, pero el **canónico es `odoo-development-skill`** por
  seguir estándares OCA estrictos y cubrir versiones 14–19.

## Stack y estructura

- **Doodba** scaffolding (plantilla copier v9.6.1) para **Odoo 18.0**, Postgres 18,
  proxy Traefik 2. Ver docs upstream: <https://github.com/Tecnativa/doodba>.
- Todo corre en Docker Compose. No se espera toolchain local de Python/Node; los
  comandos se ejecutan a través de `invoke` (ver `tasks.py`).
- La raíz del repo es la raíz del proyecto. `docker-compose.yml` es un symlink a
  `devel.yaml`; otros entornos: `test.yaml`, `prod.yaml`. Base de servicios compartida
  en `common.yaml`.
- Fuentes de addons (montadas read-only en el contenedor en `/opt/odoo/custom`):
  - `odoo/custom/src/odoo/` — núcleo de Odoo (git-aggregated; OCB es el target por
    defecto según `repos.yaml`).
  - `odoo/custom/src/oca/` — addons OCA agregados vía `addons.yaml` (actualmente
    `bank-payment`, `community-data-files`, `l10n-spain`, `web`, todos `*`).
  - `odoo/custom/src/private/` — **nuestros propios módulos**. Aquí es donde ocurre la
    mayor parte del trabajo. Módulos actuales: `socger_hospital`, `glv_basic_module`.
  - `odoo/auto/addons/` — addons agregados/auto-instalados en build-time (generados; no
    editar, no versionados a largo plazo).
- `odoo/custom/dependencies/` — dependencias de sistema inyectadas en el build de la
  imagen (`apt.txt`, `apt_build.txt`, `pip.txt`, `npm.txt`, `gem.txt`).
- `odoo/custom/{conf.d,build.d,entrypoint.d}/` — directorios de hooks de Doodba
  (actualmente vacíos).

## Comandos de desarrollo (ejecutar desde la raíz del repo)

Todas las tareas están definidas en `tasks.py` y se ejecutan vía `invoke <task>`
(`pip install invoke` si falta). Son wrappers sobre `docker compose`.

- `invoke develop` — preparar el entorno básico de dev (ejecutar una vez).
- `invoke img_build` — construir la imagen `odoo`. Rebuild tras cambiar
  `odoo/custom/dependencies/*`, `Dockerfile`, o `repos.yaml`/`addons.yaml`.
- `invoke start` — `docker compose up` (detached) de `devel.yaml`. Odoo en
  `127.0.0.1:18069`, longpolling `18072`, livechat `18899`, pgweb `18081`, smtp
  (mailhog) `18025`, wdb `18984`.
- `invoke stop [--purge]` — detener (y opcionalmente purgar contenedores/redes).
- `invoke restart` — reiniciar el/los contenedor(es) de odoo.
- `invoke logs [--tail N] [--no-follow] [--container NAME]` — ver el tail de logs.
- `invoke install [-w socger_hospital]` — instalar un módulo (o
  `--private`/`--core`/`--extra`/`--enterprise`). Sin args, infiere el addon desde el
  CWD.
- `invoke test [-w socger_hospital] [--init ...]` — ejecutar los tests de Odoo en la BD
  `devel`. Ver `tasks.py:1005` para el set completo de flags.
- `invoke resetdb` — dropear y recrear la BD `devel` con un conjunto de módulos.
- `invoke lint` — ejecutar `pre-commit run --all-files` (este es el paso canónico de
  lint/format).

### Re-agregar las fuentes de addons

Tras editar `repos.yaml` o `addons.yaml`:

```
export DOODBA_GITAGGREGATE_UID="$(id -u)" DOODBA_GITAGGREGATE_GID="$(id -g)" DOODBA_UMASK="$(umask)"
docker compose -f setup-devel.yaml run --rm odoo
```

Luego `invoke img_build`. `invoke git_aggregate` es el wrapper de invoke.

## Lint / format / typecheck

- **Lint = `invoke lint`** (= `pre-commit run --all-files`). Este es el único paso de
  verificación; no hay typecheck separado. Ejecútalo antes de dar una tarea por
  terminada.
- Hooks de pre-commit (`.pre-commit-config.yaml`): OCA `oca-checks-odoo-module` +
  `oca-checks-po`, `ruff --fix`, `ruff-format`, `prettier` con `@prettier/plugin-xml`
  (para que el XML se reformatee), `pylint_odoo` (rcfile obligatorio
  `.pylintrc-mandatory` + opcional `.pylintrc` con `--exit-zero`), `eslint`, además de
  hooks estándar de higiene.
- Node fijado a `18.17.1`, Python `python3`. Prettier está fijado a `2.7.1` con
  `plugin-xml@v2.2.0` (no subir de versión — HACK upstream anotado en
  `.pre-commit-config.yaml`).
- Config de Python: `.ruff.toml`. Configs de Pylint: `.pylintrc`, `.pylintrc-mandatory`.

## Convenciones de módulos privados

- Layout estándar de módulo Odoo: `__manifest__.py`, `__init__.py`, `models/`, `views/`,
  `security/` (`security.xml` + `ir.model.access.csv`), `data/`, `static/description/`.
- El `version` del manifest usa el esquema `18.0.x.y.z` (p.ej. `18.0.0.1.0`). Licencia
  `LGPL-3` para `socger_hospital`.
- Los ficheros `data` en los manifests se listan en orden de carga: `security` →
  `ir.model.access.csv` → `data` → `views` → `menu.xml` al final (los menús referencian
  acciones definidas en los ficheros de vistas). **Mantén `menu.xml` el último** — en
  caso contrario los refs `action=` fallan al instalar.
- El XML de seguridad envuelve los records en
  `<odoo><data noupdate="0">…</data></odoo>`.
- Nomenclatura de `ir.model.access.csv`: `access_<model>_<group>`, columnas
  `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
- Los README de los addons privados son **generados** por el hook de pre-commit
  `oca-gen-addon-readme` a partir de fragmentos `README.rst` (template
  `.module-readme.rst.j2`, org `Galvintec`, repo `tutorial`, branch `18.0`). No edites a
  mano los `README.md` / `static/description/index.html` generados.

## Pega conocida de XML en Odoo: errores RNG "extra content"

Al instalar/actualizar un módulo, Odoo valida cada fichero de datos XML contra
`odoo/custom/src/odoo/odoo/import_xml.rng`. Un fallo lanza:

```
AssertionError: Element odoo has extra content: <tag>, line N
```

**La línea `N` reportada y el elemento infractor NO son fiables.** El validador RelaxNG
de lxml reporta el _primer_ hijo de `<odoo>` que no pudo casar, no el que realmente
tiene el error. Causa real típica: un atributo que el RNG no permite en ese elemento
(typo, singular/plural equivocado).

Trampa conocida (ya corregida una vez en este repo): `<menuitem>` acepta `groups`
(plural) pero **no** `group`. El RNG `menuitem_attrs` solo permite: `id`, `name`,
`sequence` (xsd:int, sin espacios al final), `groups`, `active`; más contextualmente
`parent`, `action`, `web_icon`. Un `group="…"` suelto hacía que _cada_ `<menuitem>` del
fichero apareciera como "extra content" apuntando a la línea 7.

**Validación local rápida antes de re-actualizar en Odoo:**

```
xmllint --noout --relaxng odoo/custom/src/odoo/odoo/import_xml.rng <file.xml>
```

Esto localiza el atributo incorrecto exacto, a diferencia del traceback de Odoo.
Ejecútalo siempre que edites XML de datos y la actualización falle con una aserción
"extra content".

## Notas de Docker / env

- Nombre de la BD de dev: `devel` (usuario `odoo`, password `odoopassword`). Imagen
  Postgres `ghcr.io/tecnativa/postgres-autoconf:18-alpine`.
- El compose de dev monta `./odoo/custom` **read-only** en el contenedor; las ediciones
  de addons privados se recogen en vivo (`--dev=reload,qweb,werkzeug,xml` está definido
  en `devel.yaml`). `./odoo/auto` se monta read-write.
- `DOODBA_WITHOUT_DEMO=all` para saltar los datos demo; el default en `test.yaml` es
  `all`, en `devel.yaml` es `false`.
- Lang inicial `es_ES`. `odoo_dbfilter: ^prod` para prod.
- Env de prefijo de puerto: `PORT_PREFIX` (default `18`) controla el mapeo de puertos
  host `18xxx`.

## Sync script (resources/scripts/sync.sh)

Sincronización bidireccional local <-> remoto con `rsync` sobre SSH. Útil para
subir/bajar el proyecto (o parte de él) a un servidor de despliegue/staging sin depender
de git para ficheros no versionizados (config locales, assets, etc.).

### Setup inicial (una vez)

1. Copia la plantilla de configuración y rellena tus credenciales:
   ```
   cp resources/scripts/sync.conf.example resources/scripts/sync.conf
   ```
   Editar `resources/scripts/sync.conf`: `REMOTE_USER`, `REMOTE_HOST`, `REMOTE_PATH`
   (requeridas) y opcionalmente `REMOTE_PORT`, `SSH_IDENTITY`.
2. (Opcional) Crea excludes adicionales:
   ```
   cp .syncignore.example .syncignore
   ```
   `.syncignore` admite una regla `--exclude` de rsync por línea.

> `sync.conf` y `.syncignore` están en `.gitignore` — **no se commitean credenciales
> reales**. Las plantillas `.example` sí se versionan.

### Orden de prioridad de configuración

1. Variables de entorno ya exportadas (`REMOTE_USER=...` etc.) — **tienen prioridad**
   sobre el fichero.
2. `resources/scripts/sync.conf` (si existe).
3. Defaults internos (`REMOTE_PORT=22`, `SSH_IDENTITY=""`).

### Variables de configuración

| Variable       | Req. | Default | Descripción                                                      |
| -------------- | ---- | ------- | ---------------------------------------------------------------- |
| `REMOTE_USER`  | sí   | —       | Usuario SSH del servidor remoto.                                 |
| `REMOTE_HOST`  | sí   | —       | Host o IP del servidor remoto.                                   |
| `REMOTE_PATH`  | sí   | —       | Ruta absoluta del proyecto en el remoto.                         |
| `REMOTE_PORT`  | no   | `22`    | Puerto SSH.                                                      |
| `SSH_IDENTITY` | no   | `""`    | Fichero de clave privada (`-i`). Vacío = agente/`~/.ssh/config`. |

### Uso

```
./resources/scripts/sync.sh <push|pull> [opciones] [path...]
```

- `push` — local -> remoto
- `pull` — remoto -> local

### Opciones

| Opción          | Alias | Descripción                                                                 |
| --------------- | ----- | --------------------------------------------------------------------------- |
| `push` / `pull` | —     | Dirección de la sincronización (obligatoria, primera).                      |
| `--dry-run`     | `-n`  | Simula la transferencia (no escribe nada).                                  |
| `--delete`      | —     | Borra en destino lo que no existe en origen (mirror real). Opt-in.          |
| `--verbose`     | `-v`  | Salida detallada con `--progress`.                                          |
| `--help`        | `-h`  | Muestra la ayuda y sale.                                                    |
| `[path...]`     | —     | Paths relativos a la raíz del proyecto para acotar. Default: raíz completa. |

### Excludes

- **Por defecto** (siempre se aplican, push y pull): `.git/`, `.venv/`, `.vscode/`,
  `.zed/`.
- **Adicionales**: si existe `<raiz>/.syncignore` se pasa a rsync como `--exclude-from`.
  Una regla por línea, formato `--exclude` de rsync (patrones relativos a la raíz del
  proyecto).

### Semántica de paths

- Path local por defecto = raíz del proyecto (el script calcula `../../` desde
  `resources/scripts/`).
- Los directorios reciben **trailing slash** → rsync sincroniza el _contenido_ del dir,
  no el dir en sí.
- En `pull` con múltiples paths, el script itera internamente reconstruyendo el subpath
  relativo en el remoto (rsync no soporta múltiples destinos locales en una sola
  invocación).

### Flags rsync inyectados

Base: `-a --compress --human-readable`. Transporte:
`-e "ssh -p <REMOTE_PORT> -i <SSH_IDENTITY> -o StrictHostKeyChecking=accept-new -o ServerAliveInterval=60"`
(`-i` solo si `SSH_IDENTITY` no está vacío).

### Ejemplos

```
# Previsualizar un push de toda la raíz
./resources/scripts/sync.sh push --dry-run

# Subir solo nuestros módulos privados
./resources/scripts/sync.sh push odoo/custom/src/private/

# Bajar del remoto haciendo mirror (¡peligro! revisa --dry-run antes)
./resources/scripts/sync.sh pull --dry-run --delete
./resources/scripts/sync.sh pull --delete

# Salida detallada con progreso
./resources/scripts/sync.sh push -v odoo/custom/src/private/

# Override puntual vía env var (sin tocar sync.conf)
REMOTE_HOST=staging.example.com ./resources/scripts/sync.sh push -n

# Múltiples paths
./resources/scripts/sync.sh push odoo/custom/src/private/ tasks.py AGENTS.md
```

### Seguridad

- `--delete` es **opt-in**: por defecto el sync solo copia/actualiza, no borra. Haz
  **siempre** `--dry-run` antes de un `--delete`, especialmente en `pull`.
- El script usa `set -euo pipefail`: aborta ante errores.
- `StrictHostKeyChecking=accept-new` añade el host a `known_hosts` en la primera
  conexión (no bloquea el primer sync) pero rechaza cambios de clave de un host ya
  conocido.

### No sincronizar esto

Recuerda la sección "Cosas que no hacer" más abajo: no edites ni sincronices
`odoo/auto/`, `odoo/custom/src/odoo/` ni `odoo/custom/src/oca/` (generados /
git-aggregated). El `.syncignore.example` ya los excluye por defecto — mantén esas
reglas al crear tu `.syncignore`.

## Cosas que no hacer

- No edites ficheros bajo `odoo/auto/` — generados por el build.
- No edites `odoo/custom/src/odoo/` ni `odoo/custom/src/oca/` — agregados de repos git
  upstream; los cambios se perderán al re-agregar. Arregla upstream y re-agrega en su
  lugar.
- No subir a ciegas las versiones de Prettier/`plugin-xml` — están fijadas por una razón
  (ver comentarios HACK en `.pre-commit-config.yaml`).
- No edites a mano el `README.md` o `static/description/index.html` generados de un
  addon.
