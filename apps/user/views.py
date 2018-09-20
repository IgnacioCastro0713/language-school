from django.shortcuts import render, redirect
from apps.user.models import User
from apps.user.form import UserForm
from django.db.models import Q
from sweetify import *


def index(request):
    user = User.objects.all()
    return render(request, 'user/index.html', {'object_list': user})


def create(request):
    if request.method == 'POST':
        user = UserForm(request.POST).save()
        user.set_password(request.POST['password'])
        user.save()
        success(request, 'Usuario guardado correctamente!', toast=True, position='top', timer=2000)
        return redirect('user:index')
    return render(request, 'user/create.html', {'form': UserForm})


def show(request, code):
    user = User.objects.get(pk=code)
    return render(request, 'user/show.html', {'object_list': user})


def edit(request, code):
    user = User.objects.get(pk=code)
    if request.method == 'POST':
        user = UserForm(request.POST, instance=user).save()
        user.set_password(request.POST['password'])
        user.save()
        success(request, 'Editado correctamente!', toast=True, position='top', timer=2000)
        return redirect('user:index')
    return render(request, 'user/edit.html', {'form': UserForm(instance=user)})


def delete(request, code):
    User.objects.get(pk=code).delete()
    return render(request, 'user/table.html')


def table(request):
    user = User.objects.all()
    return render(request, 'user/table.html', {'object_list': user})


def search(request, find):
    users = User.objects.filter(
        Q(code__icontains=find) |
        Q(first_name__icontains=find) |
        Q(last_name__icontains=find) |
        Q(second_last_name__icontains=find) |
        Q(role__nombre__icontains=find))
    return render(request, 'user/table.html', {'object_list': users})
