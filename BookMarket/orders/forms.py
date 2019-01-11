from django import forms
from orders.models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders

        fields = [
            'cart',
            'status',
            'phone',
            'email',
            'delivery_address',
            'informations',
        ]

        widgets = {
            'cart': forms.HiddenInput(),
            'status': forms.HiddenInput(),
        }


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Orders

        fields = [
            'cart',
            'status',
            'phone',
            'email',
            'delivery_address',
            'informations',
        ]

        widgets = {
            'cart': forms.HiddenInput(),
        }
