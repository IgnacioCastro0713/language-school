from django.db import models
from apps.user.models import User
from apps.classroom.models import Classroom
from apps.language.models import Language


class Course(models.Model):
    name = models.CharField(max_length=45)
    day = models.CharField(max_length=15)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField(max_length=255)
    lan = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, blank=True)
