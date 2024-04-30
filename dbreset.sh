#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
python manage.py runscript csvimport
python manage.py collectstatic --noinput
python manage.py createsuperuser