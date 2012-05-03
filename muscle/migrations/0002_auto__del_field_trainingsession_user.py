# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TrainingSession.user'
        db.delete_column('muscle_trainingsession', 'user_id')

    def backwards(self, orm):
        # Adding field 'TrainingSession.user'
        db.add_column('muscle_trainingsession', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['registration.RegistrationProfile']),
                      keep_default=False)

    models = {
        'muscle.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'muscle.exercise_muscle': {
            'Meta': {'object_name': 'Exercise_Muscle'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'muscle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.Muscle']"})
        },
        'muscle.exerciseschema': {
            'Meta': {'object_name': 'ExerciseSchema'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'muscle.exerciseschema_repetitions': {
            'Meta': {'object_name': 'ExerciseSchema_Repetitions'},
            'exercise_schema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.ExerciseSchema']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repetitions': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.Repetitions']"})
        },
        'muscle.exercisesession': {
            'Meta': {'object_name': 'ExerciseSession'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'exercise_schema': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['muscle.ExerciseSchema']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'muscle.exercisesession_repetitions': {
            'Meta': {'object_name': 'ExerciseSession_Repetitions'},
            'exercise_session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.ExerciseSession']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repetitions': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.Repetitions']"})
        },
        'muscle.groupofmuscle': {
            'Meta': {'object_name': 'GroupOfMuscle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'muscle.muscle': {
            'Meta': {'object_name': 'Muscle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medically_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'muscle.muscle_groupofmuscle': {
            'Meta': {'object_name': 'Muscle_GroupOfMuscle'},
            'group_of_muscle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.GroupOfMuscle']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'muscle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.Muscle']"})
        },
        'muscle.repetitions': {
            'Meta': {'object_name': 'Repetitions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repetitions': ('django.db.models.fields.IntegerField', [], {})
        },
        'muscle.trainingschema': {
            'Meta': {'object_name': 'TrainingSchema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'muscle.trainingschema_exerciseschema': {
            'Meta': {'object_name': 'TrainingSchema_ExerciseSchema'},
            'exercise_schema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.ExerciseSchema']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'training_schema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muscle.TrainingSchema']"})
        },
        'muscle.trainingsession': {
            'Meta': {'object_name': 'TrainingSession'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'training_schema': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['muscle.TrainingSchema']", 'unique': 'True'})
        }
    }

    complete_apps = ['muscle']