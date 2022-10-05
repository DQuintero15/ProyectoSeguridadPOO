
from django.db import models
from .FuerzaMilitar import FuerzaMilitar
from django.forms import ModelForm

class RangoMilitar(models.Model):
    id_rango = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, help_text="Nombre de fuerza militar", unique=True)
    abreviatura = models.CharField(
        max_length=15, blank=True, help_text="Abreviatura del rango militar"
    )
    fuerza_militar = models.ForeignKey(
        FuerzaMilitar, on_delete=models.CASCADE, blank=True, null=True
    )
    logo = models.ImageField(
        upload_to="images\\grados_militares", help_text="Logo de rango"
    )

    class Meta:
        verbose_name = "Rango militar"
        verbose_name_plural = "Rangos militares"
        db_table = "rango_militar"

    def __str__(self) -> str:
        return self.nombre


class RangoMilitarForm(ModelForm):
    class Meta:
        model = RangoMilitar
        fields = ('nombre', "abreviatura", "fuerza_militar", "logo")