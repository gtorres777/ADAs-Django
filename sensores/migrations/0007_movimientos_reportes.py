# Generated by Django 2.2.7 on 2019-12-09 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sensores', '0006_auto_20191209_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pararse', models.IntegerField()),
                ('sentarse', models.IntegerField()),
                ('avanzar', models.IntegerField()),
                ('retroceder', models.IntegerField()),
                ('girarIzquierda', models.IntegerField()),
                ('girarDerecha', models.IntegerField()),
                ('saludar', models.IntegerField()),
                ('bailar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura_prom', models.DecimalField(decimal_places=2, max_digits=10)),
                ('humedad_prom', models.DecimalField(decimal_places=2, max_digits=10)),
                ('periodo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('ultima_Accion', models.CharField(max_length=45)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]