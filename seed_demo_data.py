#!/usr/bin/env python
"""
Demo Data Seed Script for Dil Fere School Portal
Creates sample users, courses, subjects, and data for testing.

Usage:
    python seed_demo_data.py

This script is safe to run multiple times - it will not duplicate records.
"""

import os
import sys
import django
from datetime import datetime, date

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from main_app.models import (
    CustomUser, Admin, Staff, Student, Registrar, Guardian,
    Course, Subject, Session, StudentGuardian,
    TimeSlot, Timetable, Attendance, AttendanceReport,
    StudentResult
)

def create_or_get_user(email, password, user_type, first_name, last_name, gender, address, phone_number=None):
    """Create user if doesn't exist, return existing user otherwise."""
    user, created = CustomUser.objects.get_or_create(
        email=email,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'user_type': user_type,
            'gender': gender,
            'address': address,
        }
    )
    
    if created:
        user.set_password(password)
        user.save()
        print(f"✓ Created {first_name} {last_name} ({email})")
    else:
        print(f"→ {first_name} {last_name} ({email}) already exists")
    
    # Update phone_number for guardian if provided
    if user_type == '5' and phone_number:
        try:
            guardian = Guardian.objects.get(admin=user)
            if guardian.phone_number != phone_number:
                guardian.phone_number = phone_number
                guardian.save()
        except Guardian.DoesNotExist:
            pass
    
    return user, created

def seed_users():
    """Create demo users for all roles."""
    print("\n" + "="*60)
    print("CREATING DEMO USERS")
    print("="*60)
    
    users = []
    
    # Admin/HOD
    admin_user, _ = create_or_get_user(
        email='admin@admin.com',
        password='admin',
        user_type='1',
        first_name='Admin',
        last_name='HOD',
        gender='M',
        address='School Administration Office'
    )
    users.append(('Admin/HOD', admin_user))
    
    # Registrar
    registrar_user, _ = create_or_get_user(
        email='registrar@dilfere.school',
        password='registrar123',
        user_type='4',
        first_name='John',
        last_name='Registrar',
        gender='M',
        address='School Records Office'
    )
    users.append(('Registrar', registrar_user))
    
    # Staff/Teacher
    staff_user, _ = create_or_get_user(
        email='teacher@dilfere.school',
        password='teacher123',
        user_type='2',
        first_name='Sarah',
        last_name='Teacher',
        gender='F',
        address='123 Teacher Lane'
    )
    users.append(('Staff/Teacher', staff_user))
    
    # Student
    student_user, _ = create_or_get_user(
        email='student@dilfere.school',
        password='student123',
        user_type='3',
        first_name='Jane',
        last_name='Student',
        gender='F',
        address='456 Student Avenue'
    )
    users.append(('Student', student_user))
    
    # Guardian
    guardian_user, _ = create_or_get_user(
        email='guardian@dilfere.school',
        password='guardian123',
        user_type='5',
        first_name='Mary',
        last_name='Parent',
        gender='F',
        address='789 Parent Road',
        phone_number='+1234567890'
    )
    users.append(('Guardian', guardian_user))
    
    return users

