
from django import forms

from .models import Review

class Product_review_form(forms.ModelForm):
   
    class Meta:
        model = Review
        fields =['rating','subject','reveiw']