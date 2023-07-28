from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import ListView

#models local
from .models import Libro


class ListLibros(ListView):
    context_object_name = "lista_libros"
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        # Fecha 1
        f1 = self.request.GET.get('fecha1', '')
        # Fecha 2
        f2 = self.request.GET.get('fecha2', '')

        if f1 and f2:
            # existe ambas fechas, retorna listado con filtro de fechas
            return Libro.objects.listar_libros2(palabra_clave, f1, f2)
        else:
            # retorna listado sin filtros
            return Libro.objects.listar_libros(palabra_clave)


class ListLibros2(ListView):
    context_object_name = "lista_libros"
    template_name = "libro/lista2.html"

    def get_queryset(self):
        
        return Libro.objects.listar_libros_categoria('1')
