from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'