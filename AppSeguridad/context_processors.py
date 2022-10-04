from FuerzasMilitares.models.Militar import Militar
from FuerzasMilitares.models.UbicacionMilitar import UbicacionMilitar
from FuerzasMilitares.models.RangoMilitar import RangoMilitar


def getDatosGenerales(request) -> dict:
    if request.user.is_authenticated:
        user_id = request.user.id
        datos = Militar.objects.select_related(
            "datosbasicos_ptr", "rango", "usuario"
        ).filter(usuario_id=user_id)
        id_militar = Militar.objects.get(usuario_id=user_id).id_militar
        ubicacion = UbicacionMilitar.objects.select_related("instalacion").get(
            militar_id=id_militar
        )
        context = {"ubicacion": ubicacion, "datos_militar": datos}
        return context
    return {}
