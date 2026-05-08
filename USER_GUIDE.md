# User Guide - Dil Fere School Portal

Complete guide for using the Dil Fere School Portal across all user roles.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Admin/HOD Guide](#adminhod-guide)
3. [Registrar Guide](#registrar-guide)
4. [Staff/Teacher Guide](#staffteacher-guide)
5. [Student Guide](#student-guide)
6. [Parent/Guardian Guide](#parentguardian-guide)
7. [Common Features](#common-features)
8. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Accessing the System

1. **Open your web browser** (Chrome, Firefox, Edge, or Safari)
2. **Navigate to:** `http://127.0.0.1:8000/` (or your school's URL)
3. **Enter your credentials:**
   - Email address
   - Password
4. **Click "Login"**

### First Time Login

After your first login:
1. You'll be redirected to your role-specific dashboard
2. Update your profile information
3. Change your password (recommended)
4. Explore the navigation menu

### Logging Out

- Click your name/profile in the top right corner
- Select "Logout"
- Or click the "Logout" link in the sidebar

---

## Admin/HOD Guide

**Dashboard URL:** `/admin_home`  
**Access Level:** Full system access

### Dashboard Overview

The admin dashboard displays:
- **Total Students** - Number of enrolled students
- **Total Staff** - Number of teaching staff
- **Total Classes** - Number of courses/grades
- **Total Subjects** - Number of subjects offered
- **Charts** - Visual analytics of system data

### Main Responsibilities

#### 1. Manage Sessions (Academic Years)

**Purpose:** Define academic years for the school

**Steps:**
1. Navigate to **"Manage Sessions"** in the sidebar
2. Click **"Add Session"**
3. Enter session details:
   - Start Year (e.g., 2026)
   - End Year (e.g., 2027)
4. Click **"Add Session"**

**Best Practice:** Create sessions at the beginning of each academic year.

---

#### 2. Manage Courses/Classes

**Purpose:** Define grade levels or classes (e.g., Grade 1, Grade 2)

**Steps to Add Course:**
1. Navigate to **"Manage Courses"**
2. Click **"Add Course"**
3. Enter course name (e.g., "Grade 1", "Primary 3")
4. Click **"Add Course"**

**Steps to Edit Course:**
1. Navigate to **"Manage Courses"**
2. Find the course in the table
3. Click **"Edit"**
4. Update course name
5. Click **"Update Course"**

**Steps to Delete Course:**
1. Navigate to **"Manage Courses"**
2. Find the course in the table
3. Click **"Delete"**
4. Confirm deletion

**⚠️ Warning:** Deleting a course will affect all students and subjects linked to it.

---

#### 3. Manage Subjects

**Purpose:** Define subjects taught in the school

**Steps to Add Subject:**
1. Navigate to **"Manage Subjects"**
2. Click **"Add Subject"**
3. Enter subject details:
   - Subject Name (e.g., "Mathematics", "English")
   - Select Course (grade level)
   - Select Staff (teacher assigned)
4. Click **"Add Subject"**

**Steps to Edit Subject:**
1. Navigate to **"Manage Subjects"**
2. Find the subject in the table
3. Click **"Edit"**
4. Update subject details
5. Click **"Update Subject"**

**Best Practice:** Assign subjects to staff members who specialize in those areas.

---

#### 4. Manage Staff

**Purpose:** Add and manage teaching staff accounts

**Steps to Add Staff:**
1. Navigate to **"Manage Staff"**
2. Click **"Add Staff"**
3. Fill in the form:
   - **Email** (must be unique)
   - **Password**
   - **First Name**
   - **Last Name**
   - **Gender**
   - **Date of Birth**
   - **Address**
   - **Profile Picture** (optional)
4. Click **"Add Staff"**

**Steps to Edit Staff:**
1. Navigate to **"Manage Staff"**
2. Find the staff member in the table
3. Click **"Edit"**
4. Update staff details
5. Click **"Update Staff"**

**Steps to Delete Staff:**
1. Navigate to **"Manage Staff"**
2. Find the staff member
3. Click **"Delete"**
4. Confirm deletion

**⚠️ Warning:** Deleting staff will affect subjects assigned to them.

---

#### 5. Manage Students

**Purpose:** Add and manage student accounts

**Steps to Add Student:**
1. Navigate to **"Manage Students"**
2. Click **"Add Student"**
3. Fill in the form:
   - **Email** (must be unique)
   - **Password**
   - **First Name**
   - **Last Name**
   - **Gender**
   - **Date of Birth**
   - **Course** (grade level)
   - **Session** (academic year)
   - **Address**
   - **Profile Picture** (optional)
4. Click **"Add Student"**

**Steps to Edit Student:**
1. Navigate to **"Manage Students"**
2. Find the student in the table
3. Click **"Edit"**
4. Update student details
5. Click **"Update Student"**

**Steps to Delete Student:**
1. Navigate to **"Manage Students"**
2. Find the student
3. Click **"Delete"**
4. Confirm deletion

---

#### 6. Manage Guardians

**Purpose:** Add and manage parent/guardian accounts

**Steps to Add Guardian:**
1. Navigate to **"Manage Guardians"**
2. Click **"Add Guardian"**
3. Fill in the form:
   - **Email** (must be unique)
   - **Password**
   - **First Name**
   - **Last Name**
   - **Gender**
   - **Phone Number**
   - **Address**
4. Click **"Add Guardian"**

**Steps to Link Guardian to Student:**
1. Navigate to **"Link Guardian to Student"**
2. Select **Guardian** from dropdown
3. Select **Student** from dropdown
4. Select **Relationship Type** (Father, Mother, Guardian, Other)
5. Check **"Is Primary Contact"** if applicable
6. Click **"Link Guardian"**

**Note:** A guardian can be linked to multiple students (e.g., siblings).

---

#### 7. Manage Timetable

**Purpose:** Create and manage class schedules

**Steps to Add Time Slot:**
1. Navigate to **"Manage Time Slots"**
2. Click **"Add Time Slot"**
3. Enter details:
   - **Name** (e.g., "Period 1")
   - **Start Time** (e.g., 08:00)
   - **End Time** (e.g., 09:00)
   - **Order** (sequence number)
4. Click **"Add Time Slot"**

**Steps to Add Timetable Entry:**
1. Navigate to **"Manage Timetable"**
2. Click **"Add Timetable"**
3. Enter details:
   - **Course** (grade level)
   - **Subject**
   - **Staff** (teacher)
   - **Session** (academic year)
   - **Day of Week** (Monday-Friday)
   - **Time Slot**
   - **Room** (optional)
4. Click **"Add Timetable"**

**Best Practice:** Create all time slots first, then add timetable entries.

---

#### 8. View Attendance

**Purpose:** Monitor student attendance across all classes

**Steps:**
1. Navigate to **"View Attendance"**
2. Select filters:
   - **Subject**
   - **Date Range**
3. Click **"View"**
4. Review attendance records

---

#### 9. View Results

**Purpose:** Monitor student academic performance

**Steps:**
1. Navigate to **"View Results"**
2. Select filters:
   - **Student**
   - **Subject**
   - **Session**
3. Click **"View"**
4. Review results

---

#### 10. Manage Leave Applications

**Purpose:** Approve or reject leave requests from staff and students

**Steps:**
1. Navigate to **"Staff Leave"** or **"Student Leave"**
2. Review pending applications
3. For each application:
   - Click **"Approve"** to accept
   - Click **"Reject"** to decline
   - Add comments if needed
4. Staff/Student will be notified of the decision

---

#### 11. Manage Feedback

**Purpose:** Review and respond to feedback from staff and students

**Steps:**
1. Navigate to **"Staff Feedback"** or **"Student Feedback"**
2. Review feedback messages
3. Click **"Reply"** to respond
4. Enter your response
5. Click **"Send Reply"**

---

### What Admin Should NOT Do

- ❌ Share admin credentials with others
- ❌ Delete data without backup
- ❌ Modify student results directly (staff should do this)
- ❌ Change staff assignments without consultation

---

## Registrar Guide

**Dashboard URL:** `/registrar_home`  
**Access Level:** Read-only access to most data

### Dashboard Overview

The registrar dashboard displays:
- **Total Students** - Number of enrolled students
- **Total Staff** - Number of teaching staff
- **Total Courses** - Number of courses/grades
- **Total Subjects** - Number of subjects
- **Total Sessions** - Number of academic years
- **Attendance Records** - Total attendance entries
- **Attendance Reports** - Number of reports
- **Total Results** - Number of result entries
- **Recent Students** - Latest student enrollments

### Main Responsibilities

#### 1. View Student Records

**Purpose:** Access student information for record-keeping

**Steps:**
1. Navigate to **"View Students"**
2. Browse the student list
3. Use search/filter to find specific students
4. View student details (read-only)

**Note:** Registrar cannot add, edit, or delete students.

---

#### 2. View Staff Records

**Purpose:** Access staff information for record-keeping

**Steps:**
1. Navigate to **"View Staff"**
2. Browse the staff list
3. Use search/filter to find specific staff
4. View staff details (read-only)

---

#### 3. View Attendance Records

**Purpose:** Monitor attendance data

**Steps:**
1. Navigate to **"View Attendance"**
2. Select filters (subject, date, course)
3. View attendance records
4. Export data if needed (if feature is available)

---

#### 4. View Student Results

**Purpose:** Access academic performance data

**Steps:**
1. Navigate to **"View Results"**
2. Select filters (student, subject, session)
3. View results
4. Generate reports if needed

---

#### 5. View Timetable

**Purpose:** Access class schedules

**Steps:**
1. Navigate to **"View Timetable"**
2. Select course/class
3. View weekly schedule

---

#### 6. Update Profile

**Purpose:** Maintain personal information

**Steps:**
1. Navigate to **"Profile"**
2. Click **"Edit Profile"**
3. Update information
4. Click **"Update"**

---

### What Registrar CAN Do

- ✅ View all student records
- ✅ View all staff records
- ✅ View attendance data
- ✅ View student results
- ✅ View timetables
- ✅ View courses and subjects
- ✅ Update own profile
- ✅ View notifications

### What Registrar CANNOT Do

- ❌ Add, edit, or delete students
- ❌ Add, edit, or delete staff
- ❌ Add, edit, or delete courses
- ❌ Add, edit, or delete subjects
- ❌ Take attendance
- ❌ Add or edit results
- ❌ Approve leave applications
- ❌ Manage timetable
- ❌ Send notifications

---

## Staff/Teacher Guide

**Dashboard URL:** `/staff_home`  
**Access Level:** Teaching and classroom management

### Dashboard Overview

The staff dashboard displays:
- **Total Students** - Students in your classes
- **Attendance Taken** - Number of attendance records you've created
- **Leave Applied** - Your leave applications
- **Total Subjects** - Subjects assigned to you
- **Charts** - Attendance analytics

### Main Responsibilities

#### 1. Take Attendance

**Purpose:** Record student attendance for your classes

**Steps:**
1. Navigate to **"Take Attendance"**
2. Select:
   - **Subject** (your assigned subject)
   - **Date**
3. Click **"Fetch Students"**
4. Mark each student as:
   - **Present** ✓
   - **Absent** ✗
5. Click **"Submit Attendance"**

**Best Practice:** Take attendance at the beginning of each class.

---

#### 2. Update Attendance

**Purpose:** Correct attendance records if needed

**Steps:**
1. Navigate to **"Update Attendance"**
2. Select:
   - **Subject**
   - **Date**
3. Click **"Fetch Attendance"**
4. Update attendance status
5. Click **"Update Attendance"**

---

#### 3. Add Student Results

**Purpose:** Record student academic performance

**Steps:**
1. Navigate to **"Add Result"**
2. Select:
   - **Student**
   - **Subject** (your assigned subject)
   - **Session**
3. Enter scores:
   - **Assignment Marks**
   - **Exam Marks**
4. Click **"Add Result"**

**Note:** Total marks = Assignment + Exam marks

---

#### 4. Edit Student Results

**Purpose:** Update previously entered results

**Steps:**
1. Navigate to **"Edit Result"**
2. Select:
   - **Student**
   - **Subject**
3. Click **"Fetch Result"**
4. Update marks
5. Click **"Update Result"**

---

#### 5. Apply for Leave

**Purpose:** Request time off

**Steps:**
1. Navigate to **"Apply Leave"**
2. Fill in the form:
   - **Leave Date**
   - **Leave Reason**
3. Click **"Apply Leave"**
4. Wait for admin approval

**Status Check:**
- Navigate to **"Leave Status"**
- View pending/approved/rejected applications

---

#### 6. Send Feedback

**Purpose:** Communicate with admin

**Steps:**
1. Navigate to **"Send Feedback"**
2. Enter your message
3. Click **"Send Feedback"**
4. Check **"Feedback Reply"** for admin responses

---

#### 7. View Timetable

**Purpose:** Check your teaching schedule

**Steps:**
1. Navigate to **"My Timetable"**
2. View your weekly schedule
3. Note your classes, times, and rooms

---

### What Staff CAN Do

- ✅ Take and update attendance for assigned subjects
- ✅ Add and edit results for assigned subjects
- ✅ View students in their classes
- ✅ Apply for leave
- ✅ Send feedback to admin
- ✅ View own timetable
- ✅ Update own profile
- ✅ View notifications

### What Staff CANNOT Do

- ❌ Add or delete students
- ❌ Add or delete other staff
- ❌ Manage courses or subjects
- ❌ Approve leave applications
- ❌ View other staff's data
- ❌ Manage timetable
- ❌ Access admin features

---

## Student Guide

**Dashboard URL:** `/student_home`  
**Access Level:** Student portal access

### Dashboard Overview

The student dashboard displays:
- **Total Attendance** - Your attendance records
- **Present %** - Percentage of classes attended
- **Absent %** - Percentage of classes missed
- **Total Subjects** - Subjects you're enrolled in
- **Charts** - Your attendance analytics

### Main Features

#### 1. View Attendance

**Purpose:** Check your attendance records

**Steps:**
1. Navigate to **"View Attendance"**
2. Select:
   - **Subject** (optional filter)
   - **Date Range** (optional filter)
3. Click **"View"**
4. Review your attendance history

**Tip:** Regular attendance improves academic performance!

---

#### 2. View Results

**Purpose:** Check your academic performance

**Steps:**
1. Navigate to **"View Results"**
2. Select:
   - **Subject** (optional filter)
   - **Session** (academic year)
3. Click **"View"**
4. Review your scores and grades

---

#### 3. View Timetable

**Purpose:** Check your class schedule

**Steps:**
1. Navigate to **"My Timetable"**
2. View your weekly schedule
3. Note your classes, times, and rooms

---

#### 4. Apply for Leave

**Purpose:** Request absence from school

**Steps:**
1. Navigate to **"Apply Leave"**
2. Fill in the form:
   - **Leave Date**
   - **Leave Reason**
3. Click **"Apply Leave"**
4. Wait for admin approval

**Status Check:**
- Navigate to **"Leave Status"**
- View pending/approved/rejected applications

---

#### 5. Send Feedback

**Purpose:** Communicate with admin

**Steps:**
1. Navigate to **"Send Feedback"**
2. Enter your message
3. Click **"Send Feedback"**
4. Check **"Feedback Reply"** for admin responses

---

#### 6. Update Profile

**Purpose:** Maintain personal information

**Steps:**
1. Navigate to **"Profile"**
2. Click **"Edit Profile"**
3. Update information (limited fields)
4. Upload profile picture (optional)
5. Click **"Update"**

---

### What Students CAN Do

- ✅ View own attendance
- ✅ View own results
- ✅ View class timetable
- ✅ Apply for leave
- ✅ Send feedback to admin
- ✅ Update own profile
- ✅ View notifications

### What Students CANNOT Do

- ❌ View other students' data
- ❌ Modify attendance records
- ❌ Modify results
- ❌ Access staff or admin features
- ❌ Approve leave applications

---

## Parent/Guardian Guide

**Dashboard URL:** `/guardian_home`  
**Access Level:** Children's data only

### Dashboard Overview

The guardian dashboard displays:
- **My Children** - Number of linked children
- **Children Overview Cards** - Individual cards for each child showing:
  - Profile picture
  - Name and class
  - Attendance percentage
  - Number of subjects
  - Relationship type
  - Primary contact status

### Main Features

#### 1. View Children

**Purpose:** See all your linked children

**Steps:**
1. Navigate to **"My Children"**
2. View list of linked children
3. Click on a child to view details

---

#### 2. View Child's Attendance

**Purpose:** Monitor your child's attendance

**Steps:**
1. From dashboard, click **"Attendance"** on child's card
2. Or navigate to **"View Attendance"**
3. Select child (if you have multiple)
4. Select date range
5. View attendance records

---

#### 3. View Child's Results

**Purpose:** Monitor your child's academic performance

**Steps:**
1. From dashboard, click **"Results"** on child's card
2. Or navigate to **"View Results"**
3. Select child (if you have multiple)
4. Select subject and session
5. View results and grades

---

#### 4. View Child's Timetable

**Purpose:** Check your child's class schedule

**Steps:**
1. Navigate to **"View Timetable"**
2. Select child (if you have multiple)
3. View weekly schedule

---

#### 5. View Notifications

**Purpose:** Stay informed about your children

**Steps:**
1. Navigate to **"Notifications"**
2. View messages from school
3. Read important updates

---

#### 6. Update Profile

**Purpose:** Maintain your contact information

**Steps:**
1. Navigate to **"Profile"**
2. Click **"Edit Profile"**
3. Update information (especially phone number)
4. Click **"Update"**

**Important:** Keep your contact information up-to-date for school communications.

---

### What Guardians CAN Do

- ✅ View linked children's information
- ✅ View children's attendance
- ✅ View children's results
- ✅ View children's timetable
- ✅ View notifications
- ✅ Update own profile

### What Guardians CANNOT Do

- ❌ View other students' data
- ❌ Modify attendance or results
- ❌ Apply for leave (contact admin)
- ❌ Access staff or admin features
- ❌ Link/unlink children (contact admin)

---

## Common Features

### Profile Management

**Available to:** All users

**Steps:**
1. Click your name in the top right corner
2. Select **"Profile"** or **"Edit Profile"**
3. Update your information:
   - First Name
   - Last Name
   - Gender
   - Address
   - Profile Picture
4. Click **"Update Profile"**

---

### Change Password

**Available to:** All users

**Steps:**
1. Navigate to **"Profile"**
2. Click **"Change Password"**
3. Enter:
   - **Current Password**
   - **New Password**
   - **Confirm New Password**
4. Click **"Change Password"**

**Password Requirements:**
- Minimum 8 characters
- Mix of letters and numbers recommended
- Avoid common passwords

---

### View Notifications

**Available to:** All users

**Steps:**
1. Click the bell icon in the top right corner
2. Or navigate to **"Notifications"**
3. View unread notifications
4. Click on a notification to mark as read

---

### Search and Filter

**Available in:** Most list views (students, staff, subjects, etc.)

**Features:**
- **Search Box:** Type to search by name, email, etc.
- **Filters:** Use dropdowns to filter by course, session, etc.
- **Sorting:** Click column headers to sort
- **Pagination:** Navigate through pages if many records

---

## Troubleshooting

### Cannot Login

**Problem:** "Invalid email or password"

**Solutions:**
1. Verify email and password are correct
2. Check if Caps Lock is on
3. Try resetting your password
4. Contact admin if issue persists

---

### Page Not Loading

**Problem:** Page shows error or doesn't load

**Solutions:**
1. Refresh the page (F5 or Ctrl+R)
2. Clear browser cache
3. Try a different browser
4. Check internet connection
5. Contact admin if issue persists

---

### Cannot Submit Form

**Problem:** Form doesn't submit or shows errors

**Solutions:**
1. Check all required fields are filled
2. Verify data format (dates, emails, etc.)
3. Check file size if uploading images
4. Try refreshing the page
5. Contact admin if issue persists

---

### Permission Denied

**Problem:** "You don't have permission to access this page"

**Solutions:**
1. Verify you're logged in
2. Check if you're using the correct role account
3. Some features are role-specific
4. Contact admin if you need access

---

### Data Not Showing

**Problem:** Lists or tables are empty

**Solutions:**
1. Check if filters are applied
2. Verify data exists (ask admin)
3. Try refreshing the page
4. Clear browser cache
5. Contact admin if issue persists

---

## Best Practices

### For All Users

1. **Keep credentials secure** - Don't share your password
2. **Update profile** - Keep your information current
3. **Check notifications** - Stay informed
4. **Logout when done** - Especially on shared computers
5. **Report issues** - Contact admin for problems

### For Admin

1. **Regular backups** - Backup database regularly
2. **Data verification** - Verify data before deletion
3. **User training** - Train staff on system usage
4. **Monitor activity** - Review system usage
5. **Security updates** - Keep system updated

### For Staff

1. **Timely attendance** - Take attendance promptly
2. **Accurate results** - Double-check marks before submission
3. **Regular updates** - Update results regularly
4. **Communication** - Use feedback system for issues
5. **Professional conduct** - Maintain student privacy

### For Students

1. **Regular checks** - Check attendance and results regularly
2. **Timely leave** - Apply for leave in advance
3. **Respectful communication** - Use feedback system appropriately
4. **Profile updates** - Keep profile information current
5. **Academic focus** - Use system to track progress

### For Guardians

1. **Regular monitoring** - Check children's progress regularly
2. **Communication** - Stay in touch with school
3. **Profile updates** - Keep contact information current
4. **Support learning** - Use data to support children
5. **Engagement** - Attend school events and meetings

---

## Getting Help

### Contact Information

**Technical Support:**
- Email: support@dilfere.school
- Phone: [School Phone Number]

**Admin Office:**
- Email: admin@dilfere.school
- Office Hours: Monday-Friday, 8:00 AM - 4:00 PM

### Additional Resources

- **README.md** - Project overview
- **SETUP.md** - Installation and setup guide
- **DEMO_CREDENTIALS.md** - Test account credentials
- **USER_TYPES.md** - User role reference

---

**Last Updated:** May 8, 2026  
**System Version:** 1.0  
**Status:** Production Ready ✅
