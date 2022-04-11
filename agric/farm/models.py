from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_farmer =models.BooleanField(default=True)
    is_laborer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Farmer(models.Model):
    farmer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    #image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.farmer.username

