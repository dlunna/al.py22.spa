"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

from core import views as core_views
from myapps.packages import views as packages_views

# ** En modo debug no se pueden ver los archivos de la carpeta media
from django.conf import settings


urlpatterns = [
    path('adm1n/', admin.site.urls),
    path('', core_views.root, name="root"),
    path('spa/', include('core.urls')),
    path('paquetes/', packages_views.packages, name="packages"),
    path('notas/', include('myapps.blog.urls')),
]


# **
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)