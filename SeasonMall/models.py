from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, identifier, email, date_of_birth, bio, password=None):
        if not name:
            raise ValueError('must have user name')
        if not identifier:
            raise ValueError('must have user identifer')
        if not email:
            raise ValueError('must have user email')
        
        user = self.model(
            name=name,
            identifier=identifier,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            bio=bio,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, identifier, email, date_of_birth, bio, password):
        user = self.create_user(
            name=name,
            identifier=identifier,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            bio=bio,
            password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
  name = models.CharField(max_length=40, null=False, blank=False)
  identifier = models.CharField(max_length=40, null=False, blank=False, unique=True)
  email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
  date_of_birth = models.DateField()
  bio = models.TextField(blank=True)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  
  objects = UserManager()
  
  USERNAME_FIELD = 'identifier'
  REQUIRED_FIELDS = ['name', 'email', 'date_of_birth', 'bio']
  
  def __str__(self):
    return self.identifier
  def has_perm(self, perm, obj=None):
    return True
  def has_module_perms(self, app_label):
    return True
  
  @property
  def is_staff(self):
    return self.is_superuser
  
class Product(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=100, blank=False)
  price = models.IntegerField(blank=False)
  content = models.TextField()
  created_date = models.DateTimeField()
  image = models.ImageField(blank=True, null=True, upload_to='uploads/')
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True) #related_name은 Product.likes , User.likes  
  like_count = models.PositiveIntegerField(default=0)
  
  def __str__(self):
    return self.name
  
class BuyList(models.Model):
  product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)