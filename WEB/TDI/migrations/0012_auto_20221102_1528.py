# Generated by Django 3.0.7 on 2022-11-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TDI', '0011_auto_20221102_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='dictar_curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=5000)),
                ('apellidos', models.CharField(max_length=5000)),
                ('correo', models.CharField(max_length=5000)),
                ('celular', models.CharField(max_length=5000)),
                ('area', models.CharField(max_length=5000)),
                ('otro', models.CharField(max_length=5000)),
                ('cv', models.CharField(max_length=5000)),
                ('dia', models.CharField(max_length=4)),
                ('mes', models.CharField(max_length=4)),
                ('anio', models.CharField(max_length=4)),
            ],
        ),
    ]
