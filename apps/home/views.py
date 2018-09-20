from django.shortcuts import render, HttpResponseRedirect, reverse
from apps.user.backends import CustomBackendUser as Auth
from django.contrib.auth import login, logout
from sweetify import *


def index(request):
    return render(request, 'home/index.html')


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = Auth.authenticate(username=username, password=password1)
        if user:
            login(request, user)
            info(request, 'Bienvenido(a) '+request.user.first_name+'!', toast=True, position='top', timer=2000)
            return HttpResponseRedirect(reverse('home:index'))
        else:
            context['error'] = 'has-danger'
            warning(request, 'Ingresar datos correctos!', toast=True, position='top', timer=2000)
            return render(request, 'home/login.html', context)
    return render(request, 'home/login.html')


def user_logout(request):
    logout(request)
    info(request, 'Se ha cerrado sesión', toast=True, position='top', timer=2000)
    return HttpResponseRedirect(reverse('home:index'))

