from django.db import models
from django.forms import ModelForm


class FuerzaMilitar(models.Model):
    id_fuerza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, unique=True)
    logo = models.ImageField(upload_to="images\\fuerzas_militares")

    class Meta:
        verbose_name = "Fuerza Militar"
        verbose_name_plural = "Fuerzas Militares"

    def __str__(self) -> str:
        return f"{self.nombre}"


class FuerzaMilitarForm(ModelForm):
    class Meta:
        model = FuerzaMilitar
        fields = ("nombre", "logo")
