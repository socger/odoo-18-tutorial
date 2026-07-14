#!/usr/bin/env bash
#
# sync.sh — Sincronización bidireccional local <-> remoto con rsync sobre SSH.
#
# Uso:
#   ./sync.sh push [--dry-run|-n] [--delete] [--verbose|-v] [-h|--help] [path...]
#   ./sync.sh pull [--dry-run|-n] [--delete] [--verbose|-v] [-h|--help] [path...]
#
# - push: local  -> remoto
# - pull: remoto -> local
#
# Configuración: lee ./sync.conf (mismo directorio que este script) si existe.
# Cualquier variable de entorno ya definida tiene PRIORIDAD sobre sync.conf.
#
# Variables (ver sync.conf.example):
#   REMOTE_USER, REMOTE_HOST, REMOTE_PORT, REMOTE_PATH, SSH_IDENTITY
#
# Excludes por defecto: .git/, .venv/, .vscode/, .zed/
# Excludes adicionales: se leen desde <raiz_proyecto>/.syncignore si existe.
#
# --delete  : borra en destino lo que no existe en origen (mirror real). Opt-in.
# --dry-run : solo simula (-n de rsync).
# --verbose : añade -v --progress a rsync.
#
set -euo pipefail

# ---------------------------------------------------------------------------
# Constantes y rutas base
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Raíz del proyecto: resources/scripts -> resources -> raíz
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

CONF_FILE="${SCRIPT_DIR}/sync.conf"
SYNCIGNORE_FILE="${PROJECT_ROOT}/.syncignore"

# Excludes por defecto (siempre se aplican, tanto en push como en pull)
DEFAULT_EXCLUDES=(
    --exclude '.git/'
    --exclude '.venv/'
    --exclude '.vscode/'
    --exclude '.zed/'
)

# ---------------------------------------------------------------------------
# usage
# ---------------------------------------------------------------------------
usage() {
    cat <<EOF
sync.sh — Sincronización local <-> remoto con rsync sobre SSH.

Uso:
  $(basename "$0") <push|pull> [opciones] [path...]

Direcciones:
  push   Local  -> Remoto
  pull   Remoto -> Local

Opciones:
  -n, --dry-run    Simula la transferencia (no escribe nada).
      --delete     Borra en destino lo que no existe en origen (mirror real).
  -v, --verbose    Salida detallada con --progress.
  -h, --help       Muestra esta ayuda y sale.

Configuración (orden de prioridad, primera gana):
  1. Variables de entorno ya exportadas.
  2. ${CONF_FILE}
  3. Defaults internos.

Variables requeridas: REMOTE_USER, REMOTE_HOST, REMOTE_PATH
Variables opcionales: REMOTE_PORT (default 22), SSH_IDENTITY

Path local por defecto: ${PROJECT_ROOT}
Puedes pasar paths relativos a ese directorio para acotar la sincronización.

Excludes por defecto: .git/ .venv/ .vscode/ .zed/
Excludes adicionales: ${SYNCIGNORE_FILE} (si existe, una regla por línea).

Ejemplos:
  $(basename "$0") push --dry-run
  $(basename "$0") pull --delete
  $(basename "$0") push odoo/custom/src/private/
EOF
}

die() {
    echo "ERROR: $*" >&2
    echo >&2
    usage >&2
    exit 1
}

# ---------------------------------------------------------------------------
# Cargar configuración (las env vars ya definidas tienen prioridad)
# ---------------------------------------------------------------------------
load_config() {
    if [[ -f "${CONF_FILE}" ]]; then
        # shellcheck disable=SC1090
        source "${CONF_FILE}"
    fi

    : "${REMOTE_USER:?Falta REMOTE_USER (defínelo en ${CONF_FILE} o como env var)}"
    : "${REMOTE_HOST:?Falta REMOTE_HOST (defínelo en ${CONF_FILE} o como env var)}"
    : "${REMOTE_PATH:?Falta REMOTE_PATH (defínelo en ${CONF_FILE} o como env var)}"
    : "${REMOTE_PORT:=22}"
    : "${SSH_IDENTITY:=}"
}

# ---------------------------------------------------------------------------
# Opciones SSH para rsync (-e)
# ---------------------------------------------------------------------------
build_ssh_opts() {
    local -a ssh_args=(-p "${REMOTE_PORT}")
    if [[ -n "${SSH_IDENTITY}" ]]; then
        ssh_args+=(-i "${SSH_IDENTITY}")
    fi
    ssh_args+=(-o StrictHostKeyChecking=accept-new -o ServerAliveInterval=60)
    printf 'ssh %s' "${ssh_args[*]}"
}

