from django.db import models


class FuerzasMilitares(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True, unique=True)
    logo = models.ImageField(upload_to="images\\fuerzas_militares")

    class Meta:
        verbose_name = "Fuerza Militar"
        verbose_name_plural = "Fuerzas Militares"

    def __str__(self) -> str:
        return f"{self.nombre}"
        