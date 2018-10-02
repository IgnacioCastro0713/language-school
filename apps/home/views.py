from django.shortcuts import render, HttpResponseRedirect, reverse
from apps.user.backends import CustomBackendUser as Auth
from django.contrib.auth import login, logout
from apps.home.form import *
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    TemplateView,
    reverse_lazy,
)
from sweetify import *


class Index(TemplateView):
    template_name = 'home/index.html'
    extra_context = {
        'title': 'Inicio'
    }


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = Auth.authenticate(username=username, password=password1)
        if user:
            login(request, user)
            info(request, 'Bienvenido(a) '+request.user.first_name+'!', toast=True, position='top', timer=2000)
            return HttpResponseRedirect(reverse('home:index'))
        else:
            context['error'] = 'has-danger'
            warning(request, 'Ingresar datos correctos!', toast=True, position='top', timer=2000)
            return render(request, 'home/login.html', context)
    return render(request, 'home/login.html')


def user_logout(request):
    logout(request)
    info(request, 'Se ha cerrado sesión!', toast=True, position='top', timer=2000)
    return HttpResponseRedirect(reverse('home:index'))


class Reset(PasswordResetView):
    template_name = "home/password_reset/form.html"
    email_template_name = "home/password_reset/email.html"
    form_class = ResetForm
    success_url = reverse_lazy('home:password_reset_done')


class ResetDone(PasswordResetDoneView):
    template_name = "home/password_reset/done.html"


class ResetConfirm(PasswordResetConfirmView):
    template_name = "home/password_reset/confirm.html"
    form_class = ResetConfirmForm
    success_url = reverse_lazy('home:password_reset_complete')


class ResetComplete(PasswordResetCompleteView):
    template_name = "home/password_reset/complete.html"

