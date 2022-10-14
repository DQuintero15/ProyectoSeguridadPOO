from django.db import models
from FuerzasMilitares.models.InstalacionMilitar import InstalacionMilitar
from django.forms import ModelForm
from django import forms
from FuerzasMilitares.models.Militar import Militar


class PracticaPoligono(models.Model):
    id_practica_poligono = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    instalacion = models.ForeignKey(
        InstalacionMilitar,
        null=True,
        blank=True,
        related_name="practica_instalacion",
        on_delete=models.CASCADE,
    )
    disponible = models.BooleanField(default=True)
    modelo_objetivo = models.ImageField(
        upload_to="images\\modelos", null=True, blank=True
    )
    militar = models.ForeignKey(
        Militar,
        null=True,
        blank=True,
        related_name="practica_militar",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Practica #{self.id_practica_poligono} de {self.fecha} por {self.militar.rango.abreviatura} {self.militar.nombres[0]}. {self.militar.apellidos}"

    class Meta:
        verbose_name = "Practica de Poligono"
        verbose_name_plural = "Practicas de Poligono"
        db_table = "practica_poligono"


class DateInput(forms.DateInput):
    input_type = "date"


class PracticaPoligoForm(ModelForm):
    class Meta:
        model = PracticaPoligono
        fields = [
            "fecha",
            "instalacion",
            "disponible",
            "modelo_objetivo",
        ]
        widgets = {"fecha": DateInput}
