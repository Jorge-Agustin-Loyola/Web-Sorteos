# Generated by Django 5.0.4 on 2024-04-15 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortear', '0008_alter_categoriapremio_options_premiosorteo_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiosorteo',
            name='nombre',
            field=models.CharField(default='premio', max_length=50),
        ),
    ]
