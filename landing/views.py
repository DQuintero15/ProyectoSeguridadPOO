from django.shortcuts import render
from FuerzasMilitares.models import FuerzasMilitares
<<<<<<< HEAD


def home(request):  
    return render(request, "home.html")

=======
from django.shortcuts import redirect

def home(request):
    if request.method == "GET":
        token = request.GET.get("token")
        if token is not None and FuerzasMilitares.objects.filter(token_acceso = token).exists():
            token = token[::-1]
    return render(request, "home.html", {"token": token})
>>>>>>> f01ceb22af857cfca7d28c500f7358420e23879e
