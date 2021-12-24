from django.contrib import admin
from .models import User, Product, BuyList
# Register your models here.
admin.site.register(BuyList)
class UserAdmin(admin.ModelAdmin):
  search_fields = ['id']
  
class ProductAdmin(admin.ModelAdmin):
  search_fields = ['name']
  
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)