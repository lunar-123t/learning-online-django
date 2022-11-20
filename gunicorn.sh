#!/bin/sh

if [ -z ${ENVIRONMENT} ]; then export ENVIRONMENT=local; fi

# build static assets
python /usr/src/learning-online-django/manage.py collectstatic --noinput --settings=config.settings.$ENVIRONMENT

# start api with gunicorn
/usr/src/learning-online-django/virtualenv/bin/gunicorn mysite.wsgi -b 0.0.0.0:8000 --chdir=/usr/src/learning-online-django
