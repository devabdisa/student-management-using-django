"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main_app.EditResultView import EditResultView

from . import hod_views, staff_views, student_views, registrar_views, guardian_views, views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("get_attendance", views.get_attendance, name='get_attendance'),
    path("firebase-messaging-sw.js", views.showFirebaseJS, name='showFirebaseJS'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),
    path("admin/home/", hod_views.admin_home, name='admin_home'),
    path("staff/add", hod_views.add_staff, name='add_staff'),
    path("course/add", hod_views.add_course, name='add_course'),
    path("send_student_notification/", hod_views.send_student_notification,
         name='send_student_notification'),
    path("send_staff_notification/", hod_views.send_staff_notification,
         name='send_staff_notification'),
    path("add_session/", hod_views.add_session, name='add_session'),
    path("admin_view_profile", hod_views.admin_view_profile,
         name='admin_view_profile'),
    path("check_email_availability", hod_views.check_email_availability,
         name="check_email_availability"),
    path("session/manage/", hod_views.manage_session, name='manage_session'),
    path("session/edit/<int:session_id>",
         hod_views.edit_session, name='edit_session'),
    path("student/view/feedback/", hod_views.student_feedback_message,
         name="student_feedback_message",),
    path("staff/view/feedback/", hod_views.staff_feedback_message,
         name="staff_feedback_message",),
    path("attendance/view/", hod_views.admin_view_attendance,
         name="admin_view_attendance",),
    path("attendance/fetch/", hod_views.get_admin_attendance,
         name='get_admin_attendance'),
    path("student/add/", hod_views.add_student, name='add_student'),
    path("subject/add/", hod_views.add_subject, name='add_subject'),
    path("staff/manage/", hod_views.manage_staff, name='manage_staff'),
    path("student/manage/", hod_views.manage_student, name='manage_student'),
    path("course/manage/", hod_views.manage_course, name='manage_course'),
    path("subject/manage/", hod_views.manage_subject, name='manage_subject'),
    path("staff/view/<int:staff_id>", hod_views.view_staff, name='view_staff'),
    path("staff/edit/<int:staff_id>", hod_views.edit_staff, name='edit_staff'),
    path("staff/delete/<int:staff_id>",
         hod_views.delete_staff, name='delete_staff'),

    path("course/delete/<int:course_id>",
         hod_views.delete_course, name='delete_course'),

    path("subject/delete/<int:subject_id>",
         hod_views.delete_subject, name='delete_subject'),

    path("session/delete/<int:session_id>",
         hod_views.delete_session, name='delete_session'),

    path("student/delete/<int:student_id>",
         hod_views.delete_student, name='delete_student'),
    path("student/view/<int:student_id>",
         hod_views.view_student, name='view_student'),
    path("student/edit/<int:student_id>",
         hod_views.edit_student, name='edit_student'),
    path("course/edit/<int:course_id>",
         hod_views.edit_course, name='edit_course'),
    path("subject/edit/<int:subject_id>",
         hod_views.edit_subject, name='edit_subject'),

    # Admin/HOD Timetable Management
    path("timeslot/manage/", hod_views.manage_timeslot, name='manage_timeslot'),
    path("timeslot/add/", hod_views.add_timeslot, name='add_timeslot'),
    path("timeslot/edit/<int:timeslot_id>/", hod_views.edit_timeslot, name='edit_timeslot'),
    path("timeslot/delete/<int:timeslot_id>/", hod_views.delete_timeslot, name='delete_timeslot'),
    path("timetable/manage/", hod_views.manage_timetable, name='manage_timetable'),
    path("timetable/add/", hod_views.add_timetable, name='add_timetable'),
    path("timetable/edit/<int:timetable_id>/", hod_views.edit_timetable, name='edit_timetable'),
    path("timetable/delete/<int:timetable_id>/", hod_views.delete_timetable, name='delete_timetable'),
    path("timetable/view/", hod_views.view_timetable, name='view_timetable'),

    # Staff
    path("staff/home/", staff_views.staff_home, name='staff_home'),
    path("staff/feedback/", staff_views.staff_feedback, name='staff_feedback'),
    path("staff/view/profile/", staff_views.staff_view_profile,
         name='staff_view_profile'),
    path("staff/attendance/take/", staff_views.staff_take_attendance,
         name='staff_take_attendance'),
    path("staff/attendance/update/", staff_views.staff_update_attendance,
         name='staff_update_attendance'),
    path("staff/get_students/", staff_views.get_students, name='get_students'),
    path("staff/attendance/fetch/", staff_views.get_student_attendance,
         name='get_student_attendance'),
    path("staff/attendance/save/",
         staff_views.save_attendance, name='save_attendance'),
    path("staff/attendance/update/",
         staff_views.update_attendance, name='update_attendance'),
    path("staff/fcmtoken/", staff_views.staff_fcmtoken, name='staff_fcmtoken'),
    path("staff/result/add/", staff_views.staff_add_result, name='staff_add_result'),
    path("staff/result/edit/", EditResultView.as_view(),
         name='edit_student_result'),
    path('staff/result/fetch/', staff_views.fetch_student_result,
         name='fetch_student_result'),
    path("staff/view/timetable/", staff_views.staff_view_timetable,
         name='staff_view_timetable'),



    # Student
    path("student/home/", student_views.student_home, name='student_home'),
    path("student/view/attendance/", student_views.student_view_attendance,
         name='student_view_attendance'),
    path("student/feedback/", student_views.student_feedback,
         name='student_feedback'),
    path("student/view/profile/", student_views.student_view_profile,
         name='student_view_profile'),
    path("student/fcmtoken/", student_views.student_fcmtoken,
         name='student_fcmtoken'),
    path('student/view/result/', student_views.student_view_result,
         name='student_view_result'),
    path("student/view/timetable/", student_views.student_view_timetable,
         name='student_view_timetable'),
    path("student/study-schedule/", student_views.student_study_schedule,
         name='student_study_schedule'),
    path("student/marks-plan/", student_views.student_marks_plan,
         name='student_marks_plan'),


    # Registrar
    path("registrar/home/", registrar_views.registrar_home, name='registrar_home'),
    path("registrar/view/profile/", registrar_views.registrar_view_profile,
         name='registrar_view_profile'),
    path("registrar/view/students/", registrar_views.registrar_view_students,
         name='registrar_view_students'),
    path("registrar/view/staff/", registrar_views.registrar_view_staff,
         name='registrar_view_staff'),
    path("registrar/view/courses/", registrar_views.registrar_view_courses,
         name='registrar_view_courses'),
    path("registrar/view/subjects/", registrar_views.registrar_view_subjects,
         name='registrar_view_subjects'),
    path("registrar/view/attendance/", registrar_views.registrar_view_attendance,
         name='registrar_view_attendance'),
    path("registrar/attendance/fetch/", registrar_views.registrar_get_attendance,
         name='registrar_get_attendance'),
    path("registrar/view/results/", registrar_views.registrar_view_results,
         name='registrar_view_results'),
    path("registrar/results/fetch/", registrar_views.registrar_get_student_results,
         name='registrar_get_student_results'),
    path("registrar/view/timetable/", registrar_views.registrar_view_timetable,
         name='registrar_view_timetable'),

    # Guardian
    path("guardian/home/", guardian_views.guardian_home, name='guardian_home'),
    path("guardian/view/profile/", guardian_views.guardian_view_profile,
         name='guardian_view_profile'),
    path("guardian/view/children/", guardian_views.guardian_view_children,
         name='guardian_view_children'),
    path("guardian/view/child/<int:student_id>/", guardian_views.guardian_view_child_detail,
         name='guardian_view_child_detail'),
    path("guardian/view/child/<int:student_id>/attendance/", guardian_views.guardian_view_child_attendance,
         name='guardian_view_child_attendance'),
    path("guardian/view/child/<int:student_id>/results/", guardian_views.guardian_view_child_results,
         name='guardian_view_child_results'),
    path("guardian/view/timetable/<int:student_id>/", guardian_views.guardian_view_timetable,
         name='guardian_view_timetable'),

]
