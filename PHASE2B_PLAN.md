# Phase 2B: Parent/Guardian Implementation Plan

## Overview
Add Parent/Guardian role (user_type=5) with ability to view their children's information including attendance, results, and receive notifications.

## User Type Mapping
- 1 = Admin/HOD
- 2 = Staff/Teacher
- 3 = Student
- 4 = Registrar ✅ (Completed in Phase 2A)
- **5 = Parent/Guardian** 🔜 (This Phase)

## Implementation Steps

### 1. Models (main_app/models.py)
- [x] Update `USER_TYPE` to include `(5, "Guardian")`
- [x] Create `Guardian` model with OneToOne relationship to CustomUser
- [x] Create `StudentGuardian` model for Many-to-Many relationship
- [x] Update signals to handle user_type=5

#### Guardian Model Fields:
- admin (OneToOne to CustomUser)
- occupation (CharField, optional)
- phone_number (CharField)
- relationship_type (CharField with choices: father, mother, guardian, other)
- created_at (DateTimeField)
- updated_at (DateTimeField)

#### StudentGuardian Model Fields:
- student (ForeignKey to Student)
- guardian (ForeignKey to Guardian)
- is_primary (BooleanField) - Primary contact
- can_pickup (BooleanField) - Authorized to pickup student
- emergency_contact (BooleanField) - Emergency contact
- unique_together: (student, guardian)

### 2. Forms (main_app/forms.py)
- [x] Create `GuardianForm` for creating Guardian users
- [x] Create `GuardianEditForm` for editing Guardian profiles
- [x] Create `StudentGuardianForm` for linking students to guardians

### 3. Authentication & Routing (middleware.py, views.py)
- [x] Update `LoginCheckMiddleWare` to handle Guardian routing
- [x] Guardian users redirect to `guardian_home`
- [x] Update `doLogin` view

### 4. Views (main_app/guardian_views.py - NEW FILE)
Create the following views:
- [x] `guardian_home` - Dashboard with children's overview
- [x] `guardian_view_profile` - View/edit profile
- [x] `guardian_view_children` - List all linked children
- [x] `guardian_view_child_detail` - Detailed view of one child
- [x] `guardian_view_child_attendance` - Child's attendance records
- [x] `guardian_view_child_results` - Child's exam results
- [x] `guardian_view_notifications` - Notifications from school
- [x] `guardian_view_timetable` - Child's class timetable (placeholder)

### 5. URLs (main_app/urls.py)
Add Guardian URLs:
```python
# Guardian URLs
path('guardian/home/', guardian_views.guardian_home, name='guardian_home'),
path('guardian/view/profile/', guardian_views.guardian_view_profile, name='guardian_view_profile'),
path('guardian/view/children/', guardian_views.guardian_view_children, name='guardian_view_children'),
path('guardian/view/child/<int:student_id>/', guardian_views.guardian_view_child_detail, name='guardian_view_child_detail'),
path('guardian/view/child/<int:student_id>/attendance/', guardian_views.guardian_view_child_attendance, name='guardian_view_child_attendance'),
path('guardian/view/child/<int:student_id>/results/', guardian_views.guardian_view_child_results, name='guardian_view_child_results'),
path('guardian/view/notifications/', guardian_views.guardian_view_notifications, name='guardian_view_notifications'),
path('guardian/view/timetable/<int:student_id>/', guardian_views.guardian_view_timetable, name='guardian_view_timetable'),
```

### 6. Templates (main_app/templates/guardian_template/ - NEW DIRECTORY)
Create the following templates:
- [x] `home_content.html` - Dashboard
- [x] `guardian_view_profile.html` - Profile page
- [x] `guardian_view_children.html` - Children list
- [x] `guardian_view_child_detail.html` - Child details
- [x] `guardian_view_child_attendance.html` - Attendance view
- [x] `guardian_view_child_results.html` - Results view
- [x] `guardian_view_notifications.html` - Notifications
- [x] `guardian_view_timetable.html` - Timetable (placeholder)

### 7. Admin Views (main_app/hod_views.py)
Add admin functions to manage guardians:
- [x] `add_guardian` - Create new guardian
- [x] `manage_guardian` - List all guardians
- [x] `edit_guardian` - Edit guardian details
- [x] `delete_guardian` - Delete guardian
- [x] `link_student_guardian` - Link student to guardian
- [x] `unlink_student_guardian` - Unlink student from guardian

