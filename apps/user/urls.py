from django.urls import path
from apps.user.views import Index, create, Table

app_name = 'user'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('table/', Table.as_view(), name='table'),
    path('create/', create, name='create'),
]
