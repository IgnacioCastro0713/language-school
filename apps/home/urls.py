from django.urls import path
from apps.home.views import *
from django.contrib.auth.decorators import login_required as auth

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', user_login, name='login'),
    path('logout/', auth(user_logout), name='logout'),
    path('reset/password/', Reset.as_view(), name='password_reset'),
    path('reset/password/done/', ResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/complete/', ResetComplete.as_view(), name='password_reset_complete'),
]
