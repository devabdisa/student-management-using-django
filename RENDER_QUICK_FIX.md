# Render Deployment Quick Fix

**Issue:** `ModuleNotFoundError: No module named 'app'`  
**Cause:** Render is using default command `gunicorn app:app` instead of the correct Django WSGI command

---

## 🚨 IMMEDIATE FIX (Do This Now!)

### Go to Render Dashboard and Update Start Command

1. **Visit:** https://dashboard.render.com/

2. **Select your web service** (the one that's failing)

3. **Click "Settings"** (left sidebar)

4. **Scroll to "Start Command"**

5. **Replace with:**
   ```
   gunicorn student_management_system.wsgi:application
   ```

6. **Click "Save Changes"**

7. **Scroll to "Build Command"**

8. **Set to:**
   ```
   ./build.sh
   ```

9. **Click "Save Changes"**

10. **Go to "Manual Deploy"** section

11. **Click "Deploy latest commit"**

---

## ✅ What Should Happen

After updating the start command, you should see:
```
==> Running 'gunicorn student_management_system.wsgi:application'
[INFO] Starting gunicorn 22.0.0
[INFO] Listening at: http://0.0.0.0:10000
[INFO] Using worker: sync
[INFO] Booting worker with pid: 123
```

---

## 🔑 Required Environment Variables

Make sure these are set in the "Environment" tab:

### Required:
```
SECRET_KEY=<generate-a-long-random-string>
DATABASE_URL=<your-postgres-connection-string>
```

### Recommended:
```
DEBUG=False
ALLOWED_HOSTS=.onrender.com
PYTHON_VERSION=3.11.0
```

### Generate SECRET_KEY:
Run this locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📋 Complete Settings Checklist

### Build & Deploy Tab:
- ✅ **Build Command:** `./build.sh`
- ✅ **Start Command:** `gunicorn student_management_system.wsgi:application`
- ✅ **Branch:** `main`

### Environment Tab:
- ✅ **SECRET_KEY** - Set to a random string
- ✅ **DATABASE_URL** - Set to your PostgreSQL URL
- ✅ **DEBUG** - Set to `False`
- ✅ **ALLOWED_HOSTS** - Set to `.onrender.com`

---

## 🗄️ Database Setup

If you haven't created a PostgreSQL database yet:

1. **In Render Dashboard**, click "New" → "PostgreSQL"
2. **Name:** `dil-fere-school-db`
3. **Database:** `dil_fere_school`
4. **User:** `dil_fere_user`
5. **Region:** Same as your web service
6. **Plan:** Free
7. Click "Create Database"
8. **Copy the "Internal Database URL"**
9. **Go back to your web service** → Environment tab
10. **Set DATABASE_URL** to the copied URL

---

## 🔄 Alternative: Use Blueprint (render.yaml)

If manual configuration doesn't work, try using Blueprint:

1. **Delete your current web service** (if it exists)
2. **In Render Dashboard**, click "New" → "Blueprint"
3. **Connect your GitHub repository**
4. **Render will detect `render.yaml`** automatically
5. **Review the configuration**
6. **Click "Apply"**

The `render.yaml` file in your repo has all the correct settings.

---

## 🐛 Troubleshooting

### Still seeing "gunicorn app:app"?
- Render might be caching the old command
- Try: Settings → "Clear build cache" → Manual Deploy

### Build succeeds but app won't start?
- Check Environment variables are set
- Check DATABASE_URL is correct
- Check SECRET_KEY is set

### "No module named 'student_management_system'"?
- Make sure build.sh is executable: `chmod +x build.sh`
- Check that all files are pushed to GitHub

### Database connection errors?
- Verify DATABASE_URL is the **Internal Database URL** (not External)
- Make sure the database is in the same region as your web service

---

## 📝 Summary

**The Problem:**
- Render is using `gunicorn app:app` (wrong)
- Should be using `gunicorn student_management_system.wsgi:application` (correct)

**The Solution:**
- Manually set the Start Command in Render dashboard
- OR use Blueprint deployment with render.yaml

**After Fix:**
- Build will succeed ✅
- App will start ✅
- You'll see "Listening at: http://0.0.0.0:10000" ✅

---

**Need Help?** Check `RENDER_DEPLOYMENT_FIX.md` for more detailed troubleshooting.
