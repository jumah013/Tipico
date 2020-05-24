from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,blank=True,null=True)
    phone=models.CharField(max_length=200,blank=True,null=True)
    email=models.CharField(max_length=200,blank=True,null=True)
    profile_pic=models.ImageField(default="blank.jpg",null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
    
    
  
class Games(models.Model):
    name=models.CharField(max_length=200,null=True)
    descriptions=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)

    def __str__(self):
        return self.name

class Ordergame(models.Model):
    product=models.ForeignKey(Games,null=True,on_delete=models.SET_NULL,blank=True)

    def __str__(self):
        return self.product.name


