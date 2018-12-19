from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
# Create your views here.


class UserHomeTemplateView(TemplateView):
    template_name = 'core/user-home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_NAME'] = settings.SITE_NAME
        return context