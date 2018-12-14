from django import forms
from products.models import Book
from django.core.exceptions import ValidationError
import re


class ProductsForm(forms.ModelForm):

    class Meta:
        model = Book

        fields = [
            'name',
            'cover_image',
            'price',
            'authors',
            'series',
            'genre',
            'date_of_published',
            'numbers_of_pages',
            'binding',
            'pr_format',
            'isbn',
            'weight',
            'age_limit',
            'publisher',
            'manufacturer',
            'stock',
            'available',
            'rating',
            'created',
            'updated'
        ]

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not re.match(r'(\d{3})-(\d{1})-(\d{2,7})-(\d{1,6})-(\d{1})', isbn):
            raise ValidationError('Введите ISBN в формате xxx-x-xx-x-x')
        return isbn




