# Production Data Setup Guide

**Date:** May 9, 2026  
**Status:** Deployment Successful ✅

---

## 🎉 Your App is Live!

Your production database is now **empty** except for the admin user that was automatically created during deployment.

---

## 🔐 Initial Admin Access

### Automatic Admin Creation

The deployment automatically created an admin user:

**Credentials:**
- **Email:** `admin@admin.com`
- **Password:** `admin`

**⚠️ IMPORTANT:** Change this password immediately after first login!

---

## 📊 Understanding Your Databases

### Local Database (Development)
- **Type:** SQLite (`db.sqlite3`)
- **Location:** Your computer
- **Data:** All your local test data
- **Purpose:** Development and testing

### Production Database (Render)
- **Type:** PostgreSQL
- **Location:** Render's servers
- **Data:** Currently only has admin user
- **Purpose:** Live production data

**These are completely separate!** Data in one does NOT appear in the other.

---

## 🚀 How to Add Data to Production

### Option 1: Manual Entry (Recommended)

1. **Visit your live app:**
   ```
   https://your-app-name.onrender.com
   ```

2. **Login as admin:**
   - Email: `admin@admin.com`
   - Password: `admin`

3. **Add data through the UI:**
   - **Courses:** Go to "Manage Courses" → "Add Course"
   - **Subjects:** Go to "Manage Subjects" → "Add Subject"
   - **Staff:** Go to "Manage Staff" → "Add Staff"
   - **Students:** Go to "Manage Students" → "Add Student"
   - **Sessions:** Add academic sessions
   - **Timetables:** Create timetables

**Advantages:**
- ✅ Safe and controlled
- ✅ Validates data properly
- ✅ Uses your app's business logic
- ✅ No risk of data corruption

---

### Option 2: Run Seed Script (Advanced)

If you want to add demo data like you did locally, you have two approaches:

#### Approach A: Modify build.sh (Automatic)

**⚠️ Warning:** This will add demo data on EVERY deployment!

1. **Edit `build.sh`** and add:
   ```bash
   # Create demo data (only for testing)
   python seed_demo_data.py
   ```

2. **Commit and push:**
   ```bash
   git add build.sh
   git commit -m "Add demo data seeding"
   git push origin main
   ```

3. **Render will auto-deploy** and run the seed script

**Not recommended for production!** Only use this for demo/staging environments.

---

#### Approach B: One-Time Seed (Better)

Since Render free tier doesn't provide shell access, you'd need to:

1. **Create a special endpoint** (temporary) that runs the seed script
2. **Visit that endpoint once** to seed data
3. **Remove the endpoint** after seeding

**Example:**

Add to `urls.py`:
```python
# TEMPORARY - Remove after seeding!
path('secret-seed-data-xyz/', views.seed_production_data, name='seed_data'),
```

Add to `views.py`:
```python
def seed_production_data(request):
    # Only allow in production once
    if not settings.DEBUG:
        # Run your seed script logic here
        # ...
        return HttpResponse("Data seeded successfully!")
    return HttpResponse("Not allowed")
```

**⚠️ Security Risk:** Remove this endpoint immediately after use!

---

### Option 3: Use Django Admin (Easiest)

1. **Visit:** `https://your-app.onrender.com/admin/`
2. **Login with admin credentials**
3. **Add data through Django admin interface**

**Advantages:**
- ✅ Built-in Django feature
- ✅ No custom code needed
- ✅ Safe and validated

---

## 🎯 Recommended Approach for Production

### Step 1: Login and Change Password
```
1. Visit your app
2. Login as admin@admin.com / admin
3. Go to profile/settings
4. Change password immediately!
```

### Step 2: Create Essential Data
```
1. Create Academic Sessions (e.g., 2024-2025)
2. Create Courses (e.g., Grade 1, Grade 2, etc.)
3. Create Subjects (e.g., Math, English, Science)
```

### Step 3: Add Users
```
1. Add Staff/Teachers
2. Add Students
3. Add Guardians (if needed)
4. Link students to guardians
```

### Step 4: Setup Timetables
```
1. Create time slots
2. Assign subjects to time slots
3. Link teachers to subjects
```

---

