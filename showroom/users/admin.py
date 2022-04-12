from django.contrib import admin
from .models import CarShowroom, Customer, Supplier, ShowroomCarOnSale, SupplierSellCar


# Register your models here.
@admin.register(CarShowroom)
class CarShowroomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'balance',
        'buy_query',
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'balance',
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_of_creation',
        'buyers',
    )


@admin.register(ShowroomCarOnSale)
class ShowroomCarOnSaleAdmin(admin.ModelAdmin):
    list_display = (
        'car',
        'count',
        'price',
    )


@admin.register(SupplierSellCar)
class SupplierSellListAdmin(admin.ModelAdmin):
    list_display = (
        'car',
        'supplier',
        'price',
        'country',
        'count',
    )
