"""
Management command to create initial admin user for production deployment.
Usage: python manage.py create_initial_admin
"""
from django.core.management.base import BaseCommand
from main_app.models import CustomUser, Admin


class Command(BaseCommand):
    help = 'Creates initial admin user if it does not exist'

    def handle(self, *args, **kwargs):
        email = 'admin@admin.com'
        password = 'admin'
        
        # Check if admin already exists
        if CustomUser.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'Admin user {email} already exists!'))
            return
        
        try:
            # Create admin user
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                user_type=1,
                first_name='Admin',
                last_name='User'
            )
            user.is_staff = True
            user.is_superuser = True
            user.save()
            
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin user: {email}'))
            self.stdout.write(self.style.SUCCESS(f'Password: {password}'))
            self.stdout.write(self.style.WARNING('⚠️  IMPORTANT: Change this password after first login!'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating admin user: {str(e)}'))
