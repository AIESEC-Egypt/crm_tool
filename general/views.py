from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home(request):
    return render(request, 'index.html')

# def calender(request):
#     return render(request, 'calendar.html')

def profile(request):
    return render(request, 'profile.html')