# ---------------------------------------------------------------------------
# Lista final de excludes (default + .syncignore)
# ---------------------------------------------------------------------------
build_excludes() {
    for ex in "${DEFAULT_EXCLUDES[@]}"; do
        printf '%s\n' "${ex}"
    done
    if [[ -f "${SYNCIGNORE_FILE}" ]]; then
        printf '%s\n' "--exclude-from=${SYNCIGNORE_FILE}"
    fi
}

# ---------------------------------------------------------------------------
# Resuelve paths locales absolutos con trailing slash para dirs
# ---------------------------------------------------------------------------
resolve_local_paths() {
    local -n out=$1; shift
    if [[ $# -eq 0 ]]; then
        out=("${PROJECT_ROOT}/")
        return
    fi
    for p in "$@"; do
        local abs="${PROJECT_ROOT}/${p}"
        if [[ ! -e "${abs}" ]]; then
            die "El path local no existe: ${abs}"
        fi
        if [[ -d "${abs}" ]]; then
            out+=("${abs%/}/")
        else
            out+=("${abs}")
        fi
    done
}

# ---------------------------------------------------------------------------
# Ejecuta rsync
# ---------------------------------------------------------------------------
run_rsync() {
    local direction="$1"; shift
    local -a user_paths=()
    resolve_local_paths user_paths "$@"

    local -a rsync_opts=(-a --compress --human-readable)
    rsync_opts+=("${USER_OPTS[@]}")

    while IFS= read -r ex; do
        [[ -n "${ex}" ]] && rsync_opts+=("${ex}")
    done < <(build_excludes)

    rsync_opts+=(-e "$(build_ssh_opts)")

    local remote_path="${REMOTE_PATH%/}/"
    local remote_spec="${REMOTE_USER}@${REMOTE_HOST}:${remote_path}"

    echo "==> Dirección : ${direction}"
    if [[ "${direction}" == "push" ]]; then
        echo "==> Origen    : ${user_paths[*]}"
        echo "==> Destino   : ${remote_spec}"
    else
        echo "==> Origen    : ${remote_spec}"
        echo "==> Destino   : ${user_paths[*]}"
    fi
    echo "==> Opciones  : ${rsync_opts[*]}"
    echo

    if [[ "${direction}" == "push" ]]; then
        rsync "${rsync_opts[@]}" "${user_paths[@]}" "${remote_spec}"
    elif [[ ${#user_paths[@]} -eq 1 ]]; then
        rsync "${rsync_opts[@]}" "${remote_spec}" "${user_paths[0]}"
    else
        # pull con múltiples paths: rsync no soporta varios destinos locales,
        # así que iteramos reconstruyendo el subpath relativo en el remoto.
        for p in "${user_paths[@]}"; do
            local rel="${p#"${PROJECT_ROOT}/"}"
            rel="${rel%/}"
            local src="${remote_spec}${rel}"
            echo "--> ${src}  ->  ${p}"
            rsync "${rsync_opts[@]}" "${src}" "${p}"
        done
    fi
}

# ---------------------------------------------------------------------------
# Parseo de argumentos
# ---------------------------------------------------------------------------
DIRECTION=""
USER_OPTS=()
USER_PATHS=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        push|pull)
            [[ -n "${DIRECTION}" ]] && die "Dirección ya definida: ${DIRECTION}"
            DIRECTION="$1"
            shift
            ;;
        -n|--dry-run)
            USER_OPTS+=(--dry-run)
            shift
            ;;
        --delete)
            USER_OPTS+=(--delete)
            shift
            ;;
        -v|--verbose)
            USER_OPTS+=(--verbose --progress)
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        --*)
            die "Opción desconocida: $1"
            ;;
        -*)
            die "Opción desconocida: $1"
            ;;
        *)
            [[ -z "${DIRECTION}" ]] && die "Falta la dirección (push|pull) antes de: $1"
            USER_PATHS+=("$1")
            shift
            ;;
    esac
done

[[ -z "${DIRECTION}" ]] && die "Falta la dirección (push|pull)."

load_config
run_rsync "${DIRECTION}" "${USER_PATHS[@]}"
