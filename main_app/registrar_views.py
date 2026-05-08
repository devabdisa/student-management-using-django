import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import RegistrarEditForm
from .models import (Attendance, AttendanceReport, Course, CustomUser,
                     Registrar, Session, Staff, Student, StudentResult,
                     Subject)


def registrar_home(request):
    """Registrar dashboard view"""
    registrar = get_object_or_404(Registrar, admin=request.user)
    
    # Get statistics
    total_students = Student.objects.all().count()
    total_staff = Staff.objects.all().count()
    total_courses = Course.objects.all().count()
    total_subjects = Subject.objects.all().count()
    total_sessions = Session.objects.all().count()
    
    # Get attendance statistics
    total_attendance = Attendance.objects.all().count()
    total_attendance_reports = AttendanceReport.objects.all().count()
    
    # Get results statistics
    total_results = StudentResult.objects.all().count()
    
    # Recent students (last 5)
    recent_students = Student.objects.all().order_by('-admin__date_joined')[:5]
    
    context = {
        'page_title': 'Registrar Dashboard',
        'total_students': total_students,
        'total_staff': total_staff,
        'total_courses': total_courses,
        'total_subjects': total_subjects,
        'total_sessions': total_sessions,
        'total_attendance': total_attendance,
        'total_attendance_reports': total_attendance_reports,
        'total_results': total_results,
        'recent_students': recent_students,
    }
    return render(request, 'registrar_template/home_content.html', context)


def registrar_view_profile(request):
    """View and edit registrar profile"""
    registrar = get_object_or_404(Registrar, admin=request.user)
    form = RegistrarEditForm(request.POST or None, request.FILES or None, instance=registrar)
    
    context = {
        'form': form,
        'page_title': 'View/Update Profile'
    }
    
    if request.method == 'POST':
        try:
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                password = form.cleaned_data.get('password') or None
                address = form.cleaned_data.get('address')
                gender = form.cleaned_data.get('gender')
                passport = request.FILES.get('profile_pic') or None
                
                admin = registrar.admin
                admin.first_name = first_name
                admin.last_name = last_name
                admin.address = address
                admin.gender = gender
                
                if password != None:
                    admin.set_password(password)
                if passport != None:
                    admin.profile_pic = passport
                    
                admin.save()
                registrar.save()
                messages.success(request, "Profile updated successfully!")
                return redirect(reverse('registrar_view_profile'))
            else:
                messages.error(request, "Invalid form data")
        except Exception as e:
            messages.error(request, "Error updating profile: " + str(e))
    
    return render(request, "registrar_template/registrar_view_profile.html", context)


def registrar_view_students(request):
    """View all students"""
    students = Student.objects.all()
    context = {
        'students': students,
        'page_title': 'View Students'
    }
    return render(request, 'registrar_template/registrar_view_students.html', context)


def registrar_view_staff(request):
    """View all staff"""
    staff = Staff.objects.all()
    context = {
        'staff': staff,
        'page_title': 'View Staff'
    }
    return render(request, 'registrar_template/registrar_view_staff.html', context)


def registrar_view_courses(request):
    """View all courses"""
    courses = Course.objects.all()
    context = {
        'courses': courses,
        'page_title': 'View Courses'
    }
    return render(request, 'registrar_template/registrar_view_courses.html', context)


def registrar_view_subjects(request):
    """View all subjects"""
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
        'page_title': 'View Subjects'
    }
    return render(request, 'registrar_template/registrar_view_subjects.html', context)


def registrar_view_attendance(request):
    """View attendance records"""
    subjects = Subject.objects.all()
    sessions = Session.objects.all()
    context = {
        'subjects': subjects,
        'sessions': sessions,
        'page_title': 'View Attendance'
    }
    return render(request, 'registrar_template/registrar_view_attendance.html', context)


@csrf_exempt
def registrar_get_attendance(request):
    """Get attendance data for a specific subject and session"""
    subject_id = request.POST.get('subject')
    session_id = request.POST.get('session')
    
    try:
        subject = get_object_or_404(Subject, id=subject_id)
        session = get_object_or_404(Session, id=session_id)
        attendance = Attendance.objects.filter(subject=subject, session=session)
        
        attendance_list = []
        for att in attendance:
            data = {
                "id": att.id,
                "date": str(att.date),
                "session": str(att.session)
            }
            attendance_list.append(data)
        
        return HttpResponse(json.dumps(attendance_list), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(e)}), content_type='application/json')


def registrar_view_results(request):
    """View student results"""
    students = Student.objects.all()
    context = {
        'students': students,
        'page_title': 'View Results'
    }
    return render(request, 'registrar_template/registrar_view_results.html', context)


@csrf_exempt
def registrar_get_student_results(request):
    """Get results for a specific student"""
    student_id = request.POST.get('student')
    
    try:
        student = get_object_or_404(Student, id=student_id)
        results = StudentResult.objects.filter(student=student)
        
        results_list = []
        for result in results:
            data = {
                "subject": result.subject.name,
                "test": result.test,
                "exam": result.exam,
                "total": result.test + result.exam
            }
            results_list.append(data)
        
        return HttpResponse(json.dumps(results_list), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(e)}), content_type='application/json')


# ==================== TIMETABLE VIEWS ====================

def registrar_view_timetable(request):
    """View timetable (weekly view)"""
    from .models import TimeSlot, Timetable
    
    courses = Course.objects.all()
    sessions = Session.objects.all()
    timeslots = TimeSlot.objects.all().order_by('order', 'start_time')
    
    # Get filters
    course_id = request.GET.get('course')
    session_id = request.GET.get('session')
    
    timetable_data = None
    selected_course = None
    selected_session = None
    
    if course_id and session_id:
        selected_course = get_object_or_404(Course, id=course_id)
        selected_session = get_object_or_404(Session, id=session_id)
        
        # Get timetable entries
        timetables = Timetable.objects.filter(
            course=selected_course,
            session=selected_session
        ).select_related('subject', 'staff', 'time_slot')
        
        # Organize by day and time slot
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        timetable_data = {}
        
        for day in days:
            timetable_data[day] = {}
            for timeslot in timeslots:
                entry = timetables.filter(day_of_week=day, time_slot=timeslot).first()
                timetable_data[day][timeslot.id] = entry
    
    context = {
        'courses': courses,
        'sessions': sessions,
        'timeslots': timeslots,
        'timetable_data': timetable_data,
        'selected_course': selected_course,
        'selected_session': selected_session,
        'days': [('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), 
                 ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday')],
        'page_title': 'View Timetable'
    }
    return render(request, 'registrar_template/registrar_view_timetable.html', context)
