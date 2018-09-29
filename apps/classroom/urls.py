from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.classroom.views import *

app_name = 'classroom'

urlpatterns = [
    path(' /', auth(index), name='index'),
    path('create/', auth(create), name='create'),
    path('edit/<int:id_class>/', auth(edit), name='edit'),
    path('delete/<int:id_class>/', auth(delete), name='delete'),
    path('search/<slug:find>/', auth(search), name='search'),
    path('table/', auth(table), name='table'),
]
