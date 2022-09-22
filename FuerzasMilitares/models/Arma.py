from django.db import models
from .ModeloArma import ModeloArma
from .FuerzaMilitar import FuerzaMilitar


class Arma(models.Model):
    serial = models.CharField(max_length=100, primary_key=True)
    modelo = models.ForeignKey(
        ModeloArma,
        on_delete=models.CASCADE,
        related_name="modelo_arma",
        null = True, 
    )
    fuerza_militar = models.ForeignKey(
        FuerzaMilitar,
        on_delete=models.CASCADE,
        related_name="modelo_arma_fuerza_militar",
        null = True,
    )

    def __str__(self) -> str:
        return f"{self.modelo} {self.serial}"
