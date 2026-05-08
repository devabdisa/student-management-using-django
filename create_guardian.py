"""
Helper script to create a Guardian user for testing
Usage: python create_guardian.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from main_app.models import CustomUser, Guardian

def create_guardian():
    """Create a test Guardian user"""
    
    # Guardian details
    email = 'guardian@dilfere.school'
    password = 'guardian123'
    first_name = 'John'
    last_name = 'Guardian'
    gender = 'M'
    address = 'Dil Fere, Ethiopia'
    phone_number = '+251911234567'
    occupation = 'Engineer'
    relationship_type = 'father'
    
    # Check if guardian already exists
    if CustomUser.objects.filter(email=email).exists():
        print(f"❌ Guardian with email {email} already exists!")
        user = CustomUser.objects.get(email=email)
        guardian = Guardian.objects.get(admin=user)
        print(f"\nExisting Guardian Details:")
        print(f"Email: {user.email}")
        print(f"Name: {user.first_name} {user.last_name}")
        print(f"User Type: {user.user_type}")
        print(f"Phone: {guardian.phone_number}")
        print(f"Occupation: {guardian.occupation}")
        print(f"Relationship: {guardian.get_relationship_type_display()}")
        return
    
    try:
        # Create CustomUser with user_type=5 (Guardian)
        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            user_type=5,  # Important: Integer 5, not string '5'
            gender=gender,
            address=address
        )
        
        print(f"✅ Guardian user created successfully!")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Name: {first_name} {last_name}")
        print(f"User Type: {user.user_type}")
        
        # Update Guardian profile (auto-created by signal)
        guardian = Guardian.objects.get(admin=user)
        guardian.phone_number = phone_number
        guardian.occupation = occupation
        guardian.relationship_type = relationship_type
        guardian.save()
        
        print(f"✅ Guardian profile updated: {guardian}")
        print(f"Phone: {guardian.phone_number}")
        print(f"Occupation: {guardian.occupation}")
        print(f"Relationship: {guardian.get_relationship_type_display()}")
        
        print(f"\n🎉 Guardian created successfully!")
        print(f"\nLogin Credentials:")
        print(f"URL: http://127.0.0.1:8000/")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"\n⚠️  Note: You need to link this guardian to students using the admin panel or link_student_to_guardian.py script")
        
    except Exception as e:
        print(f"❌ Error creating guardian: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("=" * 60)
    print("Creating Guardian User for Dil Fere Primary School")
    print("=" * 60)
    create_guardian()
    print("=" * 60)
