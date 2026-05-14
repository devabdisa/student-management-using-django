import json
import math
from datetime import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *


def student_home(request):
    student = get_object_or_404(Student, admin=request.user)
    total_subject = Subject.objects.filter(course=student.course).count()
    total_attendance = AttendanceReport.objects.filter(student=student).count()
    total_present = AttendanceReport.objects.filter(student=student, status=True).count()
    if total_attendance == 0:  # Don't divide. DivisionByZero
        percent_absent = percent_present = 0
    else:
        percent_present = math.floor((total_present/total_attendance) * 100)
        percent_absent = math.ceil(100 - percent_present)
    subject_name = []
    data_present = []
    data_absent = []
    subjects = Subject.objects.filter(course=student.course)
    for subject in subjects:
        attendance = Attendance.objects.filter(subject=subject)
        present_count = AttendanceReport.objects.filter(
            attendance__in=attendance, status=True, student=student).count()
        absent_count = AttendanceReport.objects.filter(
            attendance__in=attendance, status=False, student=student).count()
        subject_name.append(subject.name)
        data_present.append(present_count)
        data_absent.append(absent_count)
    context = {
        'total_attendance': total_attendance,
        'percent_present': percent_present,
        'percent_absent': percent_absent,
        'total_subject': total_subject,
        'subjects': subjects,
        'data_present': data_present,
        'data_absent': data_absent,
        'data_name': subject_name,
        'page_title': 'Student Homepage'

    }
    return render(request, 'student_template/home_content.html', context)


@ csrf_exempt
def student_view_attendance(request):
    student = get_object_or_404(Student, admin=request.user)
    if request.method != 'POST':
        course = get_object_or_404(Course, id=student.course.id)
        context = {
            'subjects': Subject.objects.filter(course=course),
            'page_title': 'View Attendance'
        }
        return render(request, 'student_template/student_view_attendance.html', context)
    else:
        subject_id = request.POST.get('subject')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')
        try:
            subject = get_object_or_404(Subject, id=subject_id)
            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")
            attendance = Attendance.objects.filter(
                date__range=(start_date, end_date), subject=subject)
            attendance_reports = AttendanceReport.objects.filter(
                attendance__in=attendance, student=student).select_related('attendance')
            json_data = []
            for report in attendance_reports:
                data = {
                    "date":  str(report.attendance.date),
                    "status": report.status
                }
                json_data.append(data)
            return JsonResponse(json.dumps(json_data), safe=False)
        except Exception as e:
            return None


def student_apply_leave(request):
    form = LeaveReportStudentForm(request.POST or None)
    student = get_object_or_404(Student, admin_id=request.user.id)
    context = {
        'form': form,
        'leave_history': LeaveReportStudent.objects.filter(student=student),
        'page_title': 'Apply for leave'
    }
    if request.method == 'POST':
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.student = student
                obj.save()
                messages.success(
                    request, "Application for leave has been submitted for review")
                return redirect(reverse('student_apply_leave'))
            except Exception:
                messages.error(request, "Could not submit")
        else:
            messages.error(request, "Form has errors!")
    return render(request, "student_template/student_apply_leave.html", context)


def student_feedback(request):
    form = FeedbackStudentForm(request.POST or None)
    student = get_object_or_404(Student, admin_id=request.user.id)
    context = {
        'form': form,
        'feedbacks': FeedbackStudent.objects.filter(student=student),
        'page_title': 'Student Feedback'

    }
    if request.method == 'POST':
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.student = student
                obj.save()
                messages.success(
                    request, "Feedback submitted for review")
                return redirect(reverse('student_feedback'))
            except Exception:
                messages.error(request, "Could not Submit!")
        else:
            messages.error(request, "Form has errors!")
    return render(request, "student_template/student_feedback.html", context)


