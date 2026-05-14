"""
Management command to handle migrations intelligently, dealing with existing tables.
Usage: python manage.py smart_migrate
"""
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
from django.db.migrations.recorder import MigrationRecorder


class Command(BaseCommand):
    help = 'Intelligently run migrations, handling existing tables'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting smart migration...'))
        
        # Cleanup duplicate courses before applying unique constraint
        self.stdout.write(self.style.WARNING('Cleaning up duplicate courses and reassigning references...'))
        try:
            with connection.cursor() as cursor:
                # 1. Update Staff references
                cursor.execute("""
                    UPDATE main_app_staff 
                    SET course_id = sub.min_id
                    FROM (
                        SELECT name, MIN(id) as min_id
                        FROM main_app_course
                        GROUP BY name
                    ) as sub
                    JOIN main_app_course c ON c.name = sub.name
                    WHERE main_app_staff.course_id = c.id
                    AND main_app_staff.course_id != sub.min_id
                """)
                
                # 2. Update Student references
                cursor.execute("""
                    UPDATE main_app_student 
                    SET course_id = sub.min_id
                    FROM (
                        SELECT name, MIN(id) as min_id
                        FROM main_app_course
                        GROUP BY name
                    ) as sub
                    JOIN main_app_course c ON c.name = sub.name
                    WHERE main_app_student.course_id = c.id
                    AND main_app_student.course_id != sub.min_id
                """)
                
                # 3. Update Subject references - Handle duplicates
                # If multiple courses with same name have a subject with the same name, we need to merge them
                cursor.execute("""
                    DELETE FROM main_app_subject s1
                    WHERE EXISTS (
                        SELECT 1 FROM main_app_subject s2
                        JOIN main_app_course c1 ON s1.course_id = c1.id
                        JOIN main_app_course c2 ON s2.course_id = c2.id
                        WHERE c1.name = c2.name
                        AND s1.name = s2.name
                        AND s1.id > s2.id
                    )
                """)

                cursor.execute("""
                    UPDATE main_app_subject 
                    SET course_id = sub.min_id
                    FROM (
                        SELECT name, MIN(id) as min_id
                        FROM main_app_course
                        GROUP BY name
                    ) as sub
                    JOIN main_app_course c ON c.name = sub.name
                    WHERE main_app_subject.course_id = c.id
                    AND main_app_subject.course_id != sub.min_id
                """)
                
                # 4. Update Timetable references - Handle conflicts
                # Delete all but the first entry for any (CourseName, Session, Day, TimeSlot) combination
                cursor.execute("""
                    DELETE FROM main_app_timetable t1
                    WHERE EXISTS (
                        SELECT 1 FROM main_app_timetable t2
                        JOIN main_app_course c1 ON t1.course_id = c1.id
                        JOIN main_app_course c2 ON t2.course_id = c2.id
                        WHERE c1.name = c2.name
                        AND t1.session_id = t2.session_id
                        AND t1.day_of_week = t2.day_of_week
                        AND t1.time_slot_id = t2.time_slot_id
                        AND t1.id > t2.id
                    )
                """)

                cursor.execute("""
                    UPDATE main_app_timetable 
                    SET course_id = sub.min_id
                    FROM (
                        SELECT name, MIN(id) as min_id
                        FROM main_app_course
                        GROUP BY name
                    ) as sub
                    JOIN main_app_course c ON c.name = sub.name
                    WHERE main_app_timetable.course_id = c.id
                    AND main_app_timetable.course_id != sub.min_id
                """)
                
                # 5. Delete duplicates
                cursor.execute("""
                    DELETE FROM main_app_course 
                    WHERE id NOT IN (
                        SELECT MIN(id) 
                        FROM main_app_course 
                        GROUP BY name
                    )
                """)
            self.stdout.write(self.style.SUCCESS('✓ Duplicate courses cleaned up and references reassigned'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Course cleanup skipped or failed: {str(e)}'))
        
        # Ensure django_migrations table exists (Postgres specific check)
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS django_migrations (
                        id SERIAL PRIMARY KEY,
                        app VARCHAR(255) NOT NULL,
                        name VARCHAR(255) NOT NULL,
                        applied TIMESTAMP WITH TIME ZONE NOT NULL
                    )
                """)
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Migration table check: {str(e)}'))
        
        # Check which tables already exist
        existing_tables = self.get_existing_tables()
        
        # Check if migration 0003 is already recorded
        migration_recorded = self.is_migration_recorded('main_app', '0003_alter_customuser_user_type_registrar_guardian_and_more')
        
        self.stdout.write(self.style.WARNING(f'Registrar table exists: {"main_app_registrar" in existing_tables}'))
        self.stdout.write(self.style.WARNING(f'Guardian table exists: {"main_app_guardian" in existing_tables}'))
        self.stdout.write(self.style.WARNING(f'Migration 0003 recorded: {migration_recorded}'))
        
        # Now run all migrations normally
        self.stdout.write(self.style.SUCCESS('Running all migrations...'))
        try:
            call_command('migrate', verbosity=1)
            self.stdout.write(self.style.SUCCESS('✓ All migrations completed successfully'))
        except Exception as e:
            error_msg = str(e)
            self.stdout.write(self.style.ERROR(f'✗ Migration error: {error_msg}'))
            
            # If it's the "relation already exists" error for migration 0003 tables
            if any(t in error_msg for t in ['main_app_registrar', 'main_app_guardian', 'main_app_studentguardian']):
                self.stdout.write(self.style.WARNING('⚠ Tables already exist, recording migration 0003...'))
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO django_migrations (app, name, applied)
                        VALUES (%s, %s, NOW())
                        ON CONFLICT DO NOTHING
                    """, ['main_app', '0003_alter_customuser_user_type_registrar_guardian_and_more'])
                
                # Retry migrate
                call_command('migrate', verbosity=1)
                self.stdout.write(self.style.SUCCESS('✓ All migrations completed successfully after retry'))
            else:
                raise

    def get_existing_tables(self):
        """Get list of existing database tables"""
        with connection.cursor() as cursor:
            # Check if we are on Postgres or SQLite
            if connection.vendor == 'postgresql':
                cursor.execute("""
                    SELECT tablename 
                    FROM pg_tables 
                    WHERE schemaname = 'public'
                """)
            else:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            return [row[0] for row in cursor.fetchall()]
    
    def is_migration_recorded(self, app_name, migration_name):
        """Check if a migration is already recorded as applied"""
        recorder = MigrationRecorder(connection)
        try:
            applied_migrations = recorder.applied_migrations()
            return (app_name, migration_name) in applied_migrations
        except:
            return False
