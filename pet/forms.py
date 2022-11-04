from django import forms
from .models import Pet
from django.core.validators import RegexValidator

class PetForm(forms.ModelForm):
    
    birthday = forms.DateField(
        validators=[RegexValidator(regex='^[1-2]\d{3}-[0-1]\d-[0-3]\d$')],
        widget=forms.DateInput())

    class Meta:
        model = Pet
        fields = ['pet_type', 'pet_name', 'birthday', 'pet_high', 'pet_weight', 'pet_passport_number']
