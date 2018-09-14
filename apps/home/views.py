from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from sweetify import *
from django.contrib.auth.hashers import check_password, make_password
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(request, username=username, password=password1)
        if user:
            login(request, user)
            info(request, 'Bienvenido(a) '+request.user.first_name+'!', toast=True, position='top', timer=2000)
            return HttpResponseRedirect(render(request, 'home/index.html'))
        else:
            warning(request, 'Ingresar datos correctos!'+str(user), toast=True, position='top', timer=2000)
    return render(request, 'home/login.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        info(request, 'Sesión finalizada!', toast=True, position='top', timer=2000)
        return redirect('user:index')

