from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=32)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField()
    location = models.CharField(max_length=32)


    def __str__(self):
        return self.name