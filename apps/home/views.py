from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login, logout
from apps.home.form import LoginForm, ResetForm, ResetConfirmForm
from sweetify import info, warning
from sweetify.views import SweetifySuccessMixin
# from language_school.settings import sms
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
        'title': 'Inicio',
        'project_name': 'Language School.',
        'description': 'Project made in Django.',
    }


class Login(LoginView):
    template_name = 'home/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        login(self.request, form.get_user())
        info(self.request, '¡Bienvenido(a) {}!'.format(self.request.user.first_name), toast=True, position='top',
             timer=2500)
        '''sms.messages.create(
            body="{} {} {} ha iniciado sesión en language school.".format(
                self.request.user.first_name,
                self.request.user.last_name,
                self.request.user.second_last_name
            ), from_='+13204293498', to='+523841086233')'''
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        warning(self.request, '¡Verifique la información ingresada!', toast=True, position='top', timer=2500)
        return self.render_to_response(self.get_context_data(form=form))


class Logout(LogoutView):
    success_url = reverse_lazy('home:login')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        next_page = self.success_url
        if next_page:
            info(request, '¡Se ha cerrado la sesión!', toast=True, position='top', timer=2500)
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)


class Reset(SweetifySuccessMixin, PasswordResetView):
    template_name = 'home/password_reset/form.html'
    email_template_name = 'home/password_reset/email.html'
    form_class = ResetForm
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Correo enviado correctamente!'
    success_url = reverse_lazy('home:password_reset_done')


class ResetDone(PasswordResetDoneView):
    template_name = 'home/password_reset/done.html'


class ResetConfirm(SweetifySuccessMixin, PasswordResetConfirmView):
    template_name = 'home/password_reset/confirm.html'
    form_class = ResetConfirmForm
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = '¡Contraseña restablecida correctamente!'
    success_url = reverse_lazy('home:password_reset_complete')


class ResetComplete(PasswordResetCompleteView):
    template_name = 'home/password_reset/complete.html'
