from django.db import models
from FuerzasMilitares.models.DatosBasicos import DatosBasicos


class ModeloVehiculo(models.Model):
    color = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(default=2)
    blindado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Modelo de vehiculo"
        verbose_name_plural = "Modelos de vehiculos"
        db_table = "modelo_vehiculo"

    def __str__(self) -> str:
        return f"{self.tipo} {self.color} {self.capacidad} {self.blindado}"


class ModeloVisitante(DatosBasicos):
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "Modelo de visitante"
        verbose_name_plural = "Modelos de visitantes"
        db_table = "modelo_visitante"

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"
