from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SERVICE_TYPES = (
    ('OIL', 'Oil Change'),
    ('TIRE', 'Tire Rotation'),
    ('BRK', 'Brake Inspection'),
    ('GEN', 'General Service'),
)

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='accessories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessory-detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True, blank=True, null=True)
    description = models.TextField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.vin})"

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})


class ServiceRecord(models.Model):
    date = models.DateField('Service date')
    service_type = models.CharField(
        max_length=10,
        choices=SERVICE_TYPES,
        default=SERVICE_TYPES[0][0]
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']  # newest services appear first
