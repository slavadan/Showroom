from rest_framework import serializers
from .models import (
    CarShowroomSale,
    SupplierSale
)


class CarShowroomSaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarShowroomSale
        fields = '__all__'


class SupplierSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierSale
        fields = '__all__'
