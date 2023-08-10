from django.urls import path
from .views import upload_product  ,products_list ,product_detail,edit_product_view,delete_product

# from .views import product_list
# Here we are going to create the url of our view we have created

urlpatterns = [
    path("products/upload",upload_product,name = "product_upload_view"),        # it is a good idea to give the path like "product/upload a name"
    path("products/list",products_list ,name = "products_list_view"),
    path("products/<int:id>/",product_detail,name = "product_detail_view"),
    path("products/edit/<int:id>/" ,edit_product_view,name = "product_edit_view"),
    path("products/delete/<int:id>/",delete_product,name = "product_delete_view"),

    #  path('delete_product/<int:id>/', views.delete_product, name='delete_product'),

    # path('delete_product/<int:id>/', delete_product, name='delete_product'),
]

