from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class DatosBasicos(models.Model):
    A_POSITIVO = "A+"
    A_NEGATIV0 = "A-"
    B_POSITIVO = "B+"
    B_NEGATIV0 = "B-"
    AB_POSITIVO = "AB+"
    AB_NEGATIV0 = "AB-"
    O_POSTIVO = "O+"
    O_NEGATIVO = "O-"

    TIPOS_SANGRE = (
        (A_POSITIVO, "A+"),
        (A_NEGATIV0, "A-"),
        (B_POSITIVO, "B+"),
        (B_NEGATIV0, "B-"),
        (AB_POSITIVO, "AB+"),
        (AB_NEGATIV0, "AB-"),
        (O_POSTIVO, "O+"),
        (O_NEGATIVO, "O-"),
    )

    id_datos_basicos = models.AutoField(primary_key=True, default=None)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo_electronico = models.EmailField(max_length=30)
    tipo_sangre = models.CharField(
        max_length=3, choices=TIPOS_SANGRE, default=TIPOS_SANGRE[6]
    )
    numero_cedula = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(
        null=True, help_text="Por favor ingrese una fecha con el formato AAAA-MM-DD"
    )
    numero_telefono = PhoneNumberField(blank=True, null=True, help_text="Indicativo de Colombia +57")

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"


class ModeloInstalacion(models.Model):
    id_modelo_instalacion = models.AutoField(primary_key=True, default=None)
    departamento = models.CharField(max_length=150)
    municipio = models.CharField(max_length=150)
    ubicacion_latitud = models.DecimalField(max_digits=9, decimal_places=6)
    ubicacion_longitud = models.DecimalField(max_digits=9, decimal_places=6)


class ModeloVehiculo(models.Model):
    color = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(default=2)
    blindado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.tipo} {self.color} {self.capacidad} {self.blindado}"


class ModeloVisitante(DatosBasicos):
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"
