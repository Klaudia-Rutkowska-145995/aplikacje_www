from django.urls import path

from . import views

urlpatterns = [
    path('brands/', views.BrandList.as_view(), name=views.BrandList.name),
    path('brands/<int:pk>/', views.GetBrand.as_view(), name=views.GetBrand.name),
    path('cars/', views.CarList.as_view(), name=views.CarList.name),
    path('cars/<int:pk>/', views.GetCar.as_view(), name=views.GetCar.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
