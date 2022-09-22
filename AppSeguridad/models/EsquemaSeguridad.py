from AppSeguridad.models.IntegranteEsquemaSeguridad import IntegranteEsquemaSeguridad
from django.db import models
from django.forms import ModelForm
from FuerzasMilitares.models.BrigadaMilitar import BrigadaMilitar
from FuerzasMilitares.models.Batallon import Batallon



class EsquemaSeguridad(models.Model):
    id_esquema_seguridad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, max_length=255, null=True, help_text="Descripcion de esquema de seguridad")
    planos = models.FileField(upload_to="archivos\\planos", blank=True, null=True, help_text="Planos de la instalación en formato .svg")
    integrante = models.ForeignKey(
        IntegranteEsquemaSeguridad,
        blank=True,
        null=True,
        related_name="esquema_integrante",
        on_delete=models.CASCADE,
    )
    batallon = models.ForeignKey(
        Batallon,
        blank=True,
        null=True,
        related_name="esquema_batallon",
        on_delete=models.CASCADE,
    )
    brigada = models.ForeignKey(
        BrigadaMilitar,
        blank=True,
        null=True,
        related_name="esquema_brigada",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Esquema de seguridad"
        verbose_name_plural = "Esquemas de seguridad"



class EsquemaSeguridadForm(ModelForm):
    class Meta:
        model = EsquemaSeguridad
        fields = ("nombre", "descripcion", "planos", "integrante")