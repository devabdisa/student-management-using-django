"""
Management command to handle migrations intelligently, dealing with existing tables.
Usage: python manage.py smart_migrate
"""
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection


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
        
        if tables_exist:
            self.stdout.write(self.style.WARNING(
                '⚠ Registrar, Guardian, and StudentGuardian tables already exist'
            ))
            self.stdout.write(self.style.WARNING('⚠ Faking migration 0003...'))
            
            try:
                # Fake migration 0003 since tables already exist
                call_command('migrate', 'main_app', '0003', '--fake', verbosity=0)
                self.stdout.write(self.style.SUCCESS('✓ Faked migration 0003'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠ Could not fake migration: {str(e)}'))
        
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
