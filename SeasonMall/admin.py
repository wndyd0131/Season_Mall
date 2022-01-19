from django.contrib import admin
from .models import User, Product, BuyList
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(BuyList)
  
class ProductAdmin(admin.ModelAdmin):
  search_fields = ['name']

admin.site.register(Product, ProductAdmin)


class UserAdmin(admin.ModelAdmin):
  pass

admin.site.register(get_user_model(), UserAdmin)