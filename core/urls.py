"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
    path("", include("landing.urls")),
    path("login/", include("user.urls")),
=======
    path("home/", include("landing.urls")),
>>>>>>> eda3c2b24b79ba3e8bef66f30288c5f82274110f
=======
    path("home/", include("landing.urls")),
>>>>>>> f01ceb22af857cfca7d28c500f7358420e23879e
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
