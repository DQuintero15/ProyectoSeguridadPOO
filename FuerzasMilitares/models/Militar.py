from django.db import models
from AppSeguridad.models.Modelos import DatosBasicos
from .RangoMilitar import RangoMilitar
from django.contrib.auth.models import User
from django.forms import ModelForm


class Militar(DatosBasicos):
    id_militar = models.AutoField(primary_key=True)
    copia_cedula = models.FileField(
        upload_to="archivos\\cedulas", null=True, blank=True
    )
    foto = models.ImageField(upload_to="images\\fotos", null=True, blank=True)
    rango = models.ForeignKey(
        RangoMilitar,
        null=True,
        blank=True,
        related_name="rango_militar",
        on_delete=models.CASCADE,
    )
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="usuario_militar",
    )

    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Militar"
        verbose_name_plural = "Militares"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return super().__str__()


class MilitarForm(ModelForm):
    class Meta:
        model = Militar
        fields = (
            "nombres",
            "apellidos",
            "correo_electronico",
            "tipo_sangre",
            "numero_cedula",
            "fecha_nacimiento",
            "numero_telefono",
            "copia_cedula",
            "foto",
            "rango",
            "disponible",
        )
