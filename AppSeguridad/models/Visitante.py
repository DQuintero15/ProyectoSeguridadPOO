from FuerzasMilitares.models.DatosBasicos import DatosBasicos
from django.db import models
from .Vehiculo import Vehiculo
from django import forms
from django.utils import timezone


class Visitante(DatosBasicos):

    vehiculo = models.ForeignKey(
        Vehiculo,
        related_name="visitante_vehiculo",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    datos_entrada = models.DateTimeField(editable=False, default=timezone.now)
    motivo = models.TextField(max_length=300, default="No presenta motivo")

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = (
            "nombres",
            "apellidos",
            "correo_electronico",
            "tipo_sangre",
            "numero_cedula",
            "fecha_nacimiento",
            "numero_telefono",
            "vehiculo",
            "motivo",
        )
