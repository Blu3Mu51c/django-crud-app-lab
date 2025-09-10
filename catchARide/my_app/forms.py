from django import forms
from .models import ServiceRecord, Accessory

class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = ['date', 'service_type']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['name', 'type', 'description', 'car']