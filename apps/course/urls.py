from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.course.views import *

app_name = 'course'

urlpatterns = [
    path('', auth(index), name='index'),
]
