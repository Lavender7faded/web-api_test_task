import django_filters
from pet.models import Pet


class PetFilter(django_filters.FilterSet):
    pet_type = django_filters.CharFilter(label='Тип животного')

    class Meta:
        model = Pet
        fields = ['pet_type']
