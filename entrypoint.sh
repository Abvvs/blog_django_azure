#!/bin/sh
echo "Waiting for PostgreSQL to start..."

# Wait for PostgreSQL to be available
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL started"

#python manage.py migrate
#echo "Applying migrations..."
#export DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-root}
#python manage.py createsuperuser --noinput \
#  --username=${DJANGO_SUPERUSER_USERNAME:-admin} \
#  --email=${DJANGO_SUPERUSER_EMAIL:-'abi@gmail.com'} || true

#levantar el servidor de Django /runserver
python manage.py runserver 0.0.0:8000