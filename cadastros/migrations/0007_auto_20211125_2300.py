# Generated by Django 2.2.12 on 2021-11-26 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_auto_20211125_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='autorL',
            new_name='autor',
        ),
    ]
