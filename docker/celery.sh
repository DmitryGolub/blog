#!/bin/bash

set -e  # Останавливать скрипт при ошибках

if [[ "${1}" == "celery" ]]; then
    celery --app=src.tasks.celery:celery worker --loglevel=INFO
elif [[ "${1}" == "flower" ]]; then
    celery --app=src.tasks.celery:celery flower
else
    echo "Unknown command: $1"
    exit 1
fi
