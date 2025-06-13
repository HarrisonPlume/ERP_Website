from django import forms
from .models import timetable_class_instance, UserProfile

class TimetableUpdateForm(forms.ModelForm):
    class Meta:
        model = timetable_class_instance
        fields = ['gym_class']

class GymMemberUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        