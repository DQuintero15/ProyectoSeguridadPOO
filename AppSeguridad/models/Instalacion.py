from django.db import models


class Instalacion(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    direccion = models.CharField(max_length=30, blank=True)

class SubInstalacionBatallon(Instalacion):
    def __str__(self) -> str:
        return f"{self.nombre}"
