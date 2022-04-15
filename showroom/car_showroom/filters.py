from django_filters.rest_framework import FilterSet
from django_filters import filters
from .models import (
    Car,
    CarShowroom,
    ShowroomSellCar,
    Customer,
    Transaction,
    Supplier,
    SupplierSellCar
)


class CarFilter(FilterSet):

    class Meta:
        model = Car
        fields = {
            'brand': ['icontains'],
            'max_speed': ['exact', 'lt', 'gt'],
            'engine': ['icontains'],
            'mileage': ['exact', 'lt', 'gt'],
            'year': ['exact', 'gt', 'lt']
        }


class CarShowroomFilter(FilterSet):

    class Meta:
        model = CarShowroom
        fields = {
            'name': ['icontains'],
            'location': ['icontains'],
            'balance': ['exact', 'lt', 'gt'],
        }


class ShowroomSellCarFilter(FilterSet):
    showroom_name = filters.CharFilter(field_name='showroom', lookup_expr="name__iexact")

    class Meta:
        model = ShowroomSellCar
        fields = {
            'supplier__name': ['iexact'],
            'showroom__name': ['iexact'],
            'count': ['exact', 'gt', 'lt'],
            'price': ['exact', 'gt', 'lt'],
        }


class CustomerFilter(FilterSet):

    class Meta:
        model = Customer
        fields = {
            'first_name': ['iexact'],
            'gender': ['iexact'],
            'age': ['exact', 'lt', 'gt'],
            'balance': ['exact', 'lt', 'gt'],
        }


class TransactionFilter(FilterSet):

    class Meta:
        model = Transaction
        fields = {
            'car__brand': ['iexact'],
            'count': ['exact', 'lt', 'gt'],
            'price': ['exact', 'lt', 'gt'],
            'car_showroom__name': ['iexact'],
        }


class SupplierFilter(FilterSet):

    class Meta:
        model = Supplier
        fields = {
            'name': ['iexact'],
            'cars__brand': ['iexact'],
            'number_of_buyers': ['exact', 'lt', 'gt'],
        }


class SupplierSellCarFilter(FilterSet):

    class Meta:
        model = SupplierSellCar
        fields = {
            'car__brand': ['iexact'],
            'car__year': ['exact', 'lt', 'gt'],
            'supplier__name': ['iexact'],
            'price': ['exact', 'lt', 'gt'],
        }
