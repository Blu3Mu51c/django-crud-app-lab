from django.contrib import admin
from .models import Car, Accessory, ServiceRecord 

admin.site.register(Car)
admin.site.register(Accessory)
admin.site.register(ServiceRecord)
