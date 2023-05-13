import datetime

from django.shortcuts import HttpResponse,redirect,render
from posts.models import Product
# Create your views here.
'''MVC - Model View Controller'''


def main_view(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")

def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        context = {
            'products': products
    }
        return render(request, "products/products.html", context=context)