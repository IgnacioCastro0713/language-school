from django.db import models
from apps.user.models import User
from apps.classroom.models import Classroom


# Create your models here.

DAYS = (
    ('lunes', 'Lunes'),
    ('martes', 'Martes'),
    ('miercoles', 'Miercoles'),
    ('jueves', 'Jueves'),
    ('viernes', 'Viernes'),
)


class Language(models.Model):
    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)

    def __str__(self):
        return '{} {}'.format(self.name, self.level)


class Course(models.Model):
    name = models.CharField(max_length=45)
    day = models.CharField(max_length=10, choices=DAYS)  #
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    classroom = models.ManyToManyField(Classroom, blank=True)
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
