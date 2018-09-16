from django.db import models
from apps.course.models import Course
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Role(models.Model):
    reference = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.nombre)


class User(AbstractUser):
    code = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=45)
    password = models.CharField(max_length=128)
    last_name = models.CharField(max_length=25)
    second_last_name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
