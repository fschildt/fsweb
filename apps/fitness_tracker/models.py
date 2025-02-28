from django.db import models


class Muscle(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class StrengthExercise(models.Model):
    name = models.CharField(max_length=64)
    muscles_worked = models.ManyToManyField('Muscle', through='StrengthExerciseNxNMuscle')

    def __str__(self):
        return self.name


class StrengthExerciseNxNMuscle(models.Model):
    exercise = models.ForeignKey(StrengthExercise, on_delete=models.CASCADE)
    muscle = models.ForeignKey(Muscle, on_delete=models.CASCADE)


class StrengthWorkout(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Workout on {self.date}"


class StrengthExerciseWorkout(models.Model):
    workout = models.ForeignKey(StrengthWorkout, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(StrengthExercise, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    def __str__(self):
        return f"workout = {self.workout}, exercise = {self.exercise.name}, weight = {self.weight}, reps = {self.repetitions}"




