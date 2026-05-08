# User Type Reference - Dil Fere Primary School Portal

## Current User Type Mapping

This document defines the user type codes used throughout the system.

### Active User Types (Implemented)

| Code | Role | Description | Status |
|------|------|-------------|--------|
| `1` | Admin/HOD | System administrator with full access | ✅ Active |
| `2` | Staff/Teacher | Teachers and staff members | ✅ Active |
| `3` | Student | Students enrolled in the school | ✅ Active |

### Planned User Types (Future Implementation)

| Code | Role | Description | Status |
|------|------|-------------|--------|
| `4` | Registrar | Handles student admissions and records | 🔜 Planned |
| `5` | Parent/Guardian | Parents and guardians of students | 🔜 Planned |

## Implementation Notes

### Current Implementation (models.py)
```python
class CustomUser(AbstractUser):
    USER_TYPE = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
```

### Future Implementation (when adding Registrar and Parent/Guardian)
```python
class CustomUser(AbstractUser):
    USER_TYPE = (
        (1, "Admin"),
        (2, "Staff"),
        (3, "Student"),
        (4, "Registrar"),
        (5, "Parent/Guardian")
    )
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
```

## Role Permissions

### Admin/HOD (Type 1)
**Full system access including:**
- Manage all users (staff, students, future: registrars, parents)
- Manage courses, subjects, sessions
- View all attendance records
- View all results
- Approve/reject leave applications
- Send notifications to all user types
- Access all reports and analytics

### Staff/Teacher (Type 2)
**Teaching and classroom management:**
- View assigned subjects and students
- Take and update attendance
- Add and edit student results
- Apply for leave
- Send feedback to admin
- View notifications
- Access class-specific reports

### Student (Type 3)
**Student portal access:**
- View own attendance
- View own results
- Apply for leave
- Send feedback to admin
- View notifications
- View own profile

### Registrar (Type 4) - PLANNED
**Student records and admissions:**
- Register new students
- Update student information
- Manage student records
- Generate admission documents
- View student data
- Limited access to academic records

### Parent/Guardian (Type 5) - PLANNED
**Child monitoring access:**
- View linked children's attendance
- View linked children's results
- Receive notifications about children
- Apply for leave on behalf of children
- Communicate with teachers/admin
- View children's profiles

## Access Control Implementation

### Current Middleware (middleware.py)
```python
if user.user_type == '1':  # Admin
    # Allow access to hod_views
elif user.user_type == '2':  # Staff
    # Allow access to staff_views
elif user.user_type == '3':  # Student
    # Allow access to student_views
```

### Future Middleware (when adding new roles)
```python
if user.user_type == '1':  # Admin
    # Allow access to hod_views
elif user.user_type == '2':  # Staff
    # Allow access to staff_views
elif user.user_type == '3':  # Student
    # Allow access to student_views
elif user.user_type == '4':  # Registrar
    # Allow access to registrar_views
elif user.user_type == '5':  # Parent/Guardian
    # Allow access to guardian_views
```

## Database Considerations

### Current Profile Models
- `Admin` (linked to user_type=1)
- `Staff` (linked to user_type=2)
- `Student` (linked to user_type=3)

### Future Profile Models
- `Registrar` (linked to user_type=4) - TO BE CREATED
- `Guardian` (linked to user_type=5) - TO BE CREATED

### Signal Handler Updates Required
When implementing new user types, update the `create_user_profile` signal in `models.py`:

```python
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Staff.objects.create(admin=instance)
        if instance.user_type == 3:
            Student.objects.create(admin=instance)
        if instance.user_type == 4:
            Registrar.objects.create(admin=instance)  # TO BE ADDED
        if instance.user_type == 5:
            Guardian.objects.create(admin=instance)   # TO BE ADDED
```

## URL Routing Structure

### Current Structure
```
/admin/home/          → Admin dashboard
/staff/home/          → Staff dashboard
/student/home/        → Student dashboard
```

### Future Structure
```
/admin/home/          → Admin dashboard
/staff/home/          → Staff dashboard
/student/home/        → Student dashboard
/registrar/home/      → Registrar dashboard (TO BE ADDED)
/guardian/home/       → Guardian dashboard (TO BE ADDED)
```

## View Files Organization

### Current Files
- `hod_views.py` - Admin/HOD views
- `staff_views.py` - Staff/Teacher views
- `student_views.py` - Student views

### Future Files
- `registrar_views.py` - Registrar views (TO BE CREATED)
- `guardian_views.py` - Parent/Guardian views (TO BE CREATED)

## Template Directories

### Current Structure
```
templates/
├── hod_template/      → Admin templates
├── staff_template/    → Staff templates
└── student_template/  → Student templates
```

### Future Structure
```
templates/
├── hod_template/       → Admin templates
├── staff_template/     → Staff templates
├── student_template/   → Student templates
├── registrar_template/ → Registrar templates (TO BE CREATED)
└── guardian_template/  → Guardian templates (TO BE CREATED)
```

## Important Notes

1. **Type Consistency:** Always use integer comparison (`user.user_type == 1`) not string comparison (`user.user_type == '1'`)

2. **Max Length:** Current `max_length=1` in CharField is sufficient for types 1-5

3. **Default Value:** Default is set to `1` (Admin) - consider if this should change

4. **Migration Required:** When adding types 4 and 5, a data migration is NOT required since we're adding new types, not changing existing ones

5. **Backward Compatibility:** Adding types 4 and 5 will not break existing functionality for types 1-3

## Testing Checklist (When Implementing New Types)

- [ ] Update `USER_TYPE` choices in `CustomUser` model
- [ ] Create new profile model (Registrar or Guardian)
- [ ] Update `create_user_profile` signal
- [ ] Update `save_user_profile` signal
- [ ] Create new views file
- [ ] Update middleware for access control
- [ ] Create URL patterns
- [ ] Create template directory
- [ ] Create forms for new user type
- [ ] Update admin interface
- [ ] Test user creation
- [ ] Test login and access control
- [ ] Test profile updates
- [ ] Update documentation

---

**Last Updated:** Phase 1 - Foundation Setup
**Next Update:** When implementing Registrar (Phase 2) or Parent/Guardian (Phase 2)
