
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.utils import timezone

from shoppingList.forms.productForm import ProductForm
from shoppingList.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {'products_list': products_list}
    return render(request, 'shoppingList/index.html', context)


def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
    return render(request, 'shoppingList/add.html', {'form': form})


def edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shoppingList/edit.html', {'form': form, "product": product})
