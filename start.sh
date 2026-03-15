#!/bin/bash

set -euo pipefail

printf "\n🔥 unzip-bot 🔥\n\n"

if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

exec python -m unzipbot
