from django.http import HttpResponse
from django.http import JsonResponse
from shoppingList.models import Product


def index(request):
    products_list = Product.objects.all()
    output = ", ".join([q.name for q in products_list])
    return HttpResponse(output)


def add(request):
    return HttpResponse("Страница добавления нового продукта")


def edit(request, question_id):
    return HttpResponse("вы изменяете продукт с идентификатором %s" % question_id)
# Create your views here.
