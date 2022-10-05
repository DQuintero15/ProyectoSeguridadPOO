from django.db import models

class ModeloInstalacion(models.Model):
    id_modelo_instalacion = models.AutoField(primary_key=True, default=None)
    departamento = models.CharField(max_length=150)
    municipio = models.CharField(max_length=150)
    ubicacion_latitud = models.DecimalField(max_digits=9, decimal_places=6)
    ubicacion_longitud = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        db_table = "modelo_instalacion"
    