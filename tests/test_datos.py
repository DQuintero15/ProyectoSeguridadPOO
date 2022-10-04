import pytest
from FuerzasMilitares.models.DatosBasicos import DatosBasicos

@pytest.mark.django_db
def test_datos_basicos():
    nuevos_datos = DatosBasicos.objects.create(
    nombres = "Nombre prueba",
    apellidos = "Apellido prueba militar",
    correo_electronico = "pruebacorreo@cerberus.com",
    tipo_sangre = "AB+",
    numero_cedula = "1006324567",
    fecha_nacimiento = "1980-02-12",
    numero_telefono = "+573207853472",
    )
    assert nuevos_datos.nombres == "Nombre prueba"
    assert nuevos_datos.numero_telefono == "+573207853472"
    assert nuevos_datos.tipo_sangre == "AB+"

