# Generated by Django 5.0.2 on 2024-04-13 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sortear', '0002_categoriasorteo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriasorteo',
            old_name='sorteo',
            new_name='sorteos',
        ),
    ]
