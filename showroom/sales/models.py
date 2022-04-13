from django.db import models
from car_showroom.models import Car
from core.abstract_classes import DateModel, AbstractSale
from car_showroom.models import CarShowroom, Supplier


# Create your models here.
class CarShowroomSale(DateModel, AbstractSale):
    showrooms = models.ForeignKey(
        CarShowroom,
        on_delete=models.CASCADE,
        related_name='sale'
    )
    cars = models.ForeignKey(Car, on_delete=models.CASCADE)


class SupplierSale(DateModel, AbstractSale):
    suppliers = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='sale'
    )
    cars = models.ForeignKey(Car, on_delete=models.CASCADE)
