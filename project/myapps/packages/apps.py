#from tabnanny import verbose
from django.apps import AppConfig


class PackagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # cuando esta dentro de una carpeta agregar ruta
    name = 'myapps.packages'
    # Tambien modificar en settings y
    # cambia el nombre en admon
    verbose_name='Promoción'
