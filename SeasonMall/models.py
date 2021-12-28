from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
  
class Product(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=100, blank=False)
  price = models.IntegerField(blank=False)
  content = models.TextField()
  created_date = models.DateTimeField()
  # image = models.ImageField(upload_to=None, height_field=None,width_field=None,max_length=100)
  author = models.ForeignKey("auth.User", on_delete=models.CASCADE, null = True)
  
  def __str__(self):
    return self.name
  
class BuyList(models.Model):
  product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)