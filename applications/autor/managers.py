from django.db import models

from django.db.models import Q


class AutorManager(models.Manager):
    """ Managers para el modelo autor """

    def buscar_autor(self, kword):

        resultado = self.filter(
            # icontains = similar y/o igual a lo que se busca
            nombre__icontains=kword
        )
        return resultado

    def buscar_autor2(self, kword):

        resultado = self.filter(
            # icontains = similar y/o igual a lo que se busca, se agrega un "or"
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return resultado

    def buscar_autor3(self, kword):

        resultado = self.filter(
            # icontains = similar y/o igual a lo que se busca, con exclude o filter anidados
            nombre__icontains=kword
        ).filter(
            Q(edad__icontains=74) | Q(edad__icontains=79)
        )
        return resultado
    
    def buscar_autor4(self, kword):

        resultado = self.filter(
            # filtro mayor igual o menor igual, mas orderby
            edad__gt=40,
            edad__lt=75
        ).order_by('apellidos', 'nombre', 'id')
        return resultado