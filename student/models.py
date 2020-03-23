from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=20, unique=True)
    credit_points = models.IntegerField(validators=[MaxValueValidator(10)])

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(unique=True, max_length=50)
    subjects = models.ManyToManyField(Subject)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name

    def get_sub_values(self):
        return self.subjects.filter(course__subjects__in=self.name)


class Student(models.Model):
    name = models.CharField(max_length=25)
    roll_num = models.IntegerField(unique=True)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=25)
    subjects_taken = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Lecturer'
        verbose_name_plural = 'Lecturers'

    def __str__(self):
        return self.name
