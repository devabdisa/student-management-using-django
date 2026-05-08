# Student Management System - Quick Setup Guide

## ✅ Setup Complete!

This project has been simplified and is ready to run. All complex features (Email, Firebase, reCAPTCHA) have been disabled.

## 🚀 Quick Start (SQLite - Default)

1. **Activate the virtual environment:**
   ```cmd
   venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```cmd
   pip install -r requirements-local.txt
   ```

3. **Run migrations:**
   ```cmd
   python manage.py migrate
   ```

4. **Create a superuser:**
   ```cmd
   python manage.py createsuperuser --email admin@dilfere.school
   ```

5. **Run the development server:**
   ```cmd
   python manage.py runserver
   ```

6. **Open your browser and visit:**
   ```
   http://127.0.0.1:8000/
   ```

## 🐘 PostgreSQL Setup (Optional)

### Prerequisites
- PostgreSQL installed on your system
- Database created

### Step 1: Install PostgreSQL
**Windows:**
Download from https://www.postgresql.org/download/windows/

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### Step 2: Create Database
```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE dilfere_school;

# Create user (optional)
CREATE USER dilfere_admin WITH PASSWORD 'your_secure_password';

# Grant privileges
GRANT ALL PRIVILEGES ON DATABASE dilfere_school TO dilfere_admin;

# Exit
\q
```

### Step 3: Configure Environment
Update your `.env` file:
```env
DATABASE_URL=postgresql://dilfere_admin:your_secure_password@localhost:5432/dilfere_school
```

Or use individual variables (alternative):
```env
DB_ENGINE=postgresql
DB_NAME=dilfere_school
DB_USER=dilfere_admin
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
```

### Step 4: Install PostgreSQL Driver
```cmd
pip install psycopg2-binary
```

### Step 5: Run Migrations
```cmd
python manage.py migrate
```

### Step 6: Create Superuser
```cmd
python manage.py createsuperuser --email admin@dilfere.school
```

### Step 7: Run Server
```cmd
python manage.py runserver
```

## 🔄 Migrating from SQLite to PostgreSQL

### Method 1: Using dumpdata/loaddata (Recommended)

1. **Export data from SQLite:**
   ```cmd
   python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission > data_backup.json
   ```

2. **Switch to PostgreSQL:**
   Update `.env` with PostgreSQL DATABASE_URL

3. **Run migrations on PostgreSQL:**
   ```cmd
   python manage.py migrate
   ```

4. **Import data:**
   ```cmd
   python manage.py loaddata data_backup.json
   ```

### Method 2: Using pgloader (Advanced)

1. **Install pgloader:**
   ```bash
   # macOS
   brew install pgloader
   
   # Ubuntu/Debian
   sudo apt install pgloader
   ```

2. **Create migration script (migrate.load):**
   ```
   LOAD DATABASE
        FROM sqlite://db.sqlite3
        INTO postgresql://user:password@localhost/dilfere_school
   
   WITH include drop, create tables, create indexes, reset sequences
   
   SET work_mem to '16MB', maintenance_work_mem to '512 MB';
   ```

3. **Run migration:**
   ```bash
   pgloader migrate.load
   ```

## 🔐 Login Credentials

**Admin/HOD Account:**
- Email: `admin@admin.com`
- Password: `admin`

## 📋 What's Included

- ✅ Student Management
- ✅ Staff Management
- ✅ Course Management
- ✅ Subject Management
- ✅ Attendance Tracking
- ✅ Leave Applications
- ✅ Feedback System
- ✅ Student Results
- ✅ In-app Notifications (database only)

## 🚫 What's Disabled (Simplified)

- ❌ Email notifications (uses console backend)
- ❌ Firebase push notifications
- ❌ Google reCAPTCHA

## 📁 Project Structure

- **Database:** SQLite (default) or PostgreSQL (optional)
- **Django Version:** 4.2.17 LTS
- **Python Version:** 3.13+

## 🛠️ Useful Commands

### Database Management

**Create migrations after model changes:**
```cmd
python manage.py makemigrations
```

**Apply migrations:**
```cmd
python manage.py migrate
```

**Show migration status:**
```cmd
python manage.py showmigrations
```

**Rollback migration:**
```cmd
python manage.py migrate main_app 0001  # Rollback to specific migration
```

### User Management

**Create superuser:**
```cmd
python manage.py createsuperuser --email your@email.com
```

**Create Registrar user (via Django shell):**
```cmd
python manage.py shell
```
Then in the shell:
```python
from main_app.models import CustomUser, Registrar

