from django.shortcuts import render, redirect
from django.contrib.auth.views import reverse_lazy
from apps.user.models import User
from apps.user.form import UserForm
from django.db.models import Q
from sweetify.views import *
from sweetify import *
from apps.home.pagination import paginate
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)


class Index(ListView):
    model = User
    template_name = 'user/index.html'
    paginate_by = 5
    extra_context = {
        'title': 'Usuarios'
    }


class Create(SweetifySuccessMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'
    extra_context = {'title': 'Registrar'}

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        success(self.request, 'Usuario guardado correctamente!', toast=True, position='top', timer=2000)
        return redirect('user:index')


class Edit(SweetifySuccessMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/edit.html'
    success_url = reverse_lazy('user:index')
    extra_context = {'title': 'Editar'}

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        success(self.request, 'Editado correctamente!', toast=True, position='top', timer=2000)
        return redirect('user:index')


class Show(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return render(self.request, 'user/show.html', {'object_list': user})


class Delete(DeleteView):
    model = User

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return render(self.request, 'user/table.html')


class Table(ListView):
    model = User
    template_name = 'user/table.html'
    paginate_by = 5


def search(request, find):
    users_list = User.objects.filter(
        Q(code__icontains=find) |
        Q(first_name__icontains=find) |
        Q(last_name__icontains=find) |
        Q(second_last_name__icontains=find) |
        Q(role__nombre__icontains=find))
    users = paginate(request, users_list, 100)
    return render(request, 'user/table.html', {'object_list': users})
