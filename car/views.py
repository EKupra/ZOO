from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

# List and create view
class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Retrieve and delete view
class CarDetailView(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
from django.shortcuts import render

# Create your views here.
