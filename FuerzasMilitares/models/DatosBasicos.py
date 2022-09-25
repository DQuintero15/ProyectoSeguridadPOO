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