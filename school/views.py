from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    student_objects = Student.objects.all()
    students = student_objects.order_by('group')
    teachers = Teacher.objects.all()
    context = {'students': students, 'teachers': teachers}
    print(students)
    print(teachers)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'

    return render(request, template, context)
