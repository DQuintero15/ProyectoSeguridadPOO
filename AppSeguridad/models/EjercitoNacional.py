from django.db import models
from .DivisionMilitar import DivisonMilitar
from .Modelos import ModeloBrigadaBatallonMilitar


class DivisonEjercitoNacional(DivisonMilitar):
    class Meta:
        verbose_name = "Divison de Ejercito Nacional"
        verbose_name_plural = "Divisones de Ejercito Nacional"


class BrigadaUnidadEjercitoNacional(ModeloBrigadaBatallonMilitar):
    division = models.ForeignKey(
        DivisonEjercitoNacional,
        on_delete=models.CASCADE,
        related_name="division_brigada_ejercito",
    )

    class Meta:
        verbose_name = "Brigada de Ejercito Nacional"
        verbose_name_plural = "Brigadas de Ejercito Nacional"

    def __str__(self) -> str:
        return self.division, self.nombre_unidad 


class BatallonEjercito(ModeloBrigadaBatallonMilitar):
    brigada = models.ForeignKey(
        BrigadaUnidadEjercitoNacional,
        on_delete=models.CASCADE,
        related_name="brigada_batallon_ejercito",
    )

    def __str__(self) -> str:
        return self.nombre_unidad
