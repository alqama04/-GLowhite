from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name        = models.CharField(max_length=255, unique=True)
    slug                 = models.SlugField(max_length=255, unique=True) 
    category_tagline     = models.CharField(max_length=350, blank=True, null=True)
    category_short_intro = models.CharField(max_length=350, blank=True, null=True)
    description          = models.TextField(blank=True, null=True)
    image1               = models.ImageField(upload_to='photos/category', blank=True, null=True)
    image2               = models.ImageField(upload_to='photos/category', blank=True, null=True)
    image3               = models.ImageField(upload_to='photos/category', blank=True, null=True)
    image4               = models.ImageField(upload_to='photos/category', blank=True, null=True)
    image5               = models.ImageField(upload_to='photos/category', blank=True, null=True)
    created_date         = models.DateTimeField(auto_now_add=True)
    modified_date        = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):
    category_name    = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subCategory_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    slug             = models.SlugField(max_length=255, unique=True, blank=True, null=True)   

    def __str__(self):
        return self.subCategory_name

    class Meta:
        verbose_name_plural = 'Sub Categories'
   
    def subcategory_url(self):
        return reverse('products_by_subcategory',args=[self.category_name.slug, self.slug])
