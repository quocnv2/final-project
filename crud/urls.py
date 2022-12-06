from django.urls import path

from . import views


urlpatterns = [
    path('student/', views.show_list_student, name='show_list_student'),
    path('student/create', views.student_create, name='student_create'),
    path("student/<int:id>/edit/",
         views.student_edit, name="student_edit"),
    path("student/<int:id>/delete/",
         views.student_delete, name="student_delete"),
]
