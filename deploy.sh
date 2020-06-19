#!/bin/bash

PROJECT_HOME=/home/test/website
ENV_BIN=/home/test/for_website/bin
cd $PROJECT_HOME
git pull

$ENV_BIN/pip install -r requirements.txt
$ENV_BIN/python3 manage.py collectstatic --noinput
#$ENV_BIN/python3 manage.py makemigrations
#$ENV_BIN/python3 manage.py migrate

killall -9 uwsgi

exit 0
