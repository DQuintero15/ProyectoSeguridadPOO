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

    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo_electronico = models.EmailField(max_length=30)
    tipo_sangre = models.CharField(
        max_length=3, choices=TIPOS_SANGRE, default=TIPOS_SANGRE[6]
    )
    numero_cedula = models.CharField(max_length=15, primary_key=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    numero_telefono = PhoneNumberField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"


class DatosMilitar(DatosBasicos):
    copia_cedula = models.FileField(upload_to="archivos\\cedulas")
    foto = models.ImageField(upload_to="images\\fotos")

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"

class ModeloArma(models.Model):
    id_modelo_arma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    calibre = models.CharField(max_length=10)
    observacion = models.TextField(
        max_length=230, blank=True, default="No presenta novedades", null=True
    )
    letal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.calibre}"

class ModeloBrigadaBatallonMilitar(models.Model):
    nombre_unidad = models.CharField(max_length=150, primary_key=True)
    departamento = models.CharField(max_length=150)
    municipio = models.CharField(max_length=150)
    ubicacion_latitud = models.FloatField()
    ubicacion_longitud = models.FloatField()
    planos = models.FileField(upload_to="archivos\\planos", blank=True, null=True)

class ModeloVehiculo(models.Model):
    color = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(default=2)
    blindado = models.BooleanField(default=False)

class ModeloVisitante(DatosBasicos):
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"

