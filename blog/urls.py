from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # Role-based home pages
    path("student/home/", views.student_home, name="student_home"),
    path("teacher/home/<int:id>/", views.teacher_home, name="teacher_home"),
    # Student-specific pages
    path("student/lessons/", views.student_lessons, name="student_lessons"),
    path("student/reyting/", views.student_reyting, name="student_reyting"),
    path("student/setting/", views.student_setting, name="student_setting"),
    # Teacher-specific pages
    path("teacher/lessons/", views.teacher_lessons, name="teacher_lessons"),
    path("teacher/reyting/", views.teacher_reyting, name="teacher_reyting"),
    path("teacher/setting/", views.teacher_setting, name="teacher_setting"),
    path("teacher/<int:teacher_id>/guruhlar/<int:group_id>/", 
     views.teacher_group_detail, 
     name="teacher_group_detail"),
    # Logout
    path("logout/", views.logout_view, name="logout"),
]
