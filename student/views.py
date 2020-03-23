from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

# Create your views here.
import student
from student.models import Student, Lecturer, Course, Subject


def homeview(request):
    return render(request, 'home.html')


def studentlistView(request):
    total_list = Student.objects.order_by('roll_num')
    context = {'total_list': total_list}
    return render(request, 'studentlist.html', context)


def lecturerslistView(request):
    total_list = Lecturer.objects.order_by('name')
    context = {'total_list': total_list}
    return render(request, 'lecturerlist.html', context)


def courselistView(request):
    total_list = Course.objects.order_by('name')
    context = {
        'total_list': total_list,
               }
    return render(request, 'courselist.html', context)


def subjectslistView(request):
    total_list = Subject.objects.order_by('name')
    context = {'total_list': total_list}
    return render(request, 'subjectlist.html', context)


def coursedetailView(request, record_id):
    selected_course = Course.objects.get(id=record_id)
    subjects_included = selected_course.subjects.all()
    context = {
        'selected_course':selected_course,
        'subjects_included':subjects_included
    }
    return render(request, 'details.html', context)


def subjectlecturerView(request, record_id):
    selected_subject = Subject.objects.get(id=record_id)
    lecturers_list = selected_subject.lecturer_set.all()
    context = {
        'selected_subject':selected_subject,
        'lecturers_list':lecturers_list

    }
    return render(request, 'subjectlecture.html', context)
