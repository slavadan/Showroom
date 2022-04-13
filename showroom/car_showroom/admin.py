from django.contrib import admin
from .models import (
    Car, CarShowroom,
    ShowroomSellCar, Customer,
    Transaction, Supplier,
    SupplierSellCar
)


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'image',
        'max_speed',
        'engine_power',
        'mileage',
        'description',
    )
    list_filter = (
        'updated',
        'created',
    )


@admin.register(CarShowroom)
class CarShowroomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'balance',
    )
    list_filter = (
        'updated',
        'created',
    )


@admin.register(ShowroomSellCar)
class ShowroomSellCarAdmin(admin.ModelAdmin):
    list_display = (
        'car',
        'showroom',
        'count',
        'price',
        'supplier',
    )
    list_filter = (
        'updated',
        'created',
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'age',
        'balance',
    )
    list_filter = (
        'updated',
        'created',
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'price',
        'count',
        'car',
        'car_showroom',
        'customer',
    )
    list_filter = (
        'updated',
        'created',
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'date_of_creation',
    )
    list_filter = (
        'updated',
        'created',
    )


@admin.register(SupplierSellCar)
class SupplierSellCar(admin.ModelAdmin):
    list_display = (
        'car',
        'supplier',
        'price',
    )
    list_filter = (
        'updated',
        'created',
    )
