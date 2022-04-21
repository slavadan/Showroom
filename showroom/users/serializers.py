from .models import ShowroomUser
from rest_framework import serializers

from .models import ShowroomUser


class ShowroomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowroomUser
        fields = [
            'username',
            'password',
            'is_customer',
            'is_showroom',
            'is_supplier',
            'email',
            'date_joined',
        ]

    def create(self, validated_data):
        user = ShowroomUser(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
