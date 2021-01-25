from django.shortcuts import render
from django.http import HttpResponse
from .models import marka


def index(request):
    query = marka.objects.all()
    return HttpResponse(query)