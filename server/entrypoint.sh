#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Creating Superuser
echo "Starting server"
python manage.py create_su

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000