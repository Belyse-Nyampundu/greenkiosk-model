from django.db import models
from inventory.models import Product

# Create your models here.

class Cart(models.Model):
    inventory = models.ManyToManyField(Product)
    products = models.CharField(max_length=90)
    id_number = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.products

