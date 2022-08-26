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
        max_length=3, choices=TIPOS_SANGRE, default=TIPOS_SANGRE[6]
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
    serial = models.CharField(max_length=40, default="Sin registrar", primary_key=True)
    nombre = models.CharField(max_length=100)
    calibre = models.CharField(max_length=10)
    observacion = models.TextField(max_length=230, blank=True, default="Sin novedad")
    letal = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre + " " + self.calibre


class Escolta(DatosPersonales):
    arma = models.OneToOneField(Arma, on_delete=models.CASCADE)
    id_escolta = models.AutoField(primary_key=True)


class Posicion(models.Model):
    id_posicion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    piso = models.IntegerField()


class Instalacion(models.Model):
    nombre = models.CharField(max_length=100, blank=True, primary_key=True)
    ubicacion_Latitud = models.DecimalField(max_digits=15, decimal_places=2)
    ubicacion_longitud = models.DecimalField(max_digits=15, decimal_places=2)
    numero_plantas = models.IntegerField(default=1, blank=True)
    direccion = models.CharField(max_length=30, blank=True)
    descipcion = models.CharField(max_length=100, blank=True)
    planos = models.FileField(upload_to="archivos\\planos", blank=True)


class EsquemaProteccion(models.Model):
    id_esquema_proteccion = models.AutoField(primary_key=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    escoltas = models.ForeignKey(Escolta, on_delete=models.CASCADE)
    fecha = models.DateField(auto_created=True)
