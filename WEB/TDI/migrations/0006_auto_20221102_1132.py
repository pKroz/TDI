# Generated by Django 3.0.7 on 2022-11-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TDI', '0005_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='anio',
            field=models.CharField(default='año', max_length=4),
        ),
        migrations.AddField(
            model_name='pagos',
            name='dia',
            field=models.CharField(default='dia', max_length=4),
        ),
        migrations.AddField(
            model_name='pagos',
            name='mes',
            field=models.CharField(default='mes', max_length=4),
        ),
    ]
