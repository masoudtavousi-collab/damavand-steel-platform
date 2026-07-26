#!/usr/bin/env sh
set -eu

repository_root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
environment_path="$repository_root/.venv"
bootstrap_python="${PYTHON_BOOTSTRAP:-python3}"

"$bootstrap_python" -m venv "$environment_path"
"$environment_path/bin/python3" -m pip install \
  --disable-pip-version-check \
  --requirement "$repository_root/requirements-validation.txt"

echo "Local validation environment is ready at .venv."
echo "Run make test from the repository root."
