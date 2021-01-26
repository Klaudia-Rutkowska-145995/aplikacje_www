from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Brand, Car
from .seralizers import BrandSerializer, CarSerializer


class GetBrand(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    name = 'brand-detail'


class GetCar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-detail'


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    name = 'brand-list'


class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-list'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'brands': reverse(BrandList.name, request=request),
            'cars': reverse(CarList.name, request=request),
        })
