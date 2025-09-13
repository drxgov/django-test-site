from django.shortcuts import render,get_object_or_404
from .models import Category,Product

def product_list(request,category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(aviable = True)
    
    category = None
    if category_slug:
        category = get_object_or_404(Category,category_slug = category_slug)
        products = Product.filter(category = category)
    
    return render(request,'main/product/list.html',
                  {'category':category,
                   'categories': categories,
                   'products':products
                   })