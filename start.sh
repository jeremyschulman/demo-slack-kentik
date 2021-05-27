#!/usr/bin/env bash

uvicorn fotomat:api \
  --host 0.0.0.0 \
  --port ${SLACK_APP_PORT} \
  --reload
