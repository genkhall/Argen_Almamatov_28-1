import datetime

from django.shortcuts import HttpResponse, redirect, render
from posts.models import Product, Review
from django.views.generic import ListView, DetailView, CreateView
from posts.forms import ProductCreateForm, ReviewCreateForm
from django.contrib.auth import logout, login
from posts.constants import PAGINATION_LIMIT

# Create your views here.
'''MVC - Model View Controller'''


def main_view(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")


class MainPageCBV(ListView):
    model = Product
    template_name = 'layouts/index.html'


def products_view(request):
    # logout(request)
    if request.method == "GET":
        # print(request.GET)
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page'))
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * (page):]

        if search:
            products = products.filter(title__contains=search)

        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, "products/products.html", context=context)


class PostCBV(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "products/products.html"

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            # print(request.GET)
            products = self.queryset
            search = request.GET.get('search')
            page = int(request.GET.get('page', 1))
            max_page = products.__len__() / PAGINATION_LIMIT
            if round(max_page) < max_page:
                max_page = round(max_page) + 1
            else:
                max_page = round(max_page)

            products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * (page):]

            if search:
                products = products.filter(title__contains=search)

            context = {
                'products': products,
                'user': request.user,
                'pages': range(1, max_page + 1)
            }
            return render(request, self.template_name, context=context)


# def comment_view(request, id):
#     if request.method == "GET":
#         product = Product.objects.get(id=id)
#         context = {
#             'product': product,
#             'comments': product.review_set.all()
#         }
#
#         return render(request, 'products/detail.html', context=context)
#     if request.method == 'GET':
#         product = Product.objects.get(id=id)
#         context = {
#             'product': Product,
#             'form': ReviewCreateForm,
#             'review': product.review_set.all()
#         }
#
#         return render(request, 'products/detail.html', context=context)
#
#     if request.method == 'POST':
#         comment = Product.objects.get(id=id)
#         form = ReviewCreateForm(request.POST)
#         if form.is_valid():
#             Review.objects.create(
#                 text=form.cleaned_data.get('text'),
#                 comment=comment
#             )
#
#         return render(request, 'products/detail.html', context={
#             'form': form,
#             'comment': comment,
#             'review': comment.review_set.all()
#         })


class CommentCBV(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.review_set.all()
        context['form'] = ReviewCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            comment = self.object
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                comment=comment
            )
        return self.render_to_response(self.get_context_data(form=form, review=self.object.review_set.all()))


def post_create_view(request):
    global form
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
