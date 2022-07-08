import django
from django.shortcuts import render,redirect
from django.db.models import Q
from category.models import Category,SubCategory
from .models import Product, Review
from .forms import Product_review_form
# Create your views here.

def store(request,category_slug=None,subcategory_slug=None):

    if category_slug !=None:
        categories = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category = categories)
        product_count = products.count()
        print(category_slug)
    
        if category_slug !=None and subcategory_slug !=None:
            subcategories = SubCategory.objects.get(slug=subcategory_slug)
            products = Product.objects.filter(subCategory = subcategories)
            product_count = products.count()

    else:
        products = Product.objects.order_by('created_date')
        product_count = products.count()
    context = {
        'products':products,
        "product_count":product_count
    }
    return render(request, 'store/store.html',context)

def product_detail(request,category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        reviews = Review.objects.filter(product__slug = product_slug,status =True)
    except Exception as e:
        raise e
    context={
        'single_product':single_product,'reviews':reviews
    }
    return render(request,'store/product_detail.html',context)


def search(request):
    keyword  = request.GET['keyword']
    products= Product.objects.order_by('-created_date') .filter(Q(product_description__icontains=keyword)|Q (product_name__icontains=keyword)|Q (product_tagline__icontains=keyword)|Q (slug__icontains=keyword))
    product_count = products.count()
   
    context = {
            'products':products,
            'product_count':product_count
        }
    return render(request, 'store/store.html',context)

def user_review(request,prod_id):
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        try:
            reviews = Review.objects.get(user_id=request.user.id, product_id=prod_id)
            form = Product_review_form(request.POST,instance=reviews)
            if form.is_valid():
                form.save()
                return redirect(url)
        except Review.DoesNotExist:
            form = Product_review_form(request.POST)
            if form.is_valid():
                data = Review()
                data.rating = form.cleaned_data['rating']
                data.subject = form.cleaned_data['subject']
                data.reveiw = form.cleaned_data['reveiw']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = prod_id
                data.user_id = request.user.id
                data.save()
                return redirect(url)


    