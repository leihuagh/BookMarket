from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


from products.models import Book
# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_book = Book.objects.all()
        context['SITE_NAME'] = settings.SITE_NAME
        context['active'] = 'core'
        last_added_book_count = 8
        context['last_book'] = last_book[len(last_book)-last_added_book_count:len(last_book)]
        print(kwargs)
        return context


class AboutTemplateView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'about'
        return context


class DeliveryTemplateView(TemplateView):
    template_name = 'core/delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'delivery'
        return context
