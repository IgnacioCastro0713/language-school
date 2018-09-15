from django.shortcuts import render
from apps.course.models import Course
from django.db.models import Q
# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'object_list': courses})


def create(request):
    pass


def edit(request):
    pass


def show(request):
    pass


def delete(request, id_course):
    Course.objects.get(pk=id_course).delete()
    return render(request, 'course/table.html')


def table(request):
    courses = Course.objects.all()
    return render(request, 'course/table.html', {'object_list': courses})


def search(request, find):
    courses = Course.objects.filter(
        Q(name__icontains=find) |
        Q(language__course__name__contains=find)
    )
    return render(request, 'course/table.html', {'object_list': courses})
