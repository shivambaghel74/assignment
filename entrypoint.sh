#!/bin/bash

set -e

echo "Starting Model Server"
echo "PROFILE=${PROFILE:-balanced}"

uvicorn app.main:app \
--host 0.0.0.0 \
--port 8000
