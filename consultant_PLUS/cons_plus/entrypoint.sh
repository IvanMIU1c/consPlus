#!/bin/sh

echo "makemigrations"
python3 manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

echo "Starting server"
python3 manage.py runserver 0.0.0.0:8002

