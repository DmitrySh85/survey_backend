#!/bin/bash

cd survey_backend

python3 manage.py migrate

gunicorn survey_backend.wsgi:application -b 0.0.0.0 -w 4