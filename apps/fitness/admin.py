from django.contrib import admin

from .models import StrengthExercise
from .models import StrengthExerciseEvent

admin.site.register(StrengthExercise)
admin.site.register(StrengthExerciseEvent)
