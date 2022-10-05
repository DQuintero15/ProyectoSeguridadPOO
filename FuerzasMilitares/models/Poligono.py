from django.db import models
from django.forms import ModelForm
from FuerzasMilitares.models.Arma import Arma


class Poligono(models.Model):
    id_poligono = models.AutoField(primary_key=True)
    distancia = models.DecimalField(max_digits=10, decimal_places=6)
    imagen_objetivo = models.ImageField(
        upload_to="images\\poligonos", null=True, blank=True
    )
    provedores = models.IntegerField()
    cartuchos = models.IntegerField()
    fecha = models.DateField()
    arma = models.ForeignKey(
        Arma,
        null=True,
        blank=True,
        related_name="poligono_arma",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Poligono"
        verbose_name_plural = "Poligonos"
        db_table = "poligono"


class PoligoForm(ModelForm):
    model = Poligono
    field = ("distancia", "imagen_objetivo", "fecha")
