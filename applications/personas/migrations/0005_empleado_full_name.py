# Generated by Django 3.2.12 on 2022-04-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombress Completos'),
        ),
    ]