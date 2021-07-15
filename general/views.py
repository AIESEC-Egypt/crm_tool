from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomersForms, UserLoginForm
from django.shortcuts import render, redirect
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.contrib.auth import logout


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect("/login.html")

# def calender(request):
#     return render(request, 'calendar.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect("/login.html")
def ec(request):
    if request.user.is_authenticated:
        return render(request,'ecommerce-dashboard.html')
    else:
        return redirect("/login.html")
def customer(request):
    if request.user.is_authenticated:
        return render(request,'customer-list.html')
    else:
        return redirect("/login.html")
def customers_create_view(request):
    if request.user.is_authenticated:
        form = CustomersForms(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form':form
        }
        return render(request, "customers/customers_create.html", context)
    else:
        return redirect("/login.html")
def user_login_view(request):
    if request.user.is_authenticated:
        return redirect("index.html")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/index.html")
    return render(request, "login.html", {"form": form})


def edit_customer(request):
    if request.user.is_authenticated:
        return render(request, "edit-customer.html")
    else:
        return redirect("/login.html")
def edit_order(request):
    if request.user.is_authenticated:
        return render(request, "edit-order.html")
    else:
        return redirect("/login.html")
def edit_product(request):
    if request.user.is_authenticated:
        return render(request, "edit-product.html")
    else:
        return redirect("/login.html")
def invoice(request):
    if request.user.is_authenticated:
        return render(request, "invoice.html")
    else:
        return redirect("/login.html")
def order_list(request):
    if request.user.is_authenticated:
        return render(request, "order-list.html")
    else:
        return redirect("/login.html")
def product_list(request):
    if request.user.is_authenticated:
        return render(request, "product-list.html")
    else:
        return redirect("/login.html")
def logoutt(request):
    logout(request)
    return redirect("index.html");