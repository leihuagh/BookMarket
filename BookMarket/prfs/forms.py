from django import forms
from django.contrib.auth.models import User


class PrflUpdateForm(forms.Form):
    delivery_address = forms.CharField(label='адрес доставки', max_length=100)
    username = forms.CharField(label='логин', max_length=100)
    first_name = forms.CharField(label='имя', max_length=100)
    last_name = forms.CharField(label='фамилия', max_length=100)
    email = forms.EmailField(label='электронный адрес')
    phone_number = forms.IntegerField(label='номер телефона')
