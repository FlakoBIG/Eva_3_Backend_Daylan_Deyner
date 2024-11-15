# Generated by Django 3.2 on 2024-11-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='cadencia',
            field=models.CharField(choices=[('alto', 'Alto'), ('medio', 'Medio'), ('bajo', 'Bajo'), ('arma_blanca', 'Arma Blanca')], max_length=50),
        ),
        migrations.AlterField(
            model_name='arma',
            name='cantidad_balas',
            field=models.IntegerField(default=1, help_text='El numero no debe ser menor a 1 balas'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='tipo_arma',
            field=models.CharField(choices=[('largo_alcanse', 'Largo Alcance'), ('medio_alcanse', 'Mediano Alcance'), ('bajo_alcanse', 'Bajo Alcance'), ('cuerpo_a_cuerpo', 'Cuerpo a Cuerpo')], max_length=50),
        ),
        migrations.AlterField(
            model_name='arma',
            name='tipo_bala',
            field=models.CharField(choices=[('9mm', '9mm'), ('calibre_45', 'calibre .45'), ('calibre_50', 'calibre .50'), ('arma_blanca', 'Arma Blanca')], max_length=50),
        ),
    ]