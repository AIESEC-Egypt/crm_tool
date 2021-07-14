from django.urls import path
from general.views import customers_create_view

urlpatterns = [
    path('customers/', customers_create_view),

]