from django.contrib import admin
from .models import WebPage

# Register your models here.

class WebPageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #list manda llamar del modelo el orden, por titulo y luego 
    # x bandera order
    #list_display = ('title', 'order')
    #list_display = ('title',)

admin.site.register(WebPage, WebPageAdmin)