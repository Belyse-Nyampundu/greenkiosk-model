from django.db import models

from payment.models import Payment
# Create your models here.


class Order(models.Model):

    payment = models.OneToOneField(Payment,on_delete=models.PROTECT,null=True)
    shipping_address = models.CharField(max_length=90)
    user_id = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
   
    order_date = models.DateField()
    
    def __str__(self):
        return self.shipping_address