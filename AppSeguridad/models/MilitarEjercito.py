from django.db import models
from Modelos import DatosMilitar
from Batallon import BatallonEjercito
from Armamento import Armamento

class MilitarEjercito(DatosMilitar):
    batallon = models.ForeignKey(
        BatallonEjercito, related_name="batallon_militar", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.nombres
