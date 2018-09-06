from django.shortcuts import render, redirect
from apps.user.form import FormUser
# Create your views here.


def index(request):
    return render(request, 'user/index.html')


def create(request):
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect('user:index')

    form = FormUser()
    return render(request, 'user/create.html', {'form': form})
