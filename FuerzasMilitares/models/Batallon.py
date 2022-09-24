from django.db import models
from .BrigadaMilitar import BrigadaMilitar
from django.forms import ModelForm
from .ModeloInstalacion import ModeloInstalacion


class Batallon(ModeloInstalacion):
    id_batallon = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="images\\batallones")
    brigada = models.ForeignKey(
        BrigadaMilitar,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="batallon_militar",
    )

    class Meta:
        verbose_name = "Batallon"
        verbose_name_plural = "Batallones"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.nombre


class BatallonForm(ModelForm):
    model = Batallon
    fields = (
        "nombre",
        "logo",
        "brigada",
        "departamento",
        "municipio",
        "ubicacion_latitud",
        "ubicacion_longitud",
        "planos",
    )
