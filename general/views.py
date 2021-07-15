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
    return render(request, "customers/customers_create.html", context)

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

def logoutt(request):
    logout(request)
    return redirect("index.html");