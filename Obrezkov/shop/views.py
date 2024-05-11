from django.shortcuts import render

from django.views.generic import ListView

from shop.models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'products.html'