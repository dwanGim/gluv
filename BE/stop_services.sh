#!/bin/bash

pkill -f "uvicorn gluv.asgi:application --host 0.0.0.0 --port 8001"
pkill -f "gunicorn -b 0.0.0.0:8000 gluv.wsgi:application"
pkill -f "celery -A gluv worker"
pkill -f "celery -A gluv beat"
