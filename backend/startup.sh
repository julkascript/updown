#!/bin/bash

# Wait for PostgreSQL to start up
while ! pg_isready -q -h db -p 5432 -U postgres
do
  echo "Waiting for PostgreSQL to start up..."
  sleep 1
done

# Apply Django migrations
echo "Applying Django migrations..."
python manage.py makemigrations
python manage.py migrate

# Create Django superuser
echo "Creating Django superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Start Django server
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000