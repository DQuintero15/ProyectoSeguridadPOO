from django.db import models

# Create your models here.
from django.db import models


class DatosPersonales(models.Model):

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

    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    edad = models.IntegerField(default=18)
    correo_electronico = models.EmailField(max_length=30, blank=True)
    tipo_sangre = models.CharField(
        max_length=3, choices=TIPOS_SANGRE, default=TIPOS_SANGRE[0]
    )
    numero_cedula = models.CharField(max_length=15)
    copia_cedula = models.FileField(upload_to="archivos\\cedulas")
    foto = models.ImageField(upload_to="images\\fotos")
    salvo_conducto_armas = models.FileField(
        upload_to="archivos\\salvo_conducto_armas", blank=True, null=True
    )
    licencia_conduccion = models.FileField(
        upload_to="archivos\\licencias", blank=True, null=True
    )
    libreta_militar = models.FileField(
        upload_to="archivos\\libreta_militar", blank=True, null=True
    )

    def __str__(self):
        return self.nombres


class Protegido(DatosPersonales):
    idProtegido = models.AutoField(primary_key=True)


class Arma(models.Model):
    id_arma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    calibre = models.CharField(max_length=10)
    serial = models.CharField(max_length=30, default="Sin registrar")
    observacion = models.TextField(max_length=230, blank=True)
    letal = models.BooleanField(default=False)
