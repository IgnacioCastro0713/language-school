from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.language.views import (Index, Create, Edit, Delete, Search, Table)

app_name = 'language'

urlpatterns = [
    path('', auth(Index.as_view()), name='index'),
    path('create/', auth(Create.as_view()), name='create'),
    path('edit/<pk>/', auth(Edit.as_view()), name='edit'),
    path('delete/<pk>/', auth(Delete.as_view()), name='delete'),
    path('search/<slug:find>/', auth(Search.as_view()), name='search'),
    path('table/', auth(Table.as_view()), name='table'),
]
