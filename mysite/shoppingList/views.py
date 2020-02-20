from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from shoppingList.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {'products_list': products_list}
    return render(request, 'shoppingList/index.html', context)


def add(request):
    return HttpResponse("Страница добавления нового продукта")


def edit(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shoppingList/edit.html', {'product': product})


def vote(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.shopName = request.POST.get("shopName")
            product.cost = request.POST.get("cost")
            product.quantity = request.POST.get("quantity")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "shoppingList/edit.html", {"product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
