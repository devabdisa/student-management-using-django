#!/usr/bin/env python
"""Script to create a test Registrar user"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from main_app.models import CustomUser, Registrar

# Check if registrar already exists
if CustomUser.objects.filter(email='registrar@dilfere.school').exists():
    print("Registrar user already exists!")
    user = CustomUser.objects.get(email='registrar@dilfere.school')
    print(f"Email: {user.email}")
    print(f"Name: {user.first_name} {user.last_name}")
    print(f"User Type: {user.user_type}")
else:
    # Create Registrar user
    user = CustomUser.objects.create_user(
        email='registrar@dilfere.school',
        password='registrar123',
        first_name='John',
        last_name='Registrar',
        user_type=4,  # Integer, not string
        gender='M',
        address='School Office'
    )
    print("✅ Registrar user created successfully!")
    print(f"Email: {user.email}")
    print(f"Password: registrar123")
    print(f"Name: {user.first_name} {user.last_name}")
    print(f"User Type: {user.user_type}")
    
    # Verify profile was created
    try:
        registrar = Registrar.objects.get(admin=user)
        print(f"✅ Registrar profile created: {registrar}")
    except Registrar.DoesNotExist:
        print("❌ Warning: Registrar profile not created automatically")
