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
        
        # Ensure django_migrations table exists
        try:
            from django.db import connection
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
        
        # Tables that migration 0003 creates
        migration_0003_tables = ['main_app_registrar', 'main_app_guardian', 'main_app_studentguardian']
        
        # Check if migration 0003 tables already exist
        tables_exist = all(table in existing_tables for table in migration_0003_tables)
        
        # Check if migration 0003 is already recorded
        migration_recorded = self.is_migration_recorded('main_app', '0003_alter_customuser_user_type_registrar_guardian_and_more')
        
        self.stdout.write(self.style.WARNING(f'Registrar table exists: {"main_app_registrar" in existing_tables}'))
        self.stdout.write(self.style.WARNING(f'Guardian table exists: {"main_app_guardian" in existing_tables}'))
        self.stdout.write(self.style.WARNING(f'StudentGuardian table exists: {"main_app_studentguardian" in existing_tables}'))
        self.stdout.write(self.style.WARNING(f'Migration 0003 recorded: {migration_recorded}'))
        
        if tables_exist and not migration_recorded:
            self.stdout.write(self.style.WARNING(
                '⚠ Registrar, Guardian, and StudentGuardian tables already exist but migration not recorded'
            ))
            self.stdout.write(self.style.WARNING('⚠ Marking migration 0003 as applied...'))
            
            try:
                # Manually record the migration as applied
                from django.db import connection
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO django_migrations (app, name, applied)
                        VALUES (%s, %s, NOW())
                        ON CONFLICT DO NOTHING
                    """, ['main_app', '0003_alter_customuser_user_type_registrar_guardian_and_more'])
                self.stdout.write(self.style.SUCCESS('✓ Marked migration 0003 as applied'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error recording migration: {str(e)}'))
                raise
        
        # Now run all migrations normally, but catch the specific error
        self.stdout.write(self.style.SUCCESS('Running all migrations...'))
        try:
            call_command('migrate', verbosity=1)
            self.stdout.write(self.style.SUCCESS('✓ All migrations completed successfully'))
        except Exception as e:
            error_msg = str(e)
            # If it's the "relation already exists" error for migration 0003 tables
            if 'main_app_registrar' in error_msg or 'main_app_guardian' in error_msg or 'main_app_studentguardian' in error_msg:
                self.stdout.write(self.style.WARNING('⚠ Tables already exist, creating missing tables and recording migration...'))
                
                # Create the tables that don't exist
                from django.db import connection
                with connection.cursor() as cursor:
                    # Create Guardian table if it doesn't exist
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS main_app_guardian (
                            id SERIAL PRIMARY KEY,
                            admin_id INTEGER NOT NULL UNIQUE REFERENCES main_app_customuser(id) ON DELETE CASCADE,
                            occupation VARCHAR(100),
                            phone_number VARCHAR(20) NOT NULL,
                            relationship_type VARCHAR(20) DEFAULT 'guardian',
                            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
                            updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
                        )
                    """)
                    
                    # Create StudentGuardian table if it doesn't exist
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS main_app_studentguardian (
                            id SERIAL PRIMARY KEY,
                            student_id INTEGER NOT NULL REFERENCES main_app_student(id) ON DELETE CASCADE,
                            guardian_id INTEGER NOT NULL REFERENCES main_app_guardian(id) ON DELETE CASCADE,
                            relationship VARCHAR(50),
                            is_primary BOOLEAN DEFAULT FALSE,
                            can_pickup BOOLEAN DEFAULT TRUE,
                            emergency_contact BOOLEAN DEFAULT FALSE,
                            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
                            updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
                            UNIQUE(student_id, guardian_id)
                        )
                    """)
                    
                    self.stdout.write(self.style.SUCCESS('✓ Created missing tables'))
                
                # Record migration 0003 as applied
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO django_migrations (app, name, applied)
                        VALUES (%s, %s, NOW())
                        ON CONFLICT DO NOTHING
                    """, ['main_app', '0003_alter_customuser_user_type_registrar_guardian_and_more'])
                
                # Try migrate again
                try:
                    call_command('migrate', verbosity=1)
                    self.stdout.write(self.style.SUCCESS('✓ All migrations completed successfully after retry'))
                except Exception as retry_error:
                    self.stdout.write(self.style.ERROR(f'✗ Migration error on retry: {str(retry_error)}'))
                    raise
            else:
                self.stdout.write(self.style.ERROR(f'✗ Migration error: {error_msg}'))
                raise

    def get_existing_tables(self):
        """Get list of existing database tables"""
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT tablename 
                FROM pg_tables 
                WHERE schemaname = 'public'
            """)
            return [row[0] for row in cursor.fetchall()]
    
    def is_migration_recorded(self, app_name, migration_name):
        """Check if a migration is already recorded as applied"""
        recorder = MigrationRecorder(connection)
        applied_migrations = recorder.applied_migrations()
        return (app_name, migration_name) in applied_migrations
