from django.shortcuts import render
from .forms import PaymentUploadForm
from .models import Payment

# Create your views here.


def upload_payment(request):
    if request.method == "POST":

        form = PaymentUploadForm(request.POST,request.FILES)
        form.is_valid()
        form.save()

    else:
            form = PaymentUploadForm()

    return render(request,"payment/payment_upload.html",{"form" : form})


def list_payments(request):
    payment = Payment.objects.all()

    return render(request,"payment/payment_list.html" ,{"payment":payment})

