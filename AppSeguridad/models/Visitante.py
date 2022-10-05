from FuerzasMilitares.models.DatosBasicos import DatosBasicos
from django.db import models
from .Vehiculo import Vehiculo
from django import forms


class Visitante(DatosBasicos):
    vehiculo = models.ForeignKey(
        Vehiculo,
        related_name="visitante_vehiculo",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"


class VisitanteForm(forms.ModelForm):
    class Meta:
        fields = (
            "nombres",
            "apellidos",
            "correo_electronico",
            "tipo_sangre",
            "numero_cedula",
            "fecha_nacimiento",
            "numero_telefono",
            "vehiculo",
        )