def student_view_profile(request):
    student = get_object_or_404(Student, admin=request.user)
    form = StudentEditForm(request.POST or None, request.FILES or None,
                           instance=student)
    context = {'form': form,
               'page_title': 'View/Edit Profile'
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
                admin = student.admin
                if password != None:
                    admin.set_password(password)
                if passport != None:
                    fs = FileSystemStorage()
                    filename = fs.save(passport.name, passport)
                    passport_url = fs.url(filename)
                    admin.profile_pic = passport_url
                admin.first_name = first_name
                admin.last_name = last_name
                admin.address = address
                admin.gender = gender
                admin.save()
                student.save()
                messages.success(request, "Profile Updated!")
                return redirect(reverse('student_view_profile'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(request, "Error Occured While Updating Profile " + str(e))

    return render(request, "student_template/student_view_profile.html", context)


@csrf_exempt
def student_fcmtoken(request):
    token = request.POST.get('token')
    student_user = get_object_or_404(CustomUser, id=request.user.id)
    try:
        student_user.fcm_token = token
        student_user.save()
        return HttpResponse("True")
    except Exception as e:
        return HttpResponse("False")


def student_view_notification(request):
    student = get_object_or_404(Student, admin=request.user)
    notifications = NotificationStudent.objects.filter(student=student)
    context = {
        'notifications': notifications,
        'page_title': "View Notifications"
    }
    return render(request, "student_template/student_view_notification.html", context)


def student_view_result(request):
    student = get_object_or_404(Student, admin=request.user)
    results = StudentResult.objects.filter(student=student)
    context = {
        'results': results,
        'page_title': "View Results"
    }
    return render(request, "student_template/student_view_result.html", context)


# ==================== TIMETABLE VIEW ====================

def student_view_timetable(request):
    """View student's class timetable"""
    from .models import TimeSlot, Timetable
    
    student = get_object_or_404(Student, admin=request.user)
    timeslots = TimeSlot.objects.all().order_by('order', 'start_time')
    
    timetable_data = None
    
    if student.course and student.session:
        # Get timetable entries for this student's course and session
        timetables = Timetable.objects.filter(
            course=student.course,
            session=student.session
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
        'timeslots': timeslots,
        'timetable_data': timetable_data,
        'student': student,
        'days': [('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), 
                 ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday')],
        'page_title': 'My Class Timetable'
    }
    return render(request, 'student_template/student_view_timetable.html', context)


# ==================== STUDY SCHEDULE ====================

def student_study_schedule(request):
    """View and manage personal study schedule"""
    student = get_object_or_404(Student, admin=request.user)
    subjects = Subject.objects.filter(course=student.course)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            subject_id = request.POST.get('subject')
            day = request.POST.get('day_of_week')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            topic = request.POST.get('topic')
            priority = request.POST.get('priority', 'medium')
            notes = request.POST.get('notes', '')
            try:
                subject = get_object_or_404(Subject, id=subject_id)
                StudySchedule.objects.create(
                    student=student, subject=subject, day_of_week=day,
                    start_time=start_time, end_time=end_time,
                    topic=topic, priority=priority, notes=notes
                )
                messages.success(request, "Study session added successfully!")
            except Exception as e:
                messages.error(request, f"Could not add session: {str(e)}")
            return redirect(reverse('student_study_schedule'))

        elif action == 'toggle':
            schedule_id = request.POST.get('schedule_id')
            try:
                schedule = get_object_or_404(StudySchedule, id=schedule_id, student=student)
                schedule.is_completed = not schedule.is_completed
                schedule.save()
                return JsonResponse({'status': 'ok', 'completed': schedule.is_completed})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

        elif action == 'delete':
            schedule_id = request.POST.get('schedule_id')
            try:
                schedule = get_object_or_404(StudySchedule, id=schedule_id, student=student)
                schedule.delete()
                messages.success(request, "Study session deleted.")
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
            return redirect(reverse('student_study_schedule'))

    # Organize schedules by day
    days_order = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day_labels = {'MON': 'Monday', 'TUE': 'Tuesday', 'WED': 'Wednesday',
                  'THU': 'Thursday', 'FRI': 'Friday', 'SAT': 'Saturday', 'SUN': 'Sunday'}

    all_schedules = StudySchedule.objects.filter(student=student).select_related('subject')
    schedule_by_day = {day: [] for day in days_order}
    for s in all_schedules:
        schedule_by_day[s.day_of_week].append(s)

    # Build a list of (code, label, sessions) for the template
    schedule_days = [(day, day_labels[day], schedule_by_day[day]) for day in days_order]

    total = all_schedules.count()
    completed = all_schedules.filter(is_completed=True).count()

    context = {
        'subjects': subjects,
        'schedule_days': schedule_days,
        'total': total,
        'completed': completed,
        'pending': total - completed,
        'page_title': 'My Study Plan & Schedule',
    }
    return render(request, 'student_template/student_study_schedule.html', context)



# ==================== MARKS PLAN ====================

def student_marks_plan(request):
    """View and manage personal marks targets"""
    student = get_object_or_404(Student, admin=request.user)
    subjects = Subject.objects.filter(course=student.course)
    results = {r.subject_id: r for r in StudentResult.objects.filter(student=student)}

    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        target_test = request.POST.get('target_test_marks', 0)
        target_exam = request.POST.get('target_exam_marks', 0)
        notes = request.POST.get('notes', '')
        try:
            subject = get_object_or_404(Subject, id=subject_id)
            plan, created = MarksPlan.objects.update_or_create(
                student=student, subject=subject,
                defaults={
                    'target_test_marks': float(target_test),
                    'target_exam_marks': float(target_exam),
                    'notes': notes,
                }
            )
            messages.success(request, f"Target for {subject.name} saved!")
        except Exception as e:
            messages.error(request, f"Could not save: {str(e)}")
        return redirect(reverse('student_marks_plan'))

    plans = {p.subject_id: p for p in MarksPlan.objects.filter(student=student)}

    subject_data = []
    for subj in subjects:
        plan = plans.get(subj.id)
        result = results.get(subj.id)
        actual_test = result.test if result else 0
        actual_exam = result.exam if result else 0
        target_test = plan.target_test_marks if plan else 0
        target_exam = plan.target_exam_marks if plan else 0
        subject_data.append({
            'subject': subj,
            'plan': plan,
            'result': result,
            'actual_test': actual_test,
            'actual_exam': actual_exam,
            'target_test': target_test,
            'target_exam': target_exam,
            'test_pct': min(100, round((actual_test / target_test * 100) if target_test > 0 else 0)),
            'exam_pct': min(100, round((actual_exam / target_exam * 100) if target_exam > 0 else 0)),
        })

    context = {
        'subject_data': subject_data,
        'subjects': subjects,
        'page_title': 'My Marks Plan',
    }
    return render(request, 'student_template/student_marks_plan.html', context)


# ==================== STUDENT TEACHER FEEDBACK ====================

def student_teacher_feedback(request):
    """View and submit feedback directly to specific teachers"""
    student = get_object_or_404(Student, admin=request.user)
    subjects = Subject.objects.filter(course=student.course)
    staff_list = Staff.objects.filter(id__in=subjects.values_list('staff_id', flat=True)).distinct()
    feedbacks = StudentTeacherFeedback.objects.filter(student=student)

    if request.method == 'POST':
        staff_id = request.POST.get('staff')
        subject_id = request.POST.get('subject')
        rating = request.POST.get('rating')
        category = request.POST.get('category')
        message = request.POST.get('message')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        
        try:
            staff = get_object_or_404(Staff, id=staff_id)
            subject = None
            if subject_id:
                subject = get_object_or_404(Subject, id=subject_id)
            
            StudentTeacherFeedback.objects.create(
                student=student, staff=staff, subject=subject,
                rating=rating, category=category, message=message,
                is_anonymous=is_anonymous
            )
            messages.success(request, "Feedback sent successfully!")
            return redirect(reverse('student_teacher_feedback'))
        except Exception as e:
            messages.error(request, f"Error sending feedback: {str(e)}")

    context = {
        'staff_list': staff_list,
        'subjects': subjects,
        'feedbacks': feedbacks,
        'page_title': 'Send Feedback to Teachers'
    }
    return render(request, 'student_template/student_teacher_feedback.html', context)



# ==================== STUDY SCHEDULE ====================

def student_study_schedule(request):
    """View and manage personal study schedule"""
    student = get_object_or_404(Student, admin=request.user)
    subjects = Subject.objects.filter(course=student.course)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            subject_id = request.POST.get('subject')
            day = request.POST.get('day_of_week')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            topic = request.POST.get('topic')
            priority = request.POST.get('priority', 'medium')
            notes = request.POST.get('notes', '')
            try:
                subject = get_object_or_404(Subject, id=subject_id)
                StudySchedule.objects.create(
                    student=student, subject=subject, day_of_week=day,
                    start_time=start_time, end_time=end_time,
                    topic=topic, priority=priority, notes=notes
                )
                messages.success(request, "Study session added successfully!")
            except Exception as e:
                messages.error(request, f"Could not add session: {str(e)}")
            return redirect(reverse('student_study_schedule'))

        elif action == 'toggle':
            schedule_id = request.POST.get('schedule_id')
            try:
                schedule = get_object_or_404(StudySchedule, id=schedule_id, student=student)
                schedule.is_completed = not schedule.is_completed
                schedule.save()
                return JsonResponse({'status': 'ok', 'completed': schedule.is_completed})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

        elif action == 'delete':
            schedule_id = request.POST.get('schedule_id')
            try:
                schedule = get_object_or_404(StudySchedule, id=schedule_id, student=student)
                schedule.delete()
                messages.success(request, "Study session deleted.")
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
            return redirect(reverse('student_study_schedule'))

    # Organize schedules by day
    days_order = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day_labels = {'MON': 'Monday', 'TUE': 'Tuesday', 'WED': 'Wednesday',
                  'THU': 'Thursday', 'FRI': 'Friday', 'SAT': 'Saturday', 'SUN': 'Sunday'}

    all_schedules = StudySchedule.objects.filter(student=student).select_related('subject')
    schedule_by_day = {day: [] for day in days_order}
    for s in all_schedules:
        schedule_by_day[s.day_of_week].append(s)

    # Build a list of (code, label, sessions) for the template
    schedule_days = [(day, day_labels[day], schedule_by_day[day]) for day in days_order]

    total = all_schedules.count()
    completed = all_schedules.filter(is_completed=True).count()

    context = {
        'subjects': subjects,
        'schedule_days': schedule_days,
        'total': total,
        'completed': completed,
        'pending': total - completed,
        'page_title': 'My Study Plan & Schedule',
    }
    return render(request, 'student_template/student_study_schedule.html', context)



# ==================== MARKS PLAN ====================

def student_marks_plan(request):
    """View and manage personal marks targets"""
    student = get_object_or_404(Student, admin=request.user)
    subjects = Subject.objects.filter(course=student.course)
    results = {r.subject_id: r for r in StudentResult.objects.filter(student=student)}

    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        target_test = request.POST.get('target_test_marks', 0)
        target_exam = request.POST.get('target_exam_marks', 0)
        notes = request.POST.get('notes', '')
        try:
            subject = get_object_or_404(Subject, id=subject_id)
            plan, created = MarksPlan.objects.update_or_create(
                student=student, subject=subject,
                defaults={
                    'target_test_marks': float(target_test),
                    'target_exam_marks': float(target_exam),
                    'notes': notes,
                }
            )
            messages.success(request, f"Target for {subject.name} saved!")
        except Exception as e:
            messages.error(request, f"Could not save: {str(e)}")
        return redirect(reverse('student_marks_plan'))

    plans = {p.subject_id: p for p in MarksPlan.objects.filter(student=student)}

    subject_data = []
    for subj in subjects:
        plan = plans.get(subj.id)
        result = results.get(subj.id)
        actual_test = result.test if result else 0
        actual_exam = result.exam if result else 0
        target_test = plan.target_test_marks if plan else 0
        target_exam = plan.target_exam_marks if plan else 0
        subject_data.append({
            'subject': subj,
            'plan': plan,
            'result': result,
            'actual_test': actual_test,
            'actual_exam': actual_exam,
            'target_test': target_test,
            'target_exam': target_exam,
            'test_pct': min(100, round((actual_test / target_test * 100) if target_test > 0 else 0)),
            'exam_pct': min(100, round((actual_exam / target_exam * 100) if target_exam > 0 else 0)),
        })

    context = {
        'subject_data': subject_data,
        'subjects': subjects,
        'page_title': 'My Marks Plan',
    }
    return render(request, 'student_template/student_marks_plan.html', context)

