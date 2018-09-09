from django.urls import path
from apps.user.views import index, create, delete, table, search

app_name = 'user'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('delete/<slug:code>/', delete, name='delete'),
    path('table/', table, name='table'),
    path('search/', search, name='search'),
]
