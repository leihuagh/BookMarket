from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView, DetailView
from .forms import AuthorRefForm, GenreRefForm, SeriesRefForm, PublisherRefForm, ManufacturerRefForm, OrderStatusRefForm
from .models import Author, Genre, Series, Publisher, Manufacturer, OrderStatus
from django.urls import reverse_lazy
from django.apps import apps
from random import choice
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

BTN_BLOCKS = [
    "btn btn-primary",
    "btn btn-secondary",
    "btn btn-success",
    "btn btn-danger",
    "btn btn-warning",
    "btn btn-info",
    "btn btn-light",
    "btn btn-dark"
]


# CRUD для АВТОРА
class AuthorRefListView(PermissionRequiredMixin, ListView):
    template_name = "reference/ref-list-base.html"
    model = Author
    paginate_by = 10

    permission_required = 'reference.view_author'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Авторы'
        context['get_create_url'] = reverse_lazy('reference:author-ref-create')
        return context


class AuthorRefDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'reference/ref-view-base.html'
    model = Author

    permission_required = 'reference.view_author'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Автор'
        return context


class AuthorRefCreateView(PermissionRequiredMixin, CreateView):
    form_class = AuthorRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:author-ref-list')

    permission_required = 'reference.add_author'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Добавление нового автора'
        return context


class AuthorRefUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = AuthorRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:author-ref-list')
    model = Author

    permission_required = 'reference.change_author'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Редактирование автора'
        context['temp'] = self.kwargs
        return context


class AuthorRefDeleteView(PermissionRequiredMixin, DeleteView):
    form_class = AuthorRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:author-ref-list')
    model = Author

    permission_required = 'reference.delete_author'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Удаление автора'
        context['temp'] = self.kwargs
        return context


# ====================================================================================
# CRUD для ЖАНРА
class GenreRefListView(PermissionRequiredMixin, ListView):
    template_name = "reference/ref-list-base.html"
    model = Genre
    paginate_by = 10

    permission_required = 'reference.view_genre'

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Жанры'
        context['get_create_url'] = reverse_lazy('reference:genre-ref-create')
        return context


class GenreRefCreateView(PermissionRequiredMixin, CreateView):
    form_class = GenreRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:genre-ref-list')

    permission_required = 'reference.add_genre'

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Добавление нового жанра'
        return context


class GenreRefDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'reference/ref-view-base.html'
    model = Genre

    permission_required = 'reference.view_genre'

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Жанр'
        return context


class GenreRefUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = GenreRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:genre-ref-list')
    model = Genre

    permission_required = 'reference.change_genre'

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Редактирование жанра'
        context['temp'] = self.kwargs
        return context


