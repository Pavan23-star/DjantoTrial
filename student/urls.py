from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [
    path('', views.homeview, name='homeview'),
    path('students/', views.studentlistView, name='studentlistView'),
    path('lecturers/', views.lecturerslistView, name='lecturerslistView'),
    path('courses/', views.courselistView, name='courselistView'),
    path('subjects/', views.subjectslistView, name='subjectslistView'),
    path('courseDetails/<int:record_id>/', views.coursedetailView, name='coursedetailView'),
    path('subject-lectures/<int:record_id>/', views.subjectlecturerView, name="subjectlecturerView"),
    ]