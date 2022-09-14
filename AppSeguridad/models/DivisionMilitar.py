from django.db import models
from .FuerzasMilitares import FuerzasMilitares


class DivisonMilitar(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True, unique=True)
    logo = models.ImageField(upload_to="images\\divisiones_militares")
    fuerza_militar = models.ForeignKey(
        FuerzasMilitares,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="fuerza_militar_divison",
    )

    class Meta:
        verbose_name = "Divison Militar"
        verbose_name_plural = "Divisiones Militares"

    def __str__(self) -> str:
        return self.nombre
