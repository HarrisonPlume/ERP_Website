from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#Index
urlpatterns = [
    path("", views.index, name = "index"),
    path("gym_classes", views.Gym_ClassListView.as_view(), name = "gym_classes"),
    path("gym_class/<int:pk>", views.Class_detail.as_view(), name="classes"),
    path("gym_class/create", views.Create_Gym_Class.as_view(), name="create_gym_class"),
    path("gym_class/<int:pk>/update", views.Update_Gym_Class.as_view(),name="update_gym_class"),
    path("gym_class/<int:pk>/delete", views.Delete_Gym_Class.as_view(),name="delete_gym_class"),
    path("timetable/", views.Show_Timetable, name='timetable'),
    path("timetable/update", views.Update_TimeTable, name="timetable_update"),
    path("timetable_class/<int:pk>", views.Timetable_Class_detail.as_view(), name="timetable_class"),
    path("timetable_class/<int:pk>/update", views.timetable_class_instace_update.as_view(), name="update_timetable_class"),
    path("user_profile/<int:pk>", views.User_Profile_detail.as_view(), name="user_profile_detail"),
    path("user_profiles", views.User_Profile_List.as_view(), name="user_profile_list"),
    path("user_profiles/create", views.Create_User_Profile.as_view(), name="create_user_profile")
    ]

