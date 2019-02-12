from django.views.generic import TemplateView
from reference.models import Genre
from products.models import Book
from django.conf import settings
import datetime


class CoreAdminTemplateView(TemplateView):
    template_name = 'admincore/staff-home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_NAME'] = settings.SITE_NAME
        context['active'] = 'admin_core'
        return context


class DashboardAdminView(TemplateView):
    template_name = 'admincore/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['active'] = 'dashboard'

        # товаров всего
        context['product_count'] = len(Book.objects.all())

        # активных товаров
        context['av_product_count'] = len(Book.objects.filter(available=True))

        # добавлено вчера
        today = datetime.date.today()
        day = datetime.timedelta(days=1)
        yesterday = today - day
        context['cr_yesterday'] = len(Book.objects.filter(created=yesterday))

        # добавлено за прошлый месяц
        last_month = today.month - 1 if today.month > 1 else 12
        last_month_year = today.year if today.month > last_month else today.year - 1
        context['cr_last_month'] = len(Book.objects.filter(created__year=last_month_year, created__month=last_month))

        # добавлено за текущий месяц
        now_month = today.month
        context['cr_now_month'] = len(Book.objects.filter(created__month=now_month))

        # товаров в каждом жанре (разделе)
        book_genre = {}
        genres = Genre.objects.all()
        for obj in genres:
            book_genre.update({obj.name: len(Book.objects.filter(genre=obj))})
        context['book_genre_count'] = book_genre

        # всего категорий (жанров)
        context['genre_count'] = len(Genre.objects.all())

        return context
