from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Category, Product, CommentProduct
from .forms import UserCommentProductForm

# Create your views here.


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "Stores/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "Stores/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    if request.method == 'POST':
        form = UserCommentProductForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(slug=slug)
            desc = form.cleaned_data['desc']
            author = request.user
            CommentProduct(product=product, author=author, desc=desc).save()
            # print(desc, author, product)
            return HttpResponseRedirect('/'+slug)
    else:
        form = UserCommentProductForm(request.POST)
        product = get_object_or_404(Product, slug=slug, is_active=True)
        productComments = CommentProduct.objects.filter(product=product)
        context ={
            "product": product,
            "productComments": productComments,
            "form": form
        }
        return render(request, "Stores/single.html", context)