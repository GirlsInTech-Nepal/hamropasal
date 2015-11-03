from django.db import models
import PIL
class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', null=True, blank=True)


    def __str__(self):
        return self.name

class ProductType(models.Model):
    category=models.ForeignKey(Category)
    product_type = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_type

class Product(models.Model):
    
    product_type = models.ForeignKey(ProductType)
    name = models.CharField(max_length=30)
    product_code = models.IntegerField()
    price = models.IntegerField()
    available_quantity = models.IntegerField()
    primary_image= models.ImageField(upload_to='Images')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    fullname=models.CharField(max_length=40)
    address=models.CharField(max_length=40)

    def __str__(self):
        return self.fullname

class Sales(models.Model):
    product = models.ForeignKey(Product)
    customer = models.ForeignKey(Customer)
    quantity = models.IntegerField()
    sales_date = models.DateTimeField(auto_now_add=True)



