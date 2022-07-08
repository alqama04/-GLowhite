from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext_lazy as _

class contactUsForm(forms.ModelForm):
   
    class Meta:
       model = ContactUs
       fields = ['username', 'email', 'subject', 'message']

       widgets ={
           'username': forms.TextInput(attrs={'placeholder': 'Enter Your Full Name', 'class':'form-control'}),
           'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email', 'class':'form-control'}),
           'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class':'form-control'}),
           'message': forms.Textarea(attrs={'rows':6, 'placeholder': 'Enter Your message','class':'form-control'}),
       }



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for fl in self.fields.values():
            fl.widget.attrs['class']='form-control ps-1'
            fl.widget.attrs['placeholder']='Enter ' + str(fl.label)



class UserLoginForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for fl in self.fields.values():
            fl.widget.attrs['class']='form-control'
            fl.widget.attrs['placeholder']=str(fl.label)

class UserPasswordResetForm(PasswordResetForm):
      email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",'class':'form-control','placeholder':'Enter Your Registerd Email'}),
    )

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
    label=_("New password"),
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control","placeholder":'Enter New Password'}),
    strip=False,)
    new_password2 = forms.CharField(
        label=_("Confirm Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control","placeholder":'Confirm New Password'}),)