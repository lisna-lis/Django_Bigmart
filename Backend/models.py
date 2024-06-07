from django.db import models

# Create your models here.
class Categorydb(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="Category Images",null=True,blank=True)

class Productdb(models.Model):
    Category=models.CharField(max_length=100,null=True,blank=True)
    Product_name=models.CharField(max_length=100,null=True,blank=True)
    Product_Image=models.ImageField(upload_to="Product Image",null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)


