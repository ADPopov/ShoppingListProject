from django import forms
from django.forms import ModelForm, DateTimeInput

from shoppingList.models import Product


class ProductDeskForm(forms.Form):
    quantity = forms.IntegerField(label='Количество')
    name = forms.CharField(label='Название', max_length=200),
    shopName = forms.CharField(label='Название магазина', max_length=30),
    purchase_date = forms.DateTimeInput(),
    cost = forms.IntegerField(label='Стоимость'),


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'shopName', 'purchase_date', 'cost']
        widgets = {
            'purchase_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
