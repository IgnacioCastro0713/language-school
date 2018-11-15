from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)

    def __str__(self):
        return '{} ({})'.format(self.name, self.level)
