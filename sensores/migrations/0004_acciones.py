# Generated by Django 2.2.4 on 2019-12-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0003_auto_20191204_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avanzar', models.IntegerField()),
                ('retroceder', models.IntegerField()),
            ],
        ),
    ]
