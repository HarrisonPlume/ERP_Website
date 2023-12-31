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
    day_list.append(today.strftime("%d/%m/%y")+str(" Today"))
    for i in range(1,7):
        newdate = today + dt.timedelta(i)
        day_list.append(newdate.strftime("%d/%m/%y"))

    day_dict = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    index = day_dict[dayname]
    len_left = 6-index
    Ordered_list = [0,0,0,0,0,0,0]
    counter = 0
    for i in range(index, index+len_left+1):
        Ordered_list[i] = day_list[counter]
        counter += 1
    counter = 0
    for k in range(-1*index,0):
        Ordered_list[counter] = day_list[k]
        counter += 1
        
    context = {"formset":formset,
               "Monday": Ordered_list[0],
               "Tuesday": Ordered_list[1],
               "Wednesday": Ordered_list[2],
               "Thursday": Ordered_list[3],     
               "Friday": Ordered_list[4],
               "Saturday": Ordered_list[5],
               "Sunday": Ordered_list[6],  
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
    day_list.append(today.strftime("%d/%m/%y")+str(" Today"))
    for i in range(1,7):
        newdate = today + dt.timedelta(i)
        day_list.append(newdate.strftime("%d/%m/%y"))

    day_dict = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    index = day_dict[dayname]
    len_left = 6-index
    Ordered_list = [0,0,0,0,0,0,0]
    counter = 0
    for i in range(index, index+len_left+1):
        Ordered_list[i] = day_list[counter]
        counter += 1
    counter = 0
    for k in range(-1*index,0):
        Ordered_list[counter] = day_list[k]
        counter += 1

    context = {"queryset":queryset,
               "Monday": Ordered_list[0],
               "Tuesday": Ordered_list[1],
               "Wednesday": Ordered_list[2],
               "Thursday": Ordered_list[3],     
               "Friday": Ordered_list[4],
               "Saturday": Ordered_list[5],
               "Sunday": Ordered_list[6],  
               }

    return render(request, "class_table.html", context = context)