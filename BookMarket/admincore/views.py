from django.shortcuts import render
from django.views.generic import TemplateView
from reference import models
from django.conf import settings
from django.urls import reverse, reverse_lazy

# Create your views here.


class CoreAdminTemplateView(TemplateView):
    template_name = 'admincore/staff-home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_NAME'] = settings.SITE_NAME
        return context
