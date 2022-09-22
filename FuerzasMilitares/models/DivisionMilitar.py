from django.db import models
from FuerzasMilitares.models.FuerzaMilitar import FuerzaMilitar
from django.forms import ModelForm


class DivisionMilitar(models.Model):
    id_division = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="images\\divisiones_militares")
    fuerza_militar = models.ForeignKey(
        FuerzaMilitar,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="fuerzamilitar_division",
    )

    def __str__(self) -> str:
        return self.nombre
        
    class Meta:
        verbose_name = "Division militar"
        verbose_name_plural = "Divisiones militares"


class DivisionMilitarForm(ModelForm):
    model = DivisionMilitar
    fields = ("nombre", "logo", "fuerza_militar")
