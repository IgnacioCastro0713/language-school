from django.urls import path
from django.contrib.auth.decorators import login_required as required
from apps.user.views import *


app_name = 'user'

urlpatterns = [
    path('', required(index), name='index'),
    path('create/', required(create), name='create'),
    path('edit/<slug:code>/', required(edit), name='edit'),
    path('show/<slug:code>/', required(show), name='show'),
    path('delete/<slug:code>/', required(delete), name='delete'),
    path('table/', required(table), name='table'),
    path('search/<slug:find>/', required(search), name='search'),
]
