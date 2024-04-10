from django.core.exceptions import ValidationError
from django.db import models

from .ImplantCompany import ImplantCompany


class ImplantName(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.ForeignKey(ImplantCompany, on_delete=models.PROTECT)

    has_preform = models.BooleanField(default=False)  # is
    has_subtractive = models.BooleanField(default=False)  # ha il milling?
    has_compatible_screw = models.BooleanField(default=True)  # ha viti aggiungibili
    has_analog = models.BooleanField(default=True)  # ha il milling?
    sintemillable = models.BooleanField(default=False)  # è riproducibile con sint e mill?

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not (self.preformable or self.subtractive or self.sintemillable):
            raise ValidationError("Has to be at least preformable subtractive or sintemillable")
        super(ImplantName, self).save(*args, **kwargs)
