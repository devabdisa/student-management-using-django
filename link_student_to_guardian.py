"""
Helper script to link a Student to a Guardian
Usage: python link_student_to_guardian.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from main_app.models import CustomUser, Guardian, Student, StudentGuardian

def link_student_to_guardian():
    """Link a student to a guardian"""
    
    # Configuration
    guardian_email = 'guardian@dilfere.school'
    student_email = input("Enter student email (or press Enter to list all students): ").strip()
    
    # Get guardian
    try:
        guardian_user = CustomUser.objects.get(email=guardian_email, user_type=5)
        guardian = Guardian.objects.get(admin=guardian_user)
        print(f"✅ Found Guardian: {guardian.admin.first_name} {guardian.admin.last_name}")
    except CustomUser.DoesNotExist:
        print(f"❌ Guardian with email {guardian_email} not found!")
        print("Run create_guardian.py first to create a guardian.")
        return
    except Guardian.DoesNotExist:
        print(f"❌ Guardian profile not found for user {guardian_email}!")
        return
    
    # List students if no email provided
    if not student_email:
        print("\n📋 Available Students:")
        print("-" * 60)
        students = Student.objects.all().select_related('admin', 'course')
        if not students:
            print("No students found in the system.")
            return
        
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.admin.first_name} {student.admin.last_name}")
            print(f"   Email: {student.admin.email}")
            print(f"   Course: {student.course.name if student.course else 'N/A'}")
            print()
        
        student_email = input("Enter student email to link: ").strip()
    
    # Get student
    try:
        student_user = CustomUser.objects.get(email=student_email, user_type=3)
        student = Student.objects.get(admin=student_user)
        print(f"✅ Found Student: {student.admin.first_name} {student.admin.last_name}")
    except CustomUser.DoesNotExist:
        print(f"❌ Student with email {student_email} not found!")
        return
    except Student.DoesNotExist:
        print(f"❌ Student profile not found for user {student_email}!")
        return
    
    # Check if link already exists
    if StudentGuardian.objects.filter(student=student, guardian=guardian).exists():
        print(f"⚠️  Link already exists between {student.admin.first_name} and {guardian.admin.first_name}!")
        link = StudentGuardian.objects.get(student=student, guardian=guardian)
        print(f"\nExisting Link Details:")
        print(f"Primary Contact: {link.is_primary}")
        print(f"Can Pickup: {link.can_pickup}")
        print(f"Emergency Contact: {link.emergency_contact}")
        return
    
    # Get link details
    print("\n📝 Link Details:")
    is_primary = input("Is this the primary contact? (y/n, default: n): ").strip().lower() == 'y'
    can_pickup = input("Can pickup student? (y/n, default: y): ").strip().lower() != 'n'
    emergency_contact = input("Is emergency contact? (y/n, default: n): ").strip().lower() == 'y'
    
    try:
        # Create link
        link = StudentGuardian.objects.create(
            student=student,
            guardian=guardian,
            is_primary=is_primary,
            can_pickup=can_pickup,
            emergency_contact=emergency_contact
        )
        
        print(f"\n✅ Successfully linked!")
        print(f"Student: {student.admin.first_name} {student.admin.last_name}")
        print(f"Guardian: {guardian.admin.first_name} {guardian.admin.last_name}")
        print(f"Relationship: {guardian.get_relationship_type_display()}")
        print(f"Primary Contact: {link.is_primary}")
        print(f"Can Pickup: {link.can_pickup}")
        print(f"Emergency Contact: {link.emergency_contact}")
        
        print(f"\n🎉 Link created successfully!")
        print(f"\nThe guardian can now log in and view this student's information:")
        print(f"URL: http://127.0.0.1:8000/")
        print(f"Email: {guardian_email}")
        
    except Exception as e:
        print(f"❌ Error creating link: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("=" * 60)
    print("Link Student to Guardian - Dil Fere Primary School")
    print("=" * 60)
    link_student_to_guardian()
    print("=" * 60)
