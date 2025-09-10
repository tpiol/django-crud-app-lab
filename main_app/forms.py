from django import forms
from .models import Cleaning

class CleaningForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields = ['date', 'cleaning_methods']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }