from .IntegranteEsquemaSeguridad import IntegranteEsquemaSeguridad
from django.db import models
from django.forms import ModelForm
from FuerzasMilitares.models.InstalacionMilitar import InstalacionMilitar


class EsquemaSeguridad(models.Model):
    id_esquema_seguridad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(
        blank=True,
        max_length=255,
        null=True,
        help_text="Descripcion de esquema de seguridad",
    )

    integrante = models.ForeignKey(
        IntegranteEsquemaSeguridad,
        blank=True,
        null=True,
        related_name="esquema_integrante",
        on_delete=models.CASCADE,
    )

    instalacion = models.ForeignKey(
        InstalacionMilitar,
        blank=True,
        null=True,
        related_name="esquema_instalacion",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Esquema de seguridad"
        verbose_name_plural = "Esquemas de seguridad"


class EsquemaSeguridadForm(ModelForm):
    class Meta:
        model = EsquemaSeguridad
        fields = ("nombre", "descripcion", "integrante", "instalacion")
