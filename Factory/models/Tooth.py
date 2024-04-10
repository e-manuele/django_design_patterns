from django.db import models


class Tooth(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)