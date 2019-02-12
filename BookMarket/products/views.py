from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from products.forms import ProductsForm
from products.models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class BookProdListView(ListView):
    template_name = 'products/prod-list-base.html'
    model = Book
    paginate_by = 10

    def get_queryset(self):
        queryset = Book.objects.all().prefetch_related('authors')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'книги'
        context['get_create_url'] = reverse_lazy('products:book-prod-create')
        context['active'] = 'products'

        return context


class BookProdCreateView(PermissionRequiredMixin, CreateView):
    form_class = ProductsForm
    template_name = 'products/prod-create-update-base.html'
    success_url = reverse_lazy('products:book-prod-list')

    permission_required = 'products.add_book'

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdCreateView, self).get_context_data(*args, **kwargs)
        context['prod_action'] = 'Добавление новой книги'
        return context


class BookProdDetailView(DetailView):
    template_name = 'products/prod-view-base.html'
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Книги'
        return context


class BookProdUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = ProductsForm
    template_name = 'products/prod-create-update-base.html'
    success_url = reverse_lazy('products:book-prod-list')
    model = Book

    permission_required = 'products.change_book'

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdUpdateView, self).get_context_data(*args, **kwargs)
        context['prod_action'] = 'Редактирование книги'
        context['temp'] = self.kwargs
        context['get_update_url'] = reverse_lazy('products:book-prod-update')
        return context


class BookProdDeleteView(PermissionRequiredMixin, DeleteView):
    form_class = ProductsForm
    template_name = 'products/prod-delete-base.html'
    success_url = reverse_lazy('products:book-prod-list')
    model = Book

    permission_required = 'products.delete_book'

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdDeleteView, self).get_context_data(*args, **kwargs)
        context['prod_action'] = 'Удаление книги'
        return context



