from django import forms

class AddTrainingForm(forms.Form):
    name = forms.DateField()
    name2 = forms.CharField()
        
class AddTrainingSchemaForm(forms.Form):
    name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(AddTrainingSchemaForm, self).__init__(*args, **kwargs)