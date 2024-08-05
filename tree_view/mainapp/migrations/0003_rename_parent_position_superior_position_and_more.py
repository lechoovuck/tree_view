# Generated by Django 5.0.7 on 2024-08-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_delete_division'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='parent',
            new_name='superior_position',
        ),
        migrations.AlterField(
            model_name='position',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Level 4'), (5, 'Level 5')], verbose_name='Position Level'),
        ),
    ]
