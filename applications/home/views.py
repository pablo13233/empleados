from pyexpat import model
from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, CreateView
    )

from .models import Prueba

from .forms import PruebaForm
# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class  PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'prueba_list'
    queryset = ['uno','dos','tres']

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'
