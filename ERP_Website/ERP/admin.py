from django.contrib import admin
from .models import Gym_class,timetable_class_instance, Timetable

# Register your models here.
admin.site.register(Gym_class)
admin.site.register(timetable_class_instance)
admin.site.register(Timetable)
