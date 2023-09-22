import datetime
from .models import Gym_class
from django import forms
from django.core.exceptions import ValidationError



class GymClassForm(forms.ModelForm):
    title = forms.CharField(max_length=15, label="Part Number")
    description = forms.TextInput()
    
    class Meta:
        model = Gym_class
        fields = ("title","description")
        
class ArchiveForm(forms.ModelForm):
    archive = forms.BooleanField(required = True,
                                 label = "Archive Class?")
    
    class Meta:
        model = Gym_class
        fields = ("archive",)

class timetableForm(forms.ModelForm):
    mon6 = forms.ChoiceField(label="Monday 6am", choices=Gym_class.objects.all(), required=True)