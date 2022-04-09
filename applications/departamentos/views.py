from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .form import NewDepartamentoForm
from applications.personas.models import Empleado
from .models import Departamento
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        #form.instance.full_name = form.instance.first_name + ' ' + form.instance.last_name
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellidos,
            job='1',
            departamento = depa,
            )
        return super(NewDepartamentoView, self).form_valid(form)