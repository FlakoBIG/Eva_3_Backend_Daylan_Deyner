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
    
    # Relación OneToOne con vaquero, y si el vaquero se elimina, también se elimina el caballo
    vaquero = models.ForeignKey('vaquero', on_delete=models.CASCADE, null=True, blank=True, related_name='caballos')

    def clean(self):
        if self.vaquero:
            # Verificamos que el vaquero no tenga otro caballo asignado
            existing_caballo = caballo.objects.filter(vaquero=self.vaquero).exclude(id=self.id).first()
            if existing_caballo:
                raise ValidationError({'vaquero': f'Este vaquero ya tiene asignado el caballo: {existing_caballo.nombre}'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.raza})"

class arma(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_balas = models.IntegerField(default=20, help_text="El número no debe ser menor a 20 balas")
    
    TipoBala = [
        ('9mm', '9mm'),
        ('calibre_45', 'calibre .45'),
        ('calibre_50', 'calibre .50'),
    ]
    tipo_bala = models.CharField(max_length=50, choices=TipoBala)
    
    TipoArma = [
        ('largo_alcanse', 'Largo Alcance'),
        ('medio_alcanse', 'Mediano Alcance'),
        ('bajo_alcanse', 'Bajo Alcance'),
    ]
    tipo_arma = models.CharField(max_length=50, choices=TipoArma)
    
    TipoCadencia = [
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
    ]
    cadencia = models.CharField(max_length=50, choices=TipoCadencia)

    # Relación OneToOne con vaquero, y si el vaquero se elimina, también se elimina el arma
    vaquero = models.ForeignKey('vaquero', on_delete=models.CASCADE, null=True, blank=True, related_name='armas')

    def clean(self):
        if self.vaquero:
            # Verificamos que el vaquero no tenga otra arma asignada
            existing_arma = arma.objects.filter(vaquero=self.vaquero).exclude(id=self.id).first()
            if existing_arma:
                raise ValidationError({'vaquero': f'Este vaquero ya tiene asignada el arma: {existing_arma.nombre}'})

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

    # Relación muchos a muchos entre vaquero y caballos/armas
    caballo = models.ManyToManyField('caballo', blank=True, related_name='vaqueros')
    arma = models.ManyToManyField('arma', blank=True, related_name='vaqueros')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"