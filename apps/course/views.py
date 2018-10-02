from django.shortcuts import render, redirect
from django.contrib.auth.views import reverse_lazy
from apps.course.models import Course
from apps.course.form import CourseForm
from django.db.models import Q
from sweetify import *
from sweetify.views import *
from apps.home.pagination import paginate
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    DetailView,
)


class Index(TemplateView):
    template_name = 'course/index.html'
    extra_context = {
        'object_list': Course.objects.all(),
        'title': 'Cursos'
    }


class Create(SweetifySuccessMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'user/create.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2000}
    success_message = 'Curso guardado correctamente!'
    success_url = reverse_lazy('course:index')
    extra_context = {'title': 'Registrar'}


def edit(request, id_course):
    course = Course.objects.get(pk=id_course)
    if request.method == 'POST':
        CourseForm(request.POST, instance=course).save()
        success(request, 'Editado correctamente!', toast=True, position='top', timer=2000)
        return redirect('course:index')

    return render(request, 'course/edit.html', {
        'form': CourseForm(instance=course),
        'title': 'Editar',
    })


class Show(DetailView):
    model = Course

    def get(self, request, *args, **kwargs):
        course = self.get_object()
        return render(self.request, 'course/show.html', {'object_list': course})


def delete(request, id_course):
    Course.objects.get(pk=id_course).delete()
    return render(request, 'course/table.html')


def table(request):
    courses = paginate(request, Course.objects.all(), 5)
    return render(request, 'course/table.html', {'object_list': courses})


def search(request, find):
    courses_list = Course.objects.filter(
        Q(name__icontains=find))
    courses = paginate(request, courses_list, 5)
    return render(request, 'course/table.html', {'object_list': courses})
