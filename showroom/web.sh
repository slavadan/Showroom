#!/bin/sh

sleep 5

cd /docker

python ./showroom/manage.py makemigrations

python ./showroom/manage.py migrate

sleep 5

python ./showroom/manage.py runserver 0.0.0.0:8000