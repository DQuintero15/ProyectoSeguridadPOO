from django.db import models
from AppSeguridad.models.Modelos import ModeloArma


class Arma(models.Model):
    serial = models.CharField(max_length=40, primary_key=True)
    modelo = models.ForeignKey(
        ModeloArma,
        on_delete=models.CASCADE,
        related_name="modelo_arma",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.modelo}"
