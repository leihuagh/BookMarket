from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.


class UserHomeTemplateView(TemplateView):
    template_name = 'user-home.html'