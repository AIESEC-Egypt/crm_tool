from django import forms
from .models import Customers
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
    )


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
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This is user does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password!")
            if not user.is_active:
                raise forms.ValidationError("This is user is not active!")

        return super(UserLoginForm, self).clean(*args, **kwargs)
