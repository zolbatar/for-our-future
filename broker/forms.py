from django import forms
from .models import Company


class CompanyForm(forms.Form):
    name = forms.CharField(label='Company name', max_length=100)
    email = forms.EmailField(label='Contact email')
