from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    #define que campos son estaticos y no se pueden modificar en el panel
    #de admon
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #Se agrega para decirle al motor administrador de django
    # que muestre mas columnas
    list_display = ('title', 'author', 'published', 'post_categories')
    #Para ordenamientos, si es solo un elemento como TUPLA
    #TUPLA -> ordering = ('author',)
    ordering = ('author', 'published')
    #formulario de busqueda
    #author no, debe llevar __username
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    # Para una busqueda por años gerarquia en la parte superior
    date_hierarchy = 'published'
    # Da un cuadro del lado derecho para filtros
    list_filter = ('author__username', 'categories__name',)

    #Todo esto para mandar llamar las categorias dentro del list_display
    #Categorias es un dato complejo por lo que no se puede mostrar tal cual
    # se tiene que hacer un recorrido para listarlo
    def post_categories(self, obj):
        #return "ALGO"
        return ", ".join( [c.name for c in obj.categories.all().order_by("name")] )
    #Esto le cambia el nombre a post_categories
    post_categories.short_description = 'Categorias'

# Para administrar este modelo desde el panel admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)