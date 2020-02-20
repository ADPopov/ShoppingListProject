from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.utils import timezone

from shoppingList.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {'products_list': products_list}
    return render(request, 'shoppingList/index.html', context)


def add(request):
    try:
        if request.method == "POST":
            product = Product(
                name=request.POST.get("name"),
                shopName=request.POST.get("shopName"),
                purchase_date=timezone.now(),
                cost=request.POST.get("cost"),
                quantity=request.POST.get("quantity"))
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "shoppingList/add.html")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def edit(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shoppingList/edit.html', {'product': product})


def change(request, id):
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
        return HttpResponseNotFound("<h2>Product not found</h2>")
