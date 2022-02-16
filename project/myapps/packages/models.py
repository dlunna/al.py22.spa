from django.db import models

# Create your models here.

class Promotion(models.Model):
    # se agrega el verbose name para cambiar el nombre a español en el panel de admon
    tittle = models.CharField(max_length=100, verbose_name= "Título")
    description = models.TextField(verbose_name= "Descripción")
    # ORIGINAL image = models.ImageField(verbose_name="Imagen")
    # se agrega upload_to XXXX para colocar las imagenes dentro de una carpeta
    #image = models.ImageField(verbose_name="Imagen")
    image = models.ImageField(verbose_name="Imagen", upload_to="packages_files")
    # Campo opcional para agregar una URL
    #link = models.URLField(verbose_name="URL", null=True, blank=True)
    # Campo para el costo
    #cost = models.DecimalField(verbose_name="Costo", max_digits=10, decimal_places=2, default=0)

    #Añade automaticamente la Fecha de creacion
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    #Añade la fecha de cuando de actualiza
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")


    class Meta:
        #Nombre para singular de la clase en el admin
        verbose_name = "paquete"
        #Nombre para plural de la clase
        verbose_name_plural = "paquetes"
        # Ordena los proyectos desde el ultimo creado
        ordering = ["-created"]

    # En el panel de admin
    # en lugar del nombre raro que muestre el titulo
    def __str__(self):
        return self.tittle