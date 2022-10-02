# Generated by Django 4.1.1 on 2022-09-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_ingestao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicas',
            name='idade',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingestao',
            name='agua',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='metas',
            name='calorias',
            field=models.PositiveIntegerField(default=0),
        ),
    ]