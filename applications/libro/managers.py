import datetime

from django.db import models

from django.db.models import Q


class LibroManager(models.Manager):
    """ Managers para el modelo autor """

    def listar_libros(self, kword):

        resultado = self.filter(
            # icontains = similar y/o igual a lo que se busca
            titulo__icontains=kword,
            fecha__range=('2000-01-01', '2023-01-01')
        )
        return resultado
    
    def listar_libros2(self, kword, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(
            # icontains = similar y/o igual a lo que se busca
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )
        return resultado
    
    def listar_libros_categoria(self, categoria):

        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')
    
##### Consultas mas elaboradas
class CategoriaManager(models.Manager):
    """ Managers para el modelo categoria """

    def categoria_por_autor(self, autor):
        # desde related_name busca los autores por id segun el id que se haya enviado
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()