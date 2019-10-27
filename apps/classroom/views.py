from django.shortcuts import render
from django.contrib.auth.views import reverse_lazy
from django.utils.decorators import method_decorator
from .decorators import form_invalid_decorator
from .models import Classroom
from .form import ClassroomForm
from django.db.models import Q
from sweetify.views import SweetifySuccessMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


class Index(ListView):
    model = Classroom
    template_name = 'classroom/index.html'
    paginate_by = 5
    extra_context = {
        'title': 'Aulas'
    }


@method_decorator(form_invalid_decorator, name='form_invalid')
class Create(SweetifySuccessMixin, CreateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'classroom/form.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Aula guardada correctamente!'
    success_url = reverse_lazy('classroom:index')
    extra_context = {
        'title': 'Registrar',
        'titleButton': 'Guardar'
    }


@method_decorator(form_invalid_decorator, name='form_invalid')
class Edit(SweetifySuccessMixin, UpdateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'classroom/form.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Editado correctamente!'
    success_url = reverse_lazy('classroom:index')
    extra_context = {
        'title': 'Editar',
        'titleButton': 'Actualizar'
    }


class Delete(DeleteView):
    model = Classroom

    def delete(self, request, *args, **kwargs):
        classroom = self.get_object()
        classroom.delete()
        return render(self.request, 'classroom/table.html')


class Table(ListView):
    model = Classroom
    template_name = 'classroom/table.html'
    paginate_by = 5


class Search(ListView):
    model = Classroom
    template_name = 'classroom/table.html'
    paginate_by = 5

    def get_queryset(self):
        find = self.kwargs['find']
        return self.model.objects.filter(Q(name__icontains=find))
