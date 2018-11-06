import os
from language_school.settings import MEDIA_ROOT
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from apps.user.models import User
from apps.user.form import UserFormCreate, UserFormEdit, PasswordForm, UpdateImage
from django.contrib.auth.views import reverse_lazy, PasswordChangeView
from sweetify import success, warning
from sweetify.views import SweetifySuccessMixin
from django.db.models import Q
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


class Create(CreateView):
    model = User
    form_class = UserFormCreate
    template_name = 'user/create.html'
    extra_context = {'title': 'Registrar'}

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        success(self.request, '¡Usuario guardado correctamente!', toast=True, position='top', timer=2500)
        return redirect('user:index')

    def form_invalid(self, form):
        warning(self.request, '¡Verifique la información ingresada!', toast=True, position='top', timer=3000)
        return self.render_to_response(self.get_context_data(form=form))


class Edit(SweetifySuccessMixin, UpdateView):
    model = User
    form_class = UserFormEdit
    template_name = 'user/edit.html'
    success_url = reverse_lazy('user:index')
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Editado correctamente!'
    extra_context = {'title': 'Editar'}

    def form_invalid(self, form):
        warning(self.request, '¡Verifique la información ingresada!', toast=True, position='top', timer=3000)
        return self.render_to_response(self.get_context_data(form=form))


class ChangePassword(SweetifySuccessMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    form_class = PasswordForm
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Contraseña editada correctamente!'
    success_url = reverse_lazy('user:index')
    extra_context = {'title': 'Cambiar contraseña de usuario'}

    def form_invalid(self, form):
        warning(self.request, '¡Verifique la información ingresada!', toast=True, position='top', timer=3000)
        return self.render_to_response(self.get_context_data(form=form))


class Show(DetailView, UpdateView):
    model = User
    form_class = UpdateImage
    template_name = 'user/show.html'

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        form = self.get_form()
        return render(self.request, 'user/show.html', {'object_list': user, 'form': form})

    def post(self, request, *args, **kwargs):
        id_user = kwargs['pk']
        user = self.model.objects.get(id=id_user)
        image = str(user.filename)
        form = self.form_class(request.POST, request.FILES, instance=user)
        if image != "no.jpg":
            os.remove(os.path.join(MEDIA_ROOT+'/{}'.format(image)))
        form.save()
        success(self.request, '¡Imagen actualizada!', toast=True, position='top', timer=2500)
        return HttpResponseRedirect(reverse_lazy('user:show', kwargs={'pk': id_user}))


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


class Search(ListView):
    model = User
    template_name = 'user/table.html'
    paginate_by = 5

    def get_queryset(self):
        find = self.kwargs['find']
        return self.model.objects.filter(Q(code__icontains=find) |
                                         Q(first_name__icontains=find) |
                                         Q(last_name__icontains=find) |
                                         Q(second_last_name__icontains=find) |
                                         Q(role__nombre__icontains=find))
