from django import forms
from .models import timetable_class_instance

class TimetableUpdateForm(forms.ModelForm):
    class Meta:
        model = timetable_class_instance
        fields = ['day', 'time_slot', 'gym_class']