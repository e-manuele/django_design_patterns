from django import forms

from Factory.models.ToothDetails import PreformDetails


class PreformDetailsForm(forms.ModelForm):
    class Meta:
        model = PreformDetails
        fields = '__all__'

