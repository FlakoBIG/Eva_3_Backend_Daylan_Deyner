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
    vaquero = models.OneToOneField('vaquero', on_delete=models.CASCADE, null=True, blank=True, related_name='caballo_personal')

    def __str__(self):
        return self.nombre


class arma(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_balas = models.IntegerField(
        default=200,
        help_text="El número no debe ser menor a 200 balas"
    )
    TipoBala = [
        ('9mm', '9mm'),
        ('calibre_45', 'calibre .45'),
        ('calibre_50', 'calibre .50'),
    ]
    tipo_bala = models.CharField(max_length=50, choices=TipoBala)
    TipoArma = [
        ('largo_alcanse', 'Largo Alcance'),
        ('medio_alcanse', 'Mediano Alcance'),
        ('baja_alcanse', 'Bajo Alcance'),
    ]
    tipo_arma = models.CharField(max_length=50, choices=TipoArma)
    TipoCadencia = [
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
    ]
    cadencia = models.CharField(max_length=50, choices=TipoCadencia)
    vaquero = models.OneToOneField('vaquero', on_delete=models.CASCADE, null=True, blank=True, related_name='arma_personal')

    def __str__(self):
        return self.nombre

class vaquero(models.Model):
    SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino')]
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField(default=0)
    buscado = models.BooleanField(default=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"