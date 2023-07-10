from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=90)
    products = models.CharField(max_length=90)
    def __str__(self) :
        return self.name