from django.db import models

# Create your models here.

class Link(models.Model):
    #Slugfield alfanumerico (numeros, barras)
    #pero no caracteres especiales
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Enlace social"
        verbose_name_plural = "Enlaces sociales"
        # Tambien se pueden ordenar por nombre
        ordering = ["-created"]
        ordering = ["name"]

    def __str__(self):
        return self.name