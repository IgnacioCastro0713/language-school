from django.shortcuts import render
from django.urls import reverse_lazy  #
from django.views.generic import CreateView
from apps.user.models import User
from apps.user.form import UserForm
# Create your views here.


def index(request):
    return render(request, 'user/index.html')


class Create(CreateView):  # vista basada en clases
    model = User
    form_class = UserForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('user:index')
