from django.contrib import admin
from .models import SupplierSale, CarShowroomSale


# Register your models here.
@admin.register(SupplierSale)
class SupplierSaleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'end_date',
        'suppliers',
        'cars',
    )
    list_filter = (
        'name',
        'percent',
        'updated',
        'created',
    )
    readonly_fields = ['updated', 'created']


@admin.register(CarShowroomSale)
class CarShowroomSaleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'end_date',
        'showrooms',
        'cars',
    )
    list_filter = (
        'name',
        'percent',
        'updated',
        'created',
    )
    readonly_fields = ['updated', 'created']
