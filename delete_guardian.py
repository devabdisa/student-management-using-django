"""
Helper script to delete a Guardian user
Usage: python delete_guardian.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from main_app.models import CustomUser, Guardian, StudentGuardian

def delete_guardian():
    """Delete a Guardian user"""
    
    guardian_email = 'guardian@dilfere.school'
    
    try:
        # Get guardian user
        user = CustomUser.objects.get(email=guardian_email, user_type=5)
        guardian = Guardian.objects.get(admin=user)
        
        print(f"Found Guardian:")
        print(f"Email: {user.email}")
        print(f"Name: {user.first_name} {user.last_name}")
        print(f"Phone: {guardian.phone_number}")
        print(f"Occupation: {guardian.occupation}")
        
        # Check for linked students
        links = StudentGuardian.objects.filter(guardian=guardian)
        if links.exists():
            print(f"\n⚠️  This guardian is linked to {links.count()} student(s):")
            for link in links:
                print(f"  - {link.student.admin.first_name} {link.student.admin.last_name}")
        
        # Confirm deletion
        confirm = input(f"\n❓ Are you sure you want to delete this guardian? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            # Delete links first
            if links.exists():
                links.delete()
                print(f"✅ Deleted {links.count()} student link(s)")
            
            # Delete guardian profile (will cascade delete user)
            user.delete()
            print(f"✅ Guardian deleted successfully!")
        else:
            print("❌ Deletion cancelled.")
            
    except CustomUser.DoesNotExist:
        print(f"❌ Guardian with email {guardian_email} not found!")
    except Guardian.DoesNotExist:
        print(f"❌ Guardian profile not found!")
    except Exception as e:
        print(f"❌ Error deleting guardian: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("=" * 60)
    print("Delete Guardian User - Dil Fere Primary School")
    print("=" * 60)
    delete_guardian()
    print("=" * 60)