def seed_academic_data():
    """Create demo academic data (sessions, courses, subjects)."""
    print("\n" + "="*60)
    print("CREATING ACADEMIC DATA")
    print("="*60)
    
    # Create Session (Academic Year)
    current_year = datetime.now().year
    session, created = Session.objects.get_or_create(
        start_year=date(current_year, 1, 1),
        end_year=date(current_year + 1, 12, 31),
        defaults={}
    )
    if created:
        print(f"✓ Created Session: {current_year}-{current_year + 1}")
    else:
        print(f"→ Session {current_year}-{current_year + 1} already exists")
    
    # Create Course (Grade/Class)
    course, created = Course.objects.get_or_create(
        name='Grade 1',
        defaults={}
    )
    if created:
        print(f"✓ Created Course: {course.name}")
    else:
        print(f"→ Course {course.name} already exists")
    
    # Get staff user for subject assignment
    try:
        staff_user = CustomUser.objects.get(email='teacher@dilfere.school')
        staff = Staff.objects.get(admin=staff_user)
        
        # Create Subject
        subject, created = Subject.objects.get_or_create(
            name='Mathematics',
            course=course,
            defaults={'staff': staff}
        )
        if created:
            print(f"✓ Created Subject: {subject.name} (assigned to {staff.admin.first_name})")
        else:
            print(f"→ Subject {subject.name} already exists")
    except (CustomUser.DoesNotExist, Staff.DoesNotExist):
        print("⚠ Staff user not found, skipping subject creation")
        subject = None
    
    # Update student with course and session
    try:
        student_user = CustomUser.objects.get(email='student@dilfere.school')
        student = Student.objects.get(admin=student_user)
        
        if student.course != course or student.session != session:
            student.course = course
            student.session = session
            student.save()
            print(f"✓ Assigned student to {course.name} and session {session}")
        else:
            print(f"→ Student already assigned to {course.name}")
    except (CustomUser.DoesNotExist, Student.DoesNotExist):
        print("⚠ Student user not found, skipping course assignment")
    
    return session, course, subject

def seed_guardian_link():
    """Link guardian to student."""
    print("\n" + "="*60)
    print("LINKING GUARDIAN TO STUDENT")
    print("="*60)
    
    try:
        student_user = CustomUser.objects.get(email='student@dilfere.school')
        student = Student.objects.get(admin=student_user)
        
        guardian_user = CustomUser.objects.get(email='guardian@dilfere.school')
        guardian = Guardian.objects.get(admin=guardian_user)
        
        link, created = StudentGuardian.objects.get_or_create(
            student=student,
            guardian=guardian,
            defaults={
                'relationship_type': 'mother',
                'is_primary': True
            }
        )
        
        if created:
            print(f"✓ Linked {guardian.admin.first_name} to {student.admin.first_name} (Mother, Primary Contact)")
        else:
            print(f"→ Guardian already linked to student")
    except Exception as e:
        print(f"⚠ Could not link guardian: {e}")

def seed_timetable():
    """Create sample timetable data."""
    print("\n" + "="*60)
    print("CREATING TIMETABLE DATA")
    print("="*60)
    
    try:
        # Create Time Slot
        time_slot, created = TimeSlot.objects.get_or_create(
            name='Period 1',
            defaults={
                'start_time': '08:00:00',
                'end_time': '09:00:00',
                'order': 1
            }
        )
        if created:
            print(f"✓ Created Time Slot: {time_slot.name} (08:00-09:00)")
        else:
            print(f"→ Time Slot {time_slot.name} already exists")
        
        # Create Timetable Entry
        course = Course.objects.get(name='Grade 1')
        subject = Subject.objects.get(name='Mathematics')
        staff = subject.staff
        session = Session.objects.first()
        
        timetable, created = Timetable.objects.get_or_create(
            course=course,
            subject=subject,
            staff=staff,
            session=session,
            day_of_week='monday',
            time_slot=time_slot,
            defaults={'room': 'Room 101'}
        )
        
        if created:
            print(f"✓ Created Timetable: {subject.name} on Monday at {time_slot.name}")
        else:
            print(f"→ Timetable entry already exists")
    except Exception as e:
        print(f"⚠ Could not create timetable: {e}")

