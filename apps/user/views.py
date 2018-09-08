from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from apps.user.models import User
from apps.user.form import UserForm
from passlib.hash import pbkdf2_sha256
import sweetify
# Create your views here.


class Index(ListView):
    model = User
    template_name = 'user/index.html'


def create(request):  # Se realizo así para poder encriptar
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


class Delete(DeleteView):
    model = User
    template_name = 'user/table.html'
    success_url = reverse_lazy('user:index')


class Table(ListView):
    model = User
    template_name = 'user/index.html'


def search(request):
    return
