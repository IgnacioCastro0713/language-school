from django.db import models
# Create your models here.


class Classroom(models.Model):
    name = models.CharField(max_length=25)
    building = models.CharField(max_length=45)

    def __str__(self):
        return '{} {}'.format(self.name, self.building)
