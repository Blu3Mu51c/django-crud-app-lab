from django.db import models
from django.urls import reverse

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True, blank=True, null=True)
    description = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})
