import datetime

from django.shortcuts import HttpResponse, redirect, render
from posts.models import Product, Review
from posts.forms import ProductCreateForm, ReviewCreateForm
from django.contrib.auth import logout,login
from posts.constants import PAGINATION_LIMIT

# Create your views here.
'''MVC - Model View Controller'''


def main_view(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")


def products_view(request):
    # logout(request)
    if request.method == "GET":
        # print(request.GET)
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page'))
        max_page = products.__len__()/ PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)



        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * (page):]

        if search:
            products = products.filter(title__contains=search)

        context = {
            'products': products,
            'user':request.user,
            'pages': range(1, max_page +1)
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
