# Demo Credentials - Dil Fere School Portal

This document contains login credentials for testing different user roles in the system.

---

## 🔐 Test Accounts

### 1. Admin/HOD Account
**Role:** System Administrator  
**Email:** `admin@admin.com`  
**Password:** `admin`  
**Dashboard URL:** `http://127.0.0.1:8000/admin_home`

**What to test:**
- View overall system statistics
- Manage staff (add, edit, delete)
- Manage students (add, edit, delete)
- Manage courses/classes (add, edit, delete)
- Manage subjects (add, edit, delete)
- Manage sessions (academic years)
- View all attendance records
- View all student results
- Approve/reject leave applications
- Manage timetable and time slots
- Send notifications
- View feedback from staff and students

---

### 2. Registrar Account
**Role:** Student Records Manager  
**Email:** `registrar@dilfere.school`  
**Password:** `registrar123`  
**Dashboard URL:** `http://127.0.0.1:8000/registrar_home`

**What to test:**
- View system statistics dashboard
- View all students (read-only)
- View all staff (read-only)
- View all courses and subjects (read-only)
- View attendance records (read-only)
- View student results (read-only)
- View timetable (read-only)
- Update own profile
- View notifications

**Note:** Registrar has read-only access to most data. Cannot add/edit/delete students, staff, or courses.

---

### 3. Guardian/Parent Account
**Role:** Parent/Guardian  
**Email:** `guardian@dilfere.school`  
**Password:** `guardian123`  
**Dashboard URL:** `http://127.0.0.1:8000/guardian_home`

**What to test:**
- View linked children's information
- View children's attendance records
- View children's results
- View children's timetable
- View notifications about children
- Update own profile

**Note:** Guardian must be linked to students to see their data. Use admin account to link guardian to students.

---

### 4. Staff/Teacher Account
**Role:** Teacher  
**Email:** `teacher@dilfere.school`  
**Password:** `teacher123`  
**Dashboard URL:** `http://127.0.0.1:8000/staff_home`

**What to test:**
- View assigned subjects and students
- Take attendance for classes
- Add and update student results
- Apply for leave
- Send feedback to admin
- View own timetable
- View notifications
- Update own profile

**Status:** ✅ Created by seed script

---

### 5. Student Account
**Role:** Student  
**Email:** `student@dilfere.school`  
**Password:** `student123`  
**Dashboard URL:** `http://127.0.0.1:8000/student_home`

**What to test:**
- View own attendance records
- View own results
- View class timetable
- Apply for leave
- Send feedback to admin
- View notifications
- Update own profile

**Status:** ✅ Created by seed script

---

## 🚀 Quick Start Testing

### Step 1: Seed Demo Data (If Not Done)

If you haven't run the seed script yet:

```bash
python seed_demo_data.py
```

This creates all 5 test accounts with sample data.

### Step 2: Start the Server
```bash
cd c:\Users\hp\OneDrive\Desktop\tcbtp\student-management-using-django
.\venv\Scripts\python.exe manage.py runserver
```

### Step 3: Open Browser
Navigate to: `http://127.0.0.1:8000/`

### Step 4: Test Each Role
1. Login with admin credentials
2. Explore admin dashboard and features
3. Logout
4. Login with registrar credentials
5. Explore registrar dashboard (read-only access)
6. Logout
7. Login with teacher credentials
8. Explore staff dashboard and features
9. Logout
10. Login with student credentials
11. Explore student portal
12. Logout
13. Login with guardian credentials
14. Explore guardian dashboard

---

## 📝 Creating Additional Test Accounts

### Using the Seed Script (Recommended)

The seed script (`seed_demo_data.py`) automatically creates all necessary accounts. Just run:

```bash
python seed_demo_data.py
```

### Create Staff Account Manually (via Admin Dashboard)
1. Login as admin
2. Navigate to "Manage Staff" → "Add Staff"
3. Fill in the form:
   - Email: `teacher@dilfere.school`
   - Password: `teacher123`
   - First Name: `John`
   - Last Name: `Teacher`
   - Gender: `Male`
   - Address: `123 School Street`
