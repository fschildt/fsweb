from django.contrib import admin

from .models import StrengthExercise
from .models import StrengthExerciseEvent

from .models import FlexibilityExercise
from .models import FlexibilityExerciseEvent

from .models import CardioExercise
from .models import CardioExerciseEvent

from .models import BrainMaterial
from .models import BrainEvent


admin.site.register(StrengthExercise)
admin.site.register(StrengthExerciseEvent)

admin.site.register(FlexibilityExercise)
admin.site.register(FlexibilityExerciseEvent)

admin.site.register(CardioExercise)
admin.site.register(CardioExerciseEvent)

admin.site.register(BrainMaterial)
admin.site.register(BrainEvent)
