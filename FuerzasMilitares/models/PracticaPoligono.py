from django.db import models
from FuerzasMilitares.models.InstalacionMilitar import InstalacionMilitar
from .Poligono import Poligono
from .Militar import Militar


class PracticaPoligono(models.Model):
    id_practica_poligono = models.AutoField(primary_key=True)
    poligono = models.ForeignKey(
        Poligono,
        null=True,
        blank=True,
        related_name="poligono_practica",
        on_delete=models.CASCADE,
    )
    militar = models.ForeignKey(
        Militar,
        null=True,
        blank=True,
        related_name="militar_practica",
        on_delete=models.CASCADE,
    )
    instalacion = models.ForeignKey(
        InstalacionMilitar,
        null=True,
        blank=True,
        related_name="practica_instalacion",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Practica de Poligono"
        verbose_name_plural = "Practicas de Poligono"
        db_table = "practica_poligono"
