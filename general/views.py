from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home(request):
    return render(request, 'blue-dashboard.html')

def calender(request):
    return render(request, 'calendar.html')
