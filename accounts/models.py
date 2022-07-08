from django.core.checks import messages
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password = None):
        if not email :
            raise ValueError('User must have an email address')
       
        if not username :
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, first_name, last_name,  email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin  = True
        user.is_active = True
        user.is_staff  = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user 


# case insensitive email
class LowerEmailField(models.EmailField):
    def to_python(self, value):
        value = super().to_python(value)
        if isinstance(value,str):
            return value.lower()
        return value


class User(AbstractBaseUser):
    first_name      = models.CharField(max_length=50,blank=True,null=True)
    last_name       = models.CharField(max_length=50,blank=True,null=True)
    username        = models.CharField(max_length=50,)
    email           = LowerEmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50,blank=True,null=True)

# required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default = False)
    is_staff        = models.BooleanField(default = False)
    is_active       = models.BooleanField(default = True)
    is_superadmin   = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    class Meta:
        # verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    



class ContactUs(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'ContactUs'
    

class GlowhiteMeta(models.Model):
    meta_title       = models.CharField(max_length=130,blank=True, null=True)
    meta_description = models.TextField(blank=True,null=True)

