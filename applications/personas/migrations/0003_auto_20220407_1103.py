# Generated by Django 3.2.12 on 2022-04-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20220407_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='skill',
            field=models.ManyToManyField(to='personas.Habilidades'),
        ),
    ]
