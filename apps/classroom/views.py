from django.shortcuts import render
from django.contrib.auth.views import reverse_lazy
from apps.classroom.models import Classroom
from apps.classroom.form import ClassroomForm
from apps.home.pagination import paginate
from django.db.models import Q
from sweetify.views import *
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


class Index(ListView):
    model = Classroom
    template_name = 'classroom/index.html'
    extra_context = {
        'title': 'Aulas'
    }


class Create(SweetifySuccessMixin, CreateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'classroom/create.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2000}
    success_message = 'Aula guardada correctamente!'
    success_url = reverse_lazy('classroom:index')
    extra_context = {'title': 'Registrar'}


class Edit(SweetifySuccessMixin, UpdateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'classroom/edit.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2000}
    success_message = 'Editado correctamente!'
    success_url = reverse_lazy('classroom:index')
    extra_context = {'title': 'Editar'}


class Delete(DeleteView):
    model = Classroom

    def delete(self, request, *args, **kwargs):
        classroom = self.get_object()
        classroom.delete()
        return render(self.request, 'classroom/table.html')


class Table(ListView):
    model = Classroom
    template_name = 'classroom/table.html'


def search(request, find):
    classrooms_list = Classroom.objects.filter(
        Q(name__icontains=find) |
        Q(building__icontains=find))
    classrooms = paginate(request, classrooms_list, 5)
    return render(request, 'classroom/table.html', {'object_list': classrooms})
