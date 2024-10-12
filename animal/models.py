from django.db import models

class Animal(models.Model):
    species = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    habitat = models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
