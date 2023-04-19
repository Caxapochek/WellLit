from django.core.exceptions import ValidationError
from django import forms
from .models import *
import re 
from captcha.fields import CaptchaField, CaptchaTextInput


class ApplicationForm(forms.ModelForm):
    captcha = CaptchaField(label="Введите текст с картинки", widget=CaptchaTextInput(attrs = {'class':'form-field'}), error_messages = {"invalid": u"Неверно введено проверочное слово!"})
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
    