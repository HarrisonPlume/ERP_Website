from django.db import models
from django.urls import reverse # generate urls' by reversing url patterns
from django.contrib.auth.models import User
from django.contrib import messages
from os.path import join as path_join
from datetime import date
from django.db.models.signals import m2m_changed, post_save, pre_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext as _
from django.dispatch import receiver

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
    
    def has_foreign_key_references(self):
        # Check if the Gym_class instance is referenced by any foreign key relationships
        return self.timetable_class_instance_set.exists()
    
    class Meta:
        ordering = ['title']  

class timetable_class_instance(models.Model):
    gym_class = models.ForeignKey('Gym_class', on_delete=models.RESTRICT, null=True, blank = True)
    time_slot = models.CharField(max_length=5, null=True, blank=True)
    day = models.CharField(max_length = 10,null=True, blank = True)
    Class_status =(
        ("a", "Available"),
        ("c", "Cancelled"),
        ("h", "On Hold"),
    )
    status = models.CharField(max_length=1,choices=Class_status,blank=False,
                              default="a", help_text="Class status")
    
    max_participants = models.CharField(max_length = 2, null = True , blank = True)
    current_participants = models.CharField(max_length = 2, null = True, blank = True)
    

    def get_update_url(self):
        return reverse("update_timetable_class", args=[str(self.id)])

    
    
    class Meta:
        ordering = ['time_slot', 'day']
    
    def __str__(self):
        """String that represents the Gym Instance"""
        return f'{self.time_slot} {self.day} '
    

def user_profile_image_path(instance, filename):
    username = instance.user.username
    return path_join('profile_pics', username+".jpg")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    # first_name = models.CharField(max_length=40, blank=True, null=True)
    # last_name = models.CharField(max_length=40, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Returns the url to access a sepecfic author instance."""
        return reverse("user_profile_detail", args=[str(self.id)])

    class Meta:
        ordering = ['user'] 

    def __str__(self):
        """String that Gym User's username"""
        return f'{self.user}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@receiver(post_save, sender=UserProfile)
def update_user_is_staff(sender, instance, **kwargs):
    # Update the is_staff field of the related User object
    if instance.user.is_staff != instance.is_staff:
        instance.user.is_staff = instance.is_staff
        instance.user.save()
  


class Timetable(models.Model):
    """ Model that holds all of the current classes being run at the gym"""
    title = models.CharField(max_length=100, null=True)
    # Monday Traning Fields from 5am to 6pm
    mon5 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon5", null=True, blank=True)
    mon6 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon6", null=True, blank=True)
    mon7 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon7", null=True, blank=True)
    mon8 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon8", null=True, blank=True)
    mon9 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon9", null=True, blank=True)
    mon10 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon10", null=True, blank=True)
    mon11 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon11", null=True, blank=True)
    mon12 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon12", null=True, blank=True)
    mon13 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon13", null=True, blank=True)
    mon14 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon14", null=True, blank=True)
    mon15 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon15", null=True, blank=True)
    mon16 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon16", null=True, blank=True)
    mon17 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon17", null=True, blank=True)
    mon18 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="mon18", null=True, blank=True)
    
    # Tuesday Traning Class fields from 5am to 6pm
    tue5 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue5", null=True, blank=True)
    tue6 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue6", null=True, blank=True)
    tue7 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue7", null=True, blank=True)
    tue8 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue8", null=True, blank=True)
    tue9 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue9", null=True, blank=True)
    tue10 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue10", null=True, blank=True)
    tue11 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue11", null=True, blank=True)
    tue12 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue12", null=True, blank=True)
    tue13 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue13", null=True, blank=True)
    tue14 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue14", null=True, blank=True)
    tue15 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue15", null=True, blank=True)
    tue16 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue16", null=True, blank=True)
    tue17 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue17", null=True, blank=True)
    tue18 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="tue18", null=True, blank=True)

# Wednesday Traning Class fields from 5am to 6pm
    wed5 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed5", null=True, blank=True)
    wed6 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed6", null=True, blank=True)
    wed7 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed7", null=True, blank=True)
    wed8 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed8", null=True, blank=True)
    wed9 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed9", null=True, blank=True)
    wed10 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed10", null=True, blank=True)
    wed11 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed11", null=True, blank=True)
    wed12 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed12", null=True, blank=True)
    wed13 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed13", null=True, blank=True)
    wed14 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed14", null=True, blank=True)
    wed15 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed15", null=True, blank=True)
    wed16 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed16", null=True, blank=True)
    wed17 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed17", null=True, blank=True)
    wed18 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="wed18", null=True, blank=True)

# Thursday Traning Class fields from 5am to 6pm
    thur5 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur5", null=True, blank=True)
    thur6 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur6", null=True, blank=True)
    thur7 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur7", null=True, blank=True)
    thur8 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur8", null=True, blank=True)
    thur9 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur9", null=True, blank=True)
    thur10 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur10", null=True, blank=True)
    thur11 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur11", null=True, blank=True)
    thur12 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur12", null=True, blank=True)
    thur13 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur13", null=True, blank=True)
    thur14 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur14", null=True, blank=True)
    thur15 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur15", null=True, blank=True)
    thur16 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur16", null=True, blank=True)
    thur17 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur17", null=True, blank=True)
    thur18 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="thur18", null=True, blank=True)
    
# Friday Traning Class fields from 5am to 6pm
    fri5 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri5", null=True, blank=True)
    fri6 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri6", null=True, blank=True)
    fri7 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri7", null=True, blank=True)
    fri8 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri8", null=True, blank=True)
    fri9 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri9", null=True, blank=True)
    fri10 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri10", null=True, blank=True)
    fri11 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri11", null=True, blank=True)
    fri12 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri12", null=True, blank=True)
    fri13 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri13", null=True, blank=True)
    fri14 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri14", null=True, blank=True)
    fri15 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri15", null=True, blank=True)
    fri16 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri16", null=True, blank=True)
    fri17 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri17", null=True, blank=True)
    fri18 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="fri18", null=True, blank=True)

# Saturday Traning Class fields from 5am to 6pm
    sat5 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat5", null=True, blank=True)
    sat6 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat6", null=True, blank=True)
    sat7 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat7", null=True, blank=True)
    sat8 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat8", null=True, blank=True)
    sat9 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat9", null=True, blank=True)
    sat10 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat10", null=True, blank=True)
    sat11 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat11", null=True, blank=True)
    sat12 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat12", null=True, blank=True)
    sat13 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat13", null=True, blank=True)
    sat14 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat14", null=True, blank=True)
    sat15 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat15", null=True, blank=True)
    sat16 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat16", null=True, blank=True)
    sat17 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat17", null=True, blank=True)
    sat18 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sat18", null=True, blank=True)

# Sunday Traning Class fields from 5am to 6pm
    sun5 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun5", null=True, blank=True)
    sun6 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun6", null=True, blank=True)
    sun7 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun7", null=True, blank=True)
    sun8 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun8", null=True, blank=True)
    sun9 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun9", null=True, blank=True)
    sun10 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun10", null=True, blank=True)
    sun11 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun11", null=True, blank=True)
    sun12 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun12", null=True, blank=True)
    sun13 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun13", null=True, blank=True)
    sun14 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun14", null=True, blank=True)
    sun15 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun15", null=True, blank=True)
    sun16 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun16", null=True, blank=True)
    sun17 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun17", null=True, blank=True)
    sun18 = models.OneToOneField(timetable_class_instance, on_delete=models.CASCADE, related_name="sun18", null=True, blank=True)

    class Meta:
        permissions = [
            ("update_timetable", "Can update the Timetable")
        ]

    def __str__(self):
        return self.title