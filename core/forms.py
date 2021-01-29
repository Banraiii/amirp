from django import forms
import re
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    subject = forms.CharField(label="Тема", widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Текст", widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
