# Generated by Django 2.2.7 on 2019-12-09 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0005_auto_20191204_2351'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acciones',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]