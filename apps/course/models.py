from django.db import models
from apps.classroom.models import Classroom
# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)


class Course(models.Model):
    name = models.CharField(max_length=45)
    day = models.CharField(max_length=10)  #
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    classroom = models.ManyToManyField(Classroom, blank=True)
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)

