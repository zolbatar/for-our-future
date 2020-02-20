from django import forms
from .models import Item, Company


class ItemForm(forms.Form):
    company = forms.ModelChoiceField(Company.objects, empty_label=None)
    title = forms.CharField()
    price = forms.DecimalField()
    units = forms.IntegerField()
    description = forms.CharField()


class CompanyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
