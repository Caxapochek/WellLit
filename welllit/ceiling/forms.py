from django.core.exceptions import ValidationError
from django import forms
from .models import *
import re 

class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Application
        fields = ['name', 'phone', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs= {'class':'form-field'}),
            'phone': forms.TextInput(attrs= {'class':'form-field'}),
            'email': forms.EmailInput(attrs= {'class':'form-field'}),
            'comment': forms.Textarea(attrs={'class':'form-field', 'rows':10,'resize':'none'})
        }
    