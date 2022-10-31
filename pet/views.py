from django.shortcuts import render, redirect
from pet.forms import PetForm
from pet.models import Pet
from .filters import PetFilter
from datetime import date
import math

def pet_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = PetForm()
        else:
            pet = Pet.objects.get(id=pk)
            form = PetForm(instance=pet)
        context = {'form': form}
        return render(request, 'pet/add_new_pet.html', context)
    else:
        if pk == 0:
            form = PetForm(request.POST)
        else:
            pet = Pet.objects.get(id=pk)
            form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
        
        return redirect('search')

def pet_delete(self, pk):
    pet = Pet.objects.get(id=pk)
    pet.delete()
    return redirect('search')

def type_search(request):
    filter = PetFilter(request.GET, queryset=Pet.objects.all())
    return render(request, 'pet/list_of_pet.html', {'filter': filter})

def calculate_age(birthday):
    today = date.today()
    age = math.trunc(today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)))
    return age
