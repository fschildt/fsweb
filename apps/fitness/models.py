from django.db import models
from django.conf import settings


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



class CardioExercise(models.Model):
    name = models.CharField(max_length=64)
    zone = models.PositiveIntegerField()

    class Meta:
        db_table = "cardio_exercises"

    def __str__(self):
        return f"{self.name}, Zone {self.zone}"


class CardioExerciseEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('CardioExercise', on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()

    class Meta:
        db_table = "cardio_exercise_events"

    def __str__(self):
        return f"{self.date}, {self.user.username}, {self.exercise.name}, {self.duration}"



class FlexibilityExercise(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "flexibility_exercises"

    def __str__(self):
        return self.name


class FlexibilityExerciseEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('FlexibilityExercise', on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()

    class Meta:
        db_table = "flexibility_exercise_events"

    def __str__(self):
        return f"{self.date}, {self.user.username}, {self.exercise.name}, {self.duration}"



class BrainMaterial(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "brain_materials"

    def __str__(self):
        return f"{self.name}"


class BrainEvent(models.Model):
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    material = models.ForeignKey('BrainMaterial', on_delete=models.CASCADE)
    duration = models.DurationField()

    class Meta:
        db_table = "brain_events"

    def __str__(self):
        return f"{self.date}, {self.material}, {self.duration}"