## 📋 What Data You Need to Add

### Essential Data (Required):
- [ ] At least one Academic Session
- [ ] At least one Course
- [ ] At least one Subject
- [ ] At least one Staff member
- [ ] At least one Student

### Optional Data:
- [ ] Multiple courses for different grades
- [ ] Multiple subjects per course
- [ ] Timetable entries
- [ ] Attendance records
- [ ] Student results
- [ ] Guardian accounts

---

## 🔄 Syncing Local and Production Data

### Can I copy my local data to production?

**Short answer:** Not easily with the free tier.

**Options:**

1. **Manual recreation** (Recommended)
   - Recreate important data manually in production
   - Ensures data quality and relevance

2. **Database dump/restore** (Advanced)
   - Export from SQLite: `python manage.py dumpdata > data.json`
   - Import to PostgreSQL: `python manage.py loaddata data.json`
   - **Problem:** Requires shell access (not available on free tier)

3. **Use fixtures** (For demo data)
   - Create fixtures in your code
   - Load during deployment
   - Good for demo/staging, not production

---

## ⚠️ Important Notes

### About the Auto-Created Admin:

**What happens on each deployment:**
- The `create_initial_admin` command runs
- It checks if `admin@admin.com` exists
- If it exists: Does nothing (safe)
- If it doesn't exist: Creates it

**This means:**
- ✅ First deployment: Admin is created
- ✅ Subsequent deployments: Admin is NOT recreated
- ✅ Your data is safe on redeployments

### About Data Persistence:

**Your PostgreSQL data is persistent:**
- ✅ Survives app restarts
- ✅ Survives redeployments
- ✅ Survives code updates
- ⚠️ Free tier: Database expires after 90 days (you'll get email warnings)

---

## 🧪 Testing Your Production App

### Test Checklist:

1. **Login as Admin:**
   - [ ] Can login with admin@admin.com
   - [ ] Dashboard loads correctly
   - [ ] Can access all admin features

2. **Create Test Data:**
   - [ ] Create a course
   - [ ] Create a subject
   - [ ] Create a staff member
   - [ ] Create a student

3. **Test User Roles:**
   - [ ] Login as staff
   - [ ] Login as student
   - [ ] Verify permissions work correctly

4. **Test Core Features:**
   - [ ] Attendance tracking
   - [ ] Results management
   - [ ] Timetable viewing
   - [ ] Profile updates

---

## 🔒 Security Best Practices

### After First Login:

1. **Change admin password immediately**
2. **Create a new admin with different email**
3. **Consider disabling the default admin@admin.com**
4. **Use strong passwords for all accounts**
5. **Don't share admin credentials**

### For Production:

1. **Never commit passwords to Git**
2. **Use environment variables for secrets**
3. **Enable HTTPS (Render does this automatically)**
4. **Monitor your app logs regularly**
5. **Keep Django and dependencies updated**

---

## 📊 Monitoring Your Data

### Check Database Usage:

1. **Go to Render Dashboard**
2. **Click on your PostgreSQL database**
3. **View "Metrics" tab**
4. **Monitor:**
   - Storage used (out of 1GB free)
   - Connection count
   - Query performance

### Free Tier Limits:

- **Storage:** 1GB
- **Connections:** 97 concurrent
- **Expires:** After 90 days (renewable)

---

## 🆘 Troubleshooting

### "Admin login not working"
- Verify you're using `admin@admin.com` (not `admin@dilfere.school`)
- Check deployment logs to confirm admin was created
- Try resetting password through Django admin

### "No data showing up"
- Production database is separate from local
- You need to add data manually or through seed script
- Check that you're logged in with correct user type

### "Can't add data"
- Verify you're logged in as admin
- Check user permissions
- Look for errors in browser console

---

## 📝 Summary

**Current State:**
- ✅ App deployed successfully
- ✅ Database connected
- ✅ Admin user created automatically
- ✅ Database is empty (except admin)

**Next Steps:**
1. Login as admin
2. Change password
3. Add your production data manually
4. Test all features
5. Invite real users!

**Remember:** Local data ≠ Production data. They are completely separate!

---

**Your app is live and ready to use! Start adding your production data! 🚀**
