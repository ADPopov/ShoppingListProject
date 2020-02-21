from datetime import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(u'Название', max_length=200)
    shopName = models.CharField(u'Название магазина', max_length=30, default="Не указано")
    purchase_date = models.DateTimeField(u'Дата покупки', default=datetime.now())
    cost = models.IntegerField(u'Стоимость', default=0)
    quantity = models.IntegerField(u'Количество', default=0)

    def __str__(self):
        return "Название: {}\nКоличество: {}\nСтоимость: {}\nДата покупки:{}\n Магазин: {}".format(self.name,
                                                                                                   self.quantity,
                                                                                                   self.cost,
                                                                                                   self.purchase_date.date(),
                                                                                                   self.shopName)
