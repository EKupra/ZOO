from rest_framework import generics
from .models import Animal
from .serializers import AnimalSerializer

# List and create view
class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

# Retrieve and delete view
class AnimalDetailView(generics.RetrieveDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
from django.shortcuts import render

# Create your views here.
