from django.db import models
from django.urls import reverse # generate urls' by reversing url patterns
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models import Case, When, Value
import time
import datetime

class Gym_class(models.Model):
    """ Model represents a Gym Class"""
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length=1000)
    
    archive = models.BooleanField(null = True, default=False)
    def __str__(self):
        """String for Representing the model objetc (on admin site)"""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a sepecfic author instance."""
        return reverse("classes", args=[str(self.id)])
    
    class Meta:
        ordering = ['title']  

class timetable_class_instance(models.Model):
    gym_class = models.ForeignKey('Gym_class', on_delete=models.RESTRICT, null=True)
    time_slot = models.CharField(max_length=5, null=True, blank=True)
    day = models.CharField(max_length = 10,null=True, blank = True)
    Class_status =(
        ("a", "Available"),
        ("c", "Cancelled"),
        ("h", "On Hold"),
    )
    status = models.CharField(max_length=1,choices=Class_status,blank=False,
                              default="a", help_text="Class status")
    
    class Meta:
        ordering = ['time_slot']
    
    def __str__(self):
        """String that represents the Gym Instance"""
        return f'{self.time_slot} {self.day} '


class Timetable(models.Model):
    """ Model that holds all of the current classes being run at the gym"""
    title = models.CharField(max_length=100, null=True)
    # Monday Traning Fields from 5am to 6pm
    mon5 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon5", null=True, blank=True)

    def __str__(self):
        return self.title