# AGENTS.md

Guidance for OpenCode agents working in this Doodba-scaffolded Odoo 18 project.

## Stack & layout

- **Doodba** scaffolding (copier template v9.6.1) for **Odoo 18.0**, Postgres 18,
  Traefik 2 proxy. See upstream docs: <https://github.com/Tecnativa/doodba>.
- Everything runs in Docker Compose. No local Python/Node toolchain is expected;
  commands go through `invoke` (see `tasks.py`).
- Repo root is the project root. `docker-compose.yml` is a symlink to `devel.yaml`;
  other envs: `test.yaml`, `prod.yaml`. Shared service base in `common.yaml`.
- Addon sources (mounted read-only into the container at `/opt/odoo/custom`):
  - `odoo/custom/src/odoo/` — Odoo core (git-aggregated; OCB is the default target per
    `repos.yaml`).
  - `odoo/custom/src/oca/` — OCA addons aggregated via `addons.yaml` (currently
    `bank-payment`, `community-data-files`, `l10n-spain`, `web`, all `*`).
  - `odoo/custom/src/private/` — **our own modules**. This is where most work happens.
    Current modules: `socger_hospital`, `glv_basic_module`.
  - `odoo/auto/addons/` — build-time aggregated/auto-installed addons (generated; do not
    edit, not version-controlled long-term).
- `odoo/custom/dependencies/` — system deps injected at image build (`apt.txt`,
  `apt_build.txt`, `pip.txt`, `npm.txt`, `gem.txt`).
- `odoo/custom/{conf.d,build.d,entrypoint.d}/` — Doodba hook directories (currently
  empty).

## Dev commands (run from repo root)

All tasks are defined in `tasks.py` and run via `invoke <task>` (`pip install invoke` if
missing). They wrap `docker compose`.

- `invoke develop` — set up basic dev env (run once).
- `invoke img_build` — build the `odoo` image. Rebuild after changing
  `odoo/custom/dependencies/*`, `Dockerfile`, or `repos.yaml`/`addons.yaml`.
- `invoke start` — `docker compose up` (detached) of `devel.yaml`. Odoo on
  `127.0.0.1:18069`, longpolling `18072`, livechat `18899`, pgweb `18081`, smtp
  (mailhog) `18025`, wdb `18984`.
- `invoke stop [--purge]` — stop (and optionally purge containers/networks).
- `invoke restart` — restart odoo container(s).
- `invoke logs [--tail N] [--no-follow] [--container NAME]` — tail logs.
- `invoke install [-w socger_hospital]` — install a module (or
  `--private`/`--core`/`--extra`/`--enterprise`). With no args, infers the addon from
  CWD.
- `invoke test [-w socger_hospital] [--init ...]` — run Odoo tests in the `devel` DB.
  See `tasks.py:1005` for full flag set.
- `invoke resetdb` — drop & recreate the `devel` DB with a module set.
- `invoke lint` — run `pre-commit run --all-files` (this is the canonical lint/format
  step).

### Re-aggregating addon sources

After editing `repos.yaml` or `addons.yaml`:

```
export DOODBA_GITAGGREGATE_UID="$(id -u)" DOODBA_GITAGGREGATE_GID="$(id -g)" DOODBA_UMASK="$(umask)"
docker compose -f setup-devel.yaml run --rm odoo
```

Then `invoke img_build`. `invoke git_aggregate` is the invoke wrapper.

## Lint / format / typecheck

- **Lint = `invoke lint`** (= `pre-commit run --all-files`). This is the only
  verification step; there is no separate typecheck. Run it before declaring a task
  done.
- Pre-commit hooks (`.pre-commit-config.yaml`): OCA `oca-checks-odoo-module` +
  `oca-checks-po`, `ruff --fix`, `ruff-format`, `prettier` with `@prettier/plugin-xml`
  (so XML gets reformatted), `pylint_odoo` (mandatory rcfile `.pylintrc-mandatory` +
  optional `.pylintrc` with `--exit-zero`), `eslint`, plus standard hygiene hooks.
- Node pinned to `18.17.1`, Python `python3`. Prettier is pinned to `2.7.1` with
  `plugin-xml@v2.2.0` (do not bump — upstream HACK noted in `.pre-commit-config.yaml`).
- Python config: `.ruff.toml`. Pylint configs: `.pylintrc`, `.pylintrc-mandatory`.

## Private module conventions

- Standard Odoo module layout: `__manifest__.py`, `__init__.py`, `models/`, `views/`,
  `security/` (`security.xml` + `ir.model.access.csv`), `data/`, `static/description/`.
- Manifest `version` uses the `18.0.x.y.z` scheme (e.g. `18.0.0.1.0`). License `LGPL-3`
  for `socger_hospital`.
- `data` files in manifests are listed in load order: `security` → `ir.model.access.csv`
  → `data` → `views` → `menu.xml` last (menus reference actions defined in view files).
  **Keep `menu.xml` last** — otherwise `action=` refs fail at install.
- Security XML wraps records in `<odoo><data noupdate="0">…</data></odoo>`.
- `ir.model.access.csv` naming: `access_<model>_<group>`, columns
  `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
- READMEs for private addons are **generated** by the `oca-gen-addon-readme` pre-commit
  hook from `README.rst` fragments (template `.module-readme.rst.j2`, org `Galvintec`,
  repo `tutorial`, branch `18.0`). Do not hand-edit generated `README.md` /
  `static/description/index.html`.

## Odoo XML gotcha: RNG "extra content" errors

When installing/updating a module, Odoo validates every XML data file against
`odoo/custom/src/odoo/odoo/import_xml.rng`. A failure raises:

```
AssertionError: Element odoo has extra content: <tag>, line N
```

**The reported line `N` and the offending element are NOT reliable.** lxml's RelaxNG
validator reports the _first_ child of `<odoo>` it could not match, not the one that
actually has the error. Typical real cause: an attribute that is not allowed on that
element by the RNG (typo, wrong singular/plural).

Known trap (already fixed once in this repo): `<menuitem>` accepts `groups` (plural) but
**not** `group`. The RNG `menuitem_attrs` allows only: `id`, `name`, `sequence`
(xsd:int, no trailing spaces), `groups`, `active`; plus contextually `parent`, `action`,
`web_icon`. A stray `group="…"` made _every_ `<menuitem>` in the file show up as "extra
content" pointing at line 7.

**Fast local validation before re-updating in Odoo:**

```
xmllint --noout --relaxng odoo/custom/src/odoo/odoo/import_xml.rng <file.xml>
```

This pinpoints the exact bad attribute, unlike the Odoo traceback. Run it whenever you
edit data XML and the update fails with an "extra content" assertion.

## Docker / env notes

- Dev DB name: `devel` (user `odoo`, password `odoopassword`). Postgres image
  `ghcr.io/tecnativa/postgres-autoconf:18-alpine`.
- Dev compose mounts `./odoo/custom` **read-only** into the container; edits to private
  addons are picked up live (`--dev=reload,qweb,werkzeug,xml` is set in `devel.yaml`).
  `./odoo/auto` is mounted read-write.
- `DOODBA_WITHOUT_DEMO=all` to skip demo data; default in `test.yaml` is `all`, in
  `devel.yaml` is `false`.
- Initial lang `es_ES`. `odoo_dbfilter: ^prod` for prod.
- Port prefix env: `PORT_PREFIX` (default `18`) controls the `18xxx` host port mapping.

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

Recuerda la sección "Things not to do" más abajo: no edites ni sincronices `odoo/auto/`,
`odoo/custom/src/odoo/` ni `odoo/custom/src/oca/` (generados / git-aggregated). El
`.syncignore.example` ya los excluye por defecto — mantén esas reglas al crear tu
`.syncignore`.

## Things not to do

- Don't edit files under `odoo/auto/` — generated by the build.
- Don't edit `odoo/custom/src/odoo/` or `odoo/custom/src/oca/` — aggregated from
  upstream git repos; changes will be lost on re-aggregate. Fix upstream and
  re-aggregate instead.
- Don't bump Prettier/`plugin-xml` versions blindly — pinned for a reason (see HACK
  comments in `.pre-commit-config.yaml`).
- Don't hand-edit generated addon `README.md` or `static/description/index.html`.
