from django.db import models
from apps.course.models import Course
# Create your models here.


class Role(models.Model):
    reference = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)


class User(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=45)
    apaterno = models.CharField(max_length=25)
    amaterno = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
