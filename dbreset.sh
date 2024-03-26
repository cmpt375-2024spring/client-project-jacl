#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py runscript csvimport
python manage.py createsuperuser