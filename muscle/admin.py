from django.contrib import admin
from models import *
class Muscle_GroupOfMuscleInline(admin.StackedInline):
    model = Muscle_GroupOfMuscle
    extra = 1

class Exercise_MuscleInline(admin.StackedInline):
    model = Exercise_Muscle
    
class ExerciseSession_RepetitionsInline(admin.StackedInline):
    model = ExerciseSession_Repetitions

class MuscleAdmin(admin.ModelAdmin):
    list_display = ('name', 'medically_name')
    inlines = [Muscle_GroupOfMuscleInline,]

class GroupOfMuscleAdmin(admin.ModelAdmin):
    inlines = [Muscle_GroupOfMuscleInline,]
    
class ExerciseAdmin(admin.ModelAdmin):
    inlines = [Exercise_MuscleInline,]
    
class ExerciseSessionAdmin(admin.ModelAdmin):
    inlines = [ExerciseSession_RepetitionsInline,]
    
    
class TrainingSchema_ExerciseSchemaInline(admin.StackedInline):
    model = TrainingSchema_ExerciseSchema
class TrainingSchemaAdmin(admin.ModelAdmin):
    inlines = [TrainingSchema_ExerciseSchemaInline]
    
admin.site.register(Muscle, MuscleAdmin)
admin.site.register(GroupOfMuscle, GroupOfMuscleAdmin)
admin.site.register(TrainingSession)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseSession, ExerciseSessionAdmin)
admin.site.register(Repetitions)
admin.site.register(ExerciseSchema)
admin.site.register(TrainingSchema, TrainingSchemaAdmin)