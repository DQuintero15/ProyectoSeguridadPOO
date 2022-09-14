from tabnanny import verbose
from django.db import models
from AppSeguridad.models.Modelos import DatosMilitar
from ArmadaNacional.models.ArmadaNacional import BatallonInfanteria

class InfanteMarina(DatosMilitar):
    batallon = models.ForeignKey(
        BatallonInfanteria,
        related_name="batallon_infanteria_marina",
        on_delete=models.CASCADE,
    )
    
    class Meta:
        verbose_name = "Infante de marina"
        verbose_name_plural = "Infantes de marina"

    def __str__(self) -> str:
        return self.nombres
