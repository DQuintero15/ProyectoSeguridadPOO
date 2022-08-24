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
    copia_cedula = models.FileField(upload_to="media\\images\\cedulas")
    foto = models.ImageField(upload_to="media\\images\\fotos")
    salvo_conducto_armas = models.FileField(upload_to="media\\images\\salvo_conducto_armas")
    licencia_conduccion = models.FileField(upload_to="media\\images\\licencias")


    def __str__(self):
        return self.nombres


class Protegido(DatosPersonales):
    idProtegido = models.AutoField(primary_key=True)


class Arma(models.Model):
    id_arma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


class ArmaLetal(Arma):
    id_arma_letal = models.AutoField(primary_key=True)
    calibre = models.DecimalField(decimal_places=2, max_digits=4)
    serial = models.CharField(max_length=20)

class ArmaNoLetal(Arma):
    id_arma_no_letal = models.AutoField(primary_key=True)
