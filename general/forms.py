from django import forms
from .models import Customers


class CustomersForms(forms.Form):
    class Meta:
        model = Customers
        fields = [
            'Customer_Name',
            'contact',
            'person_in_charge',
            'description',
            'timestamp',
            'registration'
        ]
