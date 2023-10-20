from django.urls import path
from . import views
#Index
urlpatterns = [
    path("", views.index, name = "index"),
    path("gym_classes", views.Gym_ClassListView.as_view(), name = "gym_classes"),
    path("gym_class/<int:pk>", views.Class_detail.as_view(), name="classes"),
    path("gym_class/create", views.Create_Gym_Class.as_view(), name="create_gym_class"),
    path("gym_class/<int:pk>/update", views.Update_Gym_Class.as_view(),name="update_gym_class"),
    path("timetable/", views.Show_Timetable, name='timetable'),
    path("timetable/update", views.Update_TimeTable, name="timetable_update"),
    path("timetable_class/<int:pk>", views.Timetable_Class_detail.as_view(), name="timetable_class"),
    path("timetable_class/<int:pk>/update", views.timetable_class_instace_update.as_view(), name="update_timetable_class"),
    ]