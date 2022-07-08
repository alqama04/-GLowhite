from django.contrib import admin
from .models import Product,Review
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
    list_display =['id','product_name', 'category','subCategory','price','discounted_price','created_date','modified_date']

admin.site.register(Review)