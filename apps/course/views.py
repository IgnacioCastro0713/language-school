from django.shortcuts import render
from django.contrib.auth.views import reverse_lazy
from apps.course.models import Course
from apps.course.form import CourseForm
from django.db.models import Q
from sweetify.views import SweetifySuccessMixin
from sweetify import warning
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)


class Index(ListView):
    model = Course
    template_name = 'course/index.html'
    paginate_by = 5
    extra_context = {
        'title': 'Cursos'
    }


class Create(SweetifySuccessMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/create.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Curso guardado correctamente!'
    success_url = reverse_lazy('course:index')
    extra_context = {'title': 'Registrar'}

    def form_invalid(self, form):
        warning(self.request, '¡Verifique la información ingresada!', toast=True, position='top', timer=3000)
        return self.render_to_response(self.get_context_data(form=form))


class Edit(SweetifySuccessMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/edit.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Editado correctamente!'
    success_url = reverse_lazy('course:index')
    extra_context = {'title': 'Editar'}

    def form_invalid(self, form):
        warning(self.request, '¡Verifique la información ingresada!', toast=True, position='top', timer=3000)
        return self.render_to_response(self.get_context_data(form=form))


class Show(DetailView):
    model = Course

    def get(self, request, *args, **kwargs):
        course = self.get_object()
        return render(self.request, 'course/show.html', {'object_list': course})


class Delete(DeleteView):
    model = Course

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        course.delete()
        return render(self.request, 'course/table.html')


class Table(ListView):
    model = Course
    template_name = 'course/table.html'
    paginate_by = 5


class Search(ListView):
    model = Course
    template_name = 'course/table.html'
    paginate_by = 5

    def get_queryset(self):
        find = self.kwargs['find']
        return self.model.objects.filter(Q(name__icontains=find) |
                                         Q(day__icontains=find))
