import pytest
from FuerzasMilitares.models.ModeloArma import ModeloArma
from FuerzasMilitares.models.FuerzaMilitar import FuerzaMilitar


@pytest.mark.django_db
def test_modelo_armas():
    modelo_arma_nuevo = ModeloArma.objects.create(
        nombre="AK-47",
        calibre="39mm",
        observacion="Nueva arma",
        letal=True,
    )
    assert modelo_arma_nuevo.calibre == "39mm"
    assert modelo_arma_nuevo.letal == True
    assert modelo_arma_nuevo.nombre == "AK-47"
    assert modelo_arma_nuevo.observacion == "Nueva arma"


@pytest.mark.django_db
def test_modelo_armas():
    nueva_fuerza_militar = FuerzaMilitar.objects.create(
        nombre="Fuerza militar de ejemplo",
        logo="/static/images/logo.png",
    )
    assert nueva_fuerza_militar.nombre == "Fuerza militar de ejemplo"
