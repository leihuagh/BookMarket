from django.views.generic import TemplateView
from products.models import Book
from django.db.models import Q


class MakeSearchView(TemplateView):
    template_name = 'search/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        q = self.request.GET.get('q')
        sr = Book.objects.filter(
            Q(date_of_published=q) |
            Q(authors__name__icontains=q) |
            Q(name__icontains=q) &
            Q(available=True)
        )
        # если поле поиска не пустое
        if q:
            context['results'] = sr
        context['search'] = q
        return context
