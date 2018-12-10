from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from .forms import AuthorRefForm, GenreRefForm, SeriesRefForm, PublisherRefForm, \
ManufacturerRefForm
from .models import Author, Genre, Series, Publisher


class ListAuthorRefView(ListView):
    template_name = "list-base-ref.html"
    model = Author
    def get_context_data(self, *args, **kwargs):
        context = super(ListAuthorRefView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Авторы'
        return context

class DetailAuthorRefView(DeleteView):
    template_name = 'view-base-ref.html'
    model = Author

    def get_context_data(self, *args, **kwargs):
        context = super(DetailAuthorRefView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Автор'
        return context


class AuthorRefCreateView(CreateView):
    form_class = AuthorRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/author-ref-create/'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'создания нового автора'
        return context

class GenreRefCreateView(CreateView):
    form_class = GenreRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/genre-ref-create/'

class DetailGenreRefView(DeleteView):
    template_name = 'view-base-ref.html'
    model = Genre

    def get_context_data(self, *args, **kwargs):
        context = super(DetailGenreRefView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Жанр'
        return context


class SeriesRefCreateView(CreateView):
    form_class = SeriesRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/series-ref-create/'


class PublisherRefCreateView(CreateView):
    form_class = PublisherRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/publisher-ref-create/'


class ManufacturerRefCreateView(CreateView):
    form_class = ManufacturerRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/manufacturer-ref-create/'


class AuthorRefUpdateView(UpdateView):
    form_class = AuthorRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/author-ref-create/'
    model = Author

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'редактирования автора'
        context['temp'] = self.kwargs
        return context


class GenreRefUpdateView(UpdateView):
    form_class = GenreRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/genre-ref-create/'
    model = Genre


class SeriesRefUpdateView(UpdateView):
    form_class = SeriesRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/series-ref-create/'
    model = Series


class PublisherRefUpdateView(UpdateView):
    form_class = PublisherRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/publisher-ref-create/'
    model = Publisher


class ManufactorerRefUpdateView(UpdateView):
    form_class = ManufacturerRefForm
    template_name = 'author_ref_create_update.html'
    success_url = 'http://127.0.0.1:8000/admin-shop/ref/manufacturer-ref-create/'
    model = Publisher



