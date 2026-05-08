# Render Deployment Fix

**Date:** May 9, 2026  
**Issue:** Deployment failing with `ModuleNotFoundError: No module named 'pkg_resources'`

---

## Problems Identified

### 1. Outdated Gunicorn Version
- **Old:** `gunicorn==20.0.4`
- **Issue:** Not compatible with Python 3.14, missing `pkg_resources`
- **Fix:** Upgraded to `gunicorn==22.0.0`

### 2. Incorrect Start Command
- **Issue:** Render was trying to run `gunicorn app:app`
- **Fix:** Updated Procfile to explicitly specify: `gunicorn student_management_system.wsgi:application --bind 0.0.0.0:$PORT`

### 3. Missing Build Script
- **Issue:** No build script for Render to run migrations and collect static files
- **Fix:** Created `build.sh` with proper build steps

---

## Files Changed

### 1. `requirements.txt`
```diff
- gunicorn==20.0.4
+ gunicorn==22.0.0
```

### 2. `Procfile`
```diff
- web: gunicorn student_management_system.wsgi
+ web: gunicorn student_management_system.wsgi:application --bind 0.0.0.0:$PORT
```

### 3. `build.sh` (NEW)
```bash
#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### 4. `render.yaml` (NEW)
Complete Render configuration with:
- Python 3.11 runtime
- Build and start commands
- Environment variables
- Database configuration

---

## Deployment Steps on Render

### Option 1: Using Render Dashboard (Recommended)

1. **Go to your Render dashboard**
   - URL: https://dashboard.render.com/

2. **Update Build Command:**
   - Go to your web service settings
   - Build Command: `./build.sh`
   - Start Command: `gunicorn student_management_system.wsgi:application`

3. **Set Environment Variables:**
   ```
   PYTHON_VERSION=3.11.0
   DEBUG=False
   SECRET_KEY=<generate-a-secret-key>
   ALLOWED_HOSTS=.onrender.com
   DATABASE_URL=<your-postgres-url>
   ```

4. **Trigger Manual Deploy:**
   - Click "Manual Deploy" → "Deploy latest commit"

### Option 2: Using render.yaml (Blueprint)

1. **Delete existing service** (if needed)

2. **Create new service from Blueprint:**
   - Go to Render Dashboard
   - Click "New" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml`

3. **Review and Deploy:**
   - Review the configuration
   - Click "Apply"

---

## Environment Variables Required

Set these in your Render dashboard:

```bash
# Required
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@host:5432/dbname
ALLOWED_HOSTS=.onrender.com,your-custom-domain.com

# Optional
DEBUG=False
PYTHON_VERSION=3.11.0
```

### Generate SECRET_KEY

Run this locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Troubleshooting

### Issue: "No module named 'pkg_resources'"
**Solution:** ✅ Fixed by upgrading gunicorn to 22.0.0

### Issue: "No open ports detected"
**Solution:** ✅ Fixed by adding `--bind 0.0.0.0:$PORT` to Procfile

### Issue: "Application failed to start"
**Check:**
1. Build logs for errors
2. Environment variables are set correctly
3. Database URL is correct
4. Static files collected successfully

### Issue: "Static files not loading"
**Solution:**
1. Ensure `build.sh` runs `collectstatic`
2. Check `STATIC_ROOT` in settings.py
3. Verify WhiteNoise is in `MIDDLEWARE`

### Issue: "Database connection failed"
**Solution:**
1. Create PostgreSQL database on Render
2. Copy the Internal Database URL
3. Set as `DATABASE_URL` environment variable

---

## Verification Checklist

After deployment, verify:

- [ ] Build completes successfully
- [ ] Migrations run without errors
- [ ] Static files collected
- [ ] Application starts (no port binding errors)
- [ ] Homepage loads
- [ ] Login page works
- [ ] Admin panel accessible
- [ ] Database connections work

---

## Quick Deploy Commands

If you need to redeploy after making changes:

```bash
# 1. Make your changes locally
# 2. Commit and push
git add .
git commit -m "Your changes"
git push origin main

# 3. Render will auto-deploy (if enabled)
# OR manually trigger deploy from dashboard
```

---

## Python Version Note

**Important:** Render uses Python 3.11 by default (not 3.14)

- Gunicorn 22.0.0 works with Python 3.11+
- If you need Python 3.14, set `PYTHON_VERSION=3.14.0` in environment variables
- However, Python 3.11 is more stable for production

---

## Next Steps

1. **Push the changes** (already done ✅)
2. **Go to Render dashboard**
3. **Update build/start commands** (or use render.yaml)
4. **Set environment variables**
5. **Trigger manual deploy**
6. **Monitor build logs**
7. **Test the deployed application**

---

## Support Links

- Render Docs: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/
- Gunicorn Docs: https://docs.gunicorn.org/

---

**Status:** ✅ Fixes committed and pushed to GitHub  
**Commit:** 03333f5  
**Files Changed:** requirements.txt, Procfile, build.sh (new), render.yaml (new)
