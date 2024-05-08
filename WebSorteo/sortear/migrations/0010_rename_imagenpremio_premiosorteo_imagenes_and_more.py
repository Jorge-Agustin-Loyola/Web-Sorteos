# Generated by Django 5.0.4 on 2024-04-17 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortear', '0009_alter_premiosorteo_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='premiosorteo',
            old_name='imagenPremio',
            new_name='imagenes',
        ),
        migrations.RemoveField(
            model_name='premiosorteo',
            name='categoriaPremio',
        ),
        migrations.RemoveField(
            model_name='premiosorteo',
            name='sorteo',
        ),
        migrations.AddField(
            model_name='categoriapremio',
            name='premios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortear.premiosorteo'),
        ),
        migrations.AddField(
            model_name='premiosorteo',
            name='descripcion',
            field=models.TextField(default='descripcion', max_length=200),
        ),
        migrations.AddField(
            model_name='sorteo',
            name='premios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortear.premiosorteo'),
        ),
    ]
