from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.course.views import *

app_name = 'course'
urlpatterns = [
    path('', auth(index), name='index'),
    path('create/', auth(create), name='create'),
    path('delete/<int:id_course>', auth(delete), name='delete'),
    path('search/<slug:find>', auth(search), name='search'),
    path('table/', auth(table), name='table'),
]
