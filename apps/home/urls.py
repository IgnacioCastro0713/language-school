from django.urls import path
from apps.home.views import *

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
