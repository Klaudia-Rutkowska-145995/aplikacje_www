from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Brand, Car
from .seralizers import BrandSerializer, CarSerializer
from rest_framework import permissions


class GetBrand(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    name = 'brand-detail'


class GetCar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    name = 'brand-list'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-list'
    filterset_fields = ['name', 'production_year', 'price', 'brand', 'color']
    search_fields = ['name', 'production_year', 'price', 'brand__name', 'color']
    ordering_fields = ['name', 'production_year', 'price', 'brand']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'brands': reverse(BrandList.name, request=request),
            'cars': reverse(CarList.name, request=request),
        })
