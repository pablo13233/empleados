from django.shortcuts import render
from django.views.generic import (
    ListView
    )
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado

class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_area.html'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )
        return lista

class ListEmpleadosByKword(ListView):
    template_name = 'persona/list_word.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('**************************')
        palabra_clave = self.request.GET.get("kword",'')
        print("===============", palabra_clave)
        lista = Empleado.objects.filter(
        first_name = palabra_clave
        )
        print('lista result: ', lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.skill.all()