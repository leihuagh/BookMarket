from django import forms
from reference.models import Author, Genre, Series, Publisher, Manufacturer


class AuthorRefCreateForm(forms.ModelForm):
    class Meta:
        model = Author

        fields = [
            'name',
            'description'
        ]


class GenreRefCreateForm(forms.ModelForm):
    class Meta:
        model = Genre

        fields = [
            'name',
            'description'
        ]


class SeriesRefCreateForm(forms.ModelForm):
    class Meta:
        model = Series

        fields = [
            'name',
            'description'
        ]


class PublisherRefCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher

        fields = [
            'name',
            'description'
        ]


class ManufacturerRefCreateForm(forms.ModelForm):
    class Meta:
        model = Manufacturer

        fields = [
            'name',
            'description'
        ]
