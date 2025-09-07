from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Home page view
def home(request):
    return render(request, 'home.html')

# About page view
def about(request):
    return render(request, 'about.html')

# List all cars
def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

# Show details for a single car
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})

# Class-based views for CRUD

class CarCreate(CreateView):
    model = Car
    fields = '__all__'  # all fields from the model

class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'color', 'description']  # fields allowed to update

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'  # redirect after deletion
