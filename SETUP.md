# Setup Guide - Dil Fere School Portal

Complete installation and configuration guide for the Dil Fere School Portal.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start (SQLite)](#quick-start-sqlite)
3. [PostgreSQL Setup](#postgresql-setup)
4. [Environment Configuration](#environment-configuration)
5. [Database Migration](#database-migration)
6. [Creating Users](#creating-users)
7. [Running the Server](#running-the-server)
8. [Useful Commands](#useful-commands)
9. [Troubleshooting](#troubleshooting)

---

## 📦 Prerequisites

### Required Software

- **Python 3.12 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (included with Python)
- **Git** - [Download Git](https://git-scm.com/)

### Optional Software

- **PostgreSQL** - For production deployment
- **Code Editor** - VS Code, PyCharm, or similar

### System Requirements

- **OS:** Windows, macOS, or Linux
- **RAM:** 2GB minimum, 4GB recommended
- **Disk Space:** 500MB minimum

---

## 🚀 Quick Start (SQLite)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/student-management-using-django.git
cd student-management-using-django
```

### Step 2: Create Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

Edit `.env` file and set your `SECRET_KEY`:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Step 5: Run Migrations

```bash
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser --email admin@dilfere.school
```

Enter a password when prompted.

### Step 7: Run Development Server

```bash
python manage.py runserver
```

### Step 8: Access the Application

Open your browser and navigate to: `http://127.0.0.1:8000/`

**Login with:**
- Email: `admin@dilfere.school` (or the email you used)
- Password: (the password you set)

---

## 🐘 PostgreSQL Setup

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

---

## ⚙️ Environment Configuration

### Required Variables

Create a `.env` file in the project root with these variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database (SQLite - Default)
# No configuration needed for SQLite

# Database (PostgreSQL - Optional)
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### Generating SECRET_KEY

**Option 1: Using Python**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Option 2: Using Django Shell**
```bash
python manage.py shell
```
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

### Production Settings

For production deployment, update `.env`:

```env
SECRET_KEY=your-very-long-random-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

---

## 🗄️ Database Migration

### Initial Migration

After setting up your database (SQLite or PostgreSQL), run:

```bash
python manage.py migrate
```

This creates all necessary database tables.

### After Model Changes

If you modify models in `main_app/models.py`:

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Check Migration Status

```bash
python manage.py showmigrations
```

### Rollback Migration

```bash
# Rollback to specific migration
python manage.py migrate main_app 0003

# Rollback all migrations for an app
python manage.py migrate main_app zero
```

---

## 👤 Creating Users

### Create Admin/Superuser

```bash
python manage.py createsuperuser --email admin@dilfere.school
```

### Create Registrar (via Django Shell)

```bash
python manage.py shell
```

```python
from main_app.models import CustomUser

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

### Create Guardian (via Django Shell)

```bash
python manage.py shell
```

```python
from main_app.models import CustomUser

user = CustomUser.objects.create_user(
    email='guardian@dilfere.school',
    password='guardian123',
    first_name='Jane',
    last_name='Guardian',
    user_type='5',
    gender='F',
    address='123 Parent Street'
)
print(f"Guardian created: {user.email}")
exit()
```

### Create Staff and Students

Use the admin dashboard to create staff and students:

1. Login as admin
2. Navigate to "Manage Staff" or "Manage Students"
3. Click "Add Staff" or "Add Student"
4. Fill in the form and submit

---

## 🚀 Running the Server

### Development Server

```bash
python manage.py runserver
```

Access at: `http://127.0.0.1:8000/`

### Custom Port

```bash
python manage.py runserver 8080
```

Access at: `http://127.0.0.1:8080/`

### All Network Interfaces

```bash
python manage.py runserver 0.0.0.0:8000
```

Access from other devices on your network at: `http://your-ip:8000/`

### Production Server

For production, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn student_management_system.wsgi:application --bind 0.0.0.0:8000
```

---

## 📁 Project Structure

```
student-management-using-django/
├── main_app/                   # Main application
│   ├── migrations/             # Database migrations
│   ├── static/                 # Static files (CSS, JS, images)
│   ├── templates/              # HTML templates
│   ├── templatetags/           # Custom template tags
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── hod_views.py            # Admin views
│   ├── staff_views.py          # Staff views
│   ├── student_views.py        # Student views
│   ├── registrar_views.py      # Registrar views
│   ├── guardian_views.py       # Guardian views
│   ├── forms.py                # Django forms
│   ├── urls.py                 # URL routing
│   └── middleware.py           # Custom middleware
├── student_management_system/  # Project settings
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Root URL configuration
│   └── wsgi.py                 # WSGI configuration
├── static/                     # Collected static files
├── venv/                       # Virtual environment
├── .env                        # Environment variables
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview
├── SETUP.md                    # This file
├── USER_GUIDE.md               # User documentation
├── DEMO_CREDENTIALS.md         # Test accounts
└── CHANGELOG.md                # Version history
```

---

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
