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
from catalog.forms import ArchiveForm
from django import forms
from django.utils import timezone
import datetime, time
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
        

class Gym_class(generic.ListView):
    model = Timetable
    context_object_name = "gym_timetable"
    table_class = Class_Table
    template_name ="class_table.html"
    paginate_by = 40

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data()

        Current_timetable = Timetable.objects.get(title="Normal Timetable")

        context["current_timetable"] = Current_timetable

        return context

class Class_detail(generic.DetailView):
    model = Gym_class

@login_required
def class_update(request):
    model = Timetable
    return (request, "part_form.html")


 
    
