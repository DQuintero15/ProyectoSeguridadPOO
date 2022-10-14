from django.db import models
from django.forms import ModelForm
from FuerzasMilitares.models.Arma import Arma
from .PracticaPoligono import PracticaPoligono
from django import forms


class Poligono(models.Model):
    id_poligono = models.AutoField(primary_key=True, editable=False, default=0)
    arma = models.ForeignKey(
        Arma,
        null=True,
        blank=True,
        related_name="poligono_arma",
        on_delete=models.CASCADE,
    )
    provedores = models.PositiveSmallIntegerField()
    cartuchos = models.PositiveSmallIntegerField()
    distancia = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    imagen_objetivo = models.ImageField(
        upload_to="images\\poligonos", null=True, blank=True
    )
    practica_poligono = models.ForeignKey(
        PracticaPoligono,
        null=True,
        blank=True,
        related_name="poligono_practica",
        on_delete=models.CASCADE,
        limit_choices_to={"disponible": True},
    )

    class Meta:
        verbose_name = "Poligono"
        verbose_name_plural = "Poligonos"
        db_table = "poligono"

    def __str__(self) -> int:
        return f"Poligono #{self.id_poligono}"


class PoligoForm(ModelForm):
    class Meta:
        model = Poligono
        fields = [
            "practica_poligono",
            "arma",
            "distancia",
            "provedores",
            "cartuchos",
            "imagen_objetivo",
        ]
        widgets = {"distancia": forms.NumberInput()}
