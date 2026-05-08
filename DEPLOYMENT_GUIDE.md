# Deployment Guide - Dil Fere School Portal

Complete guide for running, testing, and deploying the Dil Fere School Portal.

---

## 📋 Table of Contents

1. [Quick Start - Local Testing](#quick-start---local-testing)
2. [Free Deployment Options](#free-deployment-options)
3. [Deployment Steps](#deployment-steps)
4. [Post-Deployment](#post-deployment)
5. [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start - Local Testing

### Prerequisites
- Python 3.12+ installed
- Git installed (optional)
- Internet connection

### Step-by-Step Setup

**1. Navigate to Project Directory**
```bash
cd c:\Users\hp\OneDrive\Desktop\tcbtp\student-management-using-django
```

**2. Activate Virtual Environment**
```cmd
venv\Scripts\activate
```

**3. Install Dependencies (if not done)**
```bash
pip install -r requirements.txt
```

**4. Run Migrations**
```bash
python manage.py migrate
```

**5. Seed Demo Data**
```bash
python seed_demo_data.py
```

This creates all 5 test accounts with sample data.

**6. Run Development Server**
```bash
python manage.py runserver
```

**7. Open Browser**
Navigate to: `http://127.0.0.1:8000/`

**8. Login with Demo Accounts**
- Admin: `admin@admin.com` / `admin`
- Registrar: `registrar@dilfere.school` / `registrar123`
- Teacher: `teacher@dilfere.school` / `teacher123`
- Student: `student@dilfere.school` / `student123`
- Guardian: `guardian@dilfere.school` / `guardian123`

---

## 🆓 Free Deployment Options

### Option 1: PythonAnywhere (Recommended for Beginners)

**Pros:**
- ✅ Easiest setup
- ✅ Free tier available (always free)
- ✅ No credit card required
- ✅ Built-in PostgreSQL/MySQL
- ✅ HTTPS included
- ✅ Good for small schools

**Cons:**
- ⚠️ Limited resources on free tier
- ⚠️ Daily quota limits

**Free Tier Limits:**
- 512MB disk space
- 1 web app
- 100,000 hits/day
- MySQL database included

**Best For:** Small schools, testing, demos

---

### Option 2: Render.com

**Pros:**
- ✅ Modern platform
- ✅ Free tier available
- ✅ PostgreSQL included
- ✅ Auto-deploy from Git
- ✅ HTTPS included
- ✅ Good performance

**Cons:**
- ⚠️ Free tier spins down after inactivity (slow first load)
- ⚠️ Requires credit card for verification

**Free Tier Limits:**
- 750 hours/month
- 512MB RAM
- PostgreSQL database (90 days, then expires)

**Best For:** Medium schools, production-ready

---

### Option 3: Railway.app

**Pros:**
- ✅ Very easy setup
- ✅ Free tier available
- ✅ PostgreSQL included
- ✅ Auto-deploy from Git
- ✅ HTTPS included

**Cons:**
- ⚠️ Free tier limited to $5/month credit
- ⚠️ May need to upgrade for continuous use

**Free Tier Limits:**
- $5/month credit
- Sleeps after inactivity

**Best For:** Testing, small deployments

---

### Option 4: Heroku (No Longer Free)

**Note:** Heroku discontinued free tier in November 2022. Now requires paid plans starting at $5/month.

---

## 📦 Deployment Steps

### Deploying to PythonAnywhere (Easiest)

#### Step 1: Create Account
1. Go to [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/)
2. Click "Start running Python online in less than a minute!"
3. Create a free "Beginner" account
4. No credit card required

#### Step 2: Upload Your Code

**Option A: Using Git (Recommended)**
```bash
# In PythonAnywhere Bash console
git clone https://github.com/yourusername/student-management-using-django.git
cd student-management-using-django
```

**Option B: Upload Files**
1. Use "Files" tab to upload your project
2. Upload as ZIP and extract

#### Step 3: Create Virtual Environment
```bash
# In PythonAnywhere Bash console
cd student-management-using-django
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Step 4: Configure Database
```bash
# Create .env file
nano .env
```

Add:
```env
SECRET_KEY=your-very-long-random-secret-key-change-this
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
DATABASE_URL=sqlite:///db.sqlite3
```

Save and exit (Ctrl+X, Y, Enter)

#### Step 5: Run Migrations
```bash
python manage.py migrate
python seed_demo_data.py
python manage.py collectstatic --noinput
```

#### Step 6: Configure Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Choose Python 3.10
5. Set source code directory: `/home/yourusername/student-management-using-django`
6. Set working directory: `/home/yourusername/student-management-using-django`
7. Edit WSGI file:

```python
import os
import sys

path = '/home/yourusername/student-management-using-django'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'student_management_system.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

8. Set virtualenv path: `/home/yourusername/student-management-using-django/venv`
9. Click "Reload" button

#### Step 7: Configure Static Files
In "Web" tab, add static files mapping:
- URL: `/static/`
- Directory: `/home/yourusername/student-management-using-django/static`

#### Step 8: Access Your Site
Visit: `https://yourusername.pythonanywhere.com/`

---

### Deploying to Render.com

#### Step 1: Prepare Your Code

**1. Create `render.yaml` in project root:**
```yaml
services:
  - type: web
    name: dilfere-school-portal
    env: python
    buildCommand: "pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate"
    startCommand: "gunicorn student_management_system.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.12.0
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: False
      - key: DATABASE_URL
        fromDatabase:
          name: dilfere-db
          property: connectionString

databases:
  - name: dilfere-db
    databaseName: dilfere_school
    user: dilfere_user
```

**2. Add `gunicorn` to requirements.txt:**
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

**3. Update `settings.py` for production:**
```python
# Add at the top
import dj_database_url

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Update DATABASES
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Add WhiteNoise for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### Step 2: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/student-management-using-django.git
git push -u origin main
```

#### Step 3: Deploy on Render
1. Go to [https://render.com/](https://render.com/)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your repository
5. Render will auto-detect `render.yaml`
6. Click "Create Web Service"
7. Wait for deployment (5-10 minutes)

#### Step 4: Seed Data
After deployment, go to "Shell" tab and run:
```bash
python seed_demo_data.py
```

#### Step 5: Access Your Site
Visit the URL provided by Render (e.g., `https://dilfere-school-portal.onrender.com`)

---

### Deploying to Railway.app

#### Step 1: Prepare Your Code

**1. Create `railway.json` in project root:**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn student_management_system.wsgi:application",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

**2. Create `Procfile`:**
```
web: gunicorn student_management_system.wsgi:application
release: python manage.py migrate && python manage.py collectstatic --noinput
```

**3. Add `gunicorn` to requirements.txt** (if not already added)

#### Step 2: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/student-management-using-django.git
git push -u origin main
```

#### Step 3: Deploy on Railway
1. Go to [https://railway.app/](https://railway.app/)
2. Sign up with GitHub
3. Click "New Project"
4. Choose "Deploy from GitHub repo"
5. Select your repository
6. Railway will auto-deploy

#### Step 4: Add PostgreSQL
1. Click "New" → "Database" → "Add PostgreSQL"
2. Railway will automatically set `DATABASE_URL`

#### Step 5: Set Environment Variables
In Railway dashboard, add:
- `SECRET_KEY`: (generate a random key)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `your-app.railway.app`

#### Step 6: Seed Data
In Railway dashboard, go to "Settings" → "Deploy" → "Custom Start Command":
```bash
python seed_demo_data.py && gunicorn student_management_system.wsgi:application
```

Or use Railway CLI:
```bash
railway run python seed_demo_data.py
```

#### Step 7: Access Your Site
Visit the URL provided by Railway

---

## 🔒 Post-Deployment

### Security Checklist

**1. Change All Default Passwords**
```bash
python manage.py shell
```
```python
from main_app.models import CustomUser

# Change admin password
admin = CustomUser.objects.get(email='admin@admin.com')
admin.set_password('new_secure_password')
admin.save()

# Repeat for all demo accounts
```

**2. Update Environment Variables**
```env
SECRET_KEY=very-long-random-secret-key-50-characters-minimum
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

**3. Enable HTTPS**
- Most platforms provide HTTPS automatically
- Ensure `SECURE_SSL_REDIRECT = True` in production settings

**4. Set Up Backups**
- Export database regularly
- Use platform's backup features
- Keep local backups

**5. Monitor Usage**
- Check platform dashboard for resource usage
- Monitor error logs
- Set up uptime monitoring

### Performance Optimization

**1. Enable Caching**
```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}
```

**2. Optimize Database Queries**
- Use `select_related()` and `prefetch_related()`
- Add database indexes
- Monitor slow queries

**3. Compress Static Files**
- WhiteNoise handles this automatically
- Ensure `collectstatic` runs on deployment

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "DisallowedHost" Error**
```
Solution: Add your domain to ALLOWED_HOSTS in .env
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

**Issue: Static Files Not Loading**
```
Solution: Run collectstatic
python manage.py collectstatic --noinput
```

**Issue: Database Connection Error**
```
Solution: Check DATABASE_URL in environment variables
Ensure PostgreSQL service is running
```

**Issue: "Bad Request (400)" Error**
```
Solution: Check ALLOWED_HOSTS includes your domain
Ensure DEBUG=False in production
```

**Issue: Slow First Load (Render/Railway)**
```
Solution: Free tiers spin down after inactivity
First request wakes up the server (30-60 seconds)
Consider upgrading to paid tier for always-on
```

### Getting Help

**Platform-Specific Support:**
- PythonAnywhere: [https://help.pythonanywhere.com/](https://help.pythonanywhere.com/)
- Render: [https://render.com/docs](https://render.com/docs)
- Railway: [https://docs.railway.app/](https://docs.railway.app/)

**Project Support:**
- Check [SETUP.md](SETUP.md) for installation issues
- Check [USER_GUIDE.md](USER_GUIDE.md) for usage questions
- Check [CHANGELOG.md](CHANGELOG.md) for version info

---

## 📊 Comparison Table

| Feature | PythonAnywhere | Render.com | Railway.app |
|---------|----------------|------------|-------------|
| **Ease of Setup** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Free Tier** | Always Free | Free (with limits) | $5/month credit |
| **Database** | MySQL/PostgreSQL | PostgreSQL | PostgreSQL |
| **HTTPS** | ✅ Included | ✅ Included | ✅ Included |
| **Custom Domain** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Auto-Deploy** | ❌ Manual | ✅ Git integration | ✅ Git integration |
| **Performance** | Good | Excellent | Excellent |
| **Uptime** | 100% | Spins down | Spins down |
| **Best For** | Beginners | Production | Testing |

---

## 🎯 Recommended Deployment Path

### For Learning/Testing
1. **Start with:** Local development (`python manage.py runserver`)
2. **Then try:** PythonAnywhere (easiest, always free)
3. **Practice:** Deploy to Render or Railway

### For Small School (< 100 users)
1. **Use:** PythonAnywhere free tier
2. **Upgrade to:** PythonAnywhere paid ($5/month) if needed

### For Medium School (100-500 users)
1. **Use:** Render.com or Railway.app paid tier
2. **Database:** PostgreSQL
3. **Monitoring:** Set up error tracking

### For Large School (500+ users)
1. **Use:** DigitalOcean, AWS, or Azure
2. **Database:** Managed PostgreSQL
3. **CDN:** CloudFlare for static files
4. **Monitoring:** Full application monitoring

---

## 📝 Quick Reference Commands

### Local Development
```bash
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Seed demo data
python seed_demo_data.py

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic
```

### Production
```bash
# Check deployment readiness
python manage.py check --deploy

# Create database backup
python manage.py dumpdata > backup.json

# Load database backup
python manage.py loaddata backup.json
```

---

**Last Updated:** May 8, 2026  
**Version:** 1.0  
**Status:** Production Ready ✅
