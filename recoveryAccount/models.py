from django.db import models

# Create your models here.

class RecoveryAccount(models.Model):
    user_name = models.CharField(max_length=90)
    user_id = models.PositiveIntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.user_name