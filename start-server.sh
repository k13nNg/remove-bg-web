#!/usr/bin/env bash
# start-server.sh
#if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#    (cd martor_demo; python manage.py createsuperuser --no-input)
#fi
python manage.py makemigrations && python manage.py migrate
gunicorn django_project_webapp.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 &
nginx -g "daemon off;"