4. Click "Add Staff"

### Create Student Account (via Admin Dashboard)
1. Login as admin
2. Navigate to "Manage Students" → "Add Student"
3. Fill in the form:
   - Email: `student@dilfere.school`
   - Password: `student123`
   - First Name: `Jane`
   - Last Name: `Student`
   - Gender: `Female`
   - Course: Select a course
   - Session: Select a session
   - Address: `456 Student Avenue`
4. Click "Add Student"

### Create Additional Guardian Account (via Admin Dashboard)
1. Login as admin
2. Navigate to "Manage Guardians" → "Add Guardian"
3. Fill in the form:
   - Email: `parent@dilfere.school`
   - Password: `parent123`
   - First Name: `Mary`
   - Last Name: `Parent`
   - Gender: `Female`
   - Phone: `+1234567890`
   - Address: `789 Parent Road`
4. Click "Add Guardian"
5. Link guardian to student(s) via "Link Guardian to Student"

---

## 🔒 Security Notes

### For Development/Testing
- These are **test credentials** for development and demonstration purposes
- Passwords are intentionally simple for easy testing
- **DO NOT** use these credentials in production

### For Production Deployment
1. **Change all default passwords** immediately
2. Use strong passwords (minimum 12 characters, mixed case, numbers, symbols)
3. Enable two-factor authentication (if implemented)
4. Remove or disable test accounts
5. Create new admin account with secure credentials
6. Set `DEBUG=False` in `.env`
7. Update `ALLOWED_HOSTS` in `.env`
8. Use environment variables for sensitive data
9. Enable HTTPS/SSL
10. Regular security audits

---

## 🆘 Troubleshooting

### Cannot Login
**Problem:** "Invalid email or password"  
**Solution:**
- Verify you're using the correct email and password
- Check if the account exists in the database
- Ensure the server is running
- Clear browser cache and cookies

### Account Not Found
**Problem:** "User does not exist"  
**Solution:**
- Create the account using admin dashboard
- Or use Django shell to create the account manually
- Verify the email address is correct

### Wrong Dashboard
**Problem:** Redirected to wrong dashboard after login  
**Solution:**
- Verify the user type is correct in the database
- Check middleware configuration
- Clear browser cache
- Logout and login again

### Permission Denied
**Problem:** "You don't have permission to access this page"  
**Solution:**
- Verify you're logged in with the correct role
- Check if the URL matches your role's dashboard
- Some features are role-specific (e.g., only admin can add staff)

---

## 📊 User Type Reference

| User Type | Code | Dashboard URL | Access Level |
|-----------|------|---------------|--------------|
| Admin/HOD | 1 | `/admin_home` | Full access |
| Staff/Teacher | 2 | `/staff_home` | Teaching features |
| Student | 3 | `/student_home` | Student portal |
| Registrar | 4 | `/registrar_home` | Read-only data access |
| Guardian | 5 | `/guardian_home` | Children's data only |

---

## 🔄 Resetting Passwords

### Via Django Shell
```bash
python manage.py shell
```

Then in the shell:
```python
from main_app.models import CustomUser

# Reset admin password
user = CustomUser.objects.get(email='admin@admin.com')
user.set_password('new_password')
user.save()
print(f"Password reset for {user.email}")

# Exit
exit()
```

### Via Django Admin
1. Navigate to `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Go to "Users"
4. Select the user
5. Click "Change password"
6. Enter new password
7. Save

---

## 📞 Support

For issues or questions:
- Check the [USER_GUIDE.md](USER_GUIDE.md) for detailed usage instructions
- Review [SETUP.md](SETUP.md) for installation and configuration
- Check [README.md](README.md) for project overview

---

**Last Updated:** May 8, 2026  
**System Version:** 1.0  
**Status:** Production Ready ✅
