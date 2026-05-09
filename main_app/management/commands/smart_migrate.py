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
        
        # Check which tables already exist
        existing_tables = self.get_existing_tables()
        
        # Tables that migration 0003 creates
        migration_0003_tables = ['main_app_registrar', 'main_app_guardian', 'main_app_studentguardian']
        
        # Check if migration 0003 tables already exist
        tables_exist = all(table in existing_tables for table in migration_0003_tables)
        
        # Check if migration 0003 is already recorded
        migration_recorded = self.is_migration_recorded('main_app', '0003_alter_customuser_user_type_registrar_guardian_and_more')
        
        if tables_exist and not migration_recorded:
            self.stdout.write(self.style.WARNING(
                '⚠ Registrar, Guardian, and StudentGuardian tables already exist but migration not recorded'
            ))
            self.stdout.write(self.style.WARNING('⚠ Marking migration 0003 as applied...'))
            
            try:
                # Manually record the migration as applied
                recorder = MigrationRecorder(connection)
                recorder.record_applied('main_app', '0003_alter_customuser_user_type_registrar_guardian_and_more')
                self.stdout.write(self.style.SUCCESS('✓ Marked migration 0003 as applied'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error recording migration: {str(e)}'))
                raise
        
        # Now run all migrations normally
        self.stdout.write(self.style.SUCCESS('Running all migrations...'))
        try:
            call_command('migrate', verbosity=1)
            self.stdout.write(self.style.SUCCESS('✓ All migrations completed successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Migration error: {str(e)}'))
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
