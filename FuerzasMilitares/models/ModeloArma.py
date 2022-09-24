from django.db import models

class ModeloArma(models.Model):
    id_modelo_arma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    calibre = models.CharField(max_length=10)
    observacion = models.TextField(
        max_length=230, blank=True, default="No presenta novedades", null=True
    )
    letal = models.BooleanField(default=True)


    class Meta:
        verbose_name = "Modelo de arma"
        verbose_name_plural = "Modelos de armas"

    def __str__(self):
        return f"{self.nombre} {self.calibre}"
