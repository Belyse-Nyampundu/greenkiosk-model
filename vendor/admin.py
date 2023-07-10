from django.contrib import admin
from .models import Vendor

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone_number","address","products")
admin.site.register(Vendor,VendorAdmin)