from django.db import models
from customer.models import Customer
# Create your models here.

class Shipment(models.Model):
    product = models.CharField(max_length=90)
    customer = models.OneToOneField(Customer,on_delete=models.PROTECT,null=True)
    location = models.CharField(max_length=90)
    shipDate = models.DateField()
    shipping_method = models.CharField(max_length=90)
  
    

    def __str__(self):
        return self.product
