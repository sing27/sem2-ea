#!/bin/bash
source venv/bin/activate

venv/bin/flask db init
venv/bin/flask db migrate
venv/bin/flask db upgrade

exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app