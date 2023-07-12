from django.contrib import admin
from .models import Shipment

# Register your models here.

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("product","location","shipDate","shipping_method")

admin.site.register(Shipment,ShipmentAdmin)