# Generated by Django 2.2.12 on 2021-11-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_auto_20211125_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='arquivo',
            field=models.ImageField(null=True, upload_to='jpg/'),
        ),
    ]