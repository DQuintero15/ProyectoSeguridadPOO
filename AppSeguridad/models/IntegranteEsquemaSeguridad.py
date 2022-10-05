from django.db import models
from FuerzasMilitares.models.Militar import Militar
from FuerzasMilitares.models.Arma import Arma
from django.forms import ModelForm


class IntegranteEsquemaSeguridad(models.Model):
    id_integrante = models.AutoField(primary_key=True)
    arma = models.ForeignKey(
        Arma,
        null=True,
        blank=True,
        related_name="integrate_esquema_arma",
        on_delete=models.CASCADE,
    )
    militar = models.ForeignKey(
        Militar,
        null=True,
        blank=True,
        related_name="integrate_esquema_militar",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.militar} {self.arma}"

    class Meta:
        verbose_name = "Integrante de esquema de seguridad"
        verbose_name_plural = "Integrantes de esquema de seguridad"
        db_table = "integrante_esquema_seguridad"


class IntegranteEsquemaSeguridadForm(ModelForm):
    class Meta:
        model = IntegranteEsquemaSeguridad
        fields = ("militar", "arma")
