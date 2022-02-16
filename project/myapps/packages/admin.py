from django.contrib import admin
from .models import Promotion

# Register your models here.

# Para que el panel de admon nos muestre creado y actualizado
# pasar tambien dentro del site.register
class PromotionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Para que se pueda manipular el modelo en el panel de admon
admin.site.register(Promotion, PromotionAdmin)
