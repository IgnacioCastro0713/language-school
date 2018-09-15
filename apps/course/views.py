from django.shortcuts import render
from apps.course.models import Course
# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'object_list': courses})
