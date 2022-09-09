from tokenize import blank_re
from django.db import models


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

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"


class DatosMilitar(DatosBasicos):
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

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"


class ModeloArma(models.Model):
    id_modelo_arma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    calibre = models.CharField(max_length=10, blank=True, null=True)
    observacion = models.TextField(max_length=230, blank=True, default="No presenta novedades", null=True)
    letal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.calibre}"


class Arma(ModeloArma):
    serial = models.CharField(max_length=40, primary_key=True)
    modelo = models.ForeignKey(ModeloArma, on_delete=models.CASCADE, related_name="modelo_arma", default="Modelo no disponible")

    def __str__(self) -> str:
        return f"{self.modelo}"


class Instalacion(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    direccion = models.CharField(max_length=30, blank=True)


class Posicion(models.Model):
    id_posicion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    piso = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    planos = models.FileField(upload_to="archivos\\planos", blank=True)
    ciudad = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}"

    def getPiso(self) -> int:
        return f"{self.piso}"


class Batallon(Instalacion):
    EJERCITO_NACIONAL = "Ejercito Nacional de Colombia"
    ARMADA_NACIONAL = "Armada de la República de Colombia"

    fuerzas_armadas = (
        (EJERCITO_NACIONAL, "Ejercito Nacional de Colombia"),
        (ARMADA_NACIONAL, "Armada de la República de Colombia"),
    )

    ubicacion_latitud = models.DecimalField(max_digits=30, decimal_places=15)
    tipo_fuerza = models.CharField(
        choices=fuerzas_armadas, default=fuerzas_armadas[0], max_length=50
    )
    ubicacion_longitud = models.DecimalField(max_digits=30, decimal_places=15)

    def __str__(self) -> str:
        return f"{self.nombre}"


class SubInstalacionBatallon(Instalacion):
    def __str__(self) -> str:
        return f"{self.nombre}"


class Militar(DatosMilitar):
    OFICIAL = "Oficial"
    SUBOFICIAL = "Suboficial"
    SOLDADO_PROFESIONAL = "Soldado profesional"
    SOLDADO_RASO = "Soldado raso"
    grados = (
        (OFICIAL, "Oficial"),
        (SUBOFICIAL, "Suboficial"),
        (SOLDADO_PROFESIONAL, "Soldado profesional"),
        (SOLDADO_RASO, "Soldado raso"),
    )

    arma = models.OneToOneField(
        Arma, blank=True, default="Sin registrar", on_delete=models.CASCADE
    )
    grado = models.CharField(choices=(grados), default=grados[2], max_length=20)
    posicion = models.ForeignKey(
        Posicion, on_delete=models.CASCADE, blank=True, null=True
    )

class Estadisticas(models.Model):
    id = models.AutoField(primary_key=True)
    militar = models.ForeignKey(Militar, on_delete=models.CASCADE)


class Poligono(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()


class PracticaPoligonon(models.Model):
    militar = models.ForeignKey(Militar, on_delete=models.CASCADE)
    poligono = models.ForeignKey(Poligono, on_delete=models.CASCADE)


class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, primary_key=True)
    modelo = models.IntegerField()
    color = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)


class Visitante(DatosBasicos):
    fecha = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length=50)
    motivo = models.TextField(max_length=300, blank=True, null=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"


class EsquemaSeguridad(models.Model):
    militares = models.ForeignKey(Militar, on_delete=models.CASCADE)
