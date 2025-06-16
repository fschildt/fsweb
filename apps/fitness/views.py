from django.shortcuts import render, redirect, get_object_or_404
from django import forms

from .models import StrengthExercise, StrengthEvent
from .models import CardioExercise, CardioEvent
from .models import FlexibilityExercise, FlexibilityEvent
from .models import BrainExercise, BrainEvent

from datetime import datetime



class StrengthForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    weight = forms.DecimalField(max_value=1000, decimal_places=2)
    reps = forms.IntegerField(max_value=10000)
    sets = forms.IntegerField(max_value=10000)


class CardioForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    duration = forms.DurationField()
    distance = forms.DecimalField(max_value=10000, decimal_places=2)


class FlexibilityForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    duration = forms.DurationField()


class BrainForm(forms.Form):
    exercise = forms.CharField(max_length=64)
    duration = forms.DurationField()



def view_index(request):
    context = {}
    return render(request, 'fitness/index.html', context)


def view_strength(request):
    context = {}
    date = datetime.now()

    strength_events = StrengthEvent.objects.all().order_by('-date', '-id')

    context['title'] = 'Add Strength - fsweb'
    context['date'] = date
    context['strength_events'] = strength_events

    print('viewing strength_edit')
    return render(request, 'fitness/strength.html', context)


def view_strength_add(request):
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
                    strength_exercise_event = StrengthEvent(user=user, exercise=strength_exercise_id, date=date, weight=weight, reps=reps)
                    strength_exercise_event.save()
            else:
                context['post_error'] = 'invalid exercise'
        else:
            print('strength_form is invalid')

        return redirect('fitness:strength')

    strength_exercises = StrengthExercise.objects.values_list('name', flat=True)

    context['title'] = 'Add Strength - fsweb'
    context['date'] = date
    context['strength_exercises'] = strength_exercises

    return render(request, 'fitness/strength_add.html', context)


def view_strength_delete(request, id):
    context = {}
    date = datetime.now()

    event = get_object_or_404(StrengthEvent, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('fitness:strength')
    else:
        # Todo: error message
        return redirect('fitness:strength')


def view_strength_edit(request, id):
    context = {}
    date = datetime.now()
    print('viewing strength_edit')
    return redirect('fitness:strength')


def view_cardio(request):
    context = {}
    date = datetime.now()

    if request.method == 'POST':
        cardio_form = CardioForm(request.POST)
        if cardio_form.is_valid():
            user = request.user
            exercise = cardio_form.cleaned_data['exercise']
            duration = cardio_form.cleaned_data['duration']
            distance = cardio_form.cleaned_data['distance']

            exercise_id = CardioExercise.objects.filter(name=exercise).first()
            if exercise_id:
                event = CardioEvent(date=date, user=user, exercise=exercise_id, duration=duration, distance=distance)
                event.save()
                print('saved')
            else:
                context['post_error'] = 'invalid exercise'
        else:
            print('cardio_form is invalid')

        return redirect('fitness:cardio')


    cardio_exercises = CardioExercise.objects.values_list('name', flat=True)
    cardio_events = CardioEvent.objects.filter(date=date)

    context['title'] = 'Cardio - fsweb'
    context['date'] = date
    context['cardio_exercises'] = cardio_exercises
    context['cardio_events'] = cardio_events

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
                event = FlexibilityEvent(date=date, user=user, exercise=exercise_id, duration=duration)
                event.save()
            else:
                context['post_error'] = 'invalid exercise'
        else:
            print('flexibility_form is invalid')

        return redirect('fitness:flexibility')


    flexibility_exercises = FlexibilityExercise.objects.values_list('name', flat=True)
    flexibility_events = FlexibilityEvent.objects.filter(date=date)

    context['title'] = 'Flexibility - fsweb'
    context['date'] = date
    context['flexibility_exercises'] = flexibility_exercises
    context['flexibility_events'] = flexibility_events

    return render(request, 'fitness/flexibility.html', context)



def view_brain(request):
    date = datetime.now()


    if request.method == 'POST':
        brain_form = BrainForm(request.POST)
        if brain_form.is_valid():
            user = request.user
            exercise = brain_form.cleaned_data['exercise']
            duration = brain_form.cleaned_data['duration']

            exercise_id = BrainExercise.objects.filter(name=exercise).first()
            if exercise_id:
                event = BrainEvent(date=date, user=user, exercise=exercise_id, duration=duration)
                event.save()
            else:
                print('invalid exercise')
        else:
            print('brain_form is invalid')

        return redirect('fitness:brain')


    brain_exercises = BrainExercise.objects.values_list('name', flat=True)
    brain_events = BrainEvent.objects.filter(date=date)

    context = {}
    context['title'] = 'Brain - fsweb'
    context['date'] = date
    context['brain_exercises'] = brain_exercises
    context['brain_events'] = brain_events

    return render(request, 'fitness/brain.html', context)

