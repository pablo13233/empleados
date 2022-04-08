from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar-todo-empleados/',views.ListAllEmpleados.as_view()),
    path('listar-by-area/<shorname>/',views.ListByAreaEmpleados.as_view()),
    path('listar-empleado/',views.ListEmpleadosByKword.as_view()),
    path('skills/',views.ListHabilidadesEmpleado.as_view()),
    path('detail/<pk>',views.EmpleadoDetailView.as_view()),
]