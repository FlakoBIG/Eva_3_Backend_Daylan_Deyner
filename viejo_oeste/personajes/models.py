from django.db import models
from django.core.exceptions import ValidationError

class caballo(models.Model):
    nivel = [
        ('alta', 'alta'),
        ('media', 'media'),
        ('baja', 'baja'),
    ]
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    velocidad = models.CharField(max_length=5, choices=nivel)
    resistencia = models.CharField(max_length=5, choices=nivel)

    # Relacion OneToOne con vaquero, y si el vaquero se elimina, tambien se elimina el caballo
    vaquero = models.ForeignKey('vaquero', on_delete=models.CASCADE, null=True, blank=True, related_name='caballos')
    def clean(self):
        super().clean()
        # Validar nombre
        nombre_limpio = self.nombre.strip()  # Eliminar espacios en blanco al inicio y al final
        if not nombre_limpio:
            raise ValidationError({'nombre': 'Tienes que ingresar el nombre'})
        if len(nombre_limpio) < 2 or len(nombre_limpio) > 25:
            raise ValidationError({'nombre': 'El nombre debe tener entre 2 y 25 caracteres'})
        if not nombre_limpio.isalpha():
            raise ValidationError({'nombre': 'El nombre solo puede contener letras y sin espacios'})
        if not nombre_limpio[0].isupper():
            raise ValidationError({'nombre': 'El nombre debe comenzar con una letra mayuscula'})
        #validacion de raza
        raza_limpia=self.raza.strip()
        if not raza_limpia:
            raise ValidationError({'raza':'Tienes que ingresar la raza'})
        if len(raza_limpia)<2 or len(raza_limpia)>25:
            raise ValidationError({'raza':'La raza debe contener entre 2 y 25 caracteres'})
        if not raza_limpia.isalpha():
            raise ValidationError({'raza': 'La raza solo puede contener letras y sin espacios'})
        if not raza_limpia[0].isupper():
            raise ValidationError({'raza': 'La raza debe comenzar con una letra mayuscula'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.raza})"

class arma(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_balas = models.IntegerField(default=1, help_text="El numero no debe ser menor a 1 balas")
    
    TipoBala = [
        ('9mm', '9mm'),
        ('calibre_45', 'calibre .45'),
        ('calibre_50', 'calibre .50'),
        ('arma_blanca', 'Arma Blanca')
    ]
    tipo_bala = models.CharField(max_length=50, choices=TipoBala)
    
    TipoArma = [
        ('largo_alcanse', 'Largo Alcance'),
        ('medio_alcanse', 'Mediano Alcance'),
        ('bajo_alcanse', 'Bajo Alcance'),
        ('cuerpo_a_cuerpo', 'Cuerpo a Cuerpo')
    ]
    tipo_arma = models.CharField(max_length=50, choices=TipoArma)
    
    TipoCadencia = [
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
        ('arma_blanca', 'Arma Blanca')
    ]
    cadencia = models.CharField(max_length=50, choices=TipoCadencia)

    def clean(self):
        super().clean()

        # Validar nombre
        nombre_limpio = self.nombre.strip()  # Eliminar espacios en blanco al inicio y al final
        if not nombre_limpio:
            raise ValidationError({'nombre': 'Tienes que ingresar el nombre'})
        if len(nombre_limpio) < 2 or len(nombre_limpio) > 25:
            raise ValidationError({'nombre': 'El nombre debe tener entre 2 y 25 caracteres'})
        if not nombre_limpio[0].isupper():
            raise ValidationError({'nombre': 'El nombre debe comenzar con una letra mayuscula'})

        # Validar tipo_arma y tipo_bala
        if self.tipo_arma == 'cuerpo_a_cuerpo':
            if self.tipo_bala != 'arma_blanca':
                raise ValidationError({'tipo_bala': 'Para "Cuerpo a Cuerpo", el tipo de bala debe ser "Arma Blanca"'})
            if self.cadencia != 'arma_blanca':
                raise ValidationError({'cadencia': 'Para "Cuerpo a Cuerpo", la cadencia debe ser "Arma Blanca"'})

        # Validar cantidad_balas
        if self.cantidad_balas < 1:
            raise ValidationError({'cantidad_balas': 'La cantidad de balas no puede ser menor a 1'})

            
        
    vaquero = models.ForeignKey('vaquero', on_delete=models.CASCADE, null=True, blank=True, related_name='armas')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_arma})"

class vaquero(models.Model):
    SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino')]
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField(default=0)
    buscado = models.BooleanField(default=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def clean(self):
        super().clean()
        # Validar nombre
        nombre_limpio = self.nombre.strip()  # Eliminar espacios en blanco al inicio y al final
        if not nombre_limpio:
            raise ValidationError({'nombre': 'Tienes que ingresar el nombre'})
        if len(nombre_limpio) < 2 or len(nombre_limpio) > 25:
            raise ValidationError({'nombre': 'El nombre debe tener entre 2 y 25 caracteres'})
        if not nombre_limpio.isalpha():
            raise ValidationError({'nombre': 'El nombre solo puede contener letras y sin espacios'})
        if not nombre_limpio[0].isupper():
            raise ValidationError({'nombre': 'El nombre debe comenzar con una letra mayuscula'})
        # Validar apellido
        apellido_limpio = self.apellido.strip()  # Eliminar espacios en blanco al inicio y al final
        if not apellido_limpio:
            raise ValidationError({'apellido': 'Tienes que ingresar el apellido'})
        if len(apellido_limpio) < 2 or len(apellido_limpio) > 25:
            raise ValidationError({'apellido': 'El apellido debe tener entre 2 y 25 caracteres'})
        if not apellido_limpio.isalpha():
            raise ValidationError({'apellido': 'El apellido solo puede contener letras y sin espacios'})
        if not apellido_limpio[0].isupper():
            raise ValidationError({'apellido': 'El apellido debe comenzar con una letra mayuscula'})
        # Validar edad
        if self.edad == 0:
            raise ValidationError({'edad': 'No puede tener 0 años, La edad debe estar entre 1 y 120 años'})
        if not self.edad:
            raise ValidationError({'edad': 'Tienes que ingresar la edad'})
        if self.edad < 0:
            raise ValidationError({'edad': 'No se permiten negativos ,La edad debe estar entre 1 y 120 años'})
        if self.edad > 120:
            raise ValidationError({'edad': 'La edad debe estar entre 1 y 120 años'})
        # Validar sexo
        if self.sexo not in ['M', 'F']:
            raise ValidationError({'sexo': 'Selecciona uno de los sexos'})
        if vaquero.objects.filter(
            nombre=self.nombre,
            apellido=self.apellido,
            edad=self.edad,
            sexo=self.sexo).exclude(id=self.id).exists():
            raise ValidationError({'nombre':'Ya existe un vaquero con el mismo nombre, apellido, edad y sexo.'})
        

        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    # Relación muchos a muchos entre vaquero y caballos/armas
    caballo = models.ManyToManyField('caballo', blank=True, related_name='vaqueros')
    arma = models.ManyToManyField('arma', blank=True, related_name='vaqueros')
    def __str__(self):
        return f"{self.nombre} {self.apellido}"