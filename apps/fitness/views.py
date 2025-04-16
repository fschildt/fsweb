from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.template import loader

from datetime import datetime

from .models import StrengthExercise, StrengthExerciseEvent
from .models import CardioExercise, CardioExerciseEvent
from .models import FlexibilityExercise, FlexibilityExerciseEvent


class StrengthForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    weight = forms.DecimalField(max_value=1000, decimal_places=2)
    reps = forms.IntegerField(max_value=10000)
    sets = forms.IntegerField(max_value=10000)


class CardioForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    duration = forms.DurationField()


class FlexibilityForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    duration = forms.DurationField()



def view_index(request):
    context = {}
    return render(request, 'fitness/index.html', context)


def view_strength(request):
    context = {}

    if request.method == "POST":
        posted_form = StrengthForm(request.POST)
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

        return redirect('fitness:strength')


    date = datetime.now()
    exercise_names = StrengthExercise.objects.values_list('name', flat=True)
    strength_exercise_events = StrengthExerciseEvent.objects.filter(date=date)
    context['exercise_names'] = exercise_names
    context['workouts'] = strength_exercise_events
    context['date'] = date

    return render(request, 'fitness/strength.html', context)


def view_cardio(request):
    context = {}

    date = datetime.now()
    context['date'] = date

    return render(request, 'fitness/cardio.html', context)


def view_flexibility(request):
    context = {}

    date = datetime.now()
    context['date'] = date

    return render(request, 'fitness/flexibility.html', context)


def view_hangboard_timer(request):
    return render(request, 'fitness/hangboard-timer.html')


