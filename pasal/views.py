from django.shortcuts import render , render_to_response


# Create your views here.
from .models import Product,ProductType, Category

def show(request):
    products=Product.objects.all()
    categories= Category.objects.all()
    producttypes= ProductType.objects.all()
    return render_to_response('show.html',{'products':products,'categories':categories,'producttypes':producttypes})

def category(request):
    categories= Category.objects.all()
    return render_to_response('category.html',{'categories':categories})

def customers(request):
    customers= Category.objects.all()
    return render_to_response('customer.html',{'customers':customers})



