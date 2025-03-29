from django.contrib import admin

from .models import Muscle
from .models import StrengthExercise
from .models import StrengthExerciseNxNMuscle
from .models import StrengthExerciseEvent

admin.site.register(Muscle)
admin.site.register(StrengthExercise)
admin.site.register(StrengthExerciseNxNMuscle)
admin.site.register(StrengthExerciseEvent)
