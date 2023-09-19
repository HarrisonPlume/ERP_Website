# tutorial/tables.py
import django_tables2 as tables
from .models import Gym_class

class Class_Table(tables.Table):
    class Meta:
        model = Gym_class
        template_name = "django_tables2/bootstrap.html"
        fields = ["title"]