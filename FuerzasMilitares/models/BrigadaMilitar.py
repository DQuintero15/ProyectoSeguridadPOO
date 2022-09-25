from django.db import models
from .DivisionMilitar import DivisionMilitar
from django.forms import ModelForm
from .ModeloInstalacion import ModeloInstalacion


class BrigadaMilitar(ModeloInstalacion):
    id_brigada = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="images\\brigadas_militares")
    division = models.ForeignKey(
        DivisionMilitar,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="division_brigada",
    )

    def __str__(self) -> str:
        return self.nombre

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Brigada militar"
        verbose_name_plural = "Brigadas militares"


class DivisionMilitarForm(ModelForm):
    model = BrigadaMilitar
    fields = (
        "nombre",
        "logo",
        "division",
        "departamento",
        "municipio",
        "ubicacion_latitud",
        "ubicacion_longitud",
        "planos",
    )
