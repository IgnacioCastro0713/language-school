from django.urls import path
from apps.home.views import *
from django.contrib.auth.decorators import login_required as auth
from django.contrib.auth.views import *

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', auth(user_logout), name='logout'),

    path('reset/password/', PasswordResetView.as_view(
        template_name='home/password_reset/form.html',
        email_template_name='home/password_reset/email.html',
        success_url=reverse_lazy('home:password_reset_done'),
    ), name='password_reset'),

    path('reset/password/done/', PasswordResetDoneView.as_view(
        template_name='home/password_reset/done.html',
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='home/password_reset/confirm.html',
        success_url=reverse_lazy('home:password_reset_complete'),
    ), name='password_reset_confirm'),

    path('reset/password/complete', PasswordResetCompleteView.as_view(
        template_name='home/password_reset/complete.html',
    ), name='password_reset_complete'),
]
