from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    #url de app departamentos
    path('', include('applications.departamentos.urls')),
    path('', include('applications.personas.urls')),
]
