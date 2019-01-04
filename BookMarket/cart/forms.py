from django import forms
from .models import ProductsInCart


class AddToCartForm(forms.ModelForm):

    class Meta:
        model = ProductsInCart
        fields = [
            'book',
            'quantity'
        ]

        widgets = {
            'book': forms.HiddenInput()
        }