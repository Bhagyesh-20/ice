from django.db import models

# Create your models here.
import uuid
from django.contrib.auth.models import User
# Create your models here.
#This is where the feedback goes
class Contact(models.Model):
    name = models.CharField(max_length=127)
    email = models.CharField(max_length=127)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

#the products list go here
class Product(models.Model):
    name = models.CharField(max_length=127)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=255,default="")
    subcategory = models.CharField(max_length=255,default="")
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='products')
    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    amount = models.FloatField(default=0)

    def __str__(self):
        return f"Order {self.order_id}"

    
