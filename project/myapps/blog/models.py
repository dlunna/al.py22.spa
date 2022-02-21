from django.db import models
#importar timezone para now
from django.utils import timezone
#Para importar user
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    #content = RichTextField(verbose_name="Contenido", null=True, blank=True)
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=timezone.now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)   
    #On delete - borrar en cascada todos
    #Lo contrario a cascade PROTECT pero debe tener null=True, blank=True
    author = models.ForeignKey (User, verbose_name="Autor", on_delete=models.CASCADE)
    #categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_post")
    categories = models.ManyToManyField(Category, verbose_name="Categorias")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title