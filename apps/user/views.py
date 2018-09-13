from django.shortcuts import render, redirect
from apps.user.models import User, AbstractUser
from apps.user.form import UserForm
# from passlib.hash import pbkdf2_sha256  # pip install passlib
import sweetify  # pip install sweetify
from django.db.models import Q


def index(request):
    user = User.objects.all()
    return render(request, 'user/index.html', {'object_list': user})


def create(request):
    if request.method == 'POST':
        User.objects.create(
            code=request.POST['code'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            second_last_name=request.POST['second_last_name'],
            email=request.POST['email'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            role_id=request.POST['role'],
        )
        sweetify.success(request, 'Usuario guardado correctamente!', toast=True, position='top', timer=2000)
        return redirect('user:index')
    return render(request, 'user/create.html', {'form': UserForm})


def show(request, code):
    user = User.objects.get(pk=code)
    return render(request, 'user/show.html', {'object_list': user})


def edit(request, code):
    user = User.objects.get(pk=code)

    if request.method == 'POST':
        User.objects.filter(pk=code).update(
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            second_last_name=request.POST['second_last_name'],
            email=request.POST['email'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            role_id=request.POST['role'],
        )
        sweetify.success(request, 'Editado correctamente!', toast=True, position='top', timer=2000)
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
        Q(role__nombre__icontains=find)
    )
    return render(request, 'user/table.html', {'object_list': users})
