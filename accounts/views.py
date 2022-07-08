from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetConfirmView
from django.contrib.auth import login
# Create your views here.
def contact_us(request):
    if request.method=='POST':
        form = contactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulation Your Messages Sent Successfully')
            return redirect('contac_us')
    else:
        form = contactUsForm 
    return render(request,'accounts/contact_us.html',{'form':form})
 
def user_registrations(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                u = form.save()
                if u is not None:
                    login(request=request,user=u)
                    return redirect('store')
        else:
            form = RegistrationForm
        
        context = {'form':form}
        return render(request,'accounts/user_register.html',context)



class UserloginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_url = 'store'



class UserLogoutView(LogoutView):
    success_url = 'login'


# password management
class PasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    form_class = UserPasswordResetForm

# PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',form_class='UserSetPasswordForm')
class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = UserSetPasswordForm


