from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.course.views import *

app_name = 'course'

urlpatterns = [
    path('', auth(Index.as_view()), name='index'),
    path('create/', auth(Create.as_view()), name='create'),
    path('edit/<int:id_course>/', auth(edit), name='edit'),
    path('show/<pk>/', auth(Show.as_view()), name='show'),
    path('delete/<int:id_course>/', auth(delete), name='delete'),
    path('search/<slug:find>/', auth(search), name='search'),
    path('table/', auth(table), name='table'),
]
