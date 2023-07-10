from django.contrib import admin
from .models import Order
# Register your models here.




class OrderAdmin(admin.ModelAdmin):
    list_display = ("shipping_address","user_id","total_price","order_date")
admin.site.register(Order,OrderAdmin)