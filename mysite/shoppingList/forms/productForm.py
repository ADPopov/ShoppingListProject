from django import forms
from django.forms import ModelForm

from shoppingList.models import Product


class ProductDeskForm(forms.Form):
    quantity = forms.IntegerField(label='Количество')
    name = forms.CharField(label='Название', max_length=200),
    shopName = forms.CharField(label='Название магазина', max_length=30),
    purchase_date = forms.DateTimeField(label='Дата покупки'),
    cost = forms.IntegerField(label='Стоимость'),


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'shopName', 'purchase_date', 'cost']