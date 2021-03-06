# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anunciante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('P', 'Publicidad'), ('C', 'Contenido')], default='P', max_length=1)),
                ('migracion', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha', models.DateField(db_index=True, default='1900-01-01')),
                ('hora', models.TimeField(default='00:00')),
                ('orden', models.IntegerField(blank=True, default=0, null=True, verbose_name='Numero de Pagina')),
                ('duracion', models.IntegerField(blank=True, default=0, null=True)),
                ('valor', models.IntegerField(default=0, verbose_name='Tarifa')),
                ('origen', models.CharField(blank=True, db_index=True, max_length=200)),
                ('titulo', models.CharField(blank=True, max_length=255, verbose_name='Titulo')),
                ('observaciones', models.CharField(blank=True, max_length=500, null=True)),
                ('usuario', models.IntegerField(blank=True, default=0, null=True)),
                ('horario', models.IntegerField(blank=True, default=0, null=True)),
                ('archivo', models.CharField(blank=True, max_length=200, null=True)),
                ('codigo_directv', models.CharField(blank=True, max_length=30, null=True)),
                ('confirmado', models.BooleanField(default=True)),
                ('anunciantes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soap.Anunciante')),
            ],
        ),
        migrations.CreateModel(
            name='Origen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('P', 'Publicidad'), ('C', 'Contenido'), ('F', 'Fuente')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPublicidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('es_publicidad', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Tipo de publicidad',
            },
        ),
        migrations.AddField(
            model_name='emision',
            name='fuente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soap.Origen'),
        ),
        migrations.AddField(
            model_name='emision',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soap.Producto'),
        ),
        migrations.AddField(
            model_name='emision',
            name='tipo_publicidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soap.TipoPublicidad'),
        ),
    ]