# Create Registrar user
user = CustomUser.objects.create_user(
    email='registrar@dilfere.school',
    password='registrar123',
    first_name='John',
    last_name='Registrar',
    user_type='4',
    gender='M',
    address='School Office'
)
print(f"Registrar created: {user.email}")
exit()
```

**Change user password:**
```cmd
python manage.py changepassword user@email.com
```

### Development

**Run development server:**
```cmd
python manage.py runserver
```

**Run on different port:**
```cmd
python manage.py runserver 8080
```

**Run on all interfaces:**
```cmd
python manage.py runserver 0.0.0.0:8000
```

**Check for issues:**
```cmd
python manage.py check
```

**Check deployment readiness:**
```cmd
python manage.py check --deploy
```

### Static Files

**Collect static files:**
```cmd
python manage.py collectstatic
```

**Clear collected static files:**
```cmd
python manage.py collectstatic --clear --noinput
```

### Database Shell

**Open Django shell:**
```cmd
python manage.py shell
```

**Open database shell:**
```cmd
python manage.py dbshell
```

### Data Management

**Export all data:**
```cmd
python manage.py dumpdata > backup.json
```

**Export specific app:**
```cmd
python manage.py dumpdata main_app > main_app_backup.json
```

**Import data:**
```cmd
python manage.py loaddata backup.json
```

**Flush database (delete all data):**
```cmd
python manage.py flush
```

## 🔧 Troubleshooting

### PostgreSQL Connection Issues

**Error: "could not connect to server"**
- Check if PostgreSQL is running: `pg_isready`
- Start PostgreSQL service
- Verify connection details in `.env`

**Error: "FATAL: database does not exist"**
- Create the database: `createdb dilfere_school`

**Error: "FATAL: password authentication failed"**
- Check username and password in `.env`
- Reset password: `ALTER USER username WITH PASSWORD 'newpassword';`

### Migration Issues

**Error: "No migrations to apply"**
- Run `python manage.py makemigrations` first

**Error: "Migration is already applied"**
- Use `python manage.py migrate --fake` to mark as applied without running

**Error: "Conflicting migrations detected"**
- Delete migration files (except `__init__.py`)
- Run `python manage.py makemigrations` again

### Static Files Issues

**Static files not loading:**
- Run `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` in settings
- Ensure `DEBUG=True` for development

## 📝 Environment Variables

### Required Variables
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Optional Variables
```env
# PostgreSQL Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Or SQLite (default if DATABASE_URL not set)
DATABASE_URL=sqlite:///db.sqlite3
```

## 🎯 Next Steps

1. Log in as admin
2. Create a Session (Academic Year)
3. Add Courses (Grades/Classes)
4. Add Staff members
5. Add Subjects
6. Add Students
7. Start managing attendance and results!

## 📚 User Type Reference

For future development, the system uses these user types:

| Type | Role | Status |
|------|------|--------|
| 1 | Admin/HOD | ✅ Implemented |
| 2 | Staff/Teacher | ✅ Implemented |
| 3 | Student | ✅ Implemented |
| 4 | Registrar | ✅ Implemented |
| 5 | Parent/Guardian | 🔜 Planned |

## 🆘 Getting Help

- Check the [CHANGES.md](CHANGES.md) file for recent modifications
- Review [ANALYSIS_AND_IMPLEMENTATION_PLAN.md](ANALYSIS_AND_IMPLEMENTATION_PLAN.md) for detailed technical documentation
- Open an issue on GitHub for bugs or feature requests

Enjoy your Student Management System! 🎓
