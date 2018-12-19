from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from .forms import AuthorRefForm, GenreRefForm, SeriesRefForm, PublisherRefForm, \
    ManufacturerRefForm

from .models import Author, Genre, Series, Publisher, Manufacturer
from django.urls import reverse, reverse_lazy


# Просмотр, подробно, создание обновление и удаление АВТОРА
class AuthorRefListView(ListView):
    template_name = "reference/ref-list-base.html"
    model = Author

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Авторы'
        context['get_create_url'] = reverse_lazy('reference:author-ref-create')
        return context


class AuthorRefDetailView(DeleteView):
    template_name = 'reference/ref-view-base.html'
    model = Author

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Автор'
        return context


class AuthorRefCreateView(CreateView):
    form_class = AuthorRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:author-ref-list')


    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'создания нового автора'
        context['action'] = 'Создание'
        return context


class AuthorRefUpdateView(UpdateView):
    form_class = AuthorRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:author-ref-list')
    model = Author

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'редактирования автора'
        context['action'] = 'Редактирование'
        context['temp'] = self.kwargs
        return context


class AuthorRefDeleteView(DeleteView):
    form_class = AuthorRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:author-ref-list')
    model = Author

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'удаления автора'
        context['temp'] = self.kwargs
        return context


# Просмотр, подробно, создание обновление и удаление ЖАНРА ============================================
class GenreRefListView(ListView):
    template_name = "reference/ref-list-base.html"
    model = Genre

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Жанры'
        context['get_create_url'] = reverse_lazy('reference:genre-ref-create')
        return context


class GenreRefCreateView(CreateView):
    form_class = GenreRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:genre-ref-list')

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefCreateView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Создание жанра'
        return context


class GenreRefDetailView(DeleteView):
    template_name = 'reference/ref-view-base.html'
    model = Genre

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Жанр'
        return context


class GenreRefUpdateView(UpdateView):
    form_class = GenreRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:genre-ref-list')
    model = Genre

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'редактирования жанра'
        context['temp'] = self.kwargs
        return context


class GenreRefDeleteView(DeleteView):
    form_class = GenreRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:genre-ref-list')
    model = Genre

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'удаления жанра'
        context['temp'] = self.kwargs
        return context


# Просмотр, подробно, создание обновление и удаление СЕРИИ======================================
class SeriesRefListView(ListView):
    template_name = "reference/ref-list-base.html"
    model = Series

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Серии'
        context['get_create_url'] = reverse_lazy('reference:series-ref-create')
        return context


class SeriesRefCreateView(CreateView):
    form_class = SeriesRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:series-ref-list')

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefCreateView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Создание серии'
        return context


class SeriesRefUpdateView(UpdateView):
    form_class = SeriesRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:series-ref-list')
    model = Series

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefUpdateView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Редактирования серии'
        return context


class SeriesRefDetailView(DeleteView):
    template_name = 'reference/ref-view-base.html'
    model = Series

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Серия'
        return context


class SeriesRefDeleteView(DeleteView):
    form_class = SeriesRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:series-ref-list')
    model = Series

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'удаления серии'
        context['temp'] = self.kwargs
        return context


# Просмотр, подробно, создание обновление и удаление ИЗДАТЕЛЬСТВА======================================
class PublisherRefListView(ListView):
    template_name = "reference/ref-list-base.html"
    model = Publisher

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Издательства'
        context['get_create_url'] = reverse_lazy('reference:publisher-ref-create')
        return context


class PublisherRefDetailView(DeleteView):
    template_name = 'reference/ref-view-base.html'
    model = Publisher

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Издательство'
        return context


class PublisherRefCreateView(CreateView):
    form_class = PublisherRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:publisher-ref-list')

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'создания издательства'
        context['temp'] = self.kwargs
        return context


class PublisherRefUpdateView(UpdateView):
    form_class = PublisherRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:publisher-ref-list')
    model = Publisher

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'редактирования издательства'
        context['temp'] = self.kwargs
        return context


class PublisherRefDeleteView(DeleteView):
    form_class = PublisherRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:publisher-ref-list')
    model = Publisher

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'удаления издательства'
        context['temp'] = self.kwargs
        return context


# Просмотр, подробно, создание обновление и удаление ИЗГАТОВИТЕЛЯ======================================
class ManufacturerRefListView(ListView):
    template_name = "reference/ref-list-base.html"
    model = Manufacturer

    def get_context_data(self, *args, **kwargs):
        context = super(ManufacturerRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Изгатовители'
        context['get_create_url'] = reverse_lazy('reference:manufacturer-ref-create')
        return context


class ManufacturerRefCreateView(CreateView):
    form_class = ManufacturerRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:manufacturer-ref-list')

    def get_context_data(self, *args, **kwargs):
        context = super(ManufacturerRefCreateView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'добавление изгатовителя'
        return context


class ManufacturerRefDetailView(DeleteView):
    template_name = 'reference/ref-view-base.html'
    model = Manufacturer

    def get_context_data(self, *args, **kwargs):
        context = super(ManufacturerRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Изгатовитель'
        return context


class ManufactorerRefUpdateView(UpdateView):
    form_class = ManufacturerRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:manufacturer-ref-list')
    model = Manufacturer

    def get_context_data(self, *args, **kwargs):
        context = super(ManufactorerRefUpdateView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'редактировать изгатовителя'
        return context


class ManufactorerRefDeleteView(DeleteView):
    form_class = ManufacturerRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:manufacturer-ref-list')
    model = Manufacturer

    def get_context_data(self, *args, **kwargs):
        context = super(ManufactorerRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'удаление изгатовителя'
        context['temp'] = self.kwargs
        return context





