from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.classroom.views import *

app_name = 'classroom'

urlpatterns = [
    path('', auth(Index.as_view()), name='index'),
    path('create/', auth(Create.as_view()), name='create'),
    path('edit/<int:id_class>/', auth(Edit.as_view()), name='edit'),
    path('delete/<int:id_class>/', auth(Delete.as_view()), name='delete'),
    path('search/<slug:find>/', auth(search), name='search'),
    path('table/', auth(Table.as_view()), name='table'),
]
