#!/usr/bin/env python
"""Script to delete test Registrar user"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from main_app.models import CustomUser

# Delete registrar user
deleted = CustomUser.objects.filter(email='registrar@dilfere.school').delete()
print(f"Deleted: {deleted}")
