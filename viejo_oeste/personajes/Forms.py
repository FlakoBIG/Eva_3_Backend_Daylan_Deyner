from django import forms
from .models import vaquero, arma, caballo

class formcaballo(forms.ModelForm):
    class Meta:
        model = caballo
        fields = ['nombre', 'raza', 'color', 'velocidad', 'resistencia']


class Formvaquero(forms.ModelForm):
    nuevo_caballo = forms.BooleanField(required=False, label="Agregar nuevo caballo")
    nuevo_caballo_nombre = forms.CharField(required=False)
    nuevo_caballo_raza = forms.CharField(required=False)
    nuevo_caballo_color = forms.CharField(required=False)
    nuevo_caballo_velocidad = forms.ChoiceField(choices=caballo.nivel, required=False)
    nuevo_caballo_resistencia = forms.ChoiceField(choices=caballo.nivel, required=False)

    nueva_arma = forms.BooleanField(required=False, label="Agregar nueva arma")
    nueva_arma_nombre = forms.CharField(required=False)
    nueva_arma_cantidad_balas = forms.IntegerField(required=False, min_value=200)
    nueva_arma_tipo_bala = forms.ChoiceField(choices=arma.TipoBala, required=False)
    nueva_arma_tipo_arma = forms.ChoiceField(choices=arma.TipoArma, required=False)
    nueva_arma_cadencia = forms.ChoiceField(choices=arma.TipoCadencia, required=False)

    class Meta:
        model = vaquero
        fields = ['nombre', 'apellido', 'edad', 'buscado', 'sexo']

    def save(self, commit=True):
        vaquero_instance = super().save(commit=False)
        
        if commit:
            vaquero_instance.save()

            if self.cleaned_data.get('nuevo_caballo'):
                caballo.objects.create(
                    nombre=self.cleaned_data.get('nuevo_caballo_nombre'),
                    raza=self.cleaned_data.get('nuevo_caballo_raza'),
                    color=self.cleaned_data.get('nuevo_caballo_color'),
                    velocidad=self.cleaned_data.get('nuevo_caballo_velocidad'),
                    resistencia=self.cleaned_data.get('nuevo_caballo_resistencia'),
                    vaquero=vaquero_instance
                )

            if self.cleaned_data.get('nueva_arma'):
                arma.objects.create(
                    nombre=self.cleaned_data.get('nueva_arma_nombre'),
                    cantidad_balas=self.cleaned_data.get('nueva_arma_cantidad_balas'),
                    tipo_bala=self.cleaned_data.get('nueva_arma_tipo_bala'),
                    tipo_arma=self.cleaned_data.get('nueva_arma_tipo_arma'),
                    cadencia=self.cleaned_data.get('nueva_arma_cadencia'),
                    vaquero=vaquero_instance
                )
        return vaquero_instance

class formArma(forms.ModelForm):
    class Meta:
        model = arma
        fields = ['nombre', 'cantidad_balas', 'tipo_bala', 'tipo_arma', 'cadencia'] 