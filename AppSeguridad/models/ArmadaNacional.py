from django.db import models
from .Modelos import ModeloBrigadaBatallonMilitar


class BrigadaArmadaNacional(ModeloBrigadaBatallonMilitar):
    class Meta:
        verbose_name = "Brigada de Infanteria de Marina"
        verbose_name_plural = "Brigadas de Infanteria de Marina"

    def __str__(self) -> str:
        return self.nombre_unidad


class BatallonInfanteria(ModeloBrigadaBatallonMilitar):
    brigada = models.ForeignKey(
        BrigadaArmadaNacional,
        on_delete=models.CASCADE,
        related_name="brigada_batallon",
    )

    class Meta:
        verbose_name = "Batallon de Infanteria de Marina"
        verbose_name_plural = "Batallones de Infanteria de Marina"
