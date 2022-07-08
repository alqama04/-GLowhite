from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Carousel
from category.models import Category
from store.models import Product
# Create your views here.

def home(request):
    carousel = Carousel.objects.all().order_by('-id')
    facial_kits = Category.objects.filter(category_name__icontains = 'facial kits')
    bleaches = Category.objects.filter(category_name__icontains = 'bleaches')

    featured_products = Product.objects.all().order_by('modified_date')[1::5]
    context={
        'carousel':carousel,
        'facial_kits':facial_kits,
        'bleaches':bleaches,
        'featured_products':featured_products,
    }
    return render(request, 'core/home.html',context)


def about_Company(request):
    return render(request, 'core/about.html')


