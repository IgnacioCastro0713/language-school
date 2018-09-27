from django.shortcuts import render, redirect
from apps.classroom.models import Classroom
from apps.classroom.form import ClassroomForm
from sweetify import *


def index(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classroom/index.html', {
        'object_list': classrooms,
        'title': 'Aulas',
    })


def create(request):
    if request.method == 'POST':
        ClassroomForm(request.POST).save()
        success(request, 'Aula guardada correctamente!', toast=True, position='top', timer=2000)
        return redirect('classroom:index')


def edit(request, id_class):
    pass


def show(request, id_class):
    pass
