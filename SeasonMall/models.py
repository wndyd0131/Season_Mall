from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
  id = models.CharField(max_length=50, unique=True, primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=30, unique=True)
  phone_num = models.IntegerField(blank=False)
  created_date = models.DateTimeField()
  
  def __str__(self):
    return self.id
  
class Product(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=100, blank=False)
  price = models.IntegerField(blank=False)
  content = models.TextField()
  created_date = models.DateTimeField()
  
  # image = models.ImageField(upload_to=None, height_field=None,width_field=None,max_length=100)
  # seller = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
  def __str__(self):
    return self.name
  
class BuyList(models.Model):
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  