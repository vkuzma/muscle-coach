from django import forms
from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=80, blank=False)
    medically_name = models.CharField(max_length=120)
    
    def __unicode__(self):
        return self.name
    
class GroupOfMuscle(models.Model):
    name = models.CharField(max_length=80, blank=False)
    
    def __unicode__(self):
        return self.name
    
class Muscle_GroupOfMuscle(models.Model):
    muscle = models.ForeignKey('Muscle')
    group_of_muscle = models.ForeignKey('GroupOfMuscle')
    
    def __unicode__(self):
        return '%s / %s'% (self.muscle, self.group_of_muscle,)

class Exercise_Muscle(models.Model):
    exercise = models.ForeignKey('Exercise')
    muscle = models.ForeignKey('Muscle')
    
    def __unicode__(self):
        return '%s / %s'% (self.exercise, self.muscle,)
    
class Exercise(models.Model):
    name = models.CharField(max_length=80, blank=False)
    level = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
class TrainingSchema(models.Model):
    name = models.CharField(max_length=80)
    
class TrainingSchema_ExerciseSchema(models.Model):
    exercise_schema = models.ForeignKey('ExerciseSchema')
    training_schema = models.ForeignKey('TrainingSchema')

class TrainingSession(models.Model):
    training_schema = models.OneToOneField('TrainingSchema')
    date = models.DateField(auto_now_add=True, blank=False)
    duration = models.IntegerField(help_text='Duration of the training session')
    start_time = models.TimeField()
    comment = models.TextField(max_length=300)
    
    def __unicode__(self):
        return str(self.date)
        
class ExerciseSchema(models.Model):
    exercise = models.ForeignKey('Exercise')
    
class ExerciseSchema_Repetitions(models.Model):
    exercise_schema = models.ForeignKey('ExerciseSchema')
    repetitions = models.ForeignKey('Repetitions')
        
class ExerciseSession(models.Model):
    exercise_schema = models.OneToOneField('ExerciseSchema')
    comment = models.TextField(max_length=200)
    
class ExerciseSession_Repetitions(models.Model):
    exercise_session = models.ForeignKey('ExerciseSession')
    repetitions = models.ForeignKey('Repetitions')
    
class Repetitions(models.Model):
    repetitions = models.IntegerField()
    
    def __unicode__(self):
        return str(self.repetitions)
    
