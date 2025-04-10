from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.template import loader

from datetime import datetime

from .models import StrengthExerciseEvent
from .models import StrengthExercise


class WorkoutForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    weight = forms.DecimalField(max_value=1000, decimal_places=2)
    reps = forms.IntegerField(max_value=10000)

def hangboard_timer(request):
    template = loader.get_template('fitness/hangboard-timer.html')
    return HttpResponse(template.render())

def index(request):
    post_error = None

    exercise_names = StrengthExercise.objects.values_list('name', flat=True)

    if request.method == "POST":
        posted_form = WorkoutForm(request.POST)
        if posted_form.is_valid():
            user = request.user
            date = datetime.now()
            exercise = posted_form.cleaned_data['exercise']
            weight = posted_form.cleaned_data['weight']
            reps = posted_form.cleaned_data['reps']

            strength_exercise_id = StrengthExercise.objects.filter(name=exercise).first()
            if strength_exercise_id:
                strength_exercise_event = StrengthExerciseEvent(user=user, exercise=strength_exercise_id, date=datetime.now(), weight=weight, reps=reps)
                strength_exercise_event.save()
            else:
                post_error = 'invalid exercise'


    strength_exercise_events = StrengthExerciseEvent.objects.all()

    context = {'workouts': strength_exercise_events, 'post_error': post_error, 'exercise_names': exercise_names}
    return render(request, 'fitness/index.html', context)
