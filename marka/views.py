from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Brand, Car
from .seralizers import BrandSerializer, CarSerializer


def getBrand(request, id):
    brand = Brand.objects.get(pk=id)
    return HttpResponse(brand.name)


def getCar(request, id):
    car = Car.objects.get(pk=id)
    return HttpResponse(car.name)


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
