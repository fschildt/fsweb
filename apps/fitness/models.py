from django.db import models
from django.conf import settings

from decimal import Decimal


class StrengthExercise(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "strength_exercises"

    def __str__(self):
        return self.name


class StrengthEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('StrengthExercise', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    reps = models.PositiveIntegerField()

    class Meta:
        db_table = "strength_events"

    def __str__(self):
        return f"{self.date}, {self.user.username}, {self.exercise}, {self.weight}, {self.reps}"



class CardioExercise(models.Model):
    name = models.CharField(max_length=64)
    zone = models.PositiveIntegerField()

    class Meta:
        db_table = "cardio_exercises"

    def __str__(self):
        return f"{self.name}, Zone {self.zone}"


class CardioEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('CardioExercise', on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    distance = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        db_table = "cardio_events"


    @property
    def pace(self):
        if self.duration and self.distance > 0:
            duration_seconds = Decimal(str(self.duration.total_seconds()))
            seconds_per_km = duration_seconds / self.distance
            minutes_part = int(seconds_per_km // Decimal('60'))
            seconds_part = int(seconds_per_km % Decimal('60'))
            return f"{minutes_part}:{seconds_part:02d}"
        return "N/A"


    def __str__(self):
        return f"{self.date}, {self.user.username}, {self.exercise.name}, {self.duration}, {self.distance}"



class FlexibilityExercise(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "flexibility_exercises"

    def __str__(self):
        return self.name


class FlexibilityEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('FlexibilityExercise', on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()

    class Meta:
        db_table = "flexibility_events"

    def __str__(self):
        return f"{self.date}, {self.user.username}, {self.exercise.name}, {self.duration}"



class BrainExercise(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "brain_exercises"

    def __str__(self):
        return f"{self.name}"


class BrainEvent(models.Model):
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('BrainExercise', on_delete=models.CASCADE)
    duration = models.DurationField()

    class Meta:
        db_table = "brain_events"


    def __str__(self):
        return f"{self.date}, {self.exercise}, {self.duration}"


