from email.policy import default
from django.db import models
from .Militar import Militar
from django.forms import ModelForm
from .InstalacionMilitar import InstalacionMilitar


class UbicacionMilitar(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    militar = models.ForeignKey(
        Militar,
        related_name="ubicacacion_militar",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    instalacion = models.ForeignKey(
        InstalacionMilitar,
        on_delete=models.CASCADE,
        related_name="ubicacacion_militar_instalacion",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Ubicacion Militar"
        verbose_name_plural = "Ubicaciones de Militares"
        db_table = "ubicacacion_militar"

    def __str__(self) -> str:
        return f"{self.militar}  {self.instalacion}"


class UbicacionMilitarForm(ModelForm):
    class Meta:
        model = UbicacionMilitar
        fields = ("militar", "instalacion")
