from django.contrib import admin
from .models import Category,SubCategory
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display = ('category_name','slug')

# admin.site.register(SubCategory)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('subCategory_name',)}
    list_display = ('subCategory_name','slug', 'category_name')
