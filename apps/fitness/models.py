from django.db import models
from django.contrib.auth import settings


class StrengthExercise(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "strength_exercises"

    def __str__(self):
        return self.name


class StrengthExerciseEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('StrengthExercise', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    reps = models.PositiveIntegerField()

    class Meta:
        db_table = "strength_exercise_events"

    def __str__(self):
        return f"{self.date}, {self.user.username}, {self.exercise}, {self.weight}, {self.reps}"

