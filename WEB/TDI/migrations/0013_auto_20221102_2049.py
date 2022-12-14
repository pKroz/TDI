# Generated by Django 3.0.7 on 2022-11-03 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TDI', '0012_auto_20221102_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5000)),
                ('dni', models.CharField(blank=True, max_length=5000, null=True)),
                ('nombres', models.CharField(max_length=5000)),
                ('apellidos', models.CharField(max_length=5000)),
                ('correo', models.CharField(blank=True, max_length=5000, null=True)),
                ('celular', models.CharField(blank=True, max_length=5000, null=True)),
                ('certificado', models.CharField(max_length=5000)),
                ('temaPropuesto', models.CharField(max_length=5000)),
            ],
        ),
    ]
