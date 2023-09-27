from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Gym_class, Timetable
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
import datetime as dt

# Create your views here.

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

class Gym_ClassListView(generic.ListView):
    model = Gym_class
    context_object_name = "gym_class_list"
    template_name = "gym_class_list.html"

class Gym_timetable(generic.DetailView):
    model = Timetable
    context_object_name = "gym_timetable"
    template_name ="class_table.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data()
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

        context["Monday"] = Ordered_list[0]
        context["Tuesday"] = Ordered_list[1]
        context["Wednesday"] = Ordered_list[2]
        context["Thursday"] = Ordered_list[3]
        context["Friday"] = Ordered_list[4]
        context["Saturday"] = Ordered_list[5]
        context["Sunday"] = Ordered_list[6]
        return context
    
class timetable_update(LoginRequiredMixin, UpdateView):
    model = Timetable
    fields = '__all__'
    success_url = reverse_lazy("classlist", args=[str(1)])