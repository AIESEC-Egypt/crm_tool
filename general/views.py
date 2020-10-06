from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def Home(request):
    # return render(request, 'home.html')
    return render(request, 'blue-dashboard.html')