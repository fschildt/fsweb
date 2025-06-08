from django.contrib import admin

from .models import StrengthExercise
from .models import StrengthEvent

from .models import FlexibilityExercise
from .models import FlexibilityEvent

from .models import CardioExercise
from .models import CardioEvent

from .models import BrainExercise
from .models import BrainEvent


admin.site.register(StrengthExercise)
admin.site.register(StrengthEvent)

admin.site.register(FlexibilityExercise)
admin.site.register(FlexibilityEvent)

admin.site.register(CardioExercise)
admin.site.register(CardioEvent)

admin.site.register(BrainExercise)
admin.site.register(BrainEvent)
