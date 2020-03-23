from django.contrib import admin
from .models import Subject, Student, Course, Lecturer

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_num', 'courses')


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Lecturer)
