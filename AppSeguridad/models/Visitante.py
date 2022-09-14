from django.db import models
from .Modelos import DatosBasicos
from Vehiculo import Vehiculo

class Visitante(DatosBasicos):
    fecha = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length=50)
    motivo = models.TextField(max_length=300, blank=True, null=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"