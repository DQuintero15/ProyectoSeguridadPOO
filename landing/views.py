from django.shortcuts import render
from FuerzasMilitares.models import FuerzasMilitares


def home(request):  
    return render(request, "home.html")

