from django import forms
from django.core.exceptions import ValidationError
import re
from .models import vaquero, arma, caballo

class formcaballo(forms.ModelForm):
    class Meta:
        model = caballo
        fields = ['nombre', 'raza', 'color', 'velocidad', 'resistencia']
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombre):
            raise forms.ValidationError("El nombre solo debe contener letras.")
        return nombre
    
    def clean_raza(self):
        raza = self.cleaned_data.get('raza')
        if len(raza) < 3:
            raise forms.ValidationError("La raza debe tener al menos 3 caracteres.")
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", raza):
            raise forms.ValidationError("La raza solo debe contener letras.")
        return raza
    
    def clean_color(self):
        color = self.cleaned_data.get('color')
        if len(color) < 3:
            raise forms.ValidationError("El color debe tener al menos 3 caracteres.")
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", color):
            raise forms.ValidationError("El color solo debe contener letras.")
        return color

class Formvaquero(forms.ModelForm):
    class Meta:
        model = vaquero
        fields = ['nombre', 'apellido', 'edad', 'buscado', 'sexo', 'caballo']
        widgets = {
            'caballo': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_caballo(self):
        caballo_seleccionado = self.cleaned_data.get('caballo')
        if caballo_seleccionado:
            # Verificar si el caballo ya está asignado a otro vaquero
            if vaquero.objects.filter(caballo=caballo_seleccionado).exclude(id=self.instance.id).exists():
                raise ValidationError('Este caballo ya está asignado a otro vaquero')
        return caballo_seleccionado

class formArma(forms.ModelForm):
    class Meta:
        model = arma
        fields = ['nombre', 'cantidad_balas', 'tipo_bala', 'tipo_arma', 'cadencia', 'vaquero']
        widgets = {
            'vaquero': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_cantidad_balas(self):
        cantidad = self.cleaned_data.get('cantidad_balas')
        if cantidad < 200:
            raise forms.ValidationError("La cantidad de balas no debe ser menor a 200")
        return cantidad
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")
        if not re.match("^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]+$", nombre):
            raise forms.ValidationError("El nombre solo debe contener letras, números y espacios")
        return nombre