#!/bin/sh
source venv/bin/activate
exec gunicorn -b :5000 --access-logfile - --error-logfile - time_to_planet:app
