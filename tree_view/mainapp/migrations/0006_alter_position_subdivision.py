# Generated by Django 5.0.7 on 2024-08-05 04:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_position_subdivision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='subdivision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='mainapp.subdivision'),
        ),
    ]
