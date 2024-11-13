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

    # Validación personalizada
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('El nombre del caballo es obligatorio.')

        # Validar que el nombre empiece con mayúscula y contenga solo letras
        if not nombre[0].isupper():
            raise ValidationError('El nombre debe comenzar con una letra mayuscula.')
        if not nombre.isalpha():
            raise ValidationError('El nombre solo puede contener letras.')
        return nombre
    def clean_raza(self):
        raza = self.cleaned_data.get('raza')
        if not raza:
            raise ValidationError('La raza del caballo es obligatoria.')
        if not raza[0].isupper():
            raise ValidationError('La raza debe comenzar con una letra mayuscula.')
        # Validar que la raza solo contenga letras (sin números ni caracteres especiales)
        if not raza.isalpha():
            raise ValidationError('La raza solo puede contener letras.')

        return raza
    
   

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

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('El nombre es obligatorio.')
        if not nombre.isalpha():
            raise ValidationError('El nombre solo puede contener letras.')
        if not nombre[0].isupper():
            raise ValidationError('El nombre debe comenzar con una letra mayúscula.')

        return nombre

    # Validación personalizada para la cantidad de balas
    def clean_cantidad_balas(self):
        cantidad_balas = self.cleaned_data.get('cantidad_balas')   
        # Validar que la cantidad de balas sea mayor que 0
        if cantidad_balas is None or cantidad_balas <= 0:
            raise ValidationError('La cantidad de balas debe ser mayor a cero.')
        return cantidad_balas

from django import forms
from django.core.exceptions import ValidationError
from .models import vaquero, caballo, arma

class Formvaquero(forms.ModelForm):
    # Campos para el vaquero
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

    # Campos adicionales para el caballo
    nuevo_caballo = forms.BooleanField(
        required=False, 
        label="¿Agregar nuevo caballo?",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'nuevo_caballo_checkbox'})
    )
    nuevo_caballo_nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nuevo_caballo_nombre', 'placeholder': 'Nombre del caballo'})
    )
    nuevo_caballo_raza = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nuevo_caballo_raza', 'placeholder': 'Raza del caballo'})
    )
    nuevo_caballo_color = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nuevo_caballo_color', 'placeholder': 'Color del caballo'})
    )
    nuevo_caballo_velocidad = forms.ChoiceField(
        choices=caballo.nivel,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'nuevo_caballo_velocidad'})
    )
    nuevo_caballo_resistencia = forms.ChoiceField(
        choices=caballo.nivel,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'nuevo_caballo_resistencia'})
    )

    # Campos adicionales para el arma
    nueva_arma = forms.BooleanField(
        required=False,
        label="¿Agregar nueva arma?",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'nueva_arma_checkbox'})
    )
    nueva_arma_nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nueva_arma_nombre', 'placeholder': 'Nombre del arma'})
    )
    nueva_arma_cantidad_balas = forms.IntegerField(
        required=False,
        min_value=20,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'nueva_arma_cantidad_balas', 'placeholder': 'Cantidad de balas'})
    )
    nueva_arma_tipo_bala = forms.ChoiceField(
        choices=arma.TipoBala,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'nueva_arma_tipo_bala'})
    )
    nueva_arma_tipo_arma = forms.ChoiceField(
        choices=arma.TipoArma,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'nueva_arma_tipo_arma'})
    )
    nueva_arma_cadencia = forms.ChoiceField(
        choices=arma.TipoCadencia,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'nueva_arma_cadencia'})
    )

    def clean(self):
        cleaned_data = super().clean()
        
        # Validación de datos del caballo si se marca la opción
        if cleaned_data.get('nuevo_caballo'):
            required_fields = [
                'nuevo_caballo_nombre',
                'nuevo_caballo_raza',
                'nuevo_caballo_color',
                'nuevo_caballo_velocidad',
                'nuevo_caballo_resistencia'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, 'Este campo es requerido si agregas un nuevo caballo')

            # Validación del nombre del caballo
            nombre_caballo = cleaned_data.get('nuevo_caballo_nombre')
            if nombre_caballo:
                if not nombre_caballo[0].isupper():
                    self.add_error('nuevo_caballo_nombre', 'El nombre del caballo debe comenzar con una letra mayúscula.')
                if not nombre_caballo.isalpha():
                    self.add_error('nuevo_caballo_nombre', 'El nombre del caballo solo puede contener letras.')

        # Validación de datos del arma si se marca la opción
        if cleaned_data.get('nueva_arma'):
            required_fields = [
                'nueva_arma_nombre',
                'nueva_arma_cantidad_balas',
                'nueva_arma_tipo_bala',
                'nueva_arma_tipo_arma',
                'nueva_arma_cadencia'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, 'Este campo es requerido si agregas una nueva arma')

            # Validación del nombre del arma
            nombre_arma = cleaned_data.get('nueva_arma_nombre')
            if nombre_arma and not nombre_arma[0].isupper():
                self.add_error('nueva_arma_nombre', 'El nombre del arma debe comenzar con una letra mayúscula.')

            # Validación de la cantidad de balas
            cantidad_balas = cleaned_data.get('nueva_arma_cantidad_balas')
            if cantidad_balas is not None and cantidad_balas < 20:
                self.add_error('nueva_arma_cantidad_balas', 'La cantidad de balas debe ser al menos 20.')

        return cleaned_data

    def save(self, commit=True):
        vaquero_instance = super().save(commit=False)
        
        if commit:
            vaquero_instance.save()

            # Crear y asignar caballo si se marcó la opción
            if self.cleaned_data.get('nuevo_caballo'):
                caballo.objects.create(
                    nombre=self.cleaned_data['nuevo_caballo_nombre'],
                    raza=self.cleaned_data['nuevo_caballo_raza'],
                    color=self.cleaned_data['nuevo_caballo_color'],
                    velocidad=self.cleaned_data['nuevo_caballo_velocidad'],
                    resistencia=self.cleaned_data['nuevo_caballo_resistencia'],
                    vaquero=vaquero_instance
                )

            # Crear y asignar arma si se marcó la opción
            if self.cleaned_data.get('nueva_arma'):
                arma.objects.create(
                    nombre=self.cleaned_data['nueva_arma_nombre'],
                    cantidad_balas=self.cleaned_data['nueva_arma_cantidad_balas'],
                    tipo_bala=self.cleaned_data['nueva_arma_tipo_bala'],
                    tipo_arma=self.cleaned_data['nueva_arma_tipo_arma'],
                    cadencia=self.cleaned_data['nueva_arma_cadencia'],
                    vaquero=vaquero_instance
                )

        return vaquero_instance
    # Campos para el vaquero
    class Meta:
        model = vaquero
        fields = ['nombre', 'apellido', 'edad', 'buscado', 'sexo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'buscado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }

    # Campos para el caballo
    nuevo_caballo = forms.BooleanField(
        required=False, 
        label="¿Agregar nuevo caballo?",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    nuevo_caballo_nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del caballo'})
    )
    nuevo_caballo_raza = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza del caballo'})
    )
    nuevo_caballo_color = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color del caballo'})
    )
    nuevo_caballo_velocidad = forms.ChoiceField(
        choices=caballo.nivel,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    nuevo_caballo_resistencia = forms.ChoiceField(
        choices=caballo.nivel,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Campos para el arma
    nueva_arma = forms.BooleanField(
        required=False,
        label="¿Agregar nueva arma?",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    nueva_arma_nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del arma'})
    )
    nueva_arma_cantidad_balas = forms.IntegerField(
        required=False,
        min_value=20,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de balas'})
    )
    nueva_arma_tipo_bala = forms.ChoiceField(
        choices=arma.TipoBala,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    nueva_arma_tipo_arma = forms.ChoiceField(
        choices=arma.TipoArma,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    nueva_arma_cadencia = forms.ChoiceField(
        choices=arma.TipoCadencia,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha() or len(nombre) > 50:
            raise ValidationError('El nombre del vaquero debe contener solo letras y tener un máximo de 50 caracteres.')
        
        return nombre

    def clean_nuevo_caballo_nombre(self):
        nombre = self.cleaned_data.get('nuevo_caballo_nombre')
        if nombre and (not nombre.isalpha() or len(nombre) > 50):
            raise ValidationError('El nombre del caballo debe contener solo letras y tener un máximo de 50 caracteres.')
        
        return nombre

    def clean_nueva_arma_nombre(self):
        nombre = self.cleaned_data.get('nueva_arma_nombre')
        if nombre and (not nombre.isalpha() or len(nombre) > 50):
            raise ValidationError('El nombre del arma debe contener solo letras y tener un máximo de 50 caracteres.')
        return nombre

    def clean_nueva_arma_cantidad_balas(self):
        cantidad_balas = self.cleaned_data.get('nueva_arma_cantidad_balas')
        if cantidad_balas and cantidad_balas < 20:
            raise ValidationError('La cantidad de balas debe ser al menos 20.')
        return cantidad_balas

    def clean(self):
        cleaned_data = super().clean()
        
        # Validar datos del caballo si se marca la opción
        if cleaned_data.get('nuevo_caballo'):
            required_fields = [
                'nuevo_caballo_nombre',
                'nuevo_caballo_raza',
                'nuevo_caballo_color',
                'nuevo_caballo_velocidad',
                'nuevo_caballo_resistencia'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, 'Este campo es requerido si agregas un nuevo caballo')

        # Validar datos del arma si se marca la opción
        if cleaned_data.get('nueva_arma'):
            required_fields = [
                'nueva_arma_nombre',
                'nueva_arma_cantidad_balas',
                'nueva_arma_tipo_bala',
                'nueva_arma_tipo_arma',
                'nueva_arma_cadencia'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, 'Este campo es requerido si agregas una nueva arma')

        return cleaned_data

    def save(self, commit=True):
        vaquero_instance = super().save(commit=False)
        
        if commit:
            vaquero_instance.save()

            # Crear y asignar caballo si se marcó la opción
            if self.cleaned_data.get('nuevo_caballo'):
                nuevo_caballo = caballo.objects.create(
                    nombre=self.cleaned_data['nuevo_caballo_nombre'],
                    raza=self.cleaned_data['nuevo_caballo_raza'],
                    color=self.cleaned_data['nuevo_caballo_color'],
                    velocidad=self.cleaned_data['nuevo_caballo_velocidad'],
                    resistencia=self.cleaned_data['nuevo_caballo_resistencia'],
                    vaquero=vaquero_instance
                )

            # Crear y asignar arma si se marcó la opción
            if self.cleaned_data.get('nueva_arma'):
                nueva_arma = arma.objects.create(
                    nombre=self.cleaned_data['nueva_arma_nombre'],
                    cantidad_balas=self.cleaned_data['nueva_arma_cantidad_balas'],
                    tipo_bala=self.cleaned_data['nueva_arma_tipo_bala'],
                    tipo_arma=self.cleaned_data['nueva_arma_tipo_arma'],
                    cadencia=self.cleaned_data['nueva_arma_cadencia'],
                    vaquero=vaquero_instance
                )

        return vaquero_instance