from django.contrib import admin
from .models import Refund

# Register your models here.


class RefundAdmin(admin.ModelAdmin):
    list_display = ("products","order_id","refund_id","amount","reason","status","request_date","processed_date")
admin.site.register(Refund,RefundAdmin)