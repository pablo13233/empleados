# Generated by Django 3.2.12 on 2022-04-09 16:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]