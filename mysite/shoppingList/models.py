from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(u'Название', max_length=200)
    shopName = models.CharField(u'Название магазина', max_length=30, default="Не указано")
    purchase_date = models.DateTimeField(u'Дата покупки')
    cost = models.IntegerField(u'Стоимость', default=0)
    quantity = models.IntegerField(u'Количество', default=0)

