# Generated by Django 2.2.12 on 2021-11-28 00:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Biblioteca',
            new_name='Perfil',
        ),
    ]