class GenreRefDeleteView(PermissionRequiredMixin, DeleteView):
    form_class = GenreRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:genre-ref-list')
    model = Genre

    permission_required = 'reference.delete_genre'

    def get_context_data(self, *args, **kwargs):
        context = super(GenreRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Удаление жанра'
        context['temp'] = self.kwargs
        return context


# ====================================================================================
# CRUD для СЕРИИ
class SeriesRefListView(PermissionRequiredMixin, ListView):
    template_name = "reference/ref-list-base.html"
    model = Series
    paginate_by = 10

    permission_required = 'reference.view_series'

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Серии'
        context['get_create_url'] = reverse_lazy('reference:series-ref-create')
        return context


class SeriesRefCreateView(PermissionRequiredMixin, CreateView):
    form_class = SeriesRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:series-ref-list')

    permission_required = 'reference.add_series'

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Добавление новой серии'
        return context


class SeriesRefUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = SeriesRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:series-ref-list')
    model = Series

    permission_required = 'reference.change_series'

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Редактирование серии'
        return context


class SeriesRefDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'reference/ref-view-base.html'
    model = Series

    permission_required = 'reference.view_series'

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Серия'
        return context


class SeriesRefDeleteView(PermissionRequiredMixin, DeleteView):
    form_class = SeriesRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:series-ref-list')
    model = Series

    permission_required = 'reference.delete_series'

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Удаление серии'
        context['temp'] = self.kwargs
        return context


# ====================================================================================
# CRUD для ИЗДАТЕЛЬСТВА
class PublisherRefListView(PermissionRequiredMixin, ListView):
    template_name = "reference/ref-list-base.html"
    model = Publisher
    paginate_by = 10

    permission_required = 'reference.view_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Издательства'
        context['get_create_url'] = reverse_lazy('reference:publisher-ref-create')
        return context


class PublisherRefDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'reference/ref-view-base.html'
    model = Publisher

    permission_required = 'reference.view_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Издательство'
        return context


class PublisherRefCreateView(PermissionRequiredMixin, CreateView):
    form_class = PublisherRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:publisher-ref-list')

    permission_required = 'reference.add_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Добавление нового издательства'
        context['temp'] = self.kwargs
        return context


class PublisherRefUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = PublisherRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:publisher-ref-list')
    model = Publisher

    permission_required = 'reference.change_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Редактирование издательства'
        context['temp'] = self.kwargs
        return context


class PublisherRefDeleteView(PermissionRequiredMixin, DeleteView):
    form_class = PublisherRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:publisher-ref-list')
    model = Publisher

    permission_required = 'reference.delete_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Удаление издательства'
        context['temp'] = self.kwargs
        return context


# ====================================================================================
# CRUD для ИЗГАТОВИТЕЛЯ
class ManufacturerRefListView(PermissionRequiredMixin, ListView):
    template_name = "reference/ref-list-base.html"
    model = Manufacturer
    paginate_by = 10

    permission_required = 'reference.view_manufacturer'

    def get_context_data(self, *args, **kwargs):
        context = super(ManufacturerRefListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Изгатовители'
        context['get_create_url'] = reverse_lazy('reference:manufacturer-ref-create')
        return context


class ManufacturerRefCreateView(PermissionRequiredMixin, CreateView):
    form_class = ManufacturerRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:manufacturer-ref-list')

    permission_required = 'reference.add_manufacturer'

    def get_context_data(self, *args, **kwargs):
        context = super(ManufacturerRefCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Добавление нового изгатовителя'
        return context


class ManufacturerRefDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'reference/ref-view-base.html'
    model = Manufacturer

    permission_required = 'reference.view_manufacturer'

    def get_context_data(self, *args, **kwargs):
        context = super(ManufacturerRefDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Изгатовитель'
        return context


class ManufactorerRefUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = ManufacturerRefForm
    template_name = 'reference/ref-create-update-base.html'
    success_url = reverse_lazy('reference:manufacturer-ref-list')
    model = Manufacturer

    permission_required = 'reference.change_manufacturer'

    def get_context_data(self, *args, **kwargs):
        context = super(ManufactorerRefUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Редактирование изгатовителя'
        return context


class ManufactorerRefDeleteView(PermissionRequiredMixin, DeleteView):
    form_class = ManufacturerRefForm
    template_name = 'reference/ref-delete-base.html'
    success_url = reverse_lazy('reference:manufacturer-ref-list')
    model = Manufacturer

    permission_required = 'reference.delete_manufacturer'

    def get_context_data(self, *args, **kwargs):
        context = super(ManufactorerRefDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'Удаление изгатовителя'
        context['temp'] = self.kwargs
        return context


# Класс для отображения всех моделей приложения reference
class ListReferenceTemplateView(TemplateView):
    template_name = 'reference/ref_all_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        models = []
        context['active'] = 'reference'
        context['app_name'] = apps.get_app_config('reference')
        for i in context['app_name'].get_models():
            models.append(
                (
                    i._meta.verbose_name_plural,
                    i._meta.model.lst_url,
                    choice(BTN_BLOCKS)
                )
            )
        context['models'] = models

        return context


# ====================================================================================
# CRUD для СТАТУСОВ ЗАКАЗА
class OrderStatusRefListView(PermissionRequiredMixin, ListView):
    template_name = 'reference/ref-list-base.html'
    model = OrderStatus
    paginate_by = 10

    permission_required = 'reference.view_order-status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Статусы заказа'
        context['get_create_url'] = reverse_lazy('reference:order-status-ref-create')
        return context


class OrderStatusRefCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'reference/ref-create-update-base.html'
    form_class = OrderStatusRefForm
    success_url = reverse_lazy('reference:order-status-ref-list')

    permission_required = 'reference.add_order-status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_action'] = 'Добавление нового статуса заказа'
        return context


class OrderStatusRefUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'reference/ref-create-update-base.html'
    form_class = OrderStatusRefForm
    success_url = reverse_lazy('reference:order-status-ref-list')
    model = OrderStatus

    permission_required = 'reference.change_order-status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_action'] = 'Редактирование статуса заказа'
        return context


class OrderStatusRefDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'reference/ref-view-base.html'
    model = OrderStatus

    permission_required = 'reference.view_order-status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Статус заказа'
        return context


class OrderStatusRefDeleteView(PermissionRequiredMixin, DeleteView):
    model = OrderStatus
    success_url = reverse_lazy('reference:order-status-ref-list')
    template_name = 'reference/ref-delete-base.html'

    permission_required = 'reference.delete_order-status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_action'] = 'Удаление cтатуса заказа'
        return context






