# Generated by Django 5.0.4 on 2024-05-09 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortear', '0010_rename_imagenpremio_premiosorteo_imagenes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriapremio',
            name='premios',
        ),
        migrations.RemoveField(
            model_name='premiosorteo',
            name='imagenes',
        ),
        migrations.RemoveField(
            model_name='sorteo',
            name='premios',
        ),
        migrations.AddField(
            model_name='imagenpremio',
            name='premio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortear.premiosorteo'),
        ),
        migrations.AddField(
            model_name='premiosorteo',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortear.categoriapremio'),
        ),
        migrations.AddField(
            model_name='premiosorteo',
            name='sorteo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortear.sorteo'),
        ),
    ]
