from core.fields import PositiveDecimalField
from core.abstract_classes import DateModel
from core.validators import year_validator
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Car(DateModel):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    max_speed = models.PositiveIntegerField(default=0)
    engine = models.CharField(max_length=50)
    engine_power = models.PositiveIntegerField(default=0)
    mileage = models.FloatField(default=0)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=20, default='white')
    type = models.CharField(max_length=20, default='sedan')
    year = models.IntegerField(blank=True, validators=[year_validator])
    image = models.URLField(blank=True, max_length=100)

    def __str__(self):
        template = '{0.brand} {0.model} {0.color} {0.year} {0.engine}'
        return template.format(self)


class CarShowroom(DateModel):
    name = models.CharField(max_length=100)
    location = CountryField(blank=True)
    email = models.EmailField(blank=True)
    balance = PositiveDecimalField(max_digits=5, decimal_places=2)
    cars = models.ManyToManyField(
        Car,
        through="ShowroomSellCar"
    )
    buy_query = models.JSONField(
        blank=True,
        default={
            'name': None,
            'max_speed': 0,
            'engine_power': 0,
            'color': 'white',
            'type': 'sedan'
        }
    )
    unique_buyers = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name}-{self.location}'


class ShowroomSellCar(DateModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    price = PositiveDecimalField(max_digits=5, decimal_places=2)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.showroom}->{self.supplier}->{self.car}'


class Customer(DateModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(blank=True)
    balance = PositiveDecimalField(max_digits=5, decimal_places=2)
    phone = models.CharField(max_length=30, blank=True)
    transactions = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        template = '{0.first_name} {0.last_name} {0.gender} {0.age}'
        return template.format(self)


class Transaction(DateModel):
    price = PositiveDecimalField(max_digits=5, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_showroom}-{self.count}'


class Supplier(DateModel):
    name = models.CharField(max_length=50)
    date_of_creation = models.DateField(blank=True)
    number_of_buyers = models.PositiveIntegerField(default=0)
    email = models.EmailField(blank=True)
    cars = models.ManyToManyField(Car, through='SupplierSellCar')
    location = CountryField(blank=True)

    def __str__(self):
        template = '{0.name} {0.location}'
        return template.format(self)


class SupplierSellCar(DateModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = PositiveDecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.supplier}->{self.car}'
