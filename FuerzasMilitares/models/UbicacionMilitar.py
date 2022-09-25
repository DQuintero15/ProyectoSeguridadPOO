from django.db import models
from .Militar import Militar
from .Batallon import Batallon
from .BrigadaMilitar import BrigadaMilitar
from django.forms import ModelForm


class UbicacionMilitar(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    militar = models.ForeignKey(
        Militar,
        related_name="ubicacacion_militar",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    brigada = models.ForeignKey(
        BrigadaMilitar,
        related_name="ubicacacion_militar_brigada",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    batallon = models.ForeignKey(
        Batallon,
        related_name="ubicacion_militar_batallon",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Ubicacion Militar"
        verbose_name_plural = "Ubicaciones de Militares"

    def __str__(self) -> str:
        return f"{self.militar} se encuentra ubicado en {self.brigada} {self.batallon}"


class UbicacionMilitarForm(ModelForm):
    class Meta:
        model = UbicacionMilitar
        fields = ("militar", "brigada", "batallon")
