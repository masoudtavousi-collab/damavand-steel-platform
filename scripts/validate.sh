#!/usr/bin/env sh
set -eu

required="README.md .env.example composer.json docs/adr public/wp-content config scripts assets prompts"
for path in $required; do
  if [ ! -e "$path" ]; then
    echo "Missing required path: $path" >&2
    exit 1
  fi
done

echo "Repository scaffold is valid."
