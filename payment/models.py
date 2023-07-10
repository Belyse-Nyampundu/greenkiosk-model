from django.db import models

# Create your models here.

class Payment (models.Model):
    products = models.CharField(max_length=90)
    user_id = models.PositiveIntegerField()
    order_id = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=90)
    payment_amount = models.DecimalField(max_digits=6, decimal_places= 2)
    transaction_id = models.PositiveIntegerField()
    def __str__(self):
        return self.products