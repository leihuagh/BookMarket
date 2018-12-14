from django.shortcuts import render
from django.views.generic import TemplateView
from reference import models

# Create your views here.


class CoreAdminTemplateView(TemplateView):
    template_name = 'admincore/staff-home.html'
