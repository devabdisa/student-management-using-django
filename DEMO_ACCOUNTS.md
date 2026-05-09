# 🔐 Demo Accounts & Credentials

**Auto-Generated Demo Data**  
**All passwords are simple for demo purposes**

---

## 👨‍💼 ADMIN ACCOUNT

**Email:** `admin@school.com`  
**Password:** `admin123`

**Access:**
- Full system access
- Manage all users
- Manage courses, subjects, timetables
- View all reports

---

## 👨‍🏫 TEACHER ACCOUNTS

### Teacher 1 - John Smith
**Email:** `teacher1@school.com`  
**Password:** `teacher123`  
**Course:** Grade 1  
**Subjects:** Mathematics, English

### Teacher 2 - Sarah Johnson
**Email:** `teacher2@school.com`  
**Password:** `teacher123`  
**Course:** Grade 2  
**Subjects:** Science, History

### Teacher 3 - Michael Brown
**Email:** `teacher3@school.com`  
**Password:** `teacher123`  
**Course:** Grade 3  
**Subjects:** Geography

**Access:**
- Mark attendance
- Enter student results
- View assigned students
- Manage class timetable

---

## 👨‍🎓 STUDENT ACCOUNTS

### Student 1 - Alice Williams
**Email:** `student1@school.com`  
**Password:** `student123`  
**Course:** Grade 1  
**Guardian:** Robert Williams (parent1@school.com)

### Student 2 - Bob Davis
**Email:** `student2@school.com`  
**Password:** `student123`  
**Course:** Grade 1  
**Guardian:** Linda Davis (parent2@school.com)

### Student 3 - Charlie Miller
**Email:** `student3@school.com`  
**Password:** `student123`  
**Course:** Grade 2  
**Guardian:** James Miller (parent3@school.com)

### Student 4 - Diana Wilson
**Email:** `student4@school.com`  
**Password:** `student123`  
**Course:** Grade 2

### Student 5 - Emma Moore
**Email:** `student5@school.com`  
**Password:** `student123`  
**Course:** Grade 3

**Access:**
- View own attendance
- View own results
- View timetable
- Update profile

---

## 👨‍👩‍👧 PARENT/GUARDIAN ACCOUNTS

### Parent 1 - Robert Williams
**Email:** `parent1@school.com`  
**Password:** `parent123`  
**Children:** Alice Williams (student1@school.com)  
**Relationship:** Father

### Parent 2 - Linda Davis
**Email:** `parent2@school.com`  
**Password:** `parent123`  
**Children:** Bob Davis (student2@school.com)  
**Relationship:** Mother

### Parent 3 - James Miller
**Email:** `parent3@school.com`  
**Password:** `parent123`  
**Children:** Charlie Miller (student3@school.com)  
**Relationship:** Father

**Access:**
- View children's attendance
- View children's results
- View children's timetable
- Receive notifications

---

## 📚 DEMO DATA INCLUDED

### Courses (5):
- Grade 1
- Grade 2
- Grade 3
- Grade 4
- Grade 5

### Subjects (5):
- Mathematics (Grade 1)
- English (Grade 1)
- Science (Grade 2)
- History (Grade 2)
- Geography (Grade 3)

### Academic Session:
- Current Year to Next Year

### Timetable:
- Sample schedule for all subjects
- Monday to Friday
- 08:00 - 12:00

---

## 🔄 How Demo Data is Created

### Automatic Seeding:
The demo data is automatically created during deployment through the `seed_demo_data` management command.

### Safe Re-runs:
- The command checks if data already exists
- Won't create duplicates
- Safe to run multiple times

### Manual Seeding:
If you need to seed data manually:
```bash
python manage.py seed_demo_data
```

---

## ⚠️ SECURITY WARNING

### For Demo/Testing Only!

These credentials are **intentionally simple** for demo purposes:
- ✅ Easy to remember
- ✅ Quick to test
- ❌ NOT secure for production

### For Production Use:

1. **Change all passwords immediately**
2. **Use strong, unique passwords**
3. **Enable two-factor authentication (if available)**
4. **Delete demo accounts**
5. **Create real user accounts**

---

## 🧪 Testing Scenarios

### Test Admin Functions:
1. Login as `admin@school.com`
2. Create a new course
3. Add a new teacher
4. Assign subjects to teachers

### Test Teacher Functions:
1. Login as `teacher1@school.com`
2. Mark attendance for students
3. Enter test results
4. View class timetable

### Test Student Functions:
1. Login as `student1@school.com`
2. View attendance record
3. Check results
4. View timetable

### Test Parent Functions:
1. Login as `parent1@school.com`
2. View child's attendance
3. Check child's results
4. View child's timetable

---

## 📊 Quick Reference Table

| Role | Email | Password | Name |
|------|-------|----------|------|
| Admin | admin@school.com | admin123 | Admin User |
| Teacher | teacher1@school.com | teacher123 | John Smith |
| Teacher | teacher2@school.com | teacher123 | Sarah Johnson |
| Teacher | teacher3@school.com | teacher123 | Michael Brown |
| Student | student1@school.com | student123 | Alice Williams |
| Student | student2@school.com | student123 | Bob Davis |
| Student | student3@school.com | student123 | Charlie Miller |
| Student | student4@school.com | student123 | Diana Wilson |
| Student | student5@school.com | student123 | Emma Moore |
| Parent | parent1@school.com | parent123 | Robert Williams |
| Parent | parent2@school.com | parent123 | Linda Davis |
| Parent | parent3@school.com | parent123 | James Miller |

---

## 🎯 Common Login Patterns

**All emails follow this pattern:**
- Admin: `admin@school.com`
- Teachers: `teacher[1-3]@school.com`
- Students: `student[1-5]@school.com`
- Parents: `parent[1-3]@school.com`

**All passwords follow this pattern:**
- Admin: `admin123`
- Teachers: `teacher123`
- Students: `student123`
- Parents: `parent123`

**Easy to remember!** 🎉

---

## 📝 Notes

- All accounts are created automatically on first deployment
- Data persists across redeployments
- Safe to run seed command multiple times
- No duplicate data will be created

---

**Ready to test your app with these demo accounts!** 🚀
