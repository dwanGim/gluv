#!/bin/bash

pkill -f "uvicorn gluv.asgi:application --host 0.0.0.0 --port 8000"
pkill -f "celery -A gluv worker"
pkill -f "celery -A gluv beat"
