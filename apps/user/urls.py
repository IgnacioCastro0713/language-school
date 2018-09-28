from django.urls import path
from django.contrib.auth.decorators import login_required as auth
from apps.user.views import *

app_name = 'user'

urlpatterns = [
    path('', auth(index), name='index'),
    path('create/', auth(create), name='create'),
    path('edit/<slug:code>/', auth(edit), name='edit'),
    path('show/<slug:code>/', auth(show), name='show'),
    path('delete/<slug:code>/', auth(delete), name='delete'),
    path('search/<slug:find>/', auth(search), name='search'),
    path('table/', auth(table), name='table'),
]
