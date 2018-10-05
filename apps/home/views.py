from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login, logout
from apps.home.form import LoginForm, ResetForm, ResetConfirmForm
from sweetify import *
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    TemplateView,
    reverse_lazy,
)


class Index(TemplateView):
    template_name = 'home/index.html'
    extra_context = {
        'title': 'Inicio'
    }


class Login(LoginView):
    template_name = 'home/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        login(self.request, form.get_user())
        info(self.request, 'Bienvenido(a) '+self.request.user.first_name+'!', toast=True, position='top', timer=2500)
        return HttpResponseRedirect(self.get_success_url())


class Logout(LogoutView):
    success_url = reverse_lazy('home:login')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        next_page = self.success_url
        if next_page:
            info(request, 'Se ha cerrado sesión!', toast=True, position='top', timer=2500)
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)


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