### 8. Admin URLs
Add admin URLs for guardian management:
```python
# Admin Guardian Management
path('admin/add_guardian/', hod_views.add_guardian, name='add_guardian'),
path('admin/manage_guardian/', hod_views.manage_guardian, name='manage_guardian'),
path('admin/edit_guardian/<int:guardian_id>/', hod_views.edit_guardian, name='edit_guardian'),
path('admin/delete_guardian/<int:guardian_id>/', hod_views.delete_guardian, name='delete_guardian'),
path('admin/link_student_guardian/', hod_views.link_student_guardian, name='link_student_guardian'),
path('admin/unlink_student_guardian/<int:link_id>/', hod_views.unlink_student_guardian, name='unlink_student_guardian'),
```

### 9. Admin Templates
Add admin templates for guardian management:
- [x] `hod_template/add_guardian_template.html`
- [x] `hod_template/manage_guardian_template.html`
- [x] `hod_template/edit_guardian_template.html`
- [x] `hod_template/link_student_guardian_template.html`

### 10. Database Migration
- [x] Generate migration: `python manage.py makemigrations`
- [x] Apply migration: `python manage.py migrate`

### 11. Helper Scripts
Create helper scripts:
- [x] `create_guardian.py` - Create test guardian user
- [x] `link_student_to_guardian.py` - Link existing student to guardian
- [x] `delete_guardian.py` - Delete test guardian user

### 12. Documentation
Update documentation:
- [x] `SETUP.md` - Add guardian creation instructions
- [x] `USER_TYPES.md` - Update with guardian details
- [x] `PHASE2B_COMPLETION_REPORT.md` - Full implementation report
- [x] `PHASE2B_SUMMARY.md` - Quick reference

## Guardian Permissions

### ✅ Can Do:
- View dashboard with children's overview
- View all linked children
- View child's attendance records
- View child's exam results
- View child's course/class information
- View child's subjects
- View notifications from school
- View child's timetable (when implemented)
- Update own profile

### ❌ Cannot Do:
- Add/edit/delete students
- Add/edit/delete staff
- Add/edit/delete courses
- Add/edit/delete subjects
- Modify attendance records
- Modify exam results
- Access admin functions
- Access staff functions
- Access registrar functions
- View other students (not their children)

## Testing Checklist

### Model Testing:
- [ ] Guardian model created successfully
- [ ] StudentGuardian model created successfully
- [ ] Signals create Guardian profile for user_type=5
- [ ] Can link multiple students to one guardian
- [ ] Can link multiple guardians to one student
- [ ] Unique constraint works (no duplicate links)

### Authentication Testing:
- [ ] Guardian can log in
- [ ] Guardian redirects to guardian_home
- [ ] Guardian cannot access admin views
- [ ] Guardian cannot access staff views
- [ ] Guardian cannot access student views
- [ ] Guardian cannot access registrar views

### View Testing:
- [ ] Dashboard shows all linked children
- [ ] Can view each child's details
- [ ] Can view child's attendance
- [ ] Can view child's results
- [ ] Can view notifications
- [ ] Can update own profile

### Admin Testing:
- [ ] Admin can create guardian
- [ ] Admin can edit guardian
- [ ] Admin can delete guardian
- [ ] Admin can link student to guardian
- [ ] Admin can unlink student from guardian
- [ ] Admin can view all guardians

### Integration Testing:
- [ ] Existing roles still work (Admin, Staff, Student, Registrar)
- [ ] No breaking changes
- [ ] System check passes
- [ ] All migrations applied

## Risk Assessment

**Risk Level:** LOW

**Reasons:**
1. New models, no changes to existing models
2. No data migration required
3. Additive changes only
4. No breaking changes to existing functionality
5. Similar pattern to Registrar implementation (Phase 2A)

## Estimated Time

- Models & Forms: 1 hour
- Views: 2 hours
- Templates: 2 hours
- Admin Functions: 2 hours
- Testing: 1 hour
- Documentation: 1 hour

**Total:** ~9 hours

## Success Criteria

- [x] Guardian model created
- [x] StudentGuardian relationship model created
- [x] Migration applied successfully
- [x] Guardian can log in
- [x] Guardian can view linked children
- [x] Guardian can view child's attendance
- [x] Guardian can view child's results
- [x] Admin can manage guardians
- [x] Admin can link/unlink students
- [x] All existing roles still work
- [x] System check passes with 0 issues
- [x] Documentation updated

## Next Steps After Phase 2B

**Phase 2C: Timetable Module**
- Create TimeSlot model
- Create Timetable model
- Implement timetable management
- Add conflict detection
- Display timetables for all user types

**Phase 3: UI/UX Modernization**
- Replace AdminLTE with modern framework
- Responsive design improvements
- Better mobile experience
- Modern color scheme and branding

---

**Status:** 🔜 Ready to implement  
**Dependencies:** Phase 2A (Registrar) ✅ Complete  
**Next Phase:** Phase 2C (Timetable)
