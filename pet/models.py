from django.core.validators import RegexValidator
from django.db import models, IntegrityError, DataError

class Measure(models.Model):
    pet = models.ForeignKey('Pet')
    pet_high = models.IntegerField(default='')
    pet_weight = models.IntegerField(default='')
    measure_date = models.DateField(auto_created=True)

class PetType(models.Model):
    name = models.CharField()


class Pet(models.Model):
    pet_type2 = models.ForeignKey('PetType')
    pet_type = models.CharField(default='', max_length=20)
    pet_name = models.CharField(default='', max_length=50)
    birthday = models.DateField(default='', validators=[RegexValidator(regex='^[1-2]\d{3}-[0-1]\d-[0-3]\d$')])
    # pet_high = models.IntegerField(default='')
    # pet_weight = models.IntegerField(default='')
    pet_passport_number = models.IntegerField(default='', blank=True, null=True)
    # archived = models.BooleanField(default=False)
    reason = models.CharField()



    @property
    def weight(self):
        Measure.objects.filter(pet_id=self.id).last()

    @property
    def age(self):
        from datetime import date
        import math
        today = date.today()
        age = math.trunc(today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day)))
        return age

    @property
    def has_passport(self) -> bool:
        a = bool(self.pet_passport_number)
        return bool(self.pet_passport_number)
    
    def __str__(self):
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    def get_by_id(pet_id):
        try:
            user = Pet.objects.get(id=pet_id)
            return user
        except Pet.DoesNotExist:
            pass

    @staticmethod
    def create(pet_type, pet_name, birthday, pet_high, pet_weight, pet_passport_number):
        pet = Pet(pet_type=pet_type, pet_name=pet_name, birthday=birthday, pet_high=pet_high, pet_weight=pet_weight, pet_passport_number=pet_passport_number)
        try:
            pet.save()
            return pet
        except (IntegrityError, AttributeError, DataError):
            print('error')
        
    def update(self, pet_type=None, pet_name=None, birthday=None, pet_high=None, pet_weight=None, pet_passport_number=None):

        if pet_type:
            self.pet_type = pet_type
        if pet_name:
            self.pet_name = pet_name
        if birthday:
            self.birthday = birthday
        if pet_high:
            self.pet_high = pet_high
        if pet_weight:
            self.pet_weight = pet_weight
        if pet_passport_number:
            self.pet_passport_number = pet_passport_number
        self.save()

    def to_dict(self):
        return {
            'pet_type': self.pet_type,
            'pet_name': self.pet_name,
            'birthday': self.birthday,
            'pet_high': self.pet_high,
            'pet_weight': self.pet_weight,
            'pet_passport_number': self.pet_passport_number,
        }

    @staticmethod
    def get_all():
        all_pets = Pet.objects.all()
        return list(all_pets)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Pet, self).save(*args, **kwargs)
   
