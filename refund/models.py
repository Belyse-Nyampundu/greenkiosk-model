from django.db import models

# Create your models here.

class Refund (models.Model):
    products = models.CharField(max_length=77)
    order_id = models.PositiveIntegerField()
    refund_id = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    reason = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    request_date = models.DateField()
    processed_date = models.DateField()
    def __str__(self):
        return self.products
