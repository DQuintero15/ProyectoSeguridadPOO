from FuerzasMilitares.models.Militar import Militar
from FuerzasMilitares.models.UbicacionMilitar import UbicacionMilitar
from FuerzasMilitares.models.InstalacionMilitar import InstalacionMilitar

def getDatosGenerales(request) -> dict:
    if request.user.is_authenticated:
        user_id = request.user.id
        datos = Militar.objects.select_related(
            "datosbasicos_ptr", "rango", "usuario"
        ).filter(usuario_id=user_id)
        id_militar = Militar.objects.get(usuario_id=user_id).id_militar
        try:
            ubicacion = UbicacionMilitar.objects.select_related("instalacion").get(
                militar_id=id_militar
            )
        except UbicacionMilitar.DoesNotExist:
            instalacion_defecto = InstalacionMilitar.objects.get(
                id_instalacion=-1
            ).id_instalacion
            ubicacion = UbicacionMilitar(None, id_militar, instalacion_defecto)
            ubicacion.save()
        context = {"ubicacion": ubicacion, "datos_militar": datos}
        return context
    else: 
        return {}


def getPersonalBatallon(request) -> dict:
    user = request.user
    if user.is_authenticated and user.is_superuser:
        user_id = request.user.id

        id_militar = Militar.objects.get(usuario_id=user_id).id_militar

        id_instalacion = UbicacionMilitar.objects.get(
            militar_id=id_militar
        ).instalacion.id_instalacion

        militares = UbicacionMilitar.objects.filter(
            instalacion_id=id_instalacion
        ).select_related("militar")

        context = {"militares": militares}

        return context

    return {}
