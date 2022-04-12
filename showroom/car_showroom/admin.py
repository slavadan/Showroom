from django.contrib import admin
from .models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'max_speed',
        'engine_power',
        'mileage',
        'description',
    )
