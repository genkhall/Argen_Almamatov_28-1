import datetime

from django.shortcuts import HttpResponse, redirect, render
from posts.models import Product, Review
from posts.forms import ProductCreateForm, ReviewCreateForm
from django.contrib.auth import logout,login

# Create your views here.
'''MVC - Model View Controller'''


def main_view(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")


def products_view(request):
    # logout(request)
    if request.method == "GET":
        products = Product.objects.all()
        context = {
            'products': products,
            'user':request.user
        }
        return render(request, "products/products.html", context=context)


def comment_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        context = {
            'product': product,
            'comments': product.review_set.all()
        }

        return render(request, 'products/detail.html', context=context)
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        context = {
            'product': Product,
            'form': ReviewCreateForm,
            'review': product.review_set.all()
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        comment = Product.objects.get(id=id)
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                comment=comment
            )

        return render(request, 'products/detail.html', context={
            'form': form,
            'comment':comment,
            'review': comment.review_set.all()
        })


def post_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }

        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        date, files = request.POST, request.FILES
        form = ProductCreateForm(date, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                rate=form.cleaned_data.get('rate'),
                model=form.cleaned_data.get('model'),
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


# def comments_create_view(request):
