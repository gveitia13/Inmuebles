# Generated by Django 4.1.5 on 2023-01-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=250)),
                ('pais', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.CharField(max_length=900)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('web_site', models.URLField(max_length=252)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Inmueble',
        ),
    ]
