from django.http import HttpResponse
from django.shortcuts import render
from django import forms

class WorkoutForm(forms.Form):
    exercise = forms.CharField(max_length=100)
    weight = forms.DecimalField(max_value=1000, decimal_places=2)
    reps = forms.IntegerField(max_value=10000)

workouts = []

def index(request):
    if request.method == "POST":
        validated_workout = None
        posted_form = WorkoutForm(request.POST)
        if posted_form.is_valid():
            exercise = posted_form.cleaned_data['exercise']
            weight = posted_form.cleaned_data['weight']
            reps = posted_form.cleaned_data['reps']
            validated_workout = {'exercise': exercise, 'weight': weight, 'reps': reps}
            workouts.append(validated_workout)

    context = {'workouts': workouts}
    return render(request, 'fitness-tracker/index.html', context)
