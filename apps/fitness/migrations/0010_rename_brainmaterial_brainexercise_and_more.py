# Generated by Django 5.2.1 on 2025-06-08 08:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0009_alter_cardioexerciseevent_distance'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BrainMaterial',
            new_name='BrainExercise',
        ),
        migrations.RenameModel(
            old_name='CardioExerciseEvent',
            new_name='CardioEvent',
        ),
        migrations.RenameModel(
            old_name='FlexibilityExerciseEvent',
            new_name='FlexibilityEvent',
        ),
        migrations.RenameModel(
            old_name='StrengthExerciseEvent',
            new_name='StrengthEvent',
        ),
        migrations.AlterModelTable(
            name='brainexercise',
            table='brain_exercises',
        ),
        migrations.AlterModelTable(
            name='cardioevent',
            table='cardio_events',
        ),
        migrations.AlterModelTable(
            name='flexibilityevent',
            table='flexibility_events',
        ),
        migrations.AlterModelTable(
            name='strengthevent',
            table='strength_events',
        ),
    ]
