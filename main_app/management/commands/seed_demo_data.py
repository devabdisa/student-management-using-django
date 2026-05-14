"""
Management command to seed demo data for production.
Usage: python manage.py seed_demo_data
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from main_app.models import (
    CustomUser, Admin, Staff, Student, Guardian, StudentGuardian,
    Course, Subject, Session, TimeSlot, Timetable
)


class Command(BaseCommand):
    help = 'Seeds demo data with simple credentials'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting demo data seeding...'))
        
        # Create Session
        session = self.create_session()
        
        # Create Courses
        courses = self.create_courses()
        
        # Create Admin (if not exists)
        admin = self.create_admin()
        
        # Create Staff
        staff_users = self.create_staff(courses)
        
        # Create Subjects
        subjects = self.create_subjects(courses, staff_users)
        
        # Create Students
        students = self.create_students(courses, session)
        
        # Create Guardians
        guardians = self.create_guardians()
        
        # Link Students to Guardians
        self.link_students_to_guardians(students, guardians)
        
        # Create Timetable
        self.create_timetable(subjects)
        
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('✅ Demo data seeded successfully!'))
        self.stdout.write(self.style.SUCCESS('='*60))
        self.print_credentials()

    def create_session(self):
        """Create academic session"""
        from datetime import date
        
        current_year = timezone.now().year
        start_date = date(current_year, 1, 1)
        end_date = date(current_year + 1, 12, 31)
        
        # Check if session exists first
        existing_session = Session.objects.filter(
            start_year=start_date,
            end_year=end_date
        ).first()
        
        if existing_session:
            self.stdout.write(self.style.WARNING(f'⚠ Session already exists: {existing_session}'))
            return existing_session
        
        # Create new session
        session = Session.objects.create(
            start_year=start_date,
            end_year=end_date
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Created session: {session}'))
        return session

    def create_courses(self):
        """Create courses"""
        course_names = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5']
        courses = []
        
        for name in course_names:
            course = Course.objects.filter(name=name).first()
            if course:
                courses.append(course)
                self.stdout.write(self.style.WARNING(f'⚠ Course already exists: {name}'))
            else:
                course = Course.objects.create(name=name)
                courses.append(course)
                self.stdout.write(self.style.SUCCESS(f'✓ Created course: {name}'))
        
        return courses

    def create_admin(self):
        """Create admin user"""
        email = 'admin@school.com'
        
        if CustomUser.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'⚠ Admin already exists: {email}'))
            return CustomUser.objects.get(email=email)
        
        user = CustomUser.objects.create_user(
            email=email,
            password='admin123',
            user_type=1,
            first_name='Admin',
            last_name='User'
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created admin: {email}'))
        return user

    def create_staff(self, courses):
        """Create staff members"""
        staff_data = [
            {'email': 'teacher1@school.com', 'first': 'John', 'last': 'Smith', 'course': courses[0], 'gender': 'M'},
            {'email': 'teacher2@school.com', 'first': 'Sarah', 'last': 'Johnson', 'course': courses[1], 'gender': 'F'},
            {'email': 'teacher3@school.com', 'first': 'Michael', 'last': 'Brown', 'course': courses[2], 'gender': 'M'},
        ]
        
        staff_users = []
        for data in staff_data:
            if CustomUser.objects.filter(email=data['email']).exists():
                self.stdout.write(self.style.WARNING(f'⚠ Staff already exists: {data["email"]}'))
                staff_users.append(CustomUser.objects.get(email=data['email']))
                continue
            
            user = CustomUser.objects.create_user(
                email=data['email'],
                password='teacher123',
                user_type=2,
                first_name=data['first'],
                last_name=data['last'],
                gender=data['gender'],
                address='123 School Street'
            )
            user.staff.course = data['course']
            user.save()
            staff_users.append(user)
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created staff: {data["email"]}'))
        
        return staff_users

    def create_subjects(self, courses, staff_users):
        """Create subjects"""
        subjects_data = [
            {'name': 'Mathematics', 'course': courses[0], 'staff': staff_users[0].staff},
            {'name': 'English', 'course': courses[0], 'staff': staff_users[0].staff},
            {'name': 'Science', 'course': courses[1], 'staff': staff_users[1].staff},
            {'name': 'History', 'course': courses[1], 'staff': staff_users[1].staff},
            {'name': 'Geography', 'course': courses[2], 'staff': staff_users[2].staff},
        ]
        
        subjects = []
        for data in subjects_data:
            subject = Subject.objects.filter(name=data['name'], course=data['course']).first()
            if subject:
                subjects.append(subject)
                self.stdout.write(self.style.WARNING(f'⚠ Subject already exists: {data["name"]}'))
            else:
                subject = Subject.objects.create(
                    name=data['name'],
                    course=data['course'],
                    staff=data['staff']
                )
                subjects.append(subject)
                self.stdout.write(self.style.SUCCESS(f'✓ Created subject: {data["name"]}'))
        
        return subjects

    def create_students(self, courses, session):
        """Create students"""
        students_data = [
            {'email': 'student1@school.com', 'first': 'Alice', 'last': 'Williams', 'course': courses[0], 'gender': 'F'},
            {'email': 'student2@school.com', 'first': 'Bob', 'last': 'Davis', 'course': courses[0], 'gender': 'M'},
            {'email': 'student3@school.com', 'first': 'Charlie', 'last': 'Miller', 'course': courses[1], 'gender': 'M'},
            {'email': 'student4@school.com', 'first': 'Diana', 'last': 'Wilson', 'course': courses[1], 'gender': 'F'},
            {'email': 'student5@school.com', 'first': 'Emma', 'last': 'Moore', 'course': courses[2], 'gender': 'F'},
        ]
        
        students = []
        for data in students_data:
            if CustomUser.objects.filter(email=data['email']).exists():
                self.stdout.write(self.style.WARNING(f'⚠ Student already exists: {data["email"]}'))
                students.append(CustomUser.objects.get(email=data['email']))
                continue
            
            user = CustomUser.objects.create_user(
                email=data['email'],
                password='student123',
                user_type=3,
                first_name=data['first'],
                last_name=data['last'],
                gender=data['gender'],
                address='456 Student Avenue'
            )
            user.student.course = data['course']
            user.student.session = session
            user.save()
            students.append(user)
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created student: {data["email"]}'))
        
        return students

    def create_guardians(self):
        """Create guardians"""
        guardians_data = [
            {'email': 'parent1@school.com', 'first': 'Robert', 'last': 'Williams', 'gender': 'M'},
            {'email': 'parent2@school.com', 'first': 'Linda', 'last': 'Davis', 'gender': 'F'},
            {'email': 'parent3@school.com', 'first': 'James', 'last': 'Miller', 'gender': 'M'},
        ]
        
        guardians = []
        for data in guardians_data:
            if CustomUser.objects.filter(email=data['email']).exists():
                self.stdout.write(self.style.WARNING(f'⚠ Guardian already exists: {data["email"]}'))
                guardians.append(CustomUser.objects.get(email=data['email']))
                continue
            
            user = CustomUser.objects.create_user(
                email=data['email'],
                password='parent123',
                user_type=5,
                first_name=data['first'],
                last_name=data['last'],
                gender=data['gender'],
                address='789 Parent Street'
            )
            guardians.append(user)
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created guardian: {data["email"]}'))
        
        return guardians

    def link_students_to_guardians(self, students, guardians):
        """Link students to their guardians"""
        links = [
            (students[0], guardians[0], 'father'),  # Alice -> Robert Williams
            (students[1], guardians[1], 'mother'),  # Bob -> Linda Davis
            (students[2], guardians[2], 'father'),  # Charlie -> James Miller
        ]
        
        for student_user, guardian_user, relationship in links:
            try:
                student = student_user.student
                guardian = guardian_user.guardian
                
                # Check if relationship exists on model, otherwise ignore
                link = StudentGuardian.objects.filter(
                    student=student,
                    guardian=guardian
                ).first()
                
                if not link:
                    link = StudentGuardian.objects.create(
                        student=student,
                        guardian=guardian
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'✓ Linked {student_user.first_name} to {guardian_user.first_name}'
                    ))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error linking: {str(e)}'))

    def create_timetable(self, subjects):
        """Create sample timetable"""
        from datetime import time
        
        # Get the session
        session = Session.objects.first()
        if not session:
            self.stdout.write(self.style.WARNING('⚠ No session found, skipping timetable'))
            return
        
        # Create time slots
        time_slots_data = [
            {'name': 'Period 1', 'start': time(8, 0), 'end': time(9, 0), 'order': 1},
            {'name': 'Period 2', 'start': time(9, 0), 'end': time(10, 0), 'order': 2},
            {'name': 'Period 3', 'start': time(10, 0), 'end': time(11, 0), 'order': 3},
            {'name': 'Period 4', 'start': time(11, 0), 'end': time(12, 0), 'order': 4},
        ]
        
        time_slots = []
        for data in time_slots_data:
            slot = TimeSlot.objects.filter(name=data['name']).first()
            if slot:
                time_slots.append(slot)
                self.stdout.write(self.style.WARNING(f'⚠ Time slot already exists: {data["name"]}'))
            else:
                slot = TimeSlot.objects.create(
                    name=data['name'],
                    start_time=data['start'],
                    end_time=data['end'],
                    order=data['order']
                )
                time_slots.append(slot)
                self.stdout.write(self.style.SUCCESS(f'✓ Created time slot: {data["name"]}'))
        
        # Create timetable entries
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI']
        count = 0
        
        for i, subject in enumerate(subjects[:5]):  # First 5 subjects
            day = days[i % len(days)]
            time_slot = time_slots[i % len(time_slots)]
            
            # Create Timetable entry
            timetable, created = Timetable.objects.get_or_create(
                course=subject.course,
                subject=subject,
                staff=subject.staff,
                session=session,
                day_of_week=day,
                time_slot=time_slot,
                defaults={'room': f'Room {i+1}'}
            )
            
            if created:
                count += 1
        
        if count > 0:
            self.stdout.write(self.style.SUCCESS(f'✓ Created {count} timetable entries'))

    def print_credentials(self):
        """Print all demo credentials"""
        self.stdout.write(self.style.SUCCESS('\n📋 DEMO CREDENTIALS:'))
        self.stdout.write(self.style.SUCCESS('='*60))
        
        self.stdout.write(self.style.SUCCESS('\n👨‍💼 ADMIN:'))
        self.stdout.write('  Email: admin@school.com')
        self.stdout.write('  Password: admin123')
        
        self.stdout.write(self.style.SUCCESS('\n👨‍🏫 TEACHERS:'))
        self.stdout.write('  Email: teacher1@school.com | Password: teacher123')
        self.stdout.write('  Email: teacher2@school.com | Password: teacher123')
        self.stdout.write('  Email: teacher3@school.com | Password: teacher123')
        
        self.stdout.write(self.style.SUCCESS('\n👨‍🎓 STUDENTS:'))
        self.stdout.write('  Email: student1@school.com | Password: student123')
        self.stdout.write('  Email: student2@school.com | Password: student123')
        self.stdout.write('  Email: student3@school.com | Password: student123')
        self.stdout.write('  Email: student4@school.com | Password: student123')
        self.stdout.write('  Email: student5@school.com | Password: student123')
        
        self.stdout.write(self.style.SUCCESS('\n👨‍👩‍👧 PARENTS/GUARDIANS:'))
        self.stdout.write('  Email: parent1@school.com | Password: parent123')
        self.stdout.write('  Email: parent2@school.com | Password: parent123')
        self.stdout.write('  Email: parent3@school.com | Password: parent123')
        
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.WARNING('⚠️  IMPORTANT: Change these passwords in production!'))
        self.stdout.write(self.style.SUCCESS('='*60 + '\n'))
