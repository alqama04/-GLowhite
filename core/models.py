from django.db import models
from PIL import Image

# Create your models here.
class Carousel(models.Model):
    carousel_title       = models.CharField(max_length=255, blank=True, null=True)
    carousel_description = models.TextField(blank=True, null=True)
    carousel_image       = models.ImageField(upload_to='photos/carouselImage')
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        imag = Image.open(self.carousel_image.path)
        output_size = (1280, 720,)
        newSize = imag.resize(output_size,Image.BICUBIC)
        newSize.format = 'PNG'
        newSize.save(self.carousel_image.path,quality=95)

    def __str__(self):
        return str(self.carousel_title)
    class Meta:
        verbose_name_plural = 'Sliders'

    