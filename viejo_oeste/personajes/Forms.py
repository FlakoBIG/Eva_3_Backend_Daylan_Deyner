from django import forms
from django.core.exceptions import ValidationError
from .models import vaquero, arma, caballo

class formcaballo(forms.ModelForm):
    class Meta:
        model = caballo
        fields = ['nombre', 'raza', 'color', 'velocidad', 'resistencia', 'vaquero']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}), 
            'velocidad': forms.Select(attrs={'class': 'form-control'}),
            'resistencia': forms.Select(attrs={'class': 'form-control'}),
            'vaquero': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vaquero'].queryset = vaquero.objects.all()
        self.fields['vaquero'].empty_label = "Seleccione un vaquero (opcional)"

class formArma(forms.ModelForm):
    class Meta:
        model = arma
        fields = ['nombre', 'cantidad_balas', 'tipo_bala', 'tipo_arma', 'cadencia', 'vaquero']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_balas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'tipo_bala': forms.Select(attrs={'class': 'form-control'}),
            'tipo_arma': forms.Select(attrs={'class': 'form-control'}),
            'cadencia': forms.Select(attrs={'class': 'form-control'}),
            'vaquero': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vaquero'].queryset = vaquero.objects.all()
        self.fields['vaquero'].empty_label = "Seleccione un vaquero (opcional)"

class Formvaquero(forms.ModelForm):
    class Meta:
        model = vaquero
        fields = ['nombre', 'apellido', 'edad', 'buscado', 'sexo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'buscado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }

    # Campos adicionales para caballo y arma
    nuevo_caballo = forms.BooleanField(required=False, label="¿Agregar nuevo caballo?", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    nuevo_caballo_nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del caballo'}))
    nuevo_caballo_raza = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza del caballo'}))
    nuevo_caballo_color = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color del caballo'}))
    nuevo_caballo_velocidad = forms.ChoiceField(choices=caballo.nivel, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    nuevo_caballo_resistencia = forms.ChoiceField(choices=caballo.nivel, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    nueva_arma = forms.BooleanField(required=False, label="¿Agregar nueva arma?", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    nueva_arma_nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del arma'}))
    nueva_arma_cantidad_balas = forms.IntegerField(required=False, min_value=20, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de balas'}))
    nueva_arma_tipo_bala = forms.ChoiceField(choices=arma.TipoBala, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    nueva_arma_tipo_arma = forms.ChoiceField(choices=arma.TipoArma, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    nueva_arma_cadencia = forms.ChoiceField(choices=arma.TipoCadencia, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    caballo = forms.ModelChoiceField(
        queryset=caballo.objects.filter(vaquero__isnull=True),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione un caballo sin dueño"
    )
    arma = forms.ModelChoiceField(
        queryset=arma.objects.filter(vaquero__isnull=True),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione un arma sin dueño"
    )

    def clean(self):
        cleaned_data = super().clean()
        self._validate_related_fields(cleaned_data, 'nuevo_caballo', ['nuevo_caballo_nombre', 'nuevo_caballo_raza', 'nuevo_caballo_color', 'nuevo_caballo_velocidad', 'nuevo_caballo_resistencia'])
        self._validate_related_fields(cleaned_data, 'nueva_arma', ['nueva_arma_nombre', 'nueva_arma_cantidad_balas', 'nueva_arma_tipo_bala', 'nueva_arma_tipo_arma', 'nueva_arma_cadencia'])
        return cleaned_data

    def _validate_related_fields(self, cleaned_data, field_name, required_fields):
        if cleaned_data.get(field_name):
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f'Este campo es requerido si agregas una nueva {field_name.split("_")[1]}')

    def save(self, commit=True):
        vaquero_instance = super().save(commit=False)
        if commit:
            vaquero_instance.save()

            # Agrega caballo y arma 
            if self.cleaned_data.get('nuevo_caballo'):
                caballo.objects.create(
                    nombre=self.cleaned_data['nuevo_caballo_nombre'],
                    raza=self.cleaned_data['nuevo_caballo_raza'],
                    color=self.cleaned_data['nuevo_caballo_color'],
                    velocidad=self.cleaned_data['nuevo_caballo_velocidad'],
                    resistencia=self.cleaned_data['nuevo_caballo_resistencia'],
                    vaquero=vaquero_instance
                )

            if self.cleaned_data.get('nueva_arma'):
                arma.objects.create(
                    nombre=self.cleaned_data['nueva_arma_nombre'],
                    cantidad_balas=self.cleaned_data['nueva_arma_cantidad_balas'],
                    tipo_bala=self.cleaned_data['nueva_arma_tipo_bala'],
                    tipo_arma=self.cleaned_data['nueva_arma_tipo_arma'],
                    cadencia=self.cleaned_data['nueva_arma_cadencia'],
                    vaquero=vaquero_instance)
        return vaquero_instance
