"""
Guardian Views for Dil Fere Primary School Portal
Handles all Guardian-related functionality
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import GuardianEditForm
from .models import (
    AttendanceReport, Course, CustomUser, Guardian, NotificationStudent,
    Session, Student, StudentGuardian, StudentResult, Subject
)


@login_required
def guardian_home(request):
    """Guardian dashboard showing overview of all linked children"""
    guardian = get_object_or_404(Guardian, admin=request.user)
    
    # Get all linked students
    student_links = StudentGuardian.objects.filter(guardian=guardian).select_related('student', 'student__admin', 'student__course')
    
    # Statistics
    total_children = student_links.count()
    
    # Get children details
    children_data = []
    for link in student_links:
        student = link.student
        # Get attendance stats
        total_attendance = AttendanceReport.objects.filter(student=student).count()
        present_attendance = AttendanceReport.objects.filter(student=student, status=True).count()
        attendance_percentage = (present_attendance / total_attendance * 100) if total_attendance > 0 else 0
        
        # Get results stats
        results = StudentResult.objects.filter(student=student)
        total_subjects = results.count()
        
        children_data.append({
            'student': student,
            'link': link,
            'attendance_percentage': round(attendance_percentage, 1),
            'total_subjects': total_subjects,
        })
    
    context = {
        'page_title': 'Guardian Dashboard',
        'guardian': guardian,
        'total_children': total_children,
        'children_data': children_data,
    }
    return render(request, 'guardian_template/home_content.html', context)


@login_required
def guardian_view_profile(request):
    """View and edit guardian profile"""
    guardian = get_object_or_404(Guardian, admin=request.user)
    
    if request.method == 'POST':
        form = GuardianEditForm(request.POST, request.FILES, instance=guardian)
        if form.is_valid():
            # Update CustomUser fields
            user = guardian.admin
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.gender = form.cleaned_data['gender']
            user.address = form.cleaned_data['address']
            
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            
            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']
            
            user.save()
            
            # Update Guardian fields
            guardian.phone_number = form.cleaned_data['phone_number']
            guardian.occupation = form.cleaned_data['occupation']
            guardian.relationship_type = form.cleaned_data['relationship_type']
            guardian.save()
            
            messages.success(request, "Profile updated successfully!")
            return redirect(reverse('guardian_view_profile'))
        else:
            messages.error(request, "Failed to update profile. Please check the form.")
    else:
        form = GuardianEditForm(instance=guardian)
    
    context = {
        'page_title': 'My Profile',
        'form': form,
        'guardian': guardian,
    }
    return render(request, 'guardian_template/guardian_view_profile.html', context)


@login_required
def guardian_view_children(request):
    """View all linked children"""
    guardian = get_object_or_404(Guardian, admin=request.user)
    student_links = StudentGuardian.objects.filter(guardian=guardian).select_related('student', 'student__admin', 'student__course', 'student__session')
    
    context = {
        'page_title': 'My Children',
        'student_links': student_links,
    }
    return render(request, 'guardian_template/guardian_view_children.html', context)


@login_required
def guardian_view_child_detail(request, student_id):
    """View detailed information about a specific child"""
    guardian = get_object_or_404(Guardian, admin=request.user)
    
    # Verify this guardian is linked to this student
    student_link = get_object_or_404(StudentGuardian, guardian=guardian, student_id=student_id)
    student = student_link.student
    
    # Get attendance stats
    total_attendance = AttendanceReport.objects.filter(student=student).count()
    present_attendance = AttendanceReport.objects.filter(student=student, status=True).count()
    absent_attendance = total_attendance - present_attendance
    attendance_percentage = (present_attendance / total_attendance * 100) if total_attendance > 0 else 0
    
    # Get subjects
    subjects = Subject.objects.filter(course=student.course)
    
    # Get results
    results = StudentResult.objects.filter(student=student).select_related('subject')
    
    # Calculate average
    total_marks = 0
    result_count = 0
    for result in results:
        total_marks += (result.test + result.exam)
        result_count += 1
    
    average_marks = (total_marks / result_count) if result_count > 0 else 0
    
    context = {
        'page_title': f'{student.admin.first_name} {student.admin.last_name} - Details',
        'student': student,
        'student_link': student_link,
        'total_attendance': total_attendance,
        'present_attendance': present_attendance,
        'absent_attendance': absent_attendance,
        'attendance_percentage': round(attendance_percentage, 1),
        'subjects': subjects,
        'results': results,
        'average_marks': round(average_marks, 1),
    }
    return render(request, 'guardian_template/guardian_view_child_detail.html', context)


@login_required
def guardian_view_child_attendance(request, student_id):
    """View child's attendance records"""
    guardian = get_object_or_404(Guardian, admin=request.user)
    
    # Verify this guardian is linked to this student
    student_link = get_object_or_404(StudentGuardian, guardian=guardian, student_id=student_id)
    student = student_link.student
    
    # Get attendance reports
    attendance_reports = AttendanceReport.objects.filter(student=student).select_related('attendance', 'attendance__subject').order_by('-attendance__date')
    
    # Statistics
    total_attendance = attendance_reports.count()
    present_attendance = attendance_reports.filter(status=True).count()
    absent_attendance = total_attendance - present_attendance
    attendance_percentage = (present_attendance / total_attendance * 100) if total_attendance > 0 else 0
    
    context = {
        'page_title': f'{student.admin.first_name} {student.admin.last_name} - Attendance',
        'student': student,
        'attendance_reports': attendance_reports,
        'total_attendance': total_attendance,
        'present_attendance': present_attendance,
        'absent_attendance': absent_attendance,
        'attendance_percentage': round(attendance_percentage, 1),
    }
    return render(request, 'guardian_template/guardian_view_child_attendance.html', context)


