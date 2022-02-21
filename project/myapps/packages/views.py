from django.shortcuts import render

# Create your views here.

#Para acceder a la BD los modelos importar
from .models import Promotion

# Create your views here.

def packages(request):
    #Esto debuelve todos los objetos que tienen el modelo proyecto
    projects = Promotion.objects.all()
    # Pasar el parametro en el render como anexo
    # return render(request, "promotion/promotion.html")
    return render(request, "packages/packages.html", {'clave':projects})