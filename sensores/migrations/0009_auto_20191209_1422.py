# Generated by Django 2.2.8 on 2019-12-09 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0008_auto_20191209_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportes',
            name='fecha_reporte',
        ),
        migrations.RemoveField(
            model_name='reportes',
            name='hora_reporte',
        ),
    ]