@login_required
def guardian_view_child_results(request, student_id):
    """View child's exam results"""
    guardian = get_object_or_404(Guardian, admin=request.user)
    
    # Verify this guardian is linked to this student
    student_link = get_object_or_404(StudentGuardian, guardian=guardian, student_id=student_id)
    student = student_link.student
    
    # Get results
    results = StudentResult.objects.filter(student=student).select_related('subject')
    
    # Calculate statistics
    total_marks = 0
    total_test = 0
    total_exam = 0
    result_count = results.count()
    
    for result in results:
        total_test += result.test
        total_exam += result.exam
        total_marks += (result.test + result.exam)
    
    average_test = (total_test / result_count) if result_count > 0 else 0
    average_exam = (total_exam / result_count) if result_count > 0 else 0
    average_total = (total_marks / result_count) if result_count > 0 else 0
    
    context = {
        'page_title': f'{student.admin.first_name} {student.admin.last_name} - Results',
        'student': student,
        'results': results,
        'result_count': result_count,
        'average_test': round(average_test, 1),
        'average_exam': round(average_exam, 1),
        'average_total': round(average_total, 1),
    }
    return render(request, 'guardian_template/guardian_view_child_results.html', context)


@login_required
def guardian_view_notifications(request):
    """View notifications for all children"""
    guardian = get_object_or_404(Guardian, admin=request.user)
    
    # Get all linked students
    student_links = StudentGuardian.objects.filter(guardian=guardian).select_related('student')
    student_ids = [link.student.id for link in student_links]
    
    # Get notifications for all children
    notifications = NotificationStudent.objects.filter(student_id__in=student_ids).select_related('student', 'student__admin').order_by('-created_at')
    
    context = {
        'page_title': 'Notifications',
        'notifications': notifications,
    }
    return render(request, 'guardian_template/guardian_view_notifications.html', context)


@login_required
def guardian_view_timetable(request, student_id):
    """View child's class timetable (placeholder for Phase 2C)"""
    guardian = get_object_or_404(Guardian, admin=request.user)
    
    # Verify this guardian is linked to this student
    student_link = get_object_or_404(StudentGuardian, guardian=guardian, student_id=student_id)
    student = student_link.student
    
    context = {
        'page_title': f'{student.admin.first_name} {student.admin.last_name} - Timetable',
        'student': student,
        'message': 'Timetable feature will be available in Phase 2C',
    }
    return render(request, 'guardian_template/guardian_view_timetable.html', context)
