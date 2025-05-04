from django.shortcuts import render, redirect
from django import forms

from .models import StrengthExercise, StrengthExerciseEvent
from .models import CardioExercise, CardioExerciseEvent
from .models import FlexibilityExercise, FlexibilityExerciseEvent

from datetime import datetime



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
    date = datetime.now()

    if request.method == 'POST':
        strength_form = StrengthForm(request.POST)
        if strength_form.is_valid():
            user = request.user
            exercise = strength_form.cleaned_data['exercise']
            weight = strength_form.cleaned_data['weight']
            reps = strength_form.cleaned_data['reps']
            sets = strength_form.cleaned_data['sets']

            strength_exercise_id = StrengthExercise.objects.filter(name=exercise).first()
            if strength_exercise_id:
                for _ in range(sets):
                    strength_exercise_event = StrengthExerciseEvent(user=user, exercise=strength_exercise_id, date=date, weight=weight, reps=reps)
                    strength_exercise_event.save()
            else:
                context['post_error'] = 'invalid exercise'
        else:
            print('unhandled error')

        return redirect('fitness:strength')


    strength_exercise_names = StrengthExercise.objects.values_list('name', flat=True)
    strength_exercise_events = StrengthExerciseEvent.objects.filter(date=date)

    context['title'] = 'Strength - fsweb'
    context['date'] = date
    context['exercise_names'] = strength_exercise_names
    context['exercise_events'] = strength_exercise_events

    return render(request, 'fitness/strength.html', context)



def view_cardio(request):
    context = {}
    date = datetime.now()

    if request.method == 'POST':
        cardio_form = CardioForm(request.POST)
        if cardio_form.is_valid():
            user = request.user
            exercise = cardio_form.cleaned_data['exercise']
            duration = cardio_form.cleaned_data['duration']

            exercise_id = CardioExercise.objects.filter(name=exercise).first()
            if exercise_id:
                event = CardioExerciseEvent(date=date, user=user, exercise=exercise_id, duration=duration)
                event.save()
            else:
                context['post_error'] = 'invalid exercise'
        else:
            print('unhandled error')

        return redirect('fitness:cardio')


    cardio_exercise_names = CardioExercise.objects.values_list('name', flat=True)
    cardio_exercise_events = CardioExerciseEvent.objects.filter(date=date)

    context['title'] = 'Cardio - fsweb'
    context['date'] = date
    context['exercise_names'] = cardio_exercise_names
    context['exercise_events'] = cardio_exercise_events

    return render(request, 'fitness/cardio.html', context)



def view_flexibility(request):
    context = {}
    date = datetime.now()

    if request.method == 'POST':
        flexibility_form = FlexibilityForm(request.POST)
        if flexibility_form.is_valid():
            user = request.user
            exercise = flexibility_form.cleaned_data['exercise']
            duration = flexibility_form.cleaned_data['duration']
            exercise_id = FlexibilityExercise.objects.filter(name=exercise).first()

            if exercise_id:
                event = FlexibilityExerciseEvent(date=date, user=user, exercise=exercise_id, duration=duration)
                event.save()
            else:
                context['post_error'] = 'invalid exercise'
        else:
            print('unhandled error')

        return redirect('fitness:flexibility')


    flexibility_exercise_names = FlexibilityExercise.objects.values_list('name', flat=True)
    flexibility_exercise_events = FlexibilityExerciseEvent.objects.filter(date=date)

    context['title'] = 'Flexibility - fsweb'
    context['date'] = date
    context['exercise_names'] = flexibility_exercise_names
    context['exercise_events'] = flexibility_exercise_events

    return render(request, 'fitness/flexibility.html', context)

