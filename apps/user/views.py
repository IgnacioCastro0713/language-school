from django.shortcuts import render, redirect
from apps.user.models import User
from apps.user.form import UserForm
from passlib.hash import pbkdf2_sha256
import sweetify
from sweetify.views import SweetifySuccessMixin


def index(request):
    user = User.objects.all()
    return render(request, 'user/index.html', {'object_list': user})


def create(request):
    if request.method == 'POST':
        User.objects.create(
            code=request.POST['code'],
            password=pbkdf2_sha256.encrypt(request.POST['password'], rounds=12000, salt_size=32),
            nombre=request.POST['nombre'],
            apaterno=request.POST['apaterno'],
            amaterno=request.POST['amaterno'],
            email=request.POST['email'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            role_id=request.POST['role'],
        )
        sweetify.success(request, 'Usuario guardado correctamente!', toast=True, position='top', timer=2000)
        return redirect('user:index')
    return render(request, 'user/create.html', {'form': UserForm})


def edit(request):
    return


def show(request):
    return


def delete(request, id_user):
    User.objects.get(id=id_user).delete()


def table(request):
    user = User.objects.all()
    return render(request, 'user/table.html', {'object_list': user})


def search(request):
    user = User.objects.get(headline__contains=request['search'])
    return render(request, 'user/table.html', {'object_list': user})
