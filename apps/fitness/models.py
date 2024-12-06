from django.db import models

class StrengthExercise(models.Model):
    name = models.CharField(max_length = 48)

    def __str__(self):
        return self.name


class StrengthExerciseEvent(models.Model):
    strength_exercise = models.ForeignKey(StrengthExercise, on_delete=models.CASCADE)
    date = models.DateField()
    set_count = models.PositiveSmallIntegerField()
    reps_per_set = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.date.strftime("%Y-%m-%d") + ", " + str(self.id) + ", " + self.strength_exercise.name


class FlexibilityExercise(models.Model):
    name = models.CharField(max_length = 48)

    def __str__(self):
        return self.name


class FlexibilityExerciseEvent(models.Model):
    flexibility_exercise = models.ForeignKey(FlexibilityExercise, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()

    def __str__(self):
        return self.date.strftime("%Y-%m-%d") + ", " + str(self.id) + ", " + self.flexibility_exercise.name
