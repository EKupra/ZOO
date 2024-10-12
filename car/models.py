from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.brand} {self.model}"
from django.db import models

# Create your models here.
