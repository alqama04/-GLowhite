from django.urls import path
from .import views
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
from.forms import UserSetPasswordForm


urlpatterns = [
    path("contact-Us/", views.contact_us, name='contac_us'),
    path('User-register/',views.user_registrations,name='user_registration'),
    path('login/',views.UserloginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name = 'logout'),
   
    path('password-reset/',views.PasswordResetView.as_view(),name='password_reset'),
    path("password_reset/done/",PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name="password_reset_done",),
   
    path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    
    path("reset/done/",PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name="password_reset_complete",),

   
    

]
