from django.contrib import admin
# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import *

class AccountAdmin(UserAdmin):
    list_display = ['email','first_name','last_name','username','last_login','date_joined','is_active']
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)
    filter_horizontal =()
    list_filter = ('is_admin','is_staff','is_active','is_superadmin')
    fieldsets = ()
    search_fields = ('email',)

@admin.register(GlowhiteMeta)
class GlowhiteMetaAdmin(admin.ModelAdmin):
    list_display = ['id','meta_title','meta_description']
    list_display_links = ['meta_title']


admin.site.register(User, AccountAdmin)
admin.site.register(ContactUs)


