from django.urls import path

from . import views

urlpatterns = [
    path('brands/', views.BrandList.as_view(), name=views.BrandList.name),
    path('brands/<id>/', views.getBrand, name='getBrand'),
    path('cars/', views.CarList.as_view(), name=views.CarList.name),
    path('cars/<id>/', views.getCar, name='getCar'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
