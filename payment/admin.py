from django.contrib import admin
from .models import Payment

# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("products","user_id","order_id","payment_method","payment_amount","transaction_id")
admin.site.register(Payment,PaymentAdmin)
