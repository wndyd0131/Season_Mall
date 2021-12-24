from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
  id = models.CharField(max_length=50, unique=True, primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=30, unique=True)
  created_date = models.DateTimeField()
  
class Product(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=100)
  price = models.IntegerField(blank=False)
  

  
class BuyList(models.Model):
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  