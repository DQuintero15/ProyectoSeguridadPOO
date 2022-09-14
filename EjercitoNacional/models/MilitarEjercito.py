from django.db import models
from AppSeguridad.models.Modelos import DatosMilitar
from EjercitoNacional.models.EjercitoNacional import BatallonEjercito 
from AppSeguridad.models.Armamento import Arma
from AppSeguridad.models.Posicion import PosicionEsquemaSeguridad

class MilitarEjercito(DatosMilitar):
    batallon = models.ForeignKey(
        BatallonEjercito, related_name="batallon_militar_ejercito", on_delete=models.CASCADE
    )
    
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE, null=True, blank=True)
    posicion = models.ForeignKey(PosicionEsquemaSeguridad, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Militar de Ejercito Nacional"
        verbose_name_plural = "Militares de Ejercito Nacional"


    def __str__(self) -> str:
        return self.nombres
