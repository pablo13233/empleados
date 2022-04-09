from django.contrib import admin
from django.urls import path

from . import views


def DesdeApps(self):
    print('=================akljsdlaksjkdl=================')


urlpatterns = [
    path(
        'new-departamento/',
        views.NewDepartamentoView.as_view(),
        name='nuevo_departamento'
    ),
]
