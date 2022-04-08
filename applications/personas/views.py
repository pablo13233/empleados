from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView
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
        palabra_clave = self.request.GET.get("kword",'')
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


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['skills'] = self.object.skill.all()
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:correcto')
