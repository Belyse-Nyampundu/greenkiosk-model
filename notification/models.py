from django.db import models

# Create your models here.

class Notification(models.Model):
    message = models.CharField(max_length=300)
    user_id = models.PositiveIntegerField()
    time_stamp = models.DateTimeField()

    def __str__(self) -> str:
        return  self.message