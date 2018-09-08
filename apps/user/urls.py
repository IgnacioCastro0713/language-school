from django.urls import path
from apps.user.views import index, create

app_name = 'user'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
]
