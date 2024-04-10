from django.db import models
from Factory.models.ImplantCompany import ImplantCompany
from Factory.models.ImplantName import ImplantName
from Factory.models.Tooth import Tooth
from interfaces.IToothDetails import IToothDetails


class ImplantDetails(models.Model, IToothDetails):
    company_name = models.CharField(max_length=100)
    implant_type = models.CharField(max_length=100)
    tooth = models.ForeignKey(Tooth, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        db_table = 'tooth_details'
        verbose_name = 'Tooth Details'
        verbose_name_plural = 'Teeth Details'

    def __str__(self):
        pass

    def serialize(self):
        pass


class GengivaDetails(models.Model, IToothDetails):
    tooth = models.ForeignKey(Tooth, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        db_table = 'gengiva_details'
        verbose_name = 'Gengiva Details'
        verbose_name_plural = 'Gengiva Details'

    def __str__(self):
        pass

    def serialize(self):
        pass


class DetachableDetails(models.Model, IToothDetails):
    tooth = models.ForeignKey(Tooth, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        db_table = 'detachable_details'
        verbose_name = 'Detachable Details'
        verbose_name_plural = 'Detachable Details'

    def __str__(self):
        pass

    def serialize(self):
        pass


class ThreadingDetails(models.Model, IToothDetails):
    tooth = models.ForeignKey(Tooth, on_delete=models.PROTECT, blank=True, null=True)
    screw = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'threading_details'
        verbose_name = 'Threading Details'
        verbose_name_plural = 'Threading Details'

    def __str__(self):
        pass

    def serialize(self):
        pass


class PreformDetails(models.Model, IToothDetails):
    company_name = models.ForeignKey(ImplantCompany, on_delete=models.PROTECT, blank=True, null=True, )
    implant_type = models.ForeignKey(ImplantName, on_delete=models.PROTECT, blank=True, null=True)
    tooth = models.ForeignKey(Tooth, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        db_table = 'preform_details'
        verbose_name = 'Preform Details'
        verbose_name_plural = 'Preform Details'

    def __str__(self):
        pass

    def serialize(self):
        pass


class AnalogDetails(models.Model, IToothDetails):
    company_name = models.CharField(max_length=100)
    implant_type = models.ForeignKey(ImplantName, on_delete=models.PROTECT, blank=True, null=True)
    tooth = models.ForeignKey(Tooth, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        db_table = 'analog_details'
        verbose_name = 'Analog Details'
        verbose_name_plural = 'Analog Details'

    def __str__(self):
        pass

    def serialize(self):
        pass
