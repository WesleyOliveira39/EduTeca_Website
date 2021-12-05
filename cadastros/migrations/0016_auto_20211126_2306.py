# Generated by Django 2.2.12 on 2021-11-27 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0015_auto_20211126_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='edicao',
            field=models.PositiveIntegerField(default=0, verbose_name='Edição'),
        ),
    ]
