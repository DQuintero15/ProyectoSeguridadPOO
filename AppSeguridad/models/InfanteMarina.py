from django.db import models
from Modelos import DatosMilitar
from Batallon import BatallonInfanteriaMarina


class MilitarEjercito(DatosMilitar):
    batallon = models.ForeignKey(
        BatallonInfanteriaMarina,
        related_name="batallon_infanteria_marina",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.nombres
