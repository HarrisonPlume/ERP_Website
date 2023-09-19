from django.contrib import admin
from .models import Gym_class, Member, Timetable
# Register your models here.

# class ComponentPrepTaskAdmin(admin.ModelAdmin):
    # list_display = ("task","part","status")

# admin.site.register(ComponentPrepTaskInstance, ComponentPrepTaskAdmin)
admin.site.register(Gym_class)
admin.site.register(Member)
admin.site.register(Timetable)
