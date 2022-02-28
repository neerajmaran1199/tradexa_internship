from django.shortcuts import render
from .models import Product
# Create your views here.

def ProductView(request):
    items = Product.objects.all()
    return render(request, 'products/product.html', {'items':items})