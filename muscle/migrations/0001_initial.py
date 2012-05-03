# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Muscle'
        db.create_table('muscle_muscle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('medically_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('muscle', ['Muscle'])

        # Adding model 'GroupOfMuscle'
        db.create_table('muscle_groupofmuscle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('muscle', ['GroupOfMuscle'])

        # Adding model 'Muscle_GroupOfMuscle'
        db.create_table('muscle_muscle_groupofmuscle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('muscle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.Muscle'])),
            ('group_of_muscle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.GroupOfMuscle'])),
        ))
        db.send_create_signal('muscle', ['Muscle_GroupOfMuscle'])

        # Adding model 'Exercise_Muscle'
        db.create_table('muscle_exercise_muscle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.Exercise'])),
            ('muscle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.Muscle'])),
        ))
        db.send_create_signal('muscle', ['Exercise_Muscle'])

        # Adding model 'Exercise'
        db.create_table('muscle_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('muscle', ['Exercise'])

        # Adding model 'TrainingSchema'
        db.create_table('muscle_trainingschema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('muscle', ['TrainingSchema'])

        # Adding model 'TrainingSchema_ExerciseSchema'
        db.create_table('muscle_trainingschema_exerciseschema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise_schema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.ExerciseSchema'])),
            ('training_schema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.TrainingSchema'])),
        ))
        db.send_create_signal('muscle', ['TrainingSchema_ExerciseSchema'])

        # Adding model 'TrainingSession'
        db.create_table('muscle_trainingsession', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegistrationProfile'])),
            ('training_schema', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['muscle.TrainingSchema'], unique=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=300)),
        ))
        db.send_create_signal('muscle', ['TrainingSession'])

        # Adding model 'ExerciseSchema'
        db.create_table('muscle_exerciseschema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.Exercise'])),
        ))
        db.send_create_signal('muscle', ['ExerciseSchema'])

        # Adding model 'ExerciseSchema_Repetitions'
        db.create_table('muscle_exerciseschema_repetitions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise_schema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.ExerciseSchema'])),
            ('repetitions', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.Repetitions'])),
        ))
        db.send_create_signal('muscle', ['ExerciseSchema_Repetitions'])

        # Adding model 'ExerciseSession'
        db.create_table('muscle_exercisesession', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise_schema', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['muscle.ExerciseSchema'], unique=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal('muscle', ['ExerciseSession'])

        # Adding model 'ExerciseSession_Repetitions'
        db.create_table('muscle_exercisesession_repetitions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise_session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.ExerciseSession'])),
            ('repetitions', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['muscle.Repetitions'])),
        ))
        db.send_create_signal('muscle', ['ExerciseSession_Repetitions'])

        # Adding model 'Repetitions'
        db.create_table('muscle_repetitions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('repetitions', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('muscle', ['Repetitions'])


    def backwards(self, orm):
        
        # Deleting model 'Muscle'
        db.delete_table('muscle_muscle')

        # Deleting model 'GroupOfMuscle'
        db.delete_table('muscle_groupofmuscle')

        # Deleting model 'Muscle_GroupOfMuscle'
        db.delete_table('muscle_muscle_groupofmuscle')

        # Deleting model 'Exercise_Muscle'
        db.delete_table('muscle_exercise_muscle')

        # Deleting model 'Exercise'
        db.delete_table('muscle_exercise')

        # Deleting model 'TrainingSchema'
        db.delete_table('muscle_trainingschema')

        # Deleting model 'TrainingSchema_ExerciseSchema'
        db.delete_table('muscle_trainingschema_exerciseschema')

        # Deleting model 'TrainingSession'
        db.delete_table('muscle_trainingsession')

        # Deleting model 'ExerciseSchema'
        db.delete_table('muscle_exerciseschema')

        # Deleting model 'ExerciseSchema_Repetitions'
        db.delete_table('muscle_exerciseschema_repetitions')

        # Deleting model 'ExerciseSession'
        db.delete_table('muscle_exercisesession')

        # Deleting model 'ExerciseSession_Repetitions'
        db.delete_table('muscle_exercisesession_repetitions')

        # Deleting model 'Repetitions'
        db.delete_table('muscle_repetitions')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'training_schema': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['muscle.TrainingSchema']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.RegistrationProfile']"})
        },
        'registration.registrationprofile': {
            'Meta': {'object_name': 'RegistrationProfile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['muscle']
