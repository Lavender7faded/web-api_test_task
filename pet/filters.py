from cProfile import label
import django_filters
from .models import Pet

class PetFilter(django_filters.FilterSet):
    pet_type = django_filters.CharFilter(label='Тип животного')

    class Meta:
        model = Pet
        fields = ['pet_type']

    
