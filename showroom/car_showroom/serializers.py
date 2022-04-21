from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import (
    Car,
    CarShowroom,
    ShowroomSellCar,
    Customer,
    Transaction,
    Supplier,
    SupplierSellCar,
)


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        exclude = (
            'updated',
        )


class SupplierSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    location = CountryField()

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierSellCarSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=True, read_only=True)
    supplier = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = SupplierSellCar
        fields = '__all__'


class CarShowroomSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    location = CountryField()

    class Meta:
        model = CarShowroom
        fields = [
            'name',
            'location',
            'balance',
            'created',
            'cars',
        ]


class TransactionSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=True, read_only=True)
    car_showroom = CarShowroomSerializer

    class Meta:
        model = Transaction
        exclude = (
            'updated',
        )


class CustomerSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'created',
            'balance',
            'transactions',
        ]


class ShowroomSellCarSerializer(serializers.ModelSerializer):
    showroom = CarShowroomSerializer(many=True, read_only=True)
    car = CarSerializer(many=True, read_only=True)
    supplier = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = ShowroomSellCar
        exclude = (
            'created',
        )
