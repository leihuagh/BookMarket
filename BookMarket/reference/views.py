from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
from .forms import AuthorRefForm, GenreRefForm, SeriesRefForm, PublisherRefForm, \
ManufacturerRefForm
from .models import Author, Genre, Series, Publisher


class AuthorRefCreateView(CreateView):
    form_class = AuthorRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/author-ref-create/'


class GenreRefCreateView(CreateView):
    form_class = GenreRefForm
    template_name = 'genre_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/genre-ref-create/'


class SeriesRefCreateView(CreateView):
    form_class = SeriesRefForm
    template_name = 'series_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/series-ref-create/'


class PublisherRefCreateView(CreateView):
    form_class = PublisherRefForm
    template_name = 'publisher_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/publisher-ref-create/'


class ManufacturerRefCreateView(CreateView):
    form_class = ManufacturerRefForm
    template_name = 'manufacturer_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/manufacturer-ref-create/'


class AuthorRefUpdateView(UpdateView):
    form_class = AuthorRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/author-ref-create/'
    model = Author


class GenreRefUpdateView(UpdateView):
    form_class = GenreRefForm
    template_name = 'genre_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/genre-ref-create/'
    model = Genre


class SeriesRefUpdateView(UpdateView):
    form_class = SeriesRefForm
    template_name = 'series_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/series-ref-create/'
    model = Series


class PublisherRefUpdateView(UpdateView):
    form_class = PublisherRefForm
    template_name = 'publisher_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/publisher-ref-create/'
    model = Publisher


class ManufactorerRefUpdateView(UpdateView):
    form_class = ManufacturerRefForm
    template_name = 'manufacturer_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/manufacturer-ref-create/'
    model = Publisher



