from django.db import models
from .Visitante import Visitante
from .Vehiculo import Vehiculo
from django.forms import ModelForm
from FuerzasMilitares.models.InstalacionMilitar import InstalacionMilitar

class Visita(models.Model):
    id_visita = models.AutoField(primary_key=True)
    visitante = models.ForeignKey(
        Visitante,
        blank=True,
        null=True,
        related_name="visita_visitante",
        on_delete=models.CASCADE,
    )
    vehiculo = models.ForeignKey(
        Vehiculo,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="visita_vehiculo",
    )

    def __str__(self) -> str:
        return self.visitante

    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
        db_table = "visita"

    instalacion = models.ForeignKey(
        InstalacionMilitar,
        blank=True,
        null=True,
        related_name="visita_instalacion",
        on_delete=models.CASCADE,
    )


class VisitaForm(ModelForm):
    class Meta:
        model = Visita
        fields = ("visitante", "vehiculo")
