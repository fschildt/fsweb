from django.db import models
from django.contrib.auth import settings


class Muscle(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "muscles"

    def __str__(self):
        return self.name


class StrengthExercise(models.Model):
    name = models.CharField(max_length=64)
    muscles_worked = models.ManyToManyField('Muscle', through='StrengthExerciseNxNMuscle')

    class Meta:
        db_table = "strength_exercises"

    def __str__(self):
        return self.name


class StrengthExerciseNxNMuscle(models.Model):
    exercise = models.ForeignKey('StrengthExercise', on_delete=models.CASCADE)
    muscle = models.ForeignKey('Muscle', on_delete=models.CASCADE)

    class Meta:
        db_table = "strength_exercises_nxn_muscles"

    def __str__(self):
        return f"{self.exercise}, {self.muscle}"


class StrengthExerciseEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('StrengthExercise', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    class Meta:
        db_table = "strength_exercise_events"

    def __str__(self):
        return f"{self.date}, {self.exercise}, {self.weight}, {self.reps}"

