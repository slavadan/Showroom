from django_filters.rest_framework import FilterSet
from .models import SupplierSale, CarShowroomSale


class SupplierSaleFilter(FilterSet):

    class Meta:
        model = SupplierSale
        fields = {
            'name': ['iexact'],
            'percent': ['exact', 'gt', 'lt'],
            'suppliers__name': ['iexact'],
        }


class CarShowroomSaleFilter(FilterSet):

    class Meta:
        model = CarShowroomSale
        fields = {
            'name': ['iexact'],
            'percent': ['exact', 'gt', 'lt'],
            'showrooms__name': ['iexact'],
        }
