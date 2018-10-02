from django.shortcuts import render
from django.contrib.auth.views import reverse_lazy
from apps.course.models import Course
from apps.course.form import CourseForm
from django.db.models import Q
from sweetify.views import *
from apps.home.pagination import paginate
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
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2000}
    success_message = 'Curso guardado correctamente!'
    success_url = reverse_lazy('course:index')
    extra_context = {'title': 'Registrar'}


class Edit(SweetifySuccessMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/edit.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2000}
    success_message = 'Editado correctamente!'
    success_url = reverse_lazy('course:index')
    extra_context = {'title': 'Editar'}


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


def search(request, find):
    courses_list = Course.objects.filter(
        Q(name__icontains=find))
    courses = paginate(request, courses_list, 100)
    return render(request, 'course/table.html', {'object_list': courses})
