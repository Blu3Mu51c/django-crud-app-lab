from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Accessory, ServiceRecord
from .forms import ServiceRecordForm


# Home page (LoginView used for consistency with reference)
class Home(LoginView):
    template_name = 'home.html'


# About page view
def about(request):
    return render(request, 'about.html')


# Car views
@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})


@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    service_form = ServiceRecordForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        'service_form': service_form
    })


@login_required
def add_service(request, car_id):
    form = ServiceRecordForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.car_id = car_id
        new_service.save()
    return redirect('car-detail', car_id=car_id)


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'color', 'vin', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'color', 'description']


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'


class AccessoryCreate(CreateView):
    model = Accessory
    fields = ['name', 'type', 'description', 'car']

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['name', 'type', 'description', 'car']

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'

class AccessoryList(ListView):
    model = Accessory

class AccessoryDetail(DetailView):
    model = Accessory


# Accessory association
@login_required
def assoc_accessory(request, car_id, accessory_id):
    Car.objects.get(id=car_id).accessories.add(accessory_id)
    return redirect('car-detail', car_id=car_id)


@login_required
def unassoc_accessory(request, car_id, accessory_id):
    Car.objects.get(id=car_id).accessories.remove(accessory_id)
    return redirect('car-detail', car_id=car_id)


# Signup view
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


