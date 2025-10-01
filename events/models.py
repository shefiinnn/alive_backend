from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product/')

    def __str__(self):
        return self.name
    
class GalleryImage(models.Model):
    image=models.ImageField(upload_to='gallery/')
    description=models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or f"Image {self.id}"
    
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    number = models.BigIntegerField()  
    message=models.TextField()
    replied=models.BooleanField(default=False)
    recieved_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Enquiry {self.name}"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('DECLINED', 'Declined'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    number=models.CharField(max_length=20)
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(default="")
    place=models.TextField(default="")
    subtotal=models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    price=models.DecimalField(max_digits=10 , decimal_places=2,null=True,blank=True)
    def __str__(self):
        return f"Order for {self.product.name} by {self.customer_name}"





