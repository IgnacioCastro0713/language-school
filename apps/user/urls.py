from django.urls import path
from apps.user.views import index, Create

app_name = 'user'
urlpatterns = [
    path('', index, name='index'),
    path('create/', Create.as_view(), name='create'),
]