def seed_attendance():
    """Create sample attendance record."""
    print("\n" + "="*60)
    print("CREATING SAMPLE ATTENDANCE")
    print("="*60)
    
    try:
        subject = Subject.objects.get(name='Mathematics')
        session = Session.objects.first()
        student_user = CustomUser.objects.get(email='student@dilfere.school')
        student = Student.objects.get(admin=student_user)
        
        today = date.today()
        
        # Create Attendance Report
        attendance_report, created = AttendanceReport.objects.get_or_create(
            subject=subject,
            date=today,
            session=session,
            defaults={}
        )
        
        if created:
            print(f"✓ Created Attendance Report for {subject.name} on {today}")
        else:
            print(f"→ Attendance Report already exists for {today}")
        
        # Create Attendance Record
        attendance, created = Attendance.objects.get_or_create(
            student=student,
            report=attendance_report,
            defaults={'status': True}  # Present
        )
        
        if created:
            print(f"✓ Marked {student.admin.first_name} as Present")
        else:
            print(f"→ Attendance record already exists")
    except Exception as e:
        print(f"⚠ Could not create attendance: {e}")

def seed_result():
    """Create sample student result."""
    print("\n" + "="*60)
    print("CREATING SAMPLE RESULT")
    print("="*60)
    
    try:
        subject = Subject.objects.get(name='Mathematics')
        session = Session.objects.first()
        student_user = CustomUser.objects.get(email='student@dilfere.school')
        student = Student.objects.get(admin=student_user)
        
        result, created = StudentResult.objects.get_or_create(
            student=student,
            subject=subject,
            session=session,
            defaults={
                'test': 15.0,
                'exam': 75.0
            }
        )
        
        if created:
            print(f"✓ Created Result: {student.admin.first_name} - {subject.name} (Test: 15, Exam: 75)")
        else:
            print(f"→ Result already exists")
    except Exception as e:
        print(f"⚠ Could not create result: {e}")

def print_credentials():
    """Print all demo credentials."""
    print("\n" + "="*60)
    print("DEMO CREDENTIALS")
    print("="*60)
    print("\n📧 LOGIN CREDENTIALS:\n")
    
    credentials = [
        ("Admin/HOD", "admin@admin.com", "admin", "http://127.0.0.1:8000/admin_home"),
        ("Registrar", "registrar@dilfere.school", "registrar123", "http://127.0.0.1:8000/registrar_home"),
        ("Staff/Teacher", "teacher@dilfere.school", "teacher123", "http://127.0.0.1:8000/staff_home"),
        ("Student", "student@dilfere.school", "student123", "http://127.0.0.1:8000/student_home"),
        ("Guardian", "guardian@dilfere.school", "guardian123", "http://127.0.0.1:8000/guardian_home"),
    ]
    
    for role, email, password, dashboard in credentials:
        print(f"{role}:")
        print(f"  Email:     {email}")
        print(f"  Password:  {password}")
        print(f"  Dashboard: {dashboard}")
        print()
    
    print("="*60)
    print("✅ DEMO DATA SEEDING COMPLETE!")
    print("="*60)
    print("\nYou can now:")
    print("1. Run: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/")
    print("3. Login with any of the credentials above")
    print("\n⚠️  IMPORTANT: Change all passwords before production deployment!")
    print("="*60 + "\n")

def main():
    """Main seeding function."""
    print("\n" + "="*60)
    print("DIL FERE SCHOOL PORTAL - DEMO DATA SEED SCRIPT")
    print("="*60)
    print("\nThis script will create demo users and sample data.")
    print("It is safe to run multiple times.\n")
    
    try:
        # Seed users
        users = seed_users()
        
        # Seed academic data
        session, course, subject = seed_academic_data()
        
        # Link guardian to student
        seed_guardian_link()
        
        # Seed timetable (if models exist)
        try:
            seed_timetable()
        except Exception as e:
            print(f"⚠ Timetable seeding skipped: {e}")
        
        # Seed attendance (if safe)
        try:
            seed_attendance()
        except Exception as e:
            print(f"⚠ Attendance seeding skipped: {e}")
        
        # Seed result (if safe)
        try:
            seed_result()
        except Exception as e:
            print(f"⚠ Result seeding skipped: {e}")
        
        # Print credentials
        print_credentials()
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
