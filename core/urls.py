from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-company/', views.about_Company, name='about-company'),
]
