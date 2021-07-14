from django.shortcuts import render
from django.http import HttpResponse
from forms import CustomersForms
import datetime


# Create your views here.
def home(request):
    return render(request, 'index.html')

# def calender(request):
#     return render(request, 'calendar.html')

def profile(request):
    return render(request, 'profile.html')

def ec(request):
    return render(request,'ecommerce-dashboard.html')

def customer(request):
    return render(request,'customer-list.html')
def customers_create_view(request):
    form = CustomersForms(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,"customers/customers_create.html",context)
