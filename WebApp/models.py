from django.db import models

# Create your models here.
class Contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
class Registerdb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email =models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100,null=True,blank=True)

class cartdb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    product_name=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)