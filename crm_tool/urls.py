"""crm_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from general.views import *
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('profile.html', profile, name='profile'),
    path('index.html', home, name='home'),
    path('customer.html', customer, name='customer'),
    path('index.html', ec, name='ec'),
<<<<<<< HEAD
    path('login.html', login, name='login'),
=======
    path('login.html', user_login_view, name="auth"),
    path('customers/customers_create.html', customers_create_view, name="customer")
>>>>>>> FormsGraduation
    # path('calendar', calender, name='calendar')
]
