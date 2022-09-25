from django.db import models
from .Modelos import ModeloVehiculo
from django import forms


class Vehiculo(ModeloVehiculo):
    placa = models.CharField(max_length=10, primary_key=True)
    modelo = models.ForeignKey(
        ModeloVehiculo,
        on_delete=models.CASCADE,
        related_name="modelo_vehiculo_visitante",
    )

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"

    def __str__(self) -> str:
        return f"{self.placa}"

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"


class VehiculoForm(forms.ModelForm):
    model = Vehiculo
    fields = ("placa", "modelo")
