from django.db import models

class PosicionEsquemaSeguridad(models.Model):
    nombre_posicion = models.CharField(max_length=255)