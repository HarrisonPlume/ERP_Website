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

class Timetable(models.Model):
    """ Model that holds all of the current classes being run at the gym"""
    title = models.CharField(max_length=100, null=True)
    # Monday Traning Feilds from 6am to 5pm
    mon6 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon6", null=True)
    mon7 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon7", null=True)
    mon8 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon8", null=True)
    mon9 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon9", null=True)
    mon10 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon10", null=True)
    mon11 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon11", null=True)
    mon12 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon12", null=True)
    mon13 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon13", null=True)
    mon14 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon14", null=True)
    mon15 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon15", null=True)
    mon16 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon16", null=True)
    mon17 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="mon17", null=True)
    # Tuesday from 6am to 5pm
    tue6 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue6", null=True)
    tue7 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue7", null=True)
    tue8 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue8", null=True)
    tue9 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue9", null=True)
    tue10 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue10", null=True)
    tue11 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue11", null=True)
    tue12 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue12", null=True)
    tue13 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue13", null=True)
    tue14 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue14", null=True)
    tue15 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue15", null=True)
    tue16 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue16", null=True)
    tue17 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="tue17", null=True)
    # Wednesday from 6am to 5pm
    wed6 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed6", null=True)
    wed7 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed7", null=True)
    wed8 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed8", null=True)
    wed9 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed9", null=True)
    wed10 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed10", null=True)
    wed11 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed11", null=True)
    wed12 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed12", null=True)
    wed13 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed13", null=True)
    wed14 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed14", null=True)
    wed15 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed15", null=True)
    wed16 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed16", null=True)
    wed17 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="wed17", null=True)
    # Thursday from 6am to 5pm
    thur6 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur6", null=True)
    thur7 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur7", null=True)
    thur8 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur8", null=True)
    thur9 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur9", null=True)
    thur10 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur10", null=True)
    thur11 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur11", null=True)
    thur12 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur12", null=True)
    thur13 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur13", null=True)
    thur14 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur14", null=True)
    thur15 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur15", null=True)
    thur16 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur16", null=True)
    thur17 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="thur17", null=True)
    # Friday from 6am to 5pm
    fri6 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri6", null=True)
    fri7 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri7", null=True)
    fri8 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri8", null=True)
    fri9 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri9", null=True)
    fri10 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri10", null=True)
    fri11 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri11", null=True)
    fri12 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri12", null=True)
    fri13 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri13", null=True)
    fri14 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri14", null=True)
    fri15 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri15", null=True)
    fri16 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri16", null=True)
    fri17 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="fri17", null=True)
    # Saturday from 6am to 5pm
    sat6 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat6", null=True)
    sat7 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat7", null=True)
    sat8 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat8", null=True)
    sat9 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat9", null=True)
    sat10 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat10", null=True)
    sat11 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat11", null=True)
    sat12 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat12", null=True)
    sat13 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat13", null=True)
    sat14 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat14", null=True)
    sat15 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat15", null=True)
    sat16 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat16", null=True)
    sat17 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sat17", null=True)
    # Sunday from 6am to 5pm 
    sun6 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun6", null=True)
    sun7 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun7", null=True)
    sun8 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun8", null=True)
    sun9 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun9", null=True)
    sun10 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun10", null=True)
    sun11 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun11", null=True)
    sun12 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun12", null=True)
    sun13 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun13", null=True)
    sun14 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun14", null=True)
    sun15 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun15", null=True)
    sun16 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun16", null=True)
    sun17 = models.OneToOneField(Gym_class, on_delete=models.CASCADE, related_name="sun17", null=True)

    def __str__(self):
        """ Uswed for the Admin site to modify the Timetables"""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a sepecfic author instance."""
        return reverse("classlist", args=[str(1)])
                        

class Member(models.Model):
    """ Model that represents a Gym Member"""
    join_date = models.DateTimeField("time published", auto_now=True)
    first_name = models.CharField(max_length=100, null=False, blank = False)
    last_name = models.CharField(max_length=100, null=False, blank = False)
    active_member = models.BooleanField(null=False, default=True)
    profile_picture = models.ImageField(upload_to='static/profile_pictures', null=True)
    
    def __str__(self):
        output = str(self.first_name)+str(self.last_name)
        return output
    
    def get_absolute_url(self):
        """ Returns the url for each individual member"""
        return None

    
    class Meta:
        ordering = ['last_name','first_name','join_date']
            
            
# # Create Component Prep Tasks  
# @receiver(m2m_changed, sender = Part.Component_Prep_tasks.through)
# def CreateNewCPTaskInstance(sender, **kwargs):
#     obj = Part.objects.latest("pub_date")
#     CPtask_list = obj.Component_Prep_tasks.all()
#     Created_Time = datetime.datetime.now()
#     Created_Time = Created_Time.strftime("%X")+" on the "+Created_Time.strftime("%d/%m/%Y")
#     for task in CPtask_list:
#        try:
#            ComponentPrepTaskInstance.objects.get(task= task, part=obj)
#        except:
#            ComponentPrepTaskInstance.objects.create(task= task, part=obj, status=2, createtime = Created_Time, createtimenum = time.time())
           
#     #Delete excess tasks if requested on update
#     RequestedTaskList = CPtask_list
#     CurrentTaskList = ComponentPrepTaskInstance.objects.filter(part=obj)
#     list1 = []
#     list2 = []
#     for task in CurrentTaskList.values_list():
#         list1.append(task[1])
#     for task in RequestedTaskList.values_list():
#         list2.append(task[1])
#     for task in list1:
#         if task in list2:
#             pass
#         else:
#             ComponentPrepTaskInstance.objects.filter(task= task, part = obj).delete()
            
            