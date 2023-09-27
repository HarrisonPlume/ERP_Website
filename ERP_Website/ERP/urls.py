from django.urls import path
from . import views
#Index
urlpatterns = [
    path("", views.index, name = "index"),
    path("gym_classes", views.Gym_ClassListView.as_view(), name = "gym_classes"),
    path("gym_class/<int:pk>", views.Class_detail.as_view(), name="classes"),
    path("timetable/<int:pk>/", views.Gym_timetable.as_view(), name='timetable'),
    path("timetable/<int:pk>/update", views.timetable_update.as_view(), name="timetable_update"),
    ]