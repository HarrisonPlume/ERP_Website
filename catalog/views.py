from typing import Any
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Gym_class, Member, Timetable
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.template.defaulttags import register
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .tables import Class_Table
from catalog.forms import timetableForm
from django import forms
from django.utils import timezone
import datetime as dt
from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse
from catalog.camera import MaskDetect
import time

def index(request):
    """View for the home page of the website"""
    
    #Generate counts for soe of the main objetcs
    
    #Number of site visits by the current user    
    context = {
        }
    
    #Render the HTML template index.html with the data in the context vairable
    return render(request, "index.html", context = context)
        

class Gym_class(generic.DetailView):
    model = Timetable
    context_object_name = "gym_timetable"
    table_class = Class_Table
    template_name ="class_table.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data()
        today = dt.date.today()
        dayname = today.strftime('%A')
        day_list = []
        day_list.append(today.strftime("%d/%m/%y")+ str(" Today"))
        for i in range(1,7):
            newdate = today + dt.timedelta(i)
            day_list.append(newdate.strftime("%d/%m/%y"))
        print(day_list)
        day_dict = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
        index = day_dict[dayname]-1

        Ordered_list = [0,0,0,0,0,0,0]
        for i in range(index+1):
            Ordered_list[i] = day_list[index+i]
        index += 1
        for k in range(0,index-1):
            print(day_list[k])
            Ordered_list[index+k] = day_list[k]
        print(Ordered_list)

        context["Monday"] = Ordered_list[0]
        context["Tuesday"] = Ordered_list[1]
        context["Wednesday"] = Ordered_list[2]
        context["Thursday"] = Ordered_list[3]
        context["Friday"] = Ordered_list[4]
        context["Saturday"] = Ordered_list[5]
        context["Sunday"] = Ordered_list[6]
        return context

class Class_detail(generic.DetailView):
    model = Gym_class

@login_required
def timetable_create(request):
    model = Timetable
    if request.method == 'POST':
        form = timetableForm(request.POST or None)
        if form.is_valid():
            timetable = form.save(commit=False)
            timetable.poster = request.user
            try:
                timetable.save()
                return HttpResponseRedirect(reverse(''))
            except:
                return HttpResponseRedirect(reverse(''))
    else:
        form = timetableForm()
    return (request, "part_form.html", {'form':form})


class timetable_update(LoginRequiredMixin, UpdateView):
    model = Timetable
    fields = '__all__'
    success_url = reverse_lazy("classlist", args=[str(1)])

 
    
