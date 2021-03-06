from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class WebPage(models.Model):

    title = models.CharField(verbose_name="Título", max_length=200)
    #content = models.TextField(verbose_name="Contenido")
    #Para habilitar el ckeditor
    content = RichTextField(verbose_name="Contenido")
    #Para ordenar los modelos
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['title']
        ordering = ['order','title']
        

    def __str__(self):
        return self.title
    