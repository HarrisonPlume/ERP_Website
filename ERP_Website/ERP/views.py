from typing import Any
from django.shortcuts import render, redirect
from django.views import generic
from .models import Gym_class, Timetable, timetable_class_instance, UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.forms import modelformset_factory
from .forms import TimetableUpdateForm
import datetime as dt
import os

# Create your views here.

# Check to see if user is a staff member
class StaffUserRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return user_passes_test(lambda u: u.is_staff)(view)
    
def is_staff_user(user):
    return user.is_staff

def index(request):
    """View for the home page of the website"""
    
    #Generate counts for soe of the main objetcs
    
    #Number of site visits by the current user    
    context = {
        }
    
    #Render the HTML template index.html with the data in the context vairable
    return render(request, "index.html", context = context)

class Class_detail(generic.DetailView):
    model = Gym_class
    template_name ="gym_class_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.object.pk  # Pass the PK to the template
        return context

class Gym_ClassListView(generic.ListView):
    model = Gym_class
    context_object_name = "gym_class_list"
    template_name = "gym_class_list.html"
    paginate_by = 50

class Create_Gym_Class(StaffUserRequiredMixin, generic.CreateView):
    model = Gym_class
    template_name = "create_gymclass_form.html"
    fields = "__all__"

class Update_Gym_Class(StaffUserRequiredMixin, generic.UpdateView):
    model =Gym_class
    template_name = "update_gymclass_form.html"
    fields = "__all__"

class Delete_Gym_Class(StaffUserRequiredMixin, generic.DeleteView):
    model =Gym_class
    template_name = "delete_gym_class_form.html"
    context_object_name = 'object'
    success_url = reverse_lazy("gym_classes")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_foreign_key_references'] = self.object.has_foreign_key_references()
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.has_foreign_key_references():
            # If there are references, display a message instead of the delete button
            return self.render_to_response(self.get_context_data())
        return super().get(request, *args, **kwargs)

class Timetable_Class_detail(generic.DetailView):
    model = timetable_class_instance
    context_object_name = "timetable_class"
    template_name="timetable_class_detail.html"


class User_Profile_detail(generic.DetailView):
    model = UserProfile
    template_name = "user_profile_detail.html"
    context_object_name = "user_profile"

class User_Profile_List(StaffUserRequiredMixin, generic.ListView):
    model = UserProfile
    context_object_name = "user_profile_list"
    template_name = "user_profile_list.html"
    paginate_by = 50

    

timetableFormSet = modelformset_factory(timetable_class_instance, form=TimetableUpdateForm, extra=0)

@login_required
def Update_TimeTable(request):
    queryset = timetable_class_instance.objects.all().order_by('time_slot', 'day')
    formset = timetableFormSet(queryset=queryset)

    if request.method == "POST":
        formset = timetableFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("timetable")
        
    today = dt.date.today()
    dayname = today.strftime('%A')
    day_list = []
    day_list.append(dayname+" "+today.strftime("%d/%m/%y"))
    for i in range(1,7):
        newdate = today + dt.timedelta(i)
        day_list.append(str(newdate.strftime('%A'))+" "+newdate.strftime("%d/%m/%y"))

    times = []
    for i in range(5,18):
        if i < 12:
            times.append(str(i)+"am")
        else:
            times.append(str(i)+"pm")

    context = {
            "formset":formset,
            "Day0": day_list[0],
            "Day1": day_list[1],
            "Day2": day_list[2],
            "Day3": day_list[3],     
            "Day4": day_list[4],
            "Day5": day_list[5],
            "Day6": day_list[6], 
            "time_list": times, 
            }

    return render(request, "timetable_update_form.html", context=context)


class timetable_class_instace_update(StaffUserRequiredMixin, generic.UpdateView):
    model = timetable_class_instance
    fields = "__all__"
    template_name= "update_timetable_class.html"
    success_url = reverse_lazy('timetable')


def Show_Timetable(request):
    queryset = Timetable.objects.first()
    
    today = dt.date.today()
    dayname = today.strftime('%A')
    day_list = []
    day_list.append(dayname+" "+today.strftime("%d/%m/%y"))
    for i in range(1,7):
        newdate = today + dt.timedelta(i)
        day_list.append(str(newdate.strftime('%A'))+" "+newdate.strftime("%d/%m/%y"))

    times = []
    for i in range(5,19):
            times.append(str(i))

    day_funcs = []

    for i in range(7):
        newdate = today + dt.timedelta(i)
        dayname = newdate.strftime('%A')
        if dayname != "Thursday":
            dayname = dayname[:3].lower()
        else:
            dayname = dayname[:4].lower()
        day_funcs.append(dayname)
    today_code = day_funcs[0]

    context = {
            "queryset":queryset,
            "Day0": day_list[0],
            "Day1": day_list[1],
            "Day2": day_list[2],
            "Day3": day_list[3],     
            "Day4": day_list[4],
            "Day5": day_list[5],
            "Day6": day_list[6], 
            "times": times,
            "day_funcs": day_funcs, 
            "today_code":today_code,
            }

    return render(request, "class_table.html", context = context)