from django.db import models
from category.models import Category,SubCategory
from django.urls import reverse
from PIL import Image
from accounts.models import User
from django.db.models import Avg
# Create your models here.

class Product(models.Model):
    category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategory         = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True, null=True)
    product_name        = models.CharField(max_length=255)
    slug                = models.SlugField(max_length = 200, unique = True)
    product_tagline     = models.CharField(max_length=1000,blank=True, null=True)
    product_description = models.TextField()
    price               = models.IntegerField()
    discounted_price    = models.IntegerField(blank=True)
    ingredients         = models.CharField(max_length=1000, blank=True, null=True)
    Product_image       = models.ImageField(upload_to='photos/products')
    image_gallery_1     = models.ImageField(upload_to='photos/products', blank=True, null=True)
    image_gallery_2     = models.ImageField(upload_to='photos/products', blank=True, null=True)
    image_gallery_3     = models.ImageField(upload_to='photos/products', blank=True, null=True)
    image_gallery_4     = models.ImageField(upload_to='photos/products', blank=True, null=True)
    quantity            = models.CharField(max_length=20,blank=True)
    Product_feature1    = models.CharField(max_length=150,blank=True)
    Product_feature2    = models.CharField(max_length=150,blank=True)
    Product_feature3    = models.CharField(max_length=150,blank=True)
    Product_feature4    = models.CharField(max_length=150,blank=True)
    Product_feature5    = models.CharField(max_length=150,blank=True)
    Product_feature6    = models.CharField(max_length=150,blank=True)
    Product_feature7    = models.CharField(max_length=150,blank=True)
    url                 = models.URLField(blank=True,null=True)
    is_available        = models.BooleanField(default=True)
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_date       = models.DateTimeField(auto_now=True ,)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        imag = Image.open(self.Product_image.path)
        output_size = (650, 650,)
        newSize = imag.resize(output_size,Image.BICUBIC)
        newSize.format = 'PNG'
        newSize.save(self.Product_image.path,quality=95)


    def __str__(self):
        return self.product_name

    def product_url(self):
        return reverse('product_detail',args=[self.category.slug, self.slug])

    def avg_rate(self):
        review = Review.objects.filter(product=self).aggregate(avarage=Avg('rating'))
        avg=0
        if review["avarage"] is not None:
            avg=float(review["avarage"])
        return format(avg,'.2f')



class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product  = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
   
    rating = models.FloatField()
    subject = models.CharField(max_length=70,blank=True,null=True)
    reveiw = models.TextField(max_length=200,blank=True,null=True)
    ip = models.CharField(max_length=200)

    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username

