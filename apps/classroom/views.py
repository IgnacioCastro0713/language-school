from django.shortcuts import render
from django.contrib.auth.views import reverse_lazy
from apps.classroom.models import Classroom
from apps.classroom.form import ClassroomForm
from apps.home.pagination import paginate
from django.db.models import Q
from sweetify.views import SweetifySuccessMixin
from sweetify import warning
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


class Create(SweetifySuccessMixin, CreateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'classroom/create.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Aula guardada correctamente!'
    success_url = reverse_lazy('classroom:index')
    extra_context = {'title': 'Registrar'}

    def form_invalid(self, form):
        warning(self.request, 'Verifique la información ingresada.', toast=True, position='top', timer=3000)
        return self.render_to_response(self.get_context_data(form=form))


class Edit(SweetifySuccessMixin, UpdateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'classroom/edit.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Editado correctamente!'
    success_url = reverse_lazy('classroom:index')
    extra_context = {'title': 'Editar'}

    def form_invalid(self, form):
        warning(self.request, 'Verifique la información ingresada.', toast=True, position='top', timer=3000)
        return self.render_to_response(self.get_context_data(form=form))


class Delete(DeleteView):
    model = Classroom

    def delete(self, request, *args, **kwargs):
        classroom = self.get_object()
        classroom.delete()
        return render(self.request, 'classroom/table.html')


class Table(ListView):
    model = Classroom
    paginate_by = 5
    template_name = 'classroom/table.html'


def search(request, find):
    classrooms_list = Classroom.objects.filter(Q(name__icontains=find))
    classrooms = paginate(request, classrooms_list, 100)
    return render(request, 'classroom/table.html', {'object_list': classrooms})
