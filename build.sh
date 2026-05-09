#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create initial admin user (only runs if doesn't exist)
python manage.py create_initial_admin

# Seed demo data (only runs if data doesn't exist)
python manage.py seed_demo_data
