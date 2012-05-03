from django import forms
from django.conf import settings

from registration.forms import RegistrationForm as RegistrationForm_orig
from models import UserProfile

class RegistrationForm(RegistrationForm_orig):
    gender = forms.ChoiceField(choices=(settings.GENDER_CHOICES), 
        label='Geschlecht', widget=forms.RadioSelect)
    birthday = forms.DateField()
    
class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # exclude = ('user')
    
        

        
        
