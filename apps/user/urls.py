from django.urls import path
from apps.user.views import index

urlpatterns = [
    path('', index, name='user'),
]
