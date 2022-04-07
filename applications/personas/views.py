from django.shortcuts import render
from django.views.generic import (
    ListView
    )
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado

class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_area.html'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )
        return lista