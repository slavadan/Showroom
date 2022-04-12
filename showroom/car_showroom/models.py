from core.abstract_classes import CustomBaseModel
from django.db import models


# Create your models here.
class Car(CustomBaseModel):
    name = models.CharField(max_length=50)
    max_speed = models.PositiveIntegerField(default=0)
    engine_power = models.PositiveIntegerField(default=0)
    mileage = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=20, default='white')
    type = models.CharField(max_length=20, default='sedan')
    year = models.PositiveIntegerField(blank=True, default='2001')
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name
