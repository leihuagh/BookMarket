from django import forms
from reference.models import Author, Genre, Series, Publisher, Manufacturer, OrderStatus


class AuthorRefForm(forms.ModelForm):
    class Meta:
        model = Author

        fields = [
            'name',
            'description'
        ]


class GenreRefForm(forms.ModelForm):
    class Meta:
        model = Genre

        fields = [
            'name',
            'description'
        ]


class SeriesRefForm(forms.ModelForm):
    class Meta:
        model = Series

        fields = [
            'name',
            'description'
        ]


class PublisherRefForm(forms.ModelForm):
    class Meta:
        model = Publisher

        fields = [
            'name',
            'description'
        ]


class ManufacturerRefForm(forms.ModelForm):
    class Meta:
        model = Manufacturer

        fields = [
            'name',
            'description'
        ]


class OrderStatusRefForm(forms.ModelForm):
    class Meta:
        model = OrderStatus

        fields = [
            'name',
            'description'
        ]
