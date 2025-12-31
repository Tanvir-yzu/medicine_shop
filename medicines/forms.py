# medicines/forms.py
from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'generic_name', 'manufacturer', 'batch_number', 
                  'expiry_date', 'price', 'stock', 'description']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }