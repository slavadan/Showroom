from django.db import models
from .fields import PositiveDecimalField


class DateModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AbstractSale(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, default=None)
    percent = PositiveDecimalField(max_digits=5, decimal_places=2, default=5)
    end_date = models.DateField(blank=True)

    class Meta:
        abstract = True
