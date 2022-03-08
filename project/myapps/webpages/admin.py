from django.contrib import admin
from .models import WebPage

# Register your models here.

class WebPageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #list_display = ('title',)
    #list manda llamar del modelo y ordena por titulo 
    # y luego por el valor de la bandera
    list_display = ('title', 'order')

admin.site.register(WebPage, WebPageAdmin)