from django.shortcuts import render, redirect
from apps.classroom.models import Classroom
from apps.classroom.form import ClassroomForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from sweetify import *


def index(request):
    classrooms_list = Classroom.objects.all()
    paginator = Paginator(classrooms_list, 2)
    page = request.GET.get('page')
    # classrooms = paginator.get_page(page)

    try:
        classrooms = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        classrooms = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        classrooms = paginator.page(paginator.num_pages)

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
    classrooms_list = Classroom.objects.all()
    paginator = Paginator(classrooms_list, 2)
    page = request.GET.get('page')
    # classrooms = paginator.get_page(page)

    try:
        classrooms = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        classrooms = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        classrooms = paginator.page(paginator.num_pages)

    return render(request, 'classroom/table.html', {
        'object_list': classrooms,
    })


def search(request, find):
    classrooms = Classroom.objects.filter(
        Q(name__icontains=find) |
        Q(building__icontains=find))
    return render(request, 'classroom/table.html', {'object_list': classrooms})
