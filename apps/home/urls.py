from django.urls import path
from apps.home.views import *
from django.contrib.auth.decorators import login_required as auth

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', auth(user_logout), name='logout'),
]
