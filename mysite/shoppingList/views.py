from django.http import HttpResponse
from django.shortcuts import render

from shoppingList.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {'products_list': products_list}
    return render(request, 'shoppingList/index.html', context)


def add(request):
    return HttpResponse("Страница добавления нового продукта")


def edit(request, question_id):
    product = Product.objects.filter(id=question_id).first()
    return HttpResponse("вы изменяете продукт с названием %s" % product.name)