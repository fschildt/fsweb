from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.template import loader

from datetime import datetime

from .models import StrengthExerciseEvent
from .models import StrengthExercise


class WorkoutForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    weight = forms.DecimalField(max_value=1000, decimal_places=2)
    reps = forms.IntegerField(max_value=10000)
    sets = forms.IntegerField(max_value=10000)


def hangboard_timer(request):
    template = loader.get_template('fitness/hangboard-timer.html')
    return HttpResponse(template.render())


def index(request):
    if request.method == "POST":
        posted_form = WorkoutForm(request.POST)
        if posted_form.is_valid():
            user = request.user
            date = datetime.now()
            exercise = posted_form.cleaned_data['exercise']
            weight = posted_form.cleaned_data['weight']
            reps = posted_form.cleaned_data['reps']
            sets = posted_form.cleaned_data['sets']

            strength_exercise_id = StrengthExercise.objects.filter(name=exercise).first()
            if strength_exercise_id:
                for i in range(sets):
                    strength_exercise_event = StrengthExerciseEvent(user=user, exercise=strength_exercise_id, date=datetime.now(), weight=weight, reps=reps)
                    strength_exercise_event.save()
            else:
                context['post_error'] = 'invalid exercise'

        return redirect('fitness:index')


    exercise_names = StrengthExercise.objects.values_list('name', flat=True)
    strength_exercise_events = StrengthExerciseEvent.objects.all()
    context = {'exercise_names': exercise_names, 'workouts': strength_exercise_events}

    return render(request, 'fitness/index.html', context)

