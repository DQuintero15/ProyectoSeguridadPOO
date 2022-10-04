from django.db import models
from django.forms import ModelForm
from .ModeloInstalacion import ModeloInstalacion
from .DivisionMilitar import DivisionMilitar


class InstalacionMilitar(ModeloInstalacion):
    id_instalacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    planos = models.FileField(
        upload_to="archivos\\planos",
        blank=True,
        null=True,
        help_text="Planos de la instalación en formato .svg",
    )
    division = models.ForeignKey(
        DivisionMilitar,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="division_instalacion",
    )

    logo = models.ImageField(upload_to="images\\logos", null=True, blank=True)

    class Meta:
        verbose_name = "Instalación militar"
        verbose_name_plural = "Instalaciones militares"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.nombre


class InstalacionMilitarForm(ModelForm):
    model = InstalacionMilitar
    fields = (
        "nombre",
        "logo",
        "departamento",
        "municipio",
        "ubicacion_latitud",
        "ubicacion_longitud",
        "planos",
    )
