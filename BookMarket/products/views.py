from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from products.forms import ProductsForm
from products.models import Book
from django.urls import reverse, reverse_lazy
# Create your views here.


class BookProdListView(ListView):
    template_name = 'products/prod-list-base.html'
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdListView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'книги'
        context['get_create_url'] = reverse_lazy('products:book-prod-create')
        return context


class BookProdCreateView(CreateView):
    form_class = ProductsForm
    template_name = 'products/prod-create-update-base.html'
    success_url = reverse_lazy('products:book-prod-list')

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdCreateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'добавления книги'
        return context


class BookProdDetailView(DetailView):
    template_name = 'products/prod-view-base.html'
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdDetailView, self).get_context_data(*args, **kwargs)
        context['descr'] = 'Книги'
        return context


class BookProdUpdateView(UpdateView):
    form_class = ProductsForm
    template_name = 'products/prod-create-update-base.html'
    success_url = reverse_lazy('products:book-prod-list')
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdUpdateView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'редактирования книги'
        context['temp'] = self.kwargs
        context['get_update_url'] = reverse_lazy('products:book-prod-update')
        return context


class BookProdDeleteView(DeleteView):
    form_class = ProductsForm
    template_name = 'products/prod-delete-base.html'
    success_url = reverse_lazy('products:book-prod-list')
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(BookProdDeleteView, self).get_context_data(*args, **kwargs)
        context['ref_action'] = 'удаления книги'
        #context['temp'] = self.kwargs
        return context