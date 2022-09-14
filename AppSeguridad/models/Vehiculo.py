from django.db import models
from .Modelos import ModeloVehiculo

class Vehiculo(ModeloVehiculo):
    placa = models.CharField(max_length=10, primary_key=True, unique=True)
    modelo = models.IntegerField()

    def __str__(self) -> str:
        return