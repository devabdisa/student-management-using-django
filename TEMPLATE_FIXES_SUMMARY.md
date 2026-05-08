# Template Fixes Summary

**Date:** May 9, 2026  
**Issue:** NoReverseMatch errors when accessing manage pages

---

## Problems Fixed

### 1. reCAPTCHA Removal (login.html)
**Issue:** reCAPTCHA widget still showing on login page even though backend validation was disabled

**Files Fixed:**
- `main_app/templates/main_app/login.html`

**Changes:**
- ✅ Removed `<script src="https://www.google.com/recaptcha/api.js">`
- ✅ Removed `<div class="g-recaptcha">` widget

**Commit:** `612f31f`

---

### 2. NoReverseMatch Errors (manage_student.html, manage_staff.html)
**Issue:** `NoReverseMatch at /student/manage/` - Reverse for 'edit_student' with arguments '()','' not found

**Root Cause:**
- Templates were trying to access `student.student.id` and `staff.staff.id`
- If the related Student or Staff record doesn't exist, this causes a NoReverseMatch error
- The error occurs when CustomUser exists but the related Student/Staff model wasn't created

**Files Fixed:**
- `main_app/templates/hod_template/manage_student.html`
- `main_app/templates/hod_template/manage_staff.html`

**Changes:**

#### manage_student.html
```django
<!-- BEFORE -->
<td>{{student.student.course.name}}</td>
<td>
    <a href="{% url 'edit_student' student.student.id %}">Edit</a>
    <a href="{% url 'delete_student' student.student.id %}">Delete</a>
</td>

<!-- AFTER -->
<td>{% if student.student and student.student.course %}{{student.student.course.name}}{% else %}N/A{% endif %}</td>
<td>
    {% if student.student %}
    <a href="{% url 'edit_student' student.student.id %}">Edit</a>
    <a href="{% url 'delete_student' student.student.id %}">Delete</a>
    {% else %}
    <span class="text-danger">No student record</span>
    {% endif %}
</td>
```

#### manage_staff.html
```django
<!-- BEFORE -->
<td>{{staff.staff.course.name}}</td>
<td>
    <a href="{% url 'edit_staff' staff.staff.id %}">Edit</a>
    <a href="{% url 'delete_staff' staff.staff.id %}">Delete</a>
</td>

<!-- AFTER -->
<td>{% if staff.staff and staff.staff.course %}{{staff.staff.course.name}}{% else %}N/A{% endif %}</td>
<td>
    {% if staff.staff %}
    <a href="{% url 'edit_staff' staff.staff.id %}">Edit</a>
    <a href="{% url 'delete_staff' staff.staff.id %}">Delete</a>
    {% else %}
    <span class="text-danger">No staff record</span>
    {% endif %}
</td>
```

**Commit:** `7a329bc`

---

## Why This Happened

### Data Model Structure
```
CustomUser (user_type=3 for students, user_type=2 for staff)
    ↓ OneToOneField
Student (has admin field pointing to CustomUser)
    ↓ ForeignKey
Course
```

### The Problem
1. `manage_student` view queries: `CustomUser.objects.filter(user_type=3)`
2. Template tries to access: `student.student.id` (CustomUser → Student → id)
3. If Student record doesn't exist, `student.student` is None
4. Trying to access `None.id` causes NoReverseMatch error

### The Solution
- Add `{% if student.student %}` checks before accessing related objects
- Display "No student record" message if the related object doesn't exist
- Prevents template errors and provides clear feedback

---

## Other Templates Checked

### ✅ No Issues Found In:
- `main_app/templates/hod_template/manage_course.html` - Uses `course.id` directly
- `main_app/templates/hod_template/manage_subject.html` - Uses `subject.id` directly
- `main_app/templates/main_app/sidebar_template.html` - Already fixed in previous commit

---

## Testing Checklist

After these fixes, verify:

- [ ] Login page loads without reCAPTCHA
- [ ] Login works correctly
- [ ] `/student/manage/` page loads without errors
- [ ] `/staff/manage/` page loads without errors
- [ ] Edit buttons work for students with valid records
- [ ] Edit buttons work for staff with valid records
- [ ] "No student record" message shows for incomplete records
- [ ] "No staff record" message shows for incomplete records
- [ ] Course/Subject manage pages still work

---

## Prevention

To prevent this issue in the future:

### 1. Always Create Related Objects
When creating a CustomUser with user_type=3 (student), ensure the Student record is created:

```python
# In add_student view
user = CustomUser.objects.create_user(...)
user.student.course = course  # This creates the Student record
user.student.session = session
user.save()
```

### 2. Use Template Safety Checks
Always check if related objects exist before accessing them:

```django
{% if object.related_object %}
    {{ object.related_object.field }}
{% else %}
    N/A
{% endif %}
```

### 3. Use get_or_create
For critical relationships, use `get_or_create`:

```python
student, created = Student.objects.get_or_create(
    admin=user,
    defaults={'course': course, 'session': session}
)
```

---

## Related Files

### Views
- `main_app/hod_views.py` - manage_student, manage_staff, edit_student, edit_staff

### Models
- `main_app/models.py` - CustomUser, Student, Staff, Course

### URLs
- `main_app/urls.py` - URL patterns for edit/delete operations

---

## Commits

1. **612f31f** - Remove reCAPTCHA from login page
2. **7a329bc** - Fix NoReverseMatch errors in manage templates

---

**Status:** ✅ All template errors fixed and pushed to GitHub  
**System Check:** ✅ 0 issues  
**Ready for Testing:** ✅ Yes
