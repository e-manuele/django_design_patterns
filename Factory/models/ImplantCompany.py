from django.db import models
class ImplantCompany(models.Model):
    name = models.CharField(max_length=50)
    short = models.CharField(max_length=5)

    def __str__(self):
        return self.name
