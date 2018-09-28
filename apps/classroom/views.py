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

    return render(request, 'classroom/create.html', {
        'form': ClassroomForm,
        'title': 'Registrar'
    })


def edit(request, id_class):
    classrooms = Classroom.objects.get(pk=id_class)
    if request.method == 'POST':
        ClassroomForm(request.POST, instance=classrooms).save()
        success(request, 'Editado correctamente!', toast=True, position='top', timer=2000)
        return redirect('classroom:index')

    return render(request, 'classroom/edit.html', {
        'form': ClassroomForm(instance=classrooms),
        'title': 'Editar'
    })


def delete(request, id_class):
    Classroom.objects.get(pk=id_class).delete()
    return render(request, 'classroom/table.html')


def table(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classroom/table.html', {'object_list': classrooms})

