from django.db import models
from FuerzasMilitares.models.DatosBasicos import DatosBasicos
from django import forms


class ModeloVehiculo(models.Model):
    color = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(default=2)
    blindado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Modelo de vehiculo"
        verbose_name_plural = "Modelos de vehiculos"
        db_table = "modelo_vehiculo"

    def __str__(self) -> str:
        return f"{self.tipo} {self.color} {self.capacidad} {self.blindado}"
