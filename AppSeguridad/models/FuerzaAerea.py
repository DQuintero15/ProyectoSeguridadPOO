from django.db import models
from .DivisionMilitar import DivisonMilitar
from .Modelos import ModeloBrigadaBatallonMilitar

class DivisionFuerzaAerea(DivisonMilitar):
    class Meta:
        verbose_name = "Division de Fuerza Area"
        verbose_name_plural = "Divisiones de Fuerza Aerea"

    pass


class BrigadaUnidadFuerzaAerea(ModeloBrigadaBatallonMilitar):
    division = models.ForeignKey(
        DivisionFuerzaAerea,
        on_delete=models.CASCADE,
        related_name="brigada_division_fuerza_aerea",
    )

    class Meta:
        verbose_name = "Brigada de Fuerza Area"
        verbose_name_plural = "Brigadas de Fuerza Area"

    def __str__(self) -> str:
        return self.nombre_unidad