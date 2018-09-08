from django.urls import path
from apps.user.views import Index, create, Table, Delete

app_name = 'user'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', create, name='create'),
    path('delete/<int:id>', Delete.as_view(), name='delete'),
    path('table/', Table.as_view(), name='table'),
]
