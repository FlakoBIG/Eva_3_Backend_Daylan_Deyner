from django.contrib import admin
from django import forms
from django.forms.widgets import TextInput
from django.utils.html import format_html
from .models import vaquero, arma, caballo

# Formulario personalizado para el modelo Caballo en el administrador
class CaballoForm(forms.ModelForm):
    class Meta:
        model = caballo
        fields = ['nombre', 'raza', 'color', 'velocidad', 'resistencia', 'vaquero']
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }

class VaqueroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'edad', 'buscado', 'sexo']

class ArmaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad_balas', 'tipo_bala', 'tipo_arma', 'cadencia', 'vaquero']

class CaballoAdmin(admin.ModelAdmin):
    form = CaballoForm  # Asigna el formulario personalizado

    # Columna personalizada para mostrar el color con un input deshabilitado
    def muestra_color(self, obj):
        return format_html(
            '<input type="color" value="{}" disabled style="border: none; width: 50px; height: 25px; cursor: default;">',
            obj.color
        )
    muestra_color.short_description = "Color"

    list_display = ['nombre', 'raza', 'muestra_color', 'velocidad', 'resistencia', 'vaquero']

# Registro de los modelos en el administrador
admin.site.register(vaquero, VaqueroAdmin)
admin.site.register(arma, ArmaAdmin)
admin.site.register(caballo, CaballoAdmin)
