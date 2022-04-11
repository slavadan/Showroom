from django_countries.fields import CountryField
from django.db import models


# Create your models here.
class CustomBaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Car(CustomBaseModel):
    name = models.CharField(max_length=50)
    max_speed = models.PositiveIntegerField()
    engine_power = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class CarShowroom(CustomBaseModel):
    name = models.CharField(max_length=100)
    location = CountryField()
    balance = models.DecimalField(max_digits=5, decimal_places=2)
    car_list = models.ManyToManyField("Car", through="ShowroomCars")

    def __str__(self):
        return self.name


class ShowroomCars(CustomBaseModel):
    showroom = models.ForeignKey(CarShowroom, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    count = models.PositiveIntegerField()


class Offer(CustomBaseModel):
    max_price = models.DecimalField(max_digits=5, decimal_places=2)
    car = models.OneToOneField("Car", on_delete=models.DO_NOTHING)


class Customer(CustomBaseModel):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=5, decimal_places=2)
    transactions = models.ForeignKey("Offer", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Supplier(CustomBaseModel):
    name = models.CharField(max_length=50)
    buyers = models.PositiveIntegerField()
    sell_list = models.ManyToManyField("Car", through='CarSellList')


class CarSellList(CustomBaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=5, decimal_places=2)
