from django.contrib import admin
from .models import RecoveryAccount

# Register your models here.


class RecoveryAccountAdmin(admin.ModelAdmin):
    list_display = ("user_name","user_id","email")
admin.site.register(RecoveryAccount,RecoveryAccountAdmin)