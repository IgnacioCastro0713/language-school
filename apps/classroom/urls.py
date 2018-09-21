from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.classroom.views import *

app_name = 'classroom'

urlpatterns = [
    path('', auth(index), name='index'),
    path('create/', auth(), name='create'),
    path('edit/<int:id_class>', auth(), name='edit'),
    path('show/<int:id_class>', auth(), name='show'),
    path('delete/<int:id_class>', auth(), name='delete'),
    path('search/<slug:find>', auth(), name='search'),
    path('table/', auth(), name='table'),
]