from car_showroom.models import Car
from core.abstract_classes import CustomBaseModel
from core.fields import PositiveDecimalField
from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


# Create your models here
class CarShowroom(CustomBaseModel, User):
    name = models.CharField(max_length=100)
    location = CountryField(blank=True)
    balance = PositiveDecimalField(max_digits=5, decimal_places=2)
    car_list = models.ManyToManyField(
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

    def __str__(self):
        return self.name


class ShowroomSellCar(CustomBaseModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    price = PositiveDecimalField(max_digits=5, decimal_places=2)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.showroom}->{self.supplier}->{self.car}'


class Customer(CustomBaseModel, User):
    balance = PositiveDecimalField(max_digits=5, decimal_places=2)
    phone = models.CharField(max_length=30, blank=True)
    transactions = models.ManyToManyField(Car, through="Offer")

    def __str__(self):
        return self.first_name


class Offer(CustomBaseModel):
    max_price = PositiveDecimalField(max_digits=5, decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer}-{self.car_showroom}'


class Supplier(CustomBaseModel, User):
    name = models.CharField(max_length=50)
    date_of_creation = models.DateField(blank=True)
    buyers = models.PositiveIntegerField(default=0)
    sell_list = models.ManyToManyField(Car, through='SupplierSellCar')

    def __str__(self):
        return self.first_name


class SupplierSellCar(CustomBaseModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = PositiveDecimalField(max_digits=5, decimal_places=2)
    country = CountryField(blank=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.supplier}->{self.car}'
