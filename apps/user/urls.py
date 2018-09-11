from django.urls import path
from apps.user.views import *

app_name = 'user'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('delete/<slug:code>/', delete, name='delete'),
    path('edit/<slug:code>/', edit, name='edit'),
    path('table/', table, name='table'),
    path('search/<slug:find>/', search, name='search'),
]
