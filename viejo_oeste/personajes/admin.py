from django.contrib import admin
from personajes.models import vaquero

class vaquerosadmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','edad','buscado','sexo']

admin.site.register(vaquero,vaquerosadmin)
