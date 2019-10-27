from django.shortcuts import render
from django.contrib.auth.views import reverse_lazy
from sweetify import warning
from .models import Language
from .form import LanguageForm
from django.db.models import Q
from sweetify.views import SweetifySuccessMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


class Index(ListView):
    model = Language
    template_name = 'language/index.html'
    paginate_by = 5
    extra_context = {
        'title': 'Idiomas'
    }


class Create(SweetifySuccessMixin, CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'language/form.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Idioma guardado correctamente!'
    success_url = reverse_lazy('language:index')
    extra_context = {
        'title': 'Registrar',
        'titleButton': 'Guardar'
    }

    def form_invalid(self, form):
        warning(self.request, 'Verifique la información ingresada.', toast=True, position='top', timer=3000)
        return super(Create, self).form_invalid(form)


class Edit(SweetifySuccessMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'language/form.html'
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Editado correctamente!'
    success_url = reverse_lazy('language:index')
    extra_context = {
        'title': 'Editar',
        'titleButton': 'Actualizar'
    }

    def form_invalid(self, form):
        warning(self.request, 'Verifique la información ingresada.', toast=True, position='top', timer=3000)
        return super(Edit, self).form_invalid(form)


class Delete(DeleteView):
    model = Language

    def delete(self, request, *args, **kwargs):
        classroom = self.get_object()
        classroom.delete()
        return render(self.request, 'language/table.html')


class Table(ListView):
    model = Language
    template_name = 'language/table.html'
    paginate_by = 5


class Search(ListView):
    model = Language
    template_name = 'language/table.html'
    paginate_by = 5

    def get_queryset(self):
        find = self.kwargs['find']
        return self.model.objects.filter(Q(name__icontains=find) |
                                         Q(level__icontains=find))
