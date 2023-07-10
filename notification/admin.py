from django.contrib import admin
from .models import Notification

# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("message","user_id","time_stamp")
admin.site.register(Notification,NotificationAdmin)