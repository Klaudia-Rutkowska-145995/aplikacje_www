from rest_framework import serializers
from .models import Brand, Car


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'description']


class CarSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.SlugRelatedField(queryset=Brand.objects.all(), slug_field='name')

    class Meta:
        model = Car
        fields = ['name', 'description', 'brand', 'production_year', 'price', 'color']
