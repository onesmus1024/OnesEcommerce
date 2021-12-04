from enum import auto
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.reverse_related import ManyToOneRel

# Create your models here.
class UserAddress(models.Model):
    street_name = models.CharField(max_length=50,null=False)
    state = models.CharField(max_length=50,null=False)
    city = models.CharField(max_length=50,null=False)
    zipcode = models.IntegerField(null=False)
    def __str__(self):
        return self.street_name

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date_registered = models.DateField(auto_now=True)
    user_address = models.ForeignKey(UserAddress,on_delete=CASCADE)

    def __str__(self):
        return self.username

class ProductBrand(models.Model):
    product_brand_name = models.CharField(max_length=50)
    def __str__(self):
        return self.product_brand_name


class ProductCategory(models.Model):
    product_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.product_category_name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='images/')
    product_price = models.DecimalField(max_digits=7,null=False,decimal_places=2)
    date_posted=models.DateField(auto_now=True)
    available = models.BooleanField(default=True)
    product_brand = models.ForeignKey(ProductBrand,on_delete=CASCADE)
    product_category=models.ForeignKey(ProductCategory,on_delete=CASCADE,default=1)


    def __str__(self):
        return self.product_name

class ProductReview(models.Model):
    product_review = models.CharField(max_length=500)
    #product = models.ForeignKey(Product,on_delete=CASCADE,default=1)
    def __str__(self):
        return self.product_review
