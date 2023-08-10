from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.



# this is the business logic

def upload_product(request):        #  http request you send the request
    if request.method == "POST":

        form = ProductUploadForm(request.POST,request.FILES)   #    you rendered that request in a form and when it comes back it's render in that form   
        if form.is_valid():
            form.save()

            

    else:
        form = ProductUploadForm()
    # return a response
    return render(request,"inventory/product-upload.html",{"form" : form})       # request and the second arugrement is the template of where you want to create that form


def products_list(request):
    products = Product.objects.all()
    return render(request,"inventory/products_list.html" ,{"products":products})     # here is to display all product and be seen by the user


def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,"inventory/product_detail.html",{"product":product})   # Here we want to render the single product

def edit_product_view(request,id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductUploadForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view",id = product.id)
    else:
        form = ProductUploadForm(instance=Product)
        return render(request,"inventory/edit_product.html",{"form":form})




# def delete_product(request, id):
#     product = get_object_or_404(Product, id=id)

#     if request.method == "POST":
#         product.delete()
#         return redirect("products_list_view")
#     return render(request, "delete_product.html", {"product": product})




def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("products_list_view")
    return render(request, "delete_product.html", {"product": product})







     

  

