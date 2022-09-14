from django.shortcuts import render
from FuerzasMilitares.models import FuerzasMilitares
from django.shortcuts import redirect

def home(request):
    if request.method == "GET":
        token = request.GET.get("token")
        if token is not None and FuerzasMilitares.objects.filter(token_acceso = token).exists():
            token = token[::-1]
    return render(request, "home.html", {"token": token})
