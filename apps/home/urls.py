from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.home.views import (Index, Login, Logout, Reset, Register, ResetDone, ResetConfirm, ResetComplete)


app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', auth(Logout.as_view()), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('reset/password/', Reset.as_view(), name='password_reset'),
    path('reset/password/done/', ResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/complete/', ResetComplete.as_view(), name='password_reset_complete'),
]
