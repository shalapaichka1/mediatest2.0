from rest_framework import serializers
from .models import *


# Для пункта A
class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)


# Для пункта B
class StreetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('name', )


# Для пункта C и D
class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', )

    def to_representation(self, instance):
        json = super(ShopSerializers, self).to_representation(instance)
        json['city_name'] = instance.city.name
        json['street_name'] = instance.street.name
        return json


class ShopCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', )
