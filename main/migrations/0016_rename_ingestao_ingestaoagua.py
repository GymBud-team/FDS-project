# Generated by Django 4.1.1 on 2022-10-15 20:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0015_delete_ingestaocalorias'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingestao',
            new_name='IngestaoAgua',
        ),
    ]
