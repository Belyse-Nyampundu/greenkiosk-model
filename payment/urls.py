from django.urls import  path
from .views import  upload_payment,list_payments

# urlpatterns = [
#     path("products/upload",upload_product,name = "product_upload_view"),  

urlpatterns = [
    path("payment/upload",upload_payment,name = "upload_payment_view"),
    path("payment/list",list_payments,name = "list_payments_view")
]