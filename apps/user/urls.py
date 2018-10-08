from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.user.views import (Index, Create, Edit, ChangePassword, Show, Delete, search, Table)

app_name = 'user'

urlpatterns = [
    path('', auth(Index.as_view()), name='index'),
    path('create/', auth(Create.as_view()), name='create'),
    path('edit/<pk>/', auth(Edit.as_view()), name='edit'),
    path('password/', auth(ChangePassword.as_view()), name='password'),
    path('show/<pk>/', auth(Show.as_view()), name='show'),
    path('delete/<pk>/', auth(Delete.as_view()), name='delete'),
    path('search/<slug:find>/', auth(search), name='search'),
    path('table/', auth(Table.as_view()), name='table'),
]
