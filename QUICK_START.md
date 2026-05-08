# Quick Start Guide - Run & Test in 5 Minutes

**Goal:** Get the Dil Fere School Portal running on your computer in 5 minutes.

---

## ✅ Prerequisites Check

You already have:
- ✅ Python installed
- ✅ Virtual environment created
- ✅ Dependencies installed
- ✅ Database migrated
- ✅ System check passed (0 issues)

---

## 🚀 Step 1: Start the Server (30 seconds)

Open your terminal in the project folder and run:

```bash
# Activate virtual environment
venv\Scripts\activate

# Start the server
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**✅ Server is running!**

---

## 🔐 Step 2: Login and Test (4 minutes)

### Open Your Browser

Navigate to: **http://127.0.0.1:8000/**

---

### Test 1: Admin Account (1 minute)

**Login with:**
- Email: `admin@admin.com`
- Password: `admin`

**What to test:**
1. ✅ Dashboard loads with 4 stat cards
2. ✅ Click "Manage Students" - see student list
3. ✅ Click "Manage Staff" - see staff list
4. ✅ Click "Manage Courses" - see courses
5. ✅ Click "Manage Timetable" - see timetable
6. ✅ Check sidebar navigation works

**Logout:** Click your name → Logout

---

### Test 2: Registrar Account (1 minute)

**Login with:**
- Email: `registrar@dilfere.school`
- Password: `registrar123`

**What to test:**
1. ✅ Dashboard loads with 8 stat cards
2. ✅ Click "View Students" - see student list (read-only)
3. ✅ Click "View Staff" - see staff list (read-only)
4. ✅ Notice: No "Add" or "Delete" buttons (read-only access)

**Logout:** Click your name → Logout

---

### Test 3: Guardian Account (1 minute)

**Login with:**
- Email: `guardian@dilfere.school`
- Password: `guardian123`

**What to test:**
1. ✅ Dashboard loads with "My Children" card
2. ✅ See children overview (if any linked)
3. ✅ Check sidebar navigation

**Logout:** Click your name → Logout

---

### Test 4: Create Staff Account (1 minute)

**Login as Admin again:**
- Email: `admin@admin.com`
- Password: `admin`

**Create a teacher:**
1. Click **"Manage Staff"** → **"Add Staff"**
2. Fill in:
   - Email: `teacher@dilfere.school`
   - Password: `teacher123`
   - First Name: `John`
   - Last Name: `Teacher`
   - Gender: `Male`
   - Address: `123 School Street`
3. Click **"Add Staff"**

**Test the new account:**
1. Logout
2. Login with: `teacher@dilfere.school` / `teacher123`
3. ✅ Staff dashboard loads
4. ✅ See attendance and results features

---

### Test 5: Create Student Account (1 minute)

**Login as Admin:**
- Email: `admin@admin.com`
- Password: `admin`

**First, create a Course (if none exists):**
1. Click **"Manage Courses"** → **"Add Course"**
2. Enter: `Grade 1`
3. Click **"Add Course"**

**Then create a student:**
1. Click **"Manage Students"** → **"Add Student"**
2. Fill in:
   - Email: `student@dilfere.school`
   - Password: `student123`
   - First Name: `Jane`
   - Last Name: `Student`
   - Gender: `Female`
   - Course: Select `Grade 1`
   - Session: Select available session (or create one first)
   - Address: `456 Student Avenue`
3. Click **"Add Student"**

**Test the new account:**
1. Logout
2. Login with: `student@dilfere.school` / `student123`
3. ✅ Student dashboard loads
4. ✅ See attendance and results view

---

## ✅ Testing Complete!

You've successfully tested all 5 user roles:
- ✅ Admin/HOD
- ✅ Registrar
- ✅ Staff/Teacher
- ✅ Student
- ✅ Guardian

---

## 🛑 Stop the Server

Press `CTRL + C` in the terminal to stop the server.

---

## 🔄 Run Again Later

Whenever you want to run the server again:

```bash
# Navigate to project folder
cd c:\Users\hp\OneDrive\Desktop\tcbtp\student-management-using-django

# Activate virtual environment
venv\Scripts\activate

# Start server
python manage.py runserver
```

---

## 🎯 Next Steps

Now that you've tested locally, you can:

1. **Explore Features** - See [USER_GUIDE.md](USER_GUIDE.md)
2. **Deploy Online** - See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
3. **Customize** - Modify templates, add features
4. **Add Data** - Add more students, staff, courses

---

## 🆘 Troubleshooting

### Server won't start
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Use different port
python manage.py runserver 8080
```

### Can't login
- Verify email and password are correct
- Check if account exists in database
- Try creating a new superuser:
  ```bash
  python manage.py createsuperuser --email test@test.com
  ```

### Page not loading
- Refresh browser (F5)
- Clear browser cache
- Try different browser
- Check terminal for errors

---

**Status:** ✅ Ready to Run  
**Time to Start:** 30 seconds  
**Time to Test:** 4 minutes  
**Total Time:** 5 minutes